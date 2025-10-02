from enum import Enum


class ApiLedgerJournalCreditDebitInd(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    def __str__(self) -> str:
        return str(self.value)
