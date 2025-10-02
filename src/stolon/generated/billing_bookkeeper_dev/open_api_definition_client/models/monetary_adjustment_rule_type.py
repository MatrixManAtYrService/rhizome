from enum import Enum


class MonetaryAdjustmentRuleType(str, Enum):
    AUTO_ADJUST = "AUTO_ADJUST"
    TIERED = "TIERED"

    def __str__(self) -> str:
        return str(self.value)
