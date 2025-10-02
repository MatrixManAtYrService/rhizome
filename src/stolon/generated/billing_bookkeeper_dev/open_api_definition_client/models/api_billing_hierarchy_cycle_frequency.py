from enum import Enum


class ApiBillingHierarchyCycleFrequency(str, Enum):
    MONTHLY = "MONTHLY"
    NO_BILL = "NO_BILL"

    def __str__(self) -> str:
        return str(self.value)
