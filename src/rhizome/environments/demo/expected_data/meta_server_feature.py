"""
Expected data for server_feature table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.server_feature_v1 import ServerFeatureV1


class ServerFeatureDemo(Emplacement[ServerFeatureV1]):
    """Expected data for ServerFeature in demo environment."""

    @classmethod
    def get_expected(cls) -> ServerFeatureV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_server_feature.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ServerFeatureV1.model_validate(data)
