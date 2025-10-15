from enum import Enum


class MerchantPlanMccMatch(str, Enum):
    CURRENT = "CURRENT"
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"

    def __str__(self) -> str:
        return str(self.value)
