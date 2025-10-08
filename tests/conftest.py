"""Pytest fixtures for rhizome tests."""

import os
import tempfile
import threading
import time
from collections import defaultdict
from collections.abc import Callable, Generator
from dataclasses import dataclass
from pathlib import Path

import pytest
import uvicorn
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from _pytest.terminal import TerminalReporter

from rhizome.client import RhizomeClient
from rhizome.environments.environment_list import environment_type
from rhizome.models.base import DataMismatchError
from rhizome.server import app, setup_logging
from tests.utils import get_open_port
from trifolium.config import Home

# --- Aggregated Test Reporting --- #

# Global list to store sync failures for aggregated reporting
SYNC_FAILURES: list[dict[str, str]] = []

# Global dictionary to store all assertion errors for aggregation
ALL_FAILURES: dict[str, dict] = {}

# Reverse map from Environment Class Name -> a.b.c.EnumName
CLASS_TO_ENUM_MAP = {v.__name__: k for k, v in environment_type.items()}


def _parse_test_parameters(nodeid: str) -> dict[str, str]:
    """Extract test parameters from pytest nodeid."""
    test_params = {}
    if "[" in nodeid:
        # Parse parametrized test name like: test_name[Env-table-Model-Emplacement] or test_name[env-table0]
        param_str = nodeid.split("[")[1].rstrip("]")
        params = param_str.split("-")
        if len(params) >= 2:
            test_params["env"] = params[0]
            # Remove any trailing numbers from table names (e.g. merchant_payment0 -> merchant_payment)
            import re

            table_name = params[1]
            # Strip trailing digits and numbers if they exist (handles merchant_payment0, merchant_payment1, etc.)
            table_name = re.sub(r"\d+$", "", table_name)
            test_params["table"] = table_name
    return test_params


