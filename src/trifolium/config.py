"""Trifolium unified configuration using XDG base directories."""

import json
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from pydantic import BaseModel
from xdg_base_dirs import xdg_config_home, xdg_state_home


class InternalTokenPreference(StrEnum):
    """User preference for internal token handling."""

    AUTO = "auto"
    PROMPT = "prompt"


class TrifoliumConfig(BaseModel):
    """Configuration settings for Trifolium components."""

    internal_token_preference: InternalTokenPreference = InternalTokenPreference.PROMPT


@dataclass
class Home:
    """
    Trifolium stores state and configuration data in the local filesystem using XDG directories.

    - Configuration: ~/.config/trifolium/ (user preferences, settings)
    - State: ~/.local/state/trifolium/ (runtime data, ports, temporary files)

    To create a sandboxed environment for testing, initialize with custom paths.
    """

    config: Path = xdg_config_home() / "trifolium"
    state: Path = xdg_state_home() / "trifolium"

    def __post_init__(self) -> None:
        self.mkdirs()

    @staticmethod
    def sandbox(parent: Path | str) -> "Home":
        """Create a sandboxed Home for testing."""
        if isinstance(parent, str):
            parent = Path(parent)
        return Home(config=parent / "config" / "trifolium", state=parent / "state" / "trifolium")

    def mkdirs(self) -> None:
        """Ensure all directories exist."""
        self.config.mkdir(parents=True, exist_ok=True)
        self.state.mkdir(parents=True, exist_ok=True)

    def set_port(self, port: int) -> None:
        """Store the rhizome server port number."""
        (self.state / "rhizome_port").write_text(str(port))

    def get_port(self) -> int | None:
        """Retrieve the stored rhizome server port number."""
        port_file = self.state / "rhizome_port"
        if port_file.exists():
            return int(port_file.read_text().strip())
        return None

    def load_config(self) -> TrifoliumConfig:
        """Load configuration from trifolium.json, creating default if it doesn't exist."""
        config_file = self.config / "trifolium.json"

        if config_file.exists():
            try:
                config_data = json.loads(config_file.read_text())
                return TrifoliumConfig.model_validate(config_data)
            except (json.JSONDecodeError, ValueError):
                # If config is corrupted, fall back to default
                pass

        # Create default config
        default_config = TrifoliumConfig()
        self.save_config(default_config)
        return default_config

    def save_config(self, config: TrifoliumConfig) -> None:
        """Save configuration to trifolium.json."""
        config_file = self.config / "trifolium.json"
        config_file.write_text(config.model_dump_json(indent=2))
