from enum import Enum


class ApiLedgerJournalProjectionCreditDebitInd(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    def __str__(self) -> str:
        return str(self.value)