def _handle_assertion_error(report: object, call: CallInfo, test_params: dict[str, str]) -> None:
    """Handle aggregation of AssertionError failures."""
    # Generate a signature for this error type
    error_msg = str(call.excinfo.value)

    # Remove the fix commands part to get the core error
    if "🔧 SUGGESTED FIX COMMANDS:" in error_msg:
        error_msg.split("🔧 SUGGESTED FIX COMMANDS:")[0].strip()

    # Create a signature based on the error pattern
    if test_params:
        signature = f"{test_params.get('env', 'Unknown')}-{test_params.get('table', 'Unknown')}"
    else:
        signature = "Generic-AssertionError"

    # Aggregate failures by signature
    if signature not in ALL_FAILURES:
        ALL_FAILURES[signature] = {
            "count": 0,
            "nodes": [],
            "env": test_params.get("env", "Unknown"),
            "table": test_params.get("table", "Unknown"),
        }

    ALL_FAILURES[signature]["count"] += 1
    ALL_FAILURES[signature]["nodes"].append(report.nodeid)

    # Suppress the verbose fix commands in individual reports
    if "🔧 SUGGESTED FIX COMMANDS:" in str(call.excinfo.value):
        env_name = test_params.get("env", "test")
        table_name = test_params.get("table", "unknown")
        report.longrepr = f"AssertionError in {env_name}/{table_name} (see summary for fix commands)"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo) -> None:
    """Hook to intercept test reports, catch errors, and aggregate them."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Extract test parameters if they exist
        test_params = _parse_test_parameters(report.nodeid)

        # Check if the failure is our custom DataMismatchError
        if call.excinfo and call.excinfo.errisinstance(DataMismatchError):
            exc = call.excinfo.value

            # Convert class name to the correct CLI enum value
            env_enum_val = CLASS_TO_ENUM_MAP.get(exc.env_name)
            if not env_enum_val:
                return

            # Store failure for summary
            SYNC_FAILURES.append({"env": str(env_enum_val), "table": exc.table_name})

            # Suppress individual error message since it will be in the summary
            report.longrepr = f"Data mismatch for {exc.env_name}/{exc.table_name} (see summary for details)"

        # For all AssertionErrors (including those wrapped with fix commands)
        elif call.excinfo and call.excinfo.errisinstance(AssertionError):
            _handle_assertion_error(report, call, test_params)


def pytest_terminal_summary(terminalreporter: "TerminalReporter") -> None:
    """Add a custom summary for aggregated sync failures."""
    if not SYNC_FAILURES and not ALL_FAILURES:
        return

    # Show summary for custom DataMismatchError failures
    if SYNC_FAILURES:
        terminalreporter.write_sep("=", "AGGREGATED SYNC FAILURES", yellow=True)
        terminalreporter.write_line(
            "The following commands are suggested to resolve the data mismatch failures reported above:"
        )

        # Group failures by environment
        grouped_failures = defaultdict(list)
        for failure in SYNC_FAILURES:
            grouped_failures[failure["env"]].append(failure["table"])

        for env, tables in grouped_failures.items():
            terminalreporter.write_line("")
            terminalreporter.write_line(f"🔧 To fix failures in {env}, run:", cyan=True)

            # Deduplicate tables and create commands
            unique_tables = list(set(tables))
            schema_tables_str = " ".join([f"--table {table}" for table in unique_tables])
            schema_command = f"rhizome sync schema --env {env} {schema_tables_str}"
            terminalreporter.write_line(schema_command)

            # Create data command
            data_tables_str = " ".join([f"--table {table}" for table in unique_tables])
            data_command = f"rhizome sync data --env {env} {data_tables_str}"
            terminalreporter.write_line(data_command)

        terminalreporter.write_line("")
        terminalreporter.write_line(
            "💡 TIP: If this is a schema evolution issue, the schema sync will update the model definitions.",
            yellow=True,
        )
        terminalreporter.write_line(
            "💡 IMPORTANT: Always run schema syncs before data syncs to ensure proper ordering.", yellow=True
        )

    # Show summary for aggregated assertion errors
    if ALL_FAILURES:
        terminalreporter.write_sep("=", "AGGREGATED TEST FAILURES SUMMARY", red=True)
        terminalreporter.write_line(
            "Multiple tests failed with the same error pattern. Fix commands grouped by environment/table:", red=True
        )

        # Sort failures by count (most frequent first)
        sorted_failures = sorted(ALL_FAILURES.items(), key=lambda x: x[1]["count"], reverse=True)

        # Group by environment for cleaner output
        env_groups = defaultdict(list)
        for signature, data in sorted_failures:
            env = data["env"]
            env_groups[env].append((signature, data))

        for env, failures in env_groups.items():
            terminalreporter.write_line("")
            terminalreporter.write_line(f"🔧 Environment: {env}", cyan=True)

            # Collect all tables for this environment
            tables = []
            total_failures = 0
            for _signature, data in failures:
                table = data["table"]
                count = data["count"]
                if table not in tables:
                    tables.append(table)
                total_failures += count
                terminalreporter.write_line(f"   {table}: {count} failure(s)")

            terminalreporter.write_line("")
            terminalreporter.write_line("   Run these commands in order:")

            # Generate consolidated fix commands for this environment
            tables_str = " ".join([f"--table {table}" for table in tables])
            terminalreporter.write_line(f"   1. rhizome sync schema --env {env} {tables_str}")
            terminalreporter.write_line(f"   2. rhizome sync data --env {env} {tables_str}")

        terminalreporter.write_line("")
        terminalreporter.write_line(
            "💡 TIP: If this is a schema evolution issue, the schema sync will update the model definitions.",
            yellow=True,
        )
        terminalreporter.write_line(
            "💡 IMPORTANT: Always run schema syncs before data syncs to ensure proper ordering.", yellow=True
        )


# --- Standard Fixtures --- #


def pytest_addoption(parser: Parser) -> None:
    """Add custom pytest command line options."""
    parser.addoption(
        "--local-cluster",
        action="store_true",
        default=False,
        help="run tests that require a local Kind cluster",
    )
    parser.addoption(
        "--external-infra",
        action="store_true",
        default=False,
        help="run tests that require external infrastructure (production CloudSQL, 1Password, etc.)",
    )


def pytest_configure(config: Config) -> None:
    """Register custom markers."""
    config.addinivalue_line("markers", "local_cluster: mark test as requiring a local Kind cluster")
    config.addinivalue_line("markers", "external_infra: mark test as requiring external infrastructure")


def pytest_collection_modifyitems(config: Config, items: list[Item]) -> None:
    """Skip cluster and external infra tests unless their respective options are passed."""
    local_cluster_enabled = config.getoption("--local-cluster")
    external_infra_enabled = config.getoption("--external-infra")

    skip_local_cluster = pytest.mark.skip(reason="need --local-cluster option to run")
    skip_external_infra = pytest.mark.skip(reason="need --external-infra option to run")

    for item in items:
        if "local_cluster" in item.keywords and not local_cluster_enabled:
            item.add_marker(skip_local_cluster)
        if "external_infra" in item.keywords and not external_infra_enabled:
            item.add_marker(skip_external_infra)


@dataclass
class RunningServer:
    """Represents a running rhizome server instance for testing."""

    port: int
    home: Home


@pytest.fixture(scope="session")
def local_cluster() -> None:
    """Ensure Kind cluster 'rhizome-test' is available and set KUBECONFIG.

    Raises:
        Exception: If the cluster is not available.
    """
    # Set KUBECONFIG to local test config to avoid touching remote infrastructure
    kubeconfig_path = Path("local_test/kubeconfig").absolute()
    if not kubeconfig_path.exists():
        raise Exception(f"Local kubeconfig not found at {kubeconfig_path}. Run 'make up' to create the Kind cluster.")

    os.environ["KUBECONFIG"] = str(kubeconfig_path)

    # Check if Kind cluster is available
    import subprocess

    try:
        result = subprocess.run(
            ["kubectl", "cluster-info", "--context", "kind-rhizome-test"], capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            raise Exception(f"Kind cluster 'rhizome-test' not available. Run 'make up' first. Error: {result.stderr}")
    except subprocess.TimeoutExpired as e:
        raise Exception("Timeout checking Kind cluster availability.") from e
    except FileNotFoundError as e:
        raise Exception("kubectl not found. Please install kubectl.") from e


@pytest.fixture(scope="session")
def local_mysql(local_cluster: None) -> None:
    """Ensure MySQL pod is ready in the Kind cluster.

    Args:
        local_cluster: Consumes the local_cluster fixture.

    Raises:
        Exception: If the MySQL pod is not ready.
    """
    import subprocess

    try:
        # Check if MySQL pod is ready
        result = subprocess.run(
            ["kubectl", "get", "pod", "mysql", "-o", "jsonpath={.status.phase}"],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.returncode != 0 or result.stdout.strip() != "Running":
            raise Exception(
                f"MySQL pod not ready. Run 'tilt up' to deploy MySQL. Current status: {result.stdout.strip()}"
            )

        # Check if MySQL is actually ready (not just running)
        result = subprocess.run(
            ["kubectl", "get", "pod", "mysql", "-o", 'jsonpath={.status.conditions[?(@.type=="Ready")].status}'],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.stdout.strip() != "True":
            raise Exception("MySQL pod is running but not ready. Wait for the readiness probe to pass.")

    except subprocess.TimeoutExpired as e:
        raise Exception("Timeout checking MySQL pod status.") from e
    except FileNotFoundError as e:
        raise Exception("kubectl not found. Please install kubectl.") from e


@pytest.fixture(scope="module")
def rhizome_server(local_mysql: None) -> Generator[RunningServer, None, None]:
    """Start a rhizome server for testing.

    Args:
        local_mysql: Consumes the local_mysql fixture.

    Returns:
        RunningServer: Server instance with port and home attributes.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create sandboxed home
        home = Home.sandbox(Path(temp_dir))
        test_port = get_open_port()
        home.set_port(test_port)

        # Setup logging
        setup_logging()

        # Start server in background thread
        def run_server() -> None:
            uvicorn.run(app, host="0.0.0.0", port=test_port, log_config=None)

        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        time.sleep(0.5)  # Give server time to start

        yield RunningServer(port=test_port, home=home)


