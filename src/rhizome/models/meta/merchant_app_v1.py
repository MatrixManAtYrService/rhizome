"""
SQLModel definition for the merchant_app table, version 1.

This module provides the V1 implementation of the MerchantApp model.
Currently, MerchantAppV1 is identical to the base MerchantApp class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .merchant_app import MerchantApp


class MerchantAppV1(MerchantApp, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantApp model.

    Currently a name-only inheritance from the base MerchantApp class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_app"  # type: ignore

    def sanitize(self) -> MerchantAppV1:
        """Return a sanitized copy of this MerchantAppV1 instance."""
        return MerchantAppV1(
            app_id=self.app_id,
            app_subscription_id=self.app_subscription_id,
            billing_start_time=self.billing_start_time,
            created_time=self.created_time,
            deleted_time=self.deleted_time,
            id=self.id,
            launched_in_web_browser_count=self.launched_in_web_browser_count,
            merchant_id=self.merchant_id,
            modified_time=self.modified_time,
            permission_customers_ach_read=self.permission_customers_ach_read,
            permission_customers_ach_write=self.permission_customers_ach_write,
            permission_customers_address_read=self.permission_customers_address_read,
            permission_customers_address_write=self.permission_customers_address_write,
            permission_customers_birthdate_read=self.permission_customers_birthdate_read,
            permission_customers_birthdate_write=self.permission_customers_birthdate_write,
            permission_customers_businessname_read=self.permission_customers_businessname_read,
            permission_customers_businessname_write=self.permission_customers_businessname_write,
            permission_customers_card_read=self.permission_customers_card_read,
            permission_customers_card_write=self.permission_customers_card_write,
            permission_customers_email_read=self.permission_customers_email_read,
            permission_customers_email_write=self.permission_customers_email_write,
            permission_customers_marketing_read=self.permission_customers_marketing_read,
            permission_customers_marketing_write=self.permission_customers_marketing_write,
            permission_customers_note_read=self.permission_customers_note_read,
            permission_customers_note_write=self.permission_customers_note_write,
            permission_customers_phone_read=self.permission_customers_phone_read,
            permission_customers_phone_write=self.permission_customers_phone_write,
            permission_customers_read=self.permission_customers_read,
            permission_customers_write=self.permission_customers_write,
            permission_employees_read=self.permission_employees_read,
            permission_employees_write=self.permission_employees_write,
            permission_inventory_read=self.permission_inventory_read,
            permission_inventory_write=self.permission_inventory_write,
            permission_merchant_read=self.permission_merchant_read,
            permission_merchant_write=self.permission_merchant_write,
            permission_mid_read=self.permission_mid_read,
            permission_orders_read=self.permission_orders_read,
            permission_orders_write=self.permission_orders_write,
            permission_payments_read=self.permission_payments_read,
            permission_payments_write=self.permission_payments_write,
            permission_process_cards=self.permission_process_cards,
            uninstall_type=self.uninstall_type,
            uuid=self.uuid,
        )
