from enum import Enum


class ApiLedgerJournalProjectionRefUuidType(str, Enum):
    FEE_SUMMARY = "FEE_SUMMARY"
    FEE_TAX = "FEE_TAX"
    SETTLE_EXPORT = "SETTLE_EXPORT"
    SETTLE_IMPORT = "SETTLE_IMPORT"

    def __str__(self) -> str:
        return str(self.value)
