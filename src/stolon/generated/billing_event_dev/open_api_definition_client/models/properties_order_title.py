from enum import Enum


class PropertiesOrderTitle(str, Enum):
    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
