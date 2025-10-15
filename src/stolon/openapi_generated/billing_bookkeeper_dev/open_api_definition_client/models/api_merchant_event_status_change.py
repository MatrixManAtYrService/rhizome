from enum import Enum


class ApiMerchantEventStatusChange(str, Enum):
    CLOSE = "CLOSE"
    REOPENED = "REOPENED"

    def __str__(self) -> str:
        return str(self.value)
