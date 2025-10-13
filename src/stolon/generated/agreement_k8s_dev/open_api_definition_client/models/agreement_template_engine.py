from enum import Enum


class AgreementTemplateEngine(str, Enum):
    HANDLEBARS = "HANDLEBARS"
    PLAINTEXT = "PLAINTEXT"
    STATIC = "STATIC"

    def __str__(self) -> str:
        return str(self.value)
