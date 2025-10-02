from enum import Enum


class SettlementPayableReceivable(str, Enum):
    PAYABLE = "PAYABLE"
    RECEIVABLE = "RECEIVABLE"

    def __str__(self) -> str:
        return str(self.value)
