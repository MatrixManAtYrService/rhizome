"""
Expected data for fee_exception table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.fee_exception_v1 import FeeExceptionV1


class FeeExceptionNaProd(Emplacement[FeeExceptionV1]):
    """Expected data for FeeException in na_prod environment."""

    @classmethod
    def get_expected(cls) -> FeeExceptionV1:
        """Get expected fee_exception data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_fee_exception.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return FeeExceptionV1.model_validate(data)
