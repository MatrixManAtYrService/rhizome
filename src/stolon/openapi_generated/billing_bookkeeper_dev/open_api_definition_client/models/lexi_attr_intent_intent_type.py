from enum import Enum


class LexiAttrIntentIntentType(str, Enum):
    ADD = "ADD"
    DELETE = "DELETE"
    UNDELETE = "UNDELETE"

    def __str__(self) -> str:
        return str(self.value)
