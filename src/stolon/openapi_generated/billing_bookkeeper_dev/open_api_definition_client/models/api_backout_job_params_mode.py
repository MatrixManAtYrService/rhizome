from enum import Enum


class ApiBackoutJobParamsMode(str, Enum):
    APPLY = "APPLY"
    PREVIEW = "PREVIEW"

    def __str__(self) -> str:
        return str(self.value)
