from enum import Enum


class ComplianceType(str, Enum):
    HIPAA = "HIPAA"

    def __str__(self) -> str:
        return str(self.value)
