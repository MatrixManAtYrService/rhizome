from enum import Enum


class MerchantAccounStatusChangeDataSource(str, Enum):
    BACKFILL_API = "BACKFILL_API"
    BOARDING_MESSAGE = "BOARDING_MESSAGE"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
