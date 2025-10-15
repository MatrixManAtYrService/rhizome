from enum import Enum


class ApiEventIgnoredIgnoreReason(str, Enum):
    NEWER_DATE_BREAK = "NEWER_DATE_BREAK"
    NO_BILLABLE_CHANGES = "NO_BILLABLE_CHANGES"
    POST_CLOSURE = "POST_CLOSURE"
    PRE_ACCEPTANCE = "PRE_ACCEPTANCE"
    UNKNOWN_MERCHANT = "UNKNOWN_MERCHANT"

    def __str__(self) -> str:
        return str(self.value)
