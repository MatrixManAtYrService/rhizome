from enum import Enum


class ApiSettlementExportPayableReceivable(str, Enum):
    PAYABLE = "PAYABLE"
    RECEIVABLE = "RECEIVABLE"

    def __str__(self) -> str:
        return str(self.value)
