"""Expected data for fee_rate_report_action_error table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_rate_report_action_error_v1 import FeeRateReportActionErrorV1


class FeeRateReportActionErrorDemo(Emplacement[FeeRateReportActionErrorV1]):
    """Expected data for FeeRateReportActionError in demo environment."""

    @classmethod
    def get_expected(cls) -> FeeRateReportActionErrorV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_fee_rate_report_action_error.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return FeeRateReportActionErrorV1.model_validate(data)
