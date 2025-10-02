from enum import Enum


class DeveloperAppApprovalStatus(str, Enum):
    APPROVED = "APPROVED"
    APPROVED_PENDING_SIGNING = "APPROVED_PENDING_SIGNING"
    DENIED = "DENIED"
    NEW = "NEW"
    PENDING = "PENDING"
    PUBLISHED = "PUBLISHED"

    def __str__(self) -> str:
        return str(self.value)
