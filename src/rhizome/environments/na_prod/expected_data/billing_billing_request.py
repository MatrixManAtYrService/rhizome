"""
Expected data for billing_request table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.billing_request_v1 import BillingRequestV1


class BillingRequestNaProd(Emplacement[BillingRequestV1]):
    """Expected data for BillingRequest in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BillingRequestV1:
        """Get expected billing_request data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_billing_request.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BillingRequestV1.model_validate(data)
