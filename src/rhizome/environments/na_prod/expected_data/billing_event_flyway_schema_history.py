"""
Expected data for flyway_schema_history table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.flyway_schema_history_v1 import FlywaySchemaHistoryV1


class FlywaySchemaHistoryNaProd(Emplacement[FlywaySchemaHistoryV1]):
    """Expected data for FlywaySchemaHistory in na_prod environment."""

    @classmethod
    def get_expected(cls) -> FlywaySchemaHistoryV1:
        """Get expected flyway schema history data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_flyway_schema_history.json"
        with open(file_path) as f:
            data = json.load(f)
        return FlywaySchemaHistoryV1.model_validate(data)