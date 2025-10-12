"""Pydantic models for trifolium utility functions."""

from typing import Any

from pydantic import BaseModel, Field


class CurrentUser(BaseModel):
    """Information about the currently authenticated user."""

    ldap_name: str = Field(description="The user's LDAP username")
    account_uuid: str = Field(description="The user's account UUID")
    email: str = Field(description="The user's email address (typically ldapName@clover.com)")
    permissions: list[dict[str, Any]] = Field(description="List of permission objects for this user")

    model_config = {"frozen": True}


class ResellerOwnerAccount(BaseModel):
    """Account information for a reseller owner."""

    uuid: str = Field(description="Account UUID (13 characters)")
    id: int = Field(description="Account ID (database primary key)")
    email: str = Field(description="Account email address")
    name: str = Field(description="Account display name")

    model_config = {"frozen": True}

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for backwards compatibility."""
        return {
            "uuid": self.uuid,
            "id": self.id,
            "email": self.email,
            "name": self.name,
        }


class ResellerInfo(BaseModel):
    """Information about a created reseller."""

    reseller_uuid: str = Field(description="Reseller UUID")
    reseller_id: str | int = Field(description="Reseller ID (may be UUID or integer)")
    name: str = Field(description="Reseller name")
    was_reused: bool = Field(default=False, description="Whether this reseller was reused from a previous run")

    model_config = {"frozen": True}


class TestOwnerAccount(BaseModel):
    """Owner account information for test fixtures."""

    account_id: int | None = Field(description="Account ID (None for internal accounts)")
    uuid: str = Field(description="Account UUID")
    email: str = Field(description="Account email address")
    name: str = Field(description="Account display name")
    was_reused: bool = Field(default=False, description="Whether this account was reused")

    model_config = {"frozen": True}

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for backwards compatibility."""
        return {
            "account_id": self.account_id,
            "uuid": self.uuid,
            "email": self.email,
            "name": self.name,
            "was_reused": self.was_reused,
        }
