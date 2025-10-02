from enum import Enum


class ApiConsumerFailureConsumerSource(str, Enum):
    AGREEMENT = "AGREEMENT"
    MLC = "MLC"

    def __str__(self) -> str:
        return str(self.value)
