"""
Tool abstractions for external command dependencies.

This module provides injectable tool dependencies to enable testing and mocking
of external tools like kubectl, gcloud, 1password CLI, and lsof.
"""

import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CommandResult:
    """Result of a command execution."""

    returncode: int
    stdout: str
    stderr: str

    @property
    def success(self) -> bool:
        """True if command succeeded (returncode 0)."""
        return self.returncode == 0


@dataclass
class PortInfo:
    """Information about a port in use."""

    pid: int
    process_name: str
    port: int


@dataclass
class LogLine:
    """A single log line with metadata."""

    content: str
    timestamp: str | None = None


@dataclass
class ClusterCredentials:
    """Database connection credentials."""

    username: str
    password: str
    host: str


@dataclass
class BritiveInfo:
    """Information returned by pybritive checkout."""

    username: str
    password: str
    host: str
    port: int


class KubectlTool(ABC):
    """Abstract kubectl tool for Kubernetes operations."""

    @abstractmethod
    async def cluster_info(self, context: str) -> CommandResult:
        """Get cluster information."""

    @abstractmethod
    async def exec_in_pod(self, context: str, namespace: str, deployment: str, command: list[str]) -> CommandResult:
        """Execute command in a pod."""

    @abstractmethod
    async def get_logs(self, context: str, namespace: str, deployment: str, since: str = "10s") -> list[LogLine]:
        """Get recent logs from a deployment."""

    @abstractmethod
    async def port_forward(
        self, context: str, namespace: str, resource: str, local_port: int, remote_port: int
    ) -> asyncio.subprocess.Process:
        """Start port forwarding process (returns running process)."""

    @abstractmethod
    async def get_pod_status(self, pod_name: str, context: str | None = None) -> CommandResult:
        """Get pod status."""

    @abstractmethod
    async def unset_cluster_ca(self, cluster_name: str) -> CommandResult:
        """Unset cluster certificate authority data."""


class GcloudTool(ABC):
    """Abstract gcloud tool for Google Cloud operations."""

    @abstractmethod
    async def get_cluster_credentials(self, project: str, cluster: str, region: str) -> CommandResult:
        """Get cluster credentials."""

    @abstractmethod
    async def set_cluster_server(self, cluster_name: str, server_url: str) -> CommandResult:
        """Set cluster server URL."""


class OnePasswordTool(ABC):
    """Abstract 1Password CLI tool."""

    @abstractmethod
    async def read_secret(self, reference: str) -> str:
        """Read a secret from 1Password."""


class LsofTool(ABC):
    """Abstract lsof tool for checking port usage."""

    @abstractmethod
    async def check_port(self, port: int) -> list[PortInfo]:
        """Check if a port is in use."""


class PybritiveTool(ABC):
    """Abstract pybritive tool for temporary database credentials."""

    @abstractmethod
    async def checkout(
        self, resource_path: str, pattern: str | None = None, database_name: str | None = None
    ) -> BritiveInfo:
        """Checkout temporary credentials from Britive."""


# Concrete implementations using actual subprocess calls


