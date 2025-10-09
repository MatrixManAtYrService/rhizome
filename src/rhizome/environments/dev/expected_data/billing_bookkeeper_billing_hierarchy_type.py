"""Expected data for billing_hierarchy_type table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.billing_hierarchy_type_v1 import BillingHierarchyTypeV1


class BillingHierarchyTypeDev(Emplacement[BillingHierarchyTypeV1]):
    """Expected data for BillingHierarchyType in dev environment."""

    @classmethod
    def get_expected(cls) -> BillingHierarchyTypeV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_billing_hierarchy_type.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return BillingHierarchyTypeV1.model_validate(data)
