from enum import Enum


class MerchantPlanType(str, Enum):
    CLASSIC = "CLASSIC"
    DINING = "DINING"
    NO_HARDWARE = "NO_HARDWARE"
    PAYMENTS = "PAYMENTS"
    PAYMENTS_PLUS = "PAYMENTS_PLUS"
    QSR = "QSR"
    REGISTER = "REGISTER"
    REGISTER_LITE = "REGISTER_LITE"
    RETAIL = "RETAIL"
    SERVICES = "SERVICES"

    def __str__(self) -> str:
        return str(self.value)
