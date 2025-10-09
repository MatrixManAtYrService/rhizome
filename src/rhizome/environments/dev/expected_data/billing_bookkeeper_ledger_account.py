"""Expected data for ledger_account table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.ledger_account_v1 import LedgerAccountV1


class LedgerAccountDev(Emplacement[LedgerAccountV1]):
    """Expected data for LedgerAccount in dev environment."""

    @classmethod
    def get_expected(cls) -> LedgerAccountV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_ledger_account.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return LedgerAccountV1.model_validate(data)
