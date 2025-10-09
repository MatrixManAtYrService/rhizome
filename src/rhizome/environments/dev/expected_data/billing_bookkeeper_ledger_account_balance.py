"""Expected data for ledger_account_balance table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.ledger_account_balance_v1 import LedgerAccountBalanceV1


class LedgerAccountBalanceDev(Emplacement[LedgerAccountBalanceV1]):
    """Expected data for LedgerAccountBalance in dev environment."""

    @classmethod
    def get_expected(cls) -> LedgerAccountBalanceV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_ledger_account_balance.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return LedgerAccountBalanceV1.model_validate(data)
