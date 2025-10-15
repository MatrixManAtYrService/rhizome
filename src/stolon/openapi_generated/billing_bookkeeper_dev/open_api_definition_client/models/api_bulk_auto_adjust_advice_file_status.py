from enum import Enum


class ApiBulkAutoAdjustAdviceFileStatus(str, Enum):
    DUPLICATE = "DUPLICATE"
    ERROR = "ERROR"
    LOADED = "LOADED"
    LOADING = "LOADING"
    PROCESSED = "PROCESSED"
    PROCESSING = "PROCESSING"
    VALIDATED = "VALIDATED"
    VALIDATING = "VALIDATING"

    def __str__(self) -> str:
        return str(self.value)
