from enum import Enum


class ApiTestMerchantCriteriaType(str, Enum):
    EMAIL = "EMAIL"
    SOURCE = "SOURCE"

    def __str__(self) -> str:
        return str(self.value)
