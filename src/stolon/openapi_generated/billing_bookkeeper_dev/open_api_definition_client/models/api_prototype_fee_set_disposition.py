from enum import Enum


class ApiPrototypeFeeSetDisposition(str, Enum):
    DRAFT = "DRAFT"
    PROMOTED = "PROMOTED"
    REMOVED = "REMOVED"

    def __str__(self) -> str:
        return str(self.value)
