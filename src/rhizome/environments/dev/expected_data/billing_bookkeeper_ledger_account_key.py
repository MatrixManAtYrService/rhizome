"""Expected data for ledger_account_key table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.ledger_account_key_v1 import LedgerAccountKeyV1


class LedgerAccountKeyDev(Emplacement[LedgerAccountKeyV1]):
    """Expected data for LedgerAccountKey in dev environment."""

    @classmethod
    def get_expected(cls) -> LedgerAccountKeyV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_ledger_account_key.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return LedgerAccountKeyV1.model_validate(data)
