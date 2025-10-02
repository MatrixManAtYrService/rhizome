from enum import Enum


class BillingHierarchyEntityType(str, Enum):
    ARCHETYPE = "ARCHETYPE"
    DEVELOPER = "DEVELOPER"
    MERCHANT = "MERCHANT"
    PSEUDO = "PSEUDO"
    RESELLER = "RESELLER"

    def __str__(self) -> str:
        return str(self.value)
