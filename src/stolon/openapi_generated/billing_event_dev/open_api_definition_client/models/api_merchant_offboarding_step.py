from enum import Enum


class ApiMerchantOffboardingStep(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CANCELED = "CANCELED"
    IMMEDIATE = "IMMEDIATE"
    INITIATE = "INITIATE"
    OFFBOARD = "OFFBOARD"
    PROCESSED = "PROCESSED"
    PROCESSING = "PROCESSING"
    REMINDER = "REMINDER"
    REOPENED = "REOPENED"
    UNBLOCKED = "UNBLOCKED"

    def __str__(self) -> str:
        return str(self.value)
