"""
Expected data for reseller_usage_job_config table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.reseller_usage_job_config_v1 import ResellerUsageJobConfigV1


class ResellerUsageJobConfigNaProd(Emplacement[ResellerUsageJobConfigV1]):
    """Expected data for ResellerUsageJobConfig in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ResellerUsageJobConfigV1:
        """Get expected reseller_usage_job_config data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_reseller_usage_job_config.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return ResellerUsageJobConfigV1.model_validate(data)
