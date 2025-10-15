from enum import Enum


class SchemaType(str, Enum):
    ARRAY = "ARRAY"
    BOOLEAN = "BOOLEAN"
    BYTES = "BYTES"
    DOUBLE = "DOUBLE"
    ENUM = "ENUM"
    FIXED = "FIXED"
    FLOAT = "FLOAT"
    INT = "INT"
    LONG = "LONG"
    MAP = "MAP"
    NULL = "NULL"
    RECORD = "RECORD"
    STRING = "STRING"
    UNION = "UNION"

    def __str__(self) -> str:
        return str(self.value)
