from enum import Enum


class ApiManagedItemCriteria(str, Enum):
    MERCHANT = "MERCHANT"
    RESELLER = "RESELLER"

    def __str__(self) -> str:
        return str(self.value)
