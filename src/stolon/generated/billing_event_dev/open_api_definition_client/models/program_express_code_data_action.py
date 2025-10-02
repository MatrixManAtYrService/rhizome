from enum import Enum


class ProgramExpressCodeDataAction(str, Enum):
    CREATE = "CREATE"
    DELETE = "DELETE"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
