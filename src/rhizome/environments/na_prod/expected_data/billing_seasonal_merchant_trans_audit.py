"""
Expected data for seasonal_merchant_trans_audit table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.seasonal_merchant_trans_audit_v1 import SeasonalMerchantTransAuditV1


class SeasonalMerchantTransAuditNaProd(Emplacement[SeasonalMerchantTransAuditV1]):
    """Expected data for SeasonalMerchantTransAudit in na_prod environment."""

    @classmethod
    def get_expected(cls) -> SeasonalMerchantTransAuditV1:
        """Get expected seasonal_merchant_trans_audit data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_seasonal_merchant_trans_audit.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return SeasonalMerchantTransAuditV1.model_validate(data)
