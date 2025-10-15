from enum import Enum


class ApiMerchantAcceptanceAction(str, Enum):
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    OFFBOARDED = "OFFBOARDED"
    REREQUESTED = "REREQUESTED"
    REVOKED = "REVOKED"
    STALE = "STALE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