class ExternalKubectlTool(KubectlTool):
    """External kubectl tool using subprocess."""

    async def cluster_info(self, context: str) -> CommandResult:
        """Get cluster information."""
        return await self._run_command(["kubectl", "cluster-info", "--context", context])

    async def exec_in_pod(self, context: str, namespace: str, deployment: str, command: list[str]) -> CommandResult:
        """Execute command in a pod."""
        args = [
            "kubectl",
            "--context",
            context,
            "-n",
            namespace,
            "exec",
            "-it",
            f"deployment/{deployment}",
            "--",
        ] + command
        return await self._run_command(args)

    async def get_logs(self, context: str, namespace: str, deployment: str, since: str = "10s") -> list[LogLine]:
        """Get recent logs from a deployment."""
        result = await self._run_command(
            ["kubectl", "--context", context, "-n", namespace, "logs", f"deployment/{deployment}", "--since", since]
        )

        if not result.success:
            return []

        return [LogLine(content=line) for line in result.stdout.splitlines() if line.strip()]

    async def port_forward(
        self, context: str, namespace: str, resource: str, local_port: int, remote_port: int
    ) -> asyncio.subprocess.Process:
        """Start port forwarding process (returns running process)."""
        args = [
            "kubectl",
            "--context",
            context,
            "-n",
            namespace,
            "port-forward",
            resource,
            f"{local_port}:{remote_port}",
        ]

        process = await asyncio.create_subprocess_exec(*args)
        return process

    async def get_pod_status(self, pod_name: str, context: str | None = None) -> CommandResult:
        """Get pod status."""
        args = ["kubectl", "get", "pod", pod_name, "-o", "jsonpath={.status.phase}"]
        if context:
            args.extend(["--context", context])
        return await self._run_command(args)

    async def unset_cluster_ca(self, cluster_name: str) -> CommandResult:
        """Unset cluster certificate authority data."""
        return await self._run_command(
            ["kubectl", "config", "unset", f"clusters.{cluster_name}.certificate-authority-data"]
        )

    async def _run_command(self, args: list[str]) -> CommandResult:
        """Run a kubectl command and return result."""
        process = await asyncio.create_subprocess_exec(
            *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        return CommandResult(
            returncode=process.returncode or 0,
            stdout=stdout.decode() if stdout else "",
            stderr=stderr.decode() if stderr else "",
        )


class ExternalGcloudTool(GcloudTool):
    """External gcloud tool using subprocess."""

    async def get_cluster_credentials(self, project: str, cluster: str, region: str) -> CommandResult:
        """Get cluster credentials."""
        return await self._run_command(
            ["gcloud", "--project", project, "container", "clusters", "get-credentials", cluster, "--region", region]
        )

    async def set_cluster_server(self, cluster_name: str, server_url: str) -> CommandResult:
        """Set cluster server URL."""
        return await self._run_command(["kubectl", "config", "set-cluster", cluster_name, "--server", server_url])

    async def _run_command(self, args: list[str]) -> CommandResult:
        """Run a gcloud command and return result."""
        process = await asyncio.create_subprocess_exec(
            *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        return CommandResult(
            returncode=process.returncode or 0,
            stdout=stdout.decode() if stdout else "",
            stderr=stderr.decode() if stderr else "",
        )


class ExternalOnePasswordTool(OnePasswordTool):
    """External 1Password CLI tool using subprocess."""

    async def read_secret(self, reference: str) -> str:
        """Read a secret from 1Password."""
        process = await asyncio.create_subprocess_exec(
            "op", "read", reference, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            raise RuntimeError(f"Failed to read secret {reference}: {stderr.decode()}")

        return stdout.decode().strip()


class ExternalLsofTool(LsofTool):
    """External lsof tool using subprocess."""

    async def check_port(self, port: int) -> list[PortInfo]:
        """Check if a port is in use."""
        try:
            process = await asyncio.create_subprocess_exec(
                "lsof", "-i", f":{port}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )

            stdout, _ = await process.communicate()

            if process.returncode != 0:
                return []  # Port not in use

            lines = stdout.decode().splitlines()
            port_info: list[PortInfo] = []

            for line in lines[1:]:  # Skip header
                parts = line.split()
                if len(parts) >= 2:
                    port_info.append(
                        PortInfo(pid=int(parts[1]) if parts[1].isdigit() else 0, process_name=parts[0], port=port)
                    )

            return port_info

        except Exception:
            return []  # Error checking port, assume not in use


class ExternalPybritiveTool(PybritiveTool):
    """External pybritive tool using subprocess."""

    DEFAULT_PATTERN = r"""
        Temp\sMySQL\susername:\s*(?P<username>\S+).*
        Temp\spassword:\s*(?P<password>\S+).*
        For\s+(?:billing|log|orders)\s+in\s+usprod\s+connect\s+to\s+server:\s*(?P<host>[^\s]+)\s+port:(?P<port>\d+)
    """

    async def checkout(
        self, resource_path: str, pattern: str | None = None, database_name: str | None = None
    ) -> BritiveInfo:
        """Checkout temporary credentials from Britive."""
        import re

        import structlog

        log = structlog.get_logger()
        result = await self._run_command(["pybritive", "checkout", resource_path])

        if not result.success:
            log.error("Pybritive checkout failed", stderr=result.stderr, stdout=result.stdout)
            raise RuntimeError(f"Pybritive checkout failed: {result.stderr}")

        log.debug("Pybritive raw output", output=result.stdout)

        # Build database-specific pattern if database_name is provided
        if database_name and not pattern:
            checkout_pattern = rf"""
                Temp\sMySQL\susername:\s*(?P<username>\S+).*
                Temp\spassword:\s*(?P<password>\S+).*
                For\s+{re.escape(database_name)}\s+in\s+usprod\s+connect\s+to\s+server:\s*(?P<host>[^\s]+)\s+port:(?P<port>\d+)
            """
        else:
            # Use the provided pattern or the default
            checkout_pattern = pattern or self.DEFAULT_PATTERN

        match = re.search(checkout_pattern, result.stdout, re.DOTALL | re.VERBOSE)

        if not match:
            log.error(
                "Failed to parse pybritive output with regex",
                pattern=checkout_pattern,
                output=result.stdout,
            )
            raise RuntimeError(f"Failed to parse pybritive output: {result.stdout}")

        credentials = match.groupdict()
        username = credentials.get("username", "")
        password = credentials.get("password", "")
        host = credentials.get("host", "")
        port = int(credentials.get("port", 0))

        # Log parsed credentials (redacting password)
        log.info(
            "Pybritive credentials parsed",
            username=username,
            password="[REDACTED]" if password else "",
            host=host,
            port=port,
            resource_path=resource_path,
        )

        if not all([username, password, host, port]):
            log.error(
                "Failed to extract all credentials from pybritive output",
                missing_fields={
                    "username": bool(username),
                    "password": bool(password),
                    "host": bool(host),
                    "port": bool(port),
                },
            )
            raise RuntimeError(f"Failed to extract all credentials from pybritive output: {result.stdout}")

        return BritiveInfo(username=username, password=password, host=host, port=port)

    async def _run_command(self, args: list[str]) -> CommandResult:
        """Run a pybritive command and return result."""
        import asyncio

        process = await asyncio.create_subprocess_exec(
            *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        return CommandResult(
            returncode=process.returncode or 0,
            stdout=stdout.decode() if stdout else "",
            stderr=stderr.decode() if stderr else "",
        )


class Tools:
    """Container for all external tool dependencies with dependency injection."""

    def __init__(
        self,
        kubectl: KubectlTool | None = None,
        gcloud: GcloudTool | None = None,
        onepassword: OnePasswordTool | None = None,
        lsof: LsofTool | None = None,
        pybritive: PybritiveTool | None = None,
    ) -> None:
        """
        Initialize tools with optional dependency injection.

        Args:
            kubectl: kubectl tool (defaults to ExternalKubectlTool)
            gcloud: gcloud tool (defaults to ExternalGcloudTool)
            onepassword: 1Password CLI tool (defaults to ExternalOnePasswordTool)
            lsof: lsof tool (defaults to ExternalLsofTool)
            pybritive: pybritive tool (defaults to ExternalPybritiveTool)
        """
        self.kubectl = kubectl or ExternalKubectlTool()
        self.gcloud = gcloud or ExternalGcloudTool()
        self.onepassword = onepassword or ExternalOnePasswordTool()
        self.lsof = lsof or ExternalLsofTool()
        self.pybritive = pybritive or ExternalPybritiveTool()

    def is_mocked(self) -> bool:
        """Check if any of the tools are mocked (non-External implementations)."""
        return (
            not self.kubectl.__class__.__name__.startswith("External")
            or not self.gcloud.__class__.__name__.startswith("External")
            or not self.onepassword.__class__.__name__.startswith("External")
            or not self.lsof.__class__.__name__.startswith("External")
            or not self.pybritive.__class__.__name__.startswith("External")
        )
