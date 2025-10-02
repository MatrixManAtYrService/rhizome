from enum import Enum


class ApiAutoAdjustRuleRuleStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    DEPRECATED = "DEPRECATED"
    SETUP = "SETUP"

    def __str__(self) -> str:
        return str(self.value)
