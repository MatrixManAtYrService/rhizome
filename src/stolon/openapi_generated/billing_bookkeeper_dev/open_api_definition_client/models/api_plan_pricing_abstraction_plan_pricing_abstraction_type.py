from enum import Enum


class ApiPlanPricingAbstractionPlanPricingAbstractionType(str, Enum):
    CSR = "CSR"
    CUSTOM = "CUSTOM"
    ESSENTIALS = "ESSENTIALS"
    PAYMENTS = "PAYMENTS"
    PAYMENTS_HIPAA = "PAYMENTS_HIPAA"
    REGISTER = "REGISTER"
    RETAIL = "RETAIL"
    SERVICES = "SERVICES"
    STARTER = "STARTER"
    TSR = "TSR"

    def __str__(self) -> str:
        return str(self.value)
