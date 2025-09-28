"""
Expected data for merchant_role table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_role_v1 import MerchantRoleV1


class MerchantRoleNaProd(Emplacement[MerchantRoleV1]):
    """Expected data for MerchantRole in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantRoleV1:
        """Get expected merchant_role data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_role.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantRoleV1.model_validate(data)
