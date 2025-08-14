"""
Rhizome client for communicating with the rhizome server to manage port forwarding.

This module provides the client interface for requesting port forwards from the 
rhizome server and getting connection handles back.
"""

import time
from dataclasses import dataclass
from pathlib import Path

import httpx

from rhizome.config import Home


@dataclass
class Handle:
    """
    Database connection handle returned by rhizome.
    
    Contains the connection string and port information needed to connect
    to a database through kubectl port-forward managed by rhizome server.
    """
    connection_string: str
    local_port: int
    sql_connection: str  # The original SQL connection name
    
    def __post_init__(self) -> None:
        """Validate that the connection is available."""
        # TODO: Add connection validation logic if needed
        pass


class RhizomeClient:
    """Client for communicating with the rhizome server."""
    
    def __init__(self, home: Home | None = None) -> None:
        self.home = home or Home()
        self._base_url: str | None = None
    
    @property
    def base_url(self) -> str:
        """Get the rhizome server URL from the port file."""
        if self._base_url is None:
            port = self.home.get_port()
            if port is None:
                raise RuntimeError(
                    "Rhizome server port not found. Make sure the rhizome server is running."
                )
            self._base_url = f"http://0.0.0.0:{port}"
        return self._base_url
    
    def request_portforward(
        self, 
        kube_context: str,
        kube_namespace: str, 
        kube_deployment: str,
        sql_connection: str,
        local_port: int = 3306
    ) -> Handle:
        """
        Request a port forward from the rhizome server.
        
        Args:
            kube_context: Kubernetes context name
            kube_namespace: Kubernetes namespace
            kube_deployment: Kubernetes deployment name
            sql_connection: SQL connection string (e.g., "clover-prod-databases:us-central1:billing-bookkeeper")
            local_port: Local port to forward to (default: 3306)
            
        Returns:
            Handle: Connection handle with connection string and port info
        """
        # Make request to rhizome server to start port forward
        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/portforward",
                json={
                    "kube_context": kube_context,
                    "kube_namespace": kube_namespace,
                    "kube_deployment": kube_deployment,
                    "sql_connection": sql_connection,
                    "local_port": local_port
                }
            )
            response.raise_for_status()
            
        # Wait a moment for the port forward to establish
        time.sleep(2)
        
        # Build connection string
        connection_string = f"mysql://localhost:{local_port}"
        
        return Handle(
            connection_string=connection_string,
            local_port=local_port,
            sql_connection=sql_connection
        )
    
    def request_sleeper(self, iterations: int = 5) -> Handle:
        """
        Request a sleeper process from the rhizome server.
        
        Args:
            iterations: Number of times the sleeper should count (default: 5)
            
        Returns:
            Handle: Connection handle with sleeper process info
        """
        # Make request to rhizome server to start sleeper
        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/sleeper",
                json={"iterations": iterations}
            )
            response.raise_for_status()
            
        # Wait a moment for the process to start
        time.sleep(0.1)
        
        # Return a handle (sleeper doesn't have a real connection string)
        return Handle(
            connection_string=f"sleeper://localhost/test",
            local_port=0,  # No actual port for sleeper
            sql_connection=f"sleeper-{iterations}-iterations"
        )


# Global client instance
client = RhizomeClient()