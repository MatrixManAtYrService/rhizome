"""
Expected data for app_bundle table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.app_bundle_v1 import AppBundleV1


class AppBundleNaProd(Emplacement[AppBundleV1]):
    """Expected data for AppBundle in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AppBundleV1:
        """Get expected app_bundle data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_app_bundle.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return AppBundleV1.model_validate(data)
