from enum import Enum


class ApiRevShareAbstractionRevenueShareType(str, Enum):
    APP_1P = "APP_1P"
    APP_3P = "APP_3P"
    APP_CUSTOM = "APP_CUSTOM"
    CELLULAR = "CELLULAR"
    DEVICE_PLAN = "DEVICE_PLAN"
    DEV_CUSTOM = "DEV_CUSTOM"

    def __str__(self) -> str:
        return str(self.value)
