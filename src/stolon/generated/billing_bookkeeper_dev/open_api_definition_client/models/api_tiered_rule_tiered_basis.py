from enum import Enum


class ApiTieredRuleTieredBasis(str, Enum):
    BOTH = "BOTH"
    QUANTITY = "QUANTITY"
    VOLUME = "VOLUME"

    def __str__(self) -> str:
        return str(self.value)
