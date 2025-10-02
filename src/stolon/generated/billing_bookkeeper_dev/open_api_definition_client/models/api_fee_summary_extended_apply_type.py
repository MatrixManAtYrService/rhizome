from enum import Enum


class ApiFeeSummaryExtendedApplyType(str, Enum):
    BOTH = "BOTH"
    DEFAULT = "DEFAULT"
    FLAT = "FLAT"
    NONE = "NONE"
    PERCENTAGE = "PERCENTAGE"
    PER_ITEM = "PER_ITEM"

    def __str__(self) -> str:
        return str(self.value)
