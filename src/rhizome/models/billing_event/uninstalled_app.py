"""
SQLModel definition for the uninstalled_app table.

This module provides the SQLModel class for the uninstalled_app table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class UninstalledApp(RhizomeModel, table=False):
    """
    SQLModel for the `uninstalled_app` table.

    This model represents applications that have been uninstalled,
    containing app information and offboarding details.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=36, description="Unique identifier for the uninstalled app")
    offboarding_uuid: str = Field(max_length=36, description="UUID of the offboarding process")
    app_name: str | None = Field(default=None, max_length=36, description="Name of the uninstalled app")
    site_url: str | None = Field(default=None, max_length=255, description="Site URL of the uninstalled app")

    def sanitize(self) -> UninstalledApp:
        """Return a sanitized copy of this UninstalledApp instance."""
        return UninstalledApp(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 36),  # type: ignore
            offboarding_uuid=sanitize_uuid_field(self.offboarding_uuid, 36),  # type: ignore
            app_name=self.app_name,
            site_url=self.site_url,
        )