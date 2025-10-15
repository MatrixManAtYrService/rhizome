"""Discover generated client method usage and create proxy wrappers using libcst."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import libcst as cst
import libcst.matchers as m
import structlog
from pydantic import BaseModel, Field

logger = structlog.get_logger()


class CallSite(BaseModel):
    """Location where a generated method is called."""

    file_path: str = Field(description="Relative path to the file containing the call")
    line_number: int = Field(description="Line number of the call")


class GeneratedMethodCall(BaseModel):
    """Represents usage of a generated OpenAPI client method."""

    module_path: str = Field(description="Full import path to the API function module")
    function_name: str = Field(description="The wrapper function name (sync, sync_detailed, etc.)")
    service: str = Field(description="Service identifier (e.g., 'billing_bookkeeper_dev')")
    api_module: str = Field(description="API module name (e.g., 'billing_entity')")
    api_function: str = Field(description="API function name (e.g., 'create_billing_entity')")
    call_sites: list[CallSite] = Field(default_factory=list, description="Locations where this method is called")


class DiscoveryResult(BaseModel):
    """Complete discovery result with all found method calls."""

    methods: dict[str, GeneratedMethodCall] = Field(description="Map of unique method keys to their call information")

    @property
    def total_call_sites(self) -> int:
        """Total number of call sites across all methods."""
        return sum(len(method.call_sites) for method in self.methods.values())

    @property
    def services(self) -> set[str]:
        """Set of all services that have method calls."""
        return {method.service for method in self.methods.values()}

    def methods_by_service(self) -> dict[str, list[GeneratedMethodCall]]:
        """Group methods by service."""
        by_service: dict[str, list[GeneratedMethodCall]] = defaultdict(list)
        for method in self.methods.values():
            by_service[method.service].append(method)
        return dict(by_service)


class GeneratedClientUsageVisitor(cst.CSTVisitor):
    """
    Discover all calls to generated OpenAPI client methods.

    Tracks pattern: imported_name.method_name(...)
    where imported_name comes from stolon.generated.*.api.*
    """

    def __init__(self, file_path: str) -> None:
        super().__init__()
        self.file_path = file_path
        # Map: local_name -> (full_module_path, service, api_module, api_function)
        self.imports: dict[str, tuple[str, str, str, str]] = {}
        # Discovered calls
        self.calls: dict[str, GeneratedMethodCall] = {}

    def visit_ImportFrom(self, node: cst.ImportFrom) -> None:
        """Track imports from generated client API modules."""
        if node.module is None:
            return

        # Extract module path
        module_parts = self._get_dotted_name(node.module)
        module_path = ".".join(module_parts)

        # Check if this is a generated client import
        # Pattern: stolon.generated.{service}.open_api_definition_client.api.{api_module}
        if (
            len(module_parts) >= 6
            and module_parts[0] == "stolon"
            and module_parts[1] == "generated"
            and module_parts[3] == "open_api_definition_client"
            and module_parts[4] == "api"
        ):
            service = module_parts[2]  # e.g., "billing_bookkeeper_dev"
            api_module = module_parts[5]  # e.g., "billing_entity"

            # Track each imported name
            if isinstance(node.names, cst.ImportStar):
                logger.warning(f"Star import from generated client: {module_path}")
            else:
                for name_item in node.names:
                    if isinstance(name_item, cst.ImportAlias):
                        imported_name = (
                            name_item.name.value if isinstance(name_item.name, cst.Name) else str(name_item.name)
                        )
                        local_name = name_item.asname.name.value if name_item.asname else imported_name

                        # Store mapping: local_name -> (module_path, service, api_module, api_function)
                        self.imports[local_name] = (module_path, service, api_module, imported_name)

                        logger.debug(
                            "Tracked generated import",
                            local_name=local_name,
                            service=service,
                            api_module=api_module,
                            api_function=imported_name,
                        )

    def visit_Call(self, node: cst.Call) -> None:
        """Visit function calls to detect: imported_module.method(...)."""
        # Match pattern: some_name.method_name(...)
        if m.matches(node.func, m.Attribute(value=m.Name(), attr=m.Name())):
            func_attr = cst.ensure_type(node.func, cst.Attribute)
            base_name = cst.ensure_type(func_attr.value, cst.Name).value
            method_name = func_attr.attr.value

            # Check if base_name is a tracked import
            if base_name in self.imports:
                module_path, service, api_module, api_function = self.imports[base_name]

                # Create unique key
                key = f"{service}.{api_module}.{api_function}.{method_name}"

                # Get line number
                line_number = self._get_line_number(node)

                call_site = CallSite(file_path=self.file_path, line_number=line_number)

                if key not in self.calls:
                    self.calls[key] = GeneratedMethodCall(
                        module_path=f"{module_path}.{api_function}",
                        function_name=method_name,
                        service=service,
                        api_module=api_module,
                        api_function=api_function,
                        call_sites=[call_site],
                    )
                else:
                    self.calls[key].call_sites.append(call_site)

                logger.debug(
                    "Found generated method call",
                    key=key,
                    file=self.file_path,
                    line=line_number,
                )

    def _get_dotted_name(self, node: cst.BaseExpression) -> list[str]:
        """Extract dotted name parts from module path."""
        parts = []
        current = node
        while isinstance(current, cst.Attribute):
            parts.insert(0, current.attr.value)
            current = current.value
        if isinstance(current, cst.Name):
            parts.insert(0, current.value)
        return parts

    def _get_line_number(self, node: cst.CSTNode) -> int:
        """Extract line number from node metadata."""
        pos = self.get_metadata(cst.metadata.PositionProvider, node)
        return pos.start.line if pos else -1


def discover_generated_client_usage(src_dir: Path = Path("src")) -> DiscoveryResult:
    """
    Scan the codebase to find all usages of generated OpenAPI client methods.

    Args:
        src_dir: Root source directory to scan

    Returns:
        DiscoveryResult containing all discovered method calls
    """
    logger.info("Discovering generated client usage", src_dir=str(src_dir))

    all_calls: dict[str, GeneratedMethodCall] = {}

    # Find all Python files
    python_files = list(src_dir.rglob("*.py"))
    logger.info(f"Scanning {len(python_files)} Python files")

    files_scanned = 0
    for py_file in python_files:
        # Skip generated client files themselves
        if "stolon/generated/" in str(py_file):
            continue

        try:
            source_code = py_file.read_text()
            module = cst.parse_module(source_code)

            # Wrap module with metadata (needed for line numbers)
            wrapper = cst.metadata.MetadataWrapper(module)

            visitor = GeneratedClientUsageVisitor(str(py_file.relative_to(Path.cwd())))

            # Visit with metadata
            wrapper.visit(visitor)

            # Merge results
            for key, call in visitor.calls.items():
                if key in all_calls:
                    all_calls[key].call_sites.extend(call.call_sites)
                else:
                    all_calls[key] = call

            if visitor.calls:
                files_scanned += 1
                logger.debug(f"Found {len(visitor.calls)} calls in {py_file.name}")

        except Exception as e:
            logger.warning(f"Failed to parse {py_file}: {e}")

    logger.info(
        "Discovery complete",
        files_scanned=files_scanned,
        unique_methods=len(all_calls),
        total_call_sites=sum(len(c.call_sites) for c in all_calls.values()),
    )

    return DiscoveryResult(methods=all_calls)


def print_discovery_report(result: DiscoveryResult) -> None:
    """Print a human-readable report of discovered method calls."""
    print("\n" + "=" * 80)
    print("GENERATED CLIENT USAGE DISCOVERY REPORT")
    print("=" * 80)

    by_service = result.methods_by_service()

    for service in sorted(by_service.keys()):
        service_calls = by_service[service]
        print(f"\n📦 Service: {service}")
        print(f"   {len(service_calls)} unique methods used")

        for call in sorted(service_calls, key=lambda c: c.api_function):
            print(f"\n   • {call.api_function}.{call.function_name}()")
            print(f"     Module: {call.api_module}")
            print(f"     Call sites: {len(call.call_sites)}")
            for site in call.call_sites[:3]:  # Show first 3
                print(f"       - {site.file_path}:{site.line_number}")
            if len(call.call_sites) > 3:
                print(f"       ... and {len(call.call_sites) - 3} more")

    print("\n" + "=" * 80)
    print(f"TOTAL: {len(result.methods)} unique generated methods in use")
    print(f"CALL SITES: {result.total_call_sites} total call locations")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    # Run discovery
    result = discover_generated_client_usage()

    # Print report
    print_discovery_report(result)

    # Save JSON
    output_file = Path("discovered_wrappers.json")
    output_file.write_text(result.model_dump_json(indent=2))
    print(f"✅ Saved discovery results to {output_file}")
