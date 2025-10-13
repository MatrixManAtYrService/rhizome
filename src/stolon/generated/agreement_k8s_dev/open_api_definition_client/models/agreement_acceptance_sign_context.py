from enum import Enum


class AgreementAcceptanceSignContext(str, Enum):
    ACCOUNT = "ACCOUNT"
    ACCOUNT_MERCHANT = "ACCOUNT_MERCHANT"
    MERCHANT = "MERCHANT"

    def __str__(self) -> str:
        return str(self.value)
