from enum import Enum


class ApiBillingScheduleFrequency(str, Enum):
    MONTHLY = "MONTHLY"
    NO_BILL = "NO_BILL"

    def __str__(self) -> str:
        return str(self.value)
