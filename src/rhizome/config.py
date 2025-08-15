from dataclasses import dataclass
from pathlib import Path

from xdg_base_dirs import xdg_state_home


@dataclass
class Home:
    """
    Rhizome stores state data in the local filesystem.
    A 'Home' object contains the path where it stores state information.

    To create a sandboxed rhizome for testing, initialize rhizome with
    a 'Home' object that is separate from the XDG recommended directory.
    """

    state: Path = xdg_state_home() / "rhizome"

    def __post_init__(self) -> None:
        self.mkdirs()

    @staticmethod
    def sandbox(parent: Path | str) -> "Home":
        if isinstance(parent, str):
            parent = Path(parent)
        return Home(state=parent / "state" / "rhizome")

    def mkdirs(self) -> None:
        self.state.mkdir(parents=True, exist_ok=True)

    def set_port(self, port: int) -> None:
        """Store the server port number."""
        (self.state / "port").write_text(str(port))

    def get_port(self) -> int | None:
        """Retrieve the stored server port number."""
        port_file = self.state / "port"
        if port_file.exists():
            return int(port_file.read_text().strip())
        return None