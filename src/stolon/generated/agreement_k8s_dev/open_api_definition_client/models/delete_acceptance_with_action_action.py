from enum import Enum


class DeleteAcceptanceWithActionAction(str, Enum):
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    OFFBOARDED = "OFFBOARDED"
    REREQUESTED = "REREQUESTED"
    REVOKED = "REVOKED"
    STALE = "STALE"

    def __str__(self) -> str:
        return str(self.value)
