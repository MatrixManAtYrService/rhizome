from enum import Enum


class ApiEventFilterAction(str, Enum):
    CAPTURE = "CAPTURE"
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"

    def __str__(self) -> str:
        return str(self.value)
