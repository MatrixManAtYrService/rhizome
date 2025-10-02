from enum import Enum


class LedgerJournalCreditDebitInd(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    def __str__(self) -> str:
        return str(self.value)
