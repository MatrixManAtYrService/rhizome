"""
SQLModel definition for the app_app_bundle table.
"""

from __future__ import annotations

from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AppAppBundle")


class AppAppBundle(RhizomeModel, table=True):
    """
    SQLModel for the `app_app_bundle` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    app_bundle_id: int = Field(foreign_key="app_bundle.id")
    developer_app_id: int = Field(foreign_key="developer_app.id")
    allow_uninstall: bool | None = Field(default=False)
    charge: bool | None = Field(default=True)
    app_subscription_id: int = Field(foreign_key="app_subscription.id")

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AppAppBundle instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
