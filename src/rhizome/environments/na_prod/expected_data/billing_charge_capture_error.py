"""
Expected data for charge_capture_error table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.charge_capture_error_v1 import ChargeCaptureErrorV1


class ChargeCaptureErrorNaProd(Emplacement[ChargeCaptureErrorV1]):
    """Expected data for ChargeCaptureError in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ChargeCaptureErrorV1:
        """Get expected charge_capture_error data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_charge_capture_error.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return ChargeCaptureErrorV1.model_validate(data)
