from enum import Enum


class ApiLedgerAccountKeyLedgerAccountType(str, Enum):
    ASSET = "ASSET"
    EQUITY = "EQUITY"
    EXPENSE = "EXPENSE"
    LIABILITY = "LIABILITY"
    REVENUE = "REVENUE"

    def __str__(self) -> str:
        return str(self.value)