@pytest.fixture(scope="module")
def real_rhizome_client() -> Generator[RhizomeClient, None, None]:
    """Create a single RhizomeClient for use with real infrastructure tests."""
    with tempfile.TemporaryDirectory() as temp_dir:
        home = Home.sandbox(Path(temp_dir))
        client = RhizomeClient(home=home, data_in_logs=True)
        yield client


@pytest.fixture(scope="module")
def real_env_instance_factory(real_rhizome_client: RhizomeClient) -> Callable[[type], object]:
    """Provide a factory to get memoized environment instances for real infrastructure tests."""
    _cache: dict[type, object] = {}

    def get_instance(env_class: type) -> object:
        if env_class not in _cache:
            _cache[env_class] = env_class(real_rhizome_client)
        return _cache[env_class]

    return get_instance


@dataclass
class RunningStolonServer:
    """Represents a running stolon server instance for testing."""

    port: int
    home: Home


@pytest.fixture(scope="session")
def stolon_server() -> Generator[RunningStolonServer, None, None]:
    """Start a stolon server for testing.

    This fixture is session-scoped so all tests share the same server instance,
    avoiding multiple authentication prompts.

    Returns:
        RunningStolonServer: Server instance with port and home attributes.
    """
    from stolon.server import app as stolon_app

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create sandboxed home
        home = Home.sandbox(Path(temp_dir))
        test_port = get_open_port()
        home.set_stolon_port(test_port)

        # Setup logging
        setup_logging()

        # Start server in background thread
        def run_server() -> None:
            uvicorn.run(stolon_app, host="0.0.0.0", port=test_port, log_config=None)

        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        time.sleep(0.5)  # Give server time to start

        yield RunningStolonServer(port=test_port, home=home)


