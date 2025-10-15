from enum import Enum


class ApiMonetaryAdjustmentRuleType(str, Enum):
    AUTO_ADJUST = "AUTO_ADJUST"
    TIERED = "TIERED"

    def __str__(self) -> str:
        return str(self.value)
