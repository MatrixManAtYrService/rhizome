from enum import Enum


class ApiEventFilterCriteria(str, Enum):
    ABBS = "ABBS"
    ABBS_COLLECTION = "ABBS_COLLECTION"
    APP = "APP"
    DEVELOPER_APP = "DEVELOPER_APP"
    MERCHANT = "MERCHANT"
    OFFBOARDING_RESELLER = "OFFBOARDING_RESELLER"
    RESELLER = "RESELLER"

    def __str__(self) -> str:
        return str(self.value)
