from enum import Enum


class JobStateName(str, Enum):
    DELETED = "DELETED"
    ENQUEUED = "ENQUEUED"
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"
    SCHEDULED = "SCHEDULED"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
