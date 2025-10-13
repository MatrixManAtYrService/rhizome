from enum import Enum


class AcceptanceSource(str, Enum):
    CLOVERGO = "CLOVERGO"
    DEVICE = "DEVICE"
    WEB = "WEB"

    def __str__(self) -> str:
        return str(self.value)
