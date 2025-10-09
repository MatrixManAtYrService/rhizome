"""Expected data for skip_fee_category_lexi_tag table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.skip_fee_category_lexi_tag_v1 import SkipFeeCategoryLexiTagV1


class SkipFeeCategoryLexiTagDev(Emplacement[SkipFeeCategoryLexiTagV1]):
    """Expected data for SkipFeeCategoryLexiTag in dev environment."""

    @classmethod
    def get_expected(cls) -> SkipFeeCategoryLexiTagV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_skip_fee_category_lexi_tag.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return SkipFeeCategoryLexiTagV1.model_validate(data)
