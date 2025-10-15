from enum import Enum


class DeviceDataActivationType(str, Enum):
    ACTIVATION = "ACTIVATION"
    REACTIVATION = "REACTIVATION"

    def __str__(self) -> str:
        return str(self.value)
