"""
Expected data for auto_debit_no_auth_config table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.auto_debit_no_auth_config_v1 import AutoDebitNoAuthConfigV1


class AutoDebitNoAuthConfigNaProd(Emplacement[AutoDebitNoAuthConfigV1]):
    """Expected data for AutoDebitNoAuthConfig in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AutoDebitNoAuthConfigV1:
        """Get expected auto_debit_no_auth_config data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_auto_debit_no_auth_config.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return AutoDebitNoAuthConfigV1.model_validate(data)