# --- Stolon Test Fixtures for Billing Objects --- #


def _print_curl(method: str, url: str, json_data: dict | None = None, token: str = "YOUR-INTERNAL-SESSION") -> None:
    """Print a curl command for manual recreation."""
    import json as json_module

    curl_parts = [
        "curl",
        "-X",
        f"'{method.upper()}'",
        f"'{url}'",
        "--header 'x-clover-appenv: dev1'",
        f"--header 'Cookie: internalSession={token}'",
        "--header 'Content-Type: application/json'",
    ]

    if json_data:
        json_str = json_module.dumps(json_data, indent=2)
        curl_parts.append(f"--data '{json_str}'")

    print("\n" + " \\\n".join(curl_parts) + "\n")


@pytest.fixture
def revenue_share_group(stolon_server: RunningStolonServer) -> Generator[dict, None, None]:
    """Create and cleanup a revenue share group for testing."""
    import uuid

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    # Create revenue share group with MFF prefix
    group_name = f"MFF_Test_{uuid.uuid4().hex[:4]}"
    short_desc = f"MFF-{group_name}"
    description = f"The FirstData/Fiserv reseller in EMEA for {group_name}"

    json_data = {"revenueShareGroup": group_name, "shortDesc": short_desc, "description": description}

    print("\n=== Creating Revenue Share Group ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/revsharegroup", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/revsharegroup", json=json_data)

    yield {"name": group_name, "create_response": create_response}

    # Cleanup: Find and delete the revenue share group
    try:
        groups = dev.get("/billing-bookkeeper/v1/revsharegroup")
        for group in groups.get("elements", []):
            if group.get("revenueShareGroup") == group_name:
                group_uuid = group.get("uuid")
                if group_uuid:
                    # Note: API might not support deletion - TBD
                    pass
    except Exception:
        pass  # Best effort cleanup


@pytest.fixture
def billing_entity(stolon_server: RunningStolonServer) -> Generator[dict, None, None]:
    """Create and cleanup a billing entity for testing."""
    import uuid

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    # Generate unique 13-char entity UUID
    entity_uuid = f"MFF{uuid.uuid4().hex[:10].upper()}"
    entity_name = f"MFF Test Reseller {entity_uuid[-4:]}"

    json_data = {"entityUuid": entity_uuid, "entityType": "RESELLER", "name": entity_name}

    print("\n=== Creating Billing Entity ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/entity", json_data)

    # Create billing entity
    create_response = dev.post("/billing-bookkeeper/v1/entity", json=json_data)

    # Extract server-generated billing entity UUID from response
    billing_entity_uuid = create_response.get("uuid")

    if not billing_entity_uuid:
        # Fallback: try to get it via GET (though this seems to 404 in dev1)
        print(f"\n⚠️  Response did not contain uuid field. Response: {create_response}")
        print(f"\n=== Trying to GET Billing Entity by entity UUID ===")
        _print_curl("GET", f"https://dev1.dev.clover.com/billing-bookkeeper/v1/entity/entity/{entity_uuid}")
        entity_get = dev.get(f"/billing-bookkeeper/v1/entity/entity/{entity_uuid}")
        billing_entity_uuid = entity_get.get("uuid")

    print(f"\n✓ Server-generated billing_entity_uuid: {billing_entity_uuid}")

    yield {
        "entity_uuid": entity_uuid,
        "billing_entity_uuid": billing_entity_uuid,
        "name": entity_name,
        "create_response": create_response,
    }

    # Cleanup TBD
    pass


@pytest.fixture
def alliance_code(billing_entity: dict, stolon_server: RunningStolonServer) -> Generator[dict, None, None]:
    """Create and cleanup an alliance code for testing."""
    import uuid

    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    billing_entity_uuid = billing_entity["billing_entity_uuid"]
    alliance_code_value = f"9{uuid.uuid4().hex[:2].upper()}"

    json_data = {"billingEntityUuid": billing_entity_uuid, "allianceCode": alliance_code_value, "invoiceCount": 1}

    print("\n=== Creating Alliance Code ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/alliancecode", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/alliancecode", json=json_data)

    yield {"alliance_code": alliance_code_value, "billing_entity_uuid": billing_entity_uuid, "create_response": create_response}

    # Cleanup TBD
    pass


@pytest.fixture
def billing_schedule(billing_entity: dict, stolon_server: RunningStolonServer) -> Generator[dict, None, None]:
    """Create and cleanup a billing schedule for testing."""
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    json_data = {
        "billingEntityUuid": billing_entity_uuid,
        "effectiveDate": "2025-08-01",
        "frequency": "MONTHLY",
        "billingDay": 1,
        "nextBillingDate": "2025-09-01",
        "unitsInNextPeriod": 31,
        "defaultCurrency": "EUR",
    }

    print("\n=== Creating Billing Schedule ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/schedule", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/schedule", json=json_data)

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response}

    # Cleanup TBD
    pass


@pytest.fixture
def fee_rate(billing_entity: dict, stolon_server: RunningStolonServer) -> Generator[dict, None, None]:
    """Create and cleanup a fee rate for testing."""
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    json_data = {
        "billingEntityUuid": billing_entity_uuid,
        "feeCategory": "PLAN_RETAIL",
        "feeCode": "PaymentsPDVT",
        "currency": "EUR",
        "effectiveDate": "2025-08-01",
        "applyType": "DEFAULT",
        "perItemAmount": 0.0,
    }

    print("\n=== Creating Fee Rate ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/rate", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/rate", json=json_data)

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response}

    # Cleanup TBD
    pass


@pytest.fixture
def processing_group_dates(billing_entity: dict, stolon_server: RunningStolonServer) -> Generator[dict, None, None]:
    """Create and cleanup processing group dates for testing."""
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    billing_entity_uuid = billing_entity["billing_entity_uuid"]

    json_data = {
        "billingEntityUuid": billing_entity_uuid,
        "hierarchyType": "MERCHANT_SCHEDULE",
        "cycleDate": "2025-08-01",
        "postingDate": "2025-08-01",
        "billingDate": "2025-08-01",
        "settlementDate": "2025-08-01",
    }

    print("\n=== Creating Processing Group Dates ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/processgroupdates", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/processgroupdates", json=json_data)

    yield {"billing_entity_uuid": billing_entity_uuid, "create_response": create_response}

    # Cleanup TBD
    pass


@pytest.fixture
def plan_action_fee_code(stolon_server: RunningStolonServer) -> Generator[dict, None, None]:
    """Create and cleanup a plan action fee code for testing."""
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    test_plan_uuid = "YEQMV17H09HHW"

    json_data = {
        "merchantPlanUuid": test_plan_uuid,
        "planActionType": "PLAN_ASSIGN",
        "effectiveDate": "2025-08-01",
        "feeCategory": "PLAN_RETAIL",
        "feeCode": "PaymentsPDVT.PRC",
    }

    print("\n=== Creating Plan Action Fee Code ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/planactionfeecode", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/planactionfeecode", json=json_data)

    yield {"merchant_plan_uuid": test_plan_uuid, "create_response": create_response}

    # Cleanup TBD
    pass


@pytest.fixture
def cellular_action_fee_code(stolon_server: RunningStolonServer) -> Generator[dict, None, None]:
    """Create and cleanup a cellular action fee code for testing."""
    from stolon.client import StolonClient
    from stolon.environments.dev.http import DevHttp

    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    dev = DevHttp(client)

    json_data = {
        "carrier": "AT&T",
        "cellularActionType": "CELLULAR_ARREARS",
        "effectiveDate": "2025-08-01",
        "feeCategory": "CELLULAR_RETAIL",
        "feeCode": "CellularArr.ATT",
    }

    print("\n=== Creating Cellular Action Fee Code ===")
    _print_curl("POST", "https://dev1.dev.clover.com/billing-bookkeeper/v1/cellularactionfeecode", json_data)

    create_response = dev.post("/billing-bookkeeper/v1/cellularactionfeecode", json=json_data)

    yield {"carrier": "AT&T", "create_response": create_response}

    # Cleanup TBD
    pass
