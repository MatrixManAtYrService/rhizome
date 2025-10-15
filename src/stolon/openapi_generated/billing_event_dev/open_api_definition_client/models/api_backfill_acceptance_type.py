from enum import Enum


class ApiBackfillAcceptanceType(str, Enum):
    BILLING = "BILLING"
    CELLULAR_ADVANCE = "CELLULAR_ADVANCE"
    CELLULAR_ARREARS = "CELLULAR_ARREARS"

    def __str__(self) -> str:
        return str(self.value)
