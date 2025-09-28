"""
Expected data for biie_file_instance_request table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.biie_file_instance_request_v1 import BiieFileInstanceRequestV1


class BiieFileInstanceRequestNaProd(Emplacement[BiieFileInstanceRequestV1]):
    """Expected data for BiieFileInstanceRequest in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BiieFileInstanceRequestV1:
        """Get expected biie_file_instance_request data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_biie_file_instance_request.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BiieFileInstanceRequestV1.model_validate(data)
