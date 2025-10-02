from enum import Enum


class ApiFeeRateReportActionErrorActionType(str, Enum):
    APP_METER = "APP_METER"
    APP_SUB = "APP_SUB"
    CELLULAR = "CELLULAR"
    MISC = "MISC"
    PLAN = "PLAN"
    REVENUE = "REVENUE"

    def __str__(self) -> str:
        return str(self.value)
