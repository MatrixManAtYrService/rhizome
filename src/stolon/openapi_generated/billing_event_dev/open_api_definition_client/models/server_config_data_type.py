from enum import Enum


class ServerConfigDataType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DATE_TIME = "DATE_TIME"
    DECIMAL = "DECIMAL"
    EMAIL = "EMAIL"
    JSON = "JSON"
    LIST = "LIST"
    NUMBER = "NUMBER"
    PERCENTAGE = "PERCENTAGE"
    TEXT = "TEXT"
    URL = "URL"
    UUID13 = "UUID13"
    UUID26 = "UUID26"

    def __str__(self) -> str:
        return str(self.value)
