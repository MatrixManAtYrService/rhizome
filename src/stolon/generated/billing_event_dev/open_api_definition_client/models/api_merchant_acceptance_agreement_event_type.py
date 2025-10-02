from enum import Enum


class ApiMerchantAcceptanceAgreementEventType(str, Enum):
    CREATED = "CREATED"
    INVALIDATED = "INVALIDATED"

    def __str__(self) -> str:
        return str(self.value)
