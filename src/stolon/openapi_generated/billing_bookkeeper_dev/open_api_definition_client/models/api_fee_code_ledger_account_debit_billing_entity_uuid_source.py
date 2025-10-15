from enum import Enum


class ApiFeeCodeLedgerAccountDebitBillingEntityUuidSource(str, Enum):
    CLOVER = "CLOVER"
    ROLLUP_1 = "ROLLUP_1"
    ROLLUP_2 = "ROLLUP_2"
    ROLLUP_3 = "ROLLUP_3"
    TRANSACTION = "TRANSACTION"

    def __str__(self) -> str:
        return str(self.value)
