"""
Expected data for payment_processor table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.payment_processor_v1 import PaymentProcessorV1


class PaymentProcessorDemo(Emplacement[PaymentProcessorV1]):
    """Expected data for PaymentProcessor in demo environment."""

    @classmethod
    def get_expected(cls) -> PaymentProcessorV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_payment_processor.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return PaymentProcessorV1.model_validate(data)
