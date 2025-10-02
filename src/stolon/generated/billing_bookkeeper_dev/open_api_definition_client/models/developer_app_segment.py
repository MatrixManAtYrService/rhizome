from enum import Enum


class DeveloperAppSegment(str, Enum):
    APP_MARKET = "APP_MARKET"
    CLOVER_GO = "CLOVER_GO"
    MERCHANT_COMPANION = "MERCHANT_COMPANION"
    SEMI_INT = "SEMI_INT"

    def __str__(self) -> str:
        return str(self.value)
