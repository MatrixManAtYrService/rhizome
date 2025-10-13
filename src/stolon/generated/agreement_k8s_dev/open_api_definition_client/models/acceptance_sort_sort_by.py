from enum import Enum


class AcceptanceSortSortBy(str, Enum):
    CREATEDTIME = "createdTime"
    MODIFIEDTIME = "modifiedTime"

    def __str__(self) -> str:
        return str(self.value)
