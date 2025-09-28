"""
Expected data for payment_processor table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.payment_processor import PaymentProcessor


class PaymentProcessorNaProd(Emplacement[PaymentProcessor]):
    """Expected data for PaymentProcessor in na_prod environment."""

    @classmethod
    def get_expected(cls) -> PaymentProcessor:
        """Get expected payment_processor data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_payment_processor.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return PaymentProcessor.model_validate(data)
