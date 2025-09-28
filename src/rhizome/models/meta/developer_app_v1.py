"""
SQLModel definition for the developer_app table, version 1.

This module provides the V1 implementation of the DeveloperApp model.
Currently, DeveloperAppV1 is identical to the base DeveloperApp class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .developer_app import DeveloperApp


class DeveloperAppV1(DeveloperApp, MetaSQLModel, table=True):
    """
    Version 1 of the DeveloperApp model.

    Currently a name-only inheritance from the base DeveloperApp class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "developer_app"

    def sanitize(self) -> DeveloperAppV1:
        """Return a sanitized copy of this DeveloperAppV1 instance."""
        return DeveloperAppV1(
            activation_url=self.activation_url,
            android_version_id=self.android_version_id,
            app_bundle_id=self.app_bundle_id,
            app_domain=self.app_domain,
            application_id=self.application_id,
            approval_android_version_id=self.approval_android_version_id,
            approval_signature=self.approval_signature,
            approval_status=self.approval_status,
            approval_status_modified_time=self.approval_status_modified_time,
            authtoken_refresh_time=self.authtoken_refresh_time,
            benefits=self.benefits,
            concurrent_merchant_request_limit=self.concurrent_merchant_request_limit,
            concurrent_request_limit=self.concurrent_request_limit,
            created_time=self.created_time,
            default_app_locale=self.default_app_locale,
            default_response_type=self.default_response_type,
            deleted_time=self.deleted_time,
            description=self.description,
            developer_id=self.developer_id,
            distribution=self.distribution,
            ecomm_integration_type=self.ecomm_integration_type,
            editor_pick=self.editor_pick,
            eula=self.eula,
            fd_equipment_code=self.fd_equipment_code,
            fd_equipment_name=self.fd_equipment_name,
            filename_banner=self.filename_banner,
            filename_cover=self.filename_cover,
            filename_icon=self.filename_icon,
            first_approval_time=self.first_approval_time,
            first_published_time=self.first_published_time,
            first_submitted_time=self.first_submitted_time,
            hidden=self.hidden,
            id=self.id,
            install_count=self.install_count,
            launch_url_path=self.launch_url_path,
            link_label=self.link_label,
            merchant_request_limit=self.merchant_request_limit,
            modified_time=self.modified_time,
            name=self.name,
            non_clover_billing=self.non_clover_billing,
            package_name=self.package_name,
            paid_app_has_trial=self.paid_app_has_trial,
            partner_id=self.partner_id,
            popularity=self.popularity,
            privacy_policy=self.privacy_policy,
            product_type=self.product_type,
            rank=self.rank,
            recaptcha=self.recaptcha,
            rejection_reason=self.rejection_reason,
            request_limit=self.request_limit,
            segment=self.segment,
            signature=self.signature,
            site_url=self.site_url,
            smart_receipt_text=self.smart_receipt_text,
            smart_receipt_url=self.smart_receipt_url,
            sort_order=self.sort_order,
            support_email=self.support_email,
            support_phone=self.support_phone,
            support_phone_hours=self.support_phone_hours,
            support_url=self.support_url,
            system_app=self.system_app,
            tagline=self.tagline,
            tax_classification_code=self.tax_classification_code,
            trial_days=self.trial_days,
            uuid=self.uuid,
            video_url=self.video_url,
            white_list_private_api=self.white_list_private_api,
        )
