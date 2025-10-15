from enum import Enum


class ApiMerchantEvolutionBillableMerchantType(str, Enum):
    DEMO = "DEMO"
    TEST = "TEST"

    def __str__(self) -> str:
        return str(self.value)
