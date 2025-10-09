"""Expected data for fee_code_ledger_account table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_code_ledger_account_v1 import FeeCodeLedgerAccountV1


class FeeCodeLedgerAccountDemo(Emplacement[FeeCodeLedgerAccountV1]):
    """Expected data for FeeCodeLedgerAccount in demo environment."""

    @classmethod
    def get_expected(cls) -> FeeCodeLedgerAccountV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_fee_code_ledger_account.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return FeeCodeLedgerAccountV1.model_validate(data)
