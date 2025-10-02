from enum import Enum


class ApiAppRatesEventParty(str, Enum):
    FIRST = "FIRST"
    THIRD = "THIRD"

    def __str__(self) -> str:
        return str(self.value)
