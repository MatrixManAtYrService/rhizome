"""
Expected data for email_audit table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.email_audit_v1 import EmailAuditV1


class EmailAuditNaProd(Emplacement[EmailAuditV1]):
    """Expected data for EmailAudit in na_prod environment."""

    @classmethod
    def get_expected(cls) -> EmailAuditV1:
        """Get expected email_audit data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_email_audit.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return EmailAuditV1.model_validate(data)
