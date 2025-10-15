from enum import Enum


class MerchantPlanPricingModel(str, Enum):
    FREE = "FREE"
    PER_DEVICE = "PER_DEVICE"
    PER_MONTH = "PER_MONTH"
    SUPPRESSED = "SUPPRESSED"
    TIERED = "TIERED"

    def __str__(self) -> str:
        return str(self.value)
