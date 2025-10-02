from enum import Enum


class ApiTierPricingTieredBasis(str, Enum):
    BOTH = "BOTH"
    QUANTITY = "QUANTITY"
    VOLUME = "VOLUME"

    def __str__(self) -> str:
        return str(self.value)
