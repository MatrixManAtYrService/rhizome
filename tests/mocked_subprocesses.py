"""
Mocked subprocess tools for rhizome tests.

This module contains mock implementations of external tools (kubectl, 1Password, lsof)
that simulate their behavior without requiring actual external infrastructure.
"""

from unittest.mock import AsyncMock

from rhizome.tools import (
    BritiveInfo,
    CommandResult,
    GcloudTool,
    KubectlTool,
    LogLine,
    LsofTool,
    OnePasswordTool,
    PortInfo,
    PybritiveTool,
)


class MockKubectlTool(KubectlTool):
    """Mock kubectl tool that simulates CloudSQL proxy behavior for any environment."""

    async def exec_in_pod(self, context: str, namespace: str, deployment: str, command: list[str]) -> CommandResult:
        """Simulate starting CloudSQL connection script."""
        return CommandResult(returncode=0, stdout="Connection script started", stderr="")

    async def get_logs(self, context: str, namespace: str, deployment: str, since: str = "10s") -> list[LogLine]:
        """Return logs with CloudSQL proxy port information."""
        # Create a dynamic mock log that will match any SQL connection pattern
        # The mock will contain a pattern that the port discovery logic will find
        return [
            LogLine(content=("Starting proxy for connectionName 'mock-connection' on port '62956'")),
            LogLine(content="Ready for new connections"),
        ]

    async def port_forward(
        self, context: str, namespace: str, resource: str, local_port: int, remote_port: int
    ) -> AsyncMock:
        """Return a mock subprocess for port forwarding."""
        mock_process = AsyncMock()
        mock_process.pid = 12345
        mock_process.returncode = None  # Process is running

        # Create a mock stdout that yields a few messages then stops
        stdout_lines = [
            f"Forwarding from 127.0.0.1:{local_port} -> {remote_port}\n".encode(),
            f"Forwarding from [::1]:{local_port} -> {remote_port}\n".encode(),
            b"",  # Empty bytes to signal end of output
        ]
        stdout_iterator = iter(stdout_lines)

        async def mock_stdout_readline() -> bytes:
            try:
                return next(stdout_iterator)
            except StopIteration:
                return b""  # Return empty bytes when no more lines

        mock_process.stdout = AsyncMock()
        mock_process.stderr = AsyncMock()
        mock_process.stdout.readline = mock_stdout_readline
        mock_process.stderr.readline = AsyncMock(return_value=b"")
        mock_process.wait = AsyncMock(return_value=0)  # Process completes successfully

        return mock_process

    async def cluster_info(self, context: str) -> CommandResult:
        """Mock cluster info."""
        return CommandResult(returncode=0, stdout="Cluster info", stderr="")

    async def get_pod_status(self, pod_name: str, context: str | None = None) -> CommandResult:
        """Mock pod status."""
        return CommandResult(returncode=0, stdout="Running", stderr="")

    async def unset_cluster_ca(self, cluster_name: str) -> CommandResult:
        """Mock unset cluster CA."""
        return CommandResult(returncode=0, stdout="", stderr="")


class MockOnePasswordTool(OnePasswordTool):
    """Mock 1Password tool that returns environment-specific credentials."""

    async def read_secret(self, reference: str) -> str:
        """Return mock password based on 1Password reference."""
        if "EventBillingROCred-dev" in reference:
            return "mock_dev_password_123"
        elif "EventBillingROCred-demo" in reference:
            return "mock_demo_password_456"
        else:  # Production or default
            return "mock_prod_password_789"


class MockGcloudTool(GcloudTool):
    """Mock gcloud tool that simulates Google Cloud operations."""

    async def get_cluster_credentials(self, project: str, cluster: str, region: str) -> CommandResult:
        """Mock getting cluster credentials - always succeeds."""
        return CommandResult(returncode=0, stdout="kubeconfig entry generated", stderr="")

    async def set_cluster_server(self, cluster_name: str, server_url: str) -> CommandResult:
        """Mock setting cluster server - always succeeds."""
        return CommandResult(returncode=0, stdout=f"Cluster '{cluster_name}' set.", stderr="")


class MockPybritiveTool(PybritiveTool):
    """Mock pybritive tool that returns test credentials."""

    async def checkout(self, resource_path: str, pattern: str | None = None) -> BritiveInfo:
        """Return mock credentials for testing."""
        # Return mock credentials based on the nushell output format
        return BritiveInfo(
            username="btu.matthew.rixman.63854",
            password="v4REDACTEDav",
            host="db-maxscale-usprod.global.clover.network",
            port=3326,
        )


class MockLsofTool(LsofTool):
    """Mock lsof tool that simulates port usage correctly for mocked tests."""

    def __init__(self) -> None:
        self._forwarded_ports: set[int] = set()
        self._call_count: dict[int, int] = {}

    async def check_port(self, port: int) -> list[PortInfo]:
        """
        Return port info based on call patterns.

        First call for a port: return empty (port available for forwarding)
        Subsequent calls: return port info (port is now forwarded and in use)
        """
        self._call_count[port] = self._call_count.get(port, 0) + 1

        # First call: port is available for forwarding
        if self._call_count[port] == 1:
            return []

        # Subsequent calls: port is now forwarded and in use
        # This helps _wait_for_port_forward succeed
        return [PortInfo(pid=12345, process_name="kubectl", port=port)]


class MockNAProductionKubectlTool(MockKubectlTool):
    """Mock kubectl tool specifically for NA Production with realistic connection strings."""

    async def get_logs(self, context: str, namespace: str, deployment: str, since: str = "10s") -> list[LogLine]:
        """Return logs with NA production CloudSQL proxy port information."""
        return [
            LogLine(
                content=(
                    "Starting proxy for connectionName "
                    "'clover-prod-databases:us-central1:billing-bookkeeper' on port '62956'"
                )
            ),
            LogLine(content="Ready for new connections"),
        ]
