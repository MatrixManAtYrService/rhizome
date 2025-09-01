"""
Mocked subprocess tools for rhizome tests.

This module contains mock implementations of external tools (kubectl, 1Password, lsof)
that simulate their behavior without requiring actual external infrastructure.
"""

from unittest.mock import AsyncMock

from rhizome.tools import CommandResult, KubectlTool, LogLine, LsofTool, OnePasswordTool, PortInfo


class MockKubectlTool(KubectlTool):
    """Mock kubectl tool that simulates CloudSQL proxy behavior for any environment."""

    async def exec_in_pod(self, context: str, namespace: str, deployment: str, command: list[str]) -> CommandResult:
        """Simulate starting CloudSQL connection script."""
        return CommandResult(returncode=0, stdout="Connection script started", stderr="")

    async def get_logs(self, context: str, namespace: str, deployment: str, since: str = "10s") -> list[LogLine]:
        """Return logs with CloudSQL proxy port information."""
        return [
            LogLine(
                content=(
                    "Starting proxy for connectionName "
                    "'mock-connection' on port '62956'"
                )
            ),
            LogLine(content="Ready for new connections"),
        ]

    async def port_forward(
        self, context: str, namespace: str, resource: str, local_port: int, remote_port: int
    ) -> AsyncMock:
        """Return a mock subprocess for port forwarding."""
        mock_process = AsyncMock()
        mock_process.pid = 12345
        mock_process.stdout = AsyncMock()
        mock_process.stderr = AsyncMock()
        mock_process.stdout.readline = AsyncMock(
            return_value=f"Forwarding from 127.0.0.1:{local_port} -> {remote_port}\n".encode()
        )
        mock_process.stderr.readline = AsyncMock(return_value=b"")
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


class MockLsofTool(LsofTool):
    """Mock lsof tool that reports ports as available."""

    async def check_port(self, port: int) -> list[PortInfo]:
        """Return empty list indicating port is available."""
        return []


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
