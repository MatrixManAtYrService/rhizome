"""
SQLModel definition for the developer_app table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="DeveloperApp")


class DeveloperApp(RhizomeModel, table=True):
    """
    SQLModel for the `developer_app` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    approval_status: str = Field(max_length=9)
    default_response_type: str | None = Field(default='code', max_length=5)
    approval_status_modified_time: datetime.datetime
    deleted_time: datetime.datetime | None = Field(default=None)
    approval_android_version_id: int | None = Field(default=None, foreign_key="android_version.id")
    approval_signature: bytes | None = Field(default=None)
    system_app: bool | None = Field(default=False)
    hidden: bool = Field(default=False)
    distribution: str = Field(max_length=7)
    segment: str | None = Field(default=None, max_length=18)
    ecomm_integration_type: str | None = Field(default=None, max_length=15)
    developer_id: int = Field(foreign_key="developer.id")
    name: str | None = Field(default=None, max_length=250)
    description: str | None = Field(default=None, max_length=2047)
    tagline: str | None = Field(default=None, max_length=255)
    benefits: str | None = Field(default=None, max_length=2047)
    video_url: str | None = Field(default=None, max_length=255)
    activation_url: str | None = Field(default=None, max_length=255)
    site_url: str | None = Field(default=None, max_length=255)
    launch_url_path: str | None = Field(default=None, max_length=255)
    app_domain: str | None = Field(default=None, max_length=255)
    android_version_id: int | None = Field(default=None, foreign_key="android_version.id")
    package_name: str | None = Field(default=None, max_length=255)
    signature: bytes | None = Field(default=None)
    sort_order: int | None = Field(default=0)
    filename_icon: str | None = Field(default=None, max_length=100)
    filename_cover: str | None = Field(default=None, max_length=255)
    filename_banner: str | None = Field(default=None, max_length=255)
    product_type: str | None = Field(default=None, max_length=8)
    paid_app_has_trial: bool = Field(default=False)
    smart_receipt_text: str | None = Field(default=None, max_length=100)
    smart_receipt_url: str | None = Field(default=None, max_length=255)
    request_limit: int = Field(default=50)
    merchant_request_limit: int = Field(default=16)
    concurrent_request_limit: int = Field(default=10)
    concurrent_merchant_request_limit: int = Field(default=5)
    privacy_policy: str | None = Field(default=None, max_length=255)
    eula: str | None = Field(default=None, max_length=255)
    support_phone: str | None = Field(default=None, max_length=25)
    support_phone_hours: str | None = Field(default=None, max_length=127)
    support_email: str | None = Field(default=None, max_length=127)
    support_url: str | None = Field(default=None, max_length=255)
    modified_time: datetime.datetime
    authtoken_refresh_time: datetime.datetime | None = Field(default=None)
    tax_classification_code: str | None = Field(default=None, max_length=10)
    application_id: str | None = Field(default=None, max_length=255)
    partner_id: str | None = Field(default=None, max_length=64, unique=True)
    fd_equipment_code: str | None = Field(default=None, max_length=32)
    fd_equipment_name: str | None = Field(default=None, max_length=255)
    non_clover_billing: bool = Field(default=False)
    first_published_time: datetime.datetime | None = Field(default=None)
    first_approval_time: datetime.datetime | None = Field(default=None)
    first_submitted_time: datetime.datetime | None = Field(default=None)
    created_time: datetime.datetime | None = Field(default=None)
    white_list_private_api: bool = Field(default=False)
    app_bundle_id: int | None = Field(default=None)
    editor_pick: bool | None = Field(default=False)
    install_count: int | None = Field(default=0)
    popularity: int | None = Field(default=0)
    rank: int = Field(default=0)
    link_label: str | None = Field(default=None, max_length=125)
    rejection_reason: str | None = Field(default=None, max_length=2047)
    trial_days: int = Field(default=30)
    recaptcha: bool | None = Field(default=False)
    default_app_locale: str | None = Field(default=None, max_length=6)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this DeveloperApp instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
