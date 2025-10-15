from enum import Enum


class ApiTieredRuleTieredModel(str, Enum):
    APPLY_TO_ALL = "APPLY_TO_ALL"
    APPLY_TO_TIER = "APPLY_TO_TIER"

    def __str__(self) -> str:
        return str(self.value)
