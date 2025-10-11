"""
SQLModel definition for the reseller_permissions table.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="ResellerPermissionsV1")


class ResellerPermissionsType(str, Enum):
    """Enum for reseller permissions types."""

    CS = "CS"
    SALES = "Sales"
    SUPER = "Super"
    FACTORY_OPS = "FACTORY_OPS"
    SIM_VIEWER = "SIM_VIEWER"


class ResellerPermissionsV1(RhizomeModel, table=True):
    """
    SQLModel for the `reseller_permissions` table.
    """

    __tablename__ = "reseller_permissions"

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    reseller_id: int = Field(foreign_key="reseller.id")
    type: ResellerPermissionsType = Field(default=ResellerPermissionsType.CS)
    is_default: bool | None = Field(default=False)
    name: str = Field(max_length=255)
    view_merchant_dash: bool = Field(default=False)
    create_new_merchant: bool = Field(default=False)
    invite_owner: bool = Field(default=False)
    deactivate_member: bool = Field(default=False)
    support_remote_view: bool = Field(default=False)
    edit_merchant_details: bool = Field(default=False)
    edit_merchant_plan: bool = Field(default=False)
    edit_merchant_gateway: bool = Field(default=False)
    edit_merchant_details_advanced: bool = Field(default=False)
    edit_merchant_gateway_advanced: bool = Field(default=False)
    sales_view_device_list: bool = Field(default=False)
    sales_associate_devices: bool = Field(default=False)
    sales_disassociate_devices: bool = Field(default=False)
    sales_disassociate_stolen_devices: bool = Field(default=False)
    sales_manage_promotions: bool = Field(default=False)
    super_manage_accounts: bool = Field(default=False)
    sales_order_demo_devices: bool = Field(default=False)
    uninstall_apps: bool = Field(default=False)
    factory_ops_manage_accounts: bool = Field(default=False)
    factory_ops_view_factory_reset_codes: bool = Field(default=False)
    sim_viewer_view_sims: bool = Field(default=False)
    sim_viewer_manage_accounts: bool = Field(default=False)
    sim_viewer_create_sims: bool = Field(default=False)
    modify_role_permissions: bool = Field(default=False)
    assign_reseller_roles: bool = Field(default=False)
    view_members: bool = Field(default=False)
    invite_member: bool = Field(default=False)
    create_reseller_role: bool = Field(default=False)
    delete_reseller_role: bool = Field(default=False)
    close_failed_batch: bool = Field(default=False)
    view_failed_batch: bool = Field(default=False)
    disassociate_reseller_account: bool = Field(default=False)
    delete_account_auth_factor: bool = Field(default=False)
    view_enterprise_dash: bool = Field(default=False)
    billing_operations: bool = Field(default=False)
    edit_app_billing_suppression: bool = Field(default=False)
    edit_plan_billing_suppression: bool = Field(default=False)
    edit_apps_billing_suppression: bool = Field(default=False)
    create_reseller: bool = Field(default=False)
    update_rapid_deposit_rules: bool = Field(default=False)
    view_merchant_details: bool = Field(default=False)
    move_devices_across_reseller: bool = Field(default=False)
    modify_time_restrictions: bool = Field(default=False)
    support_remote_view_only: bool = Field(default=False)
    request_refunds: bool = Field(default=False)
    modify_member_auth_factors: bool = Field(default=False)
    modify_reseller: bool = Field(default=False)
    edit_client_id: bool = Field(default=False)
    modify_entitlements: bool = Field(default=False)
    transfer_merchants: bool = Field(default=False)

    def sanitize(self) -> ResellerPermissionsV1:
        """Return a sanitized copy of this ResellerPermissionsV1 instance."""
        from ...sanitize_helpers import sanitize_uuid_field

        return ResellerPermissionsV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13) or self.uuid,
            reseller_id=self.reseller_id,
            type=self.type,
            is_default=self.is_default,
            name=self.name,
            view_merchant_dash=self.view_merchant_dash,
            create_new_merchant=self.create_new_merchant,
            invite_owner=self.invite_owner,
            deactivate_member=self.deactivate_member,
            support_remote_view=self.support_remote_view,
            edit_merchant_details=self.edit_merchant_details,
            edit_merchant_plan=self.edit_merchant_plan,
            edit_merchant_gateway=self.edit_merchant_gateway,
            edit_merchant_details_advanced=self.edit_merchant_details_advanced,
            edit_merchant_gateway_advanced=self.edit_merchant_gateway_advanced,
            sales_view_device_list=self.sales_view_device_list,
            sales_associate_devices=self.sales_associate_devices,
            sales_disassociate_devices=self.sales_disassociate_devices,
            sales_disassociate_stolen_devices=self.sales_disassociate_stolen_devices,
            sales_manage_promotions=self.sales_manage_promotions,
            super_manage_accounts=self.super_manage_accounts,
            sales_order_demo_devices=self.sales_order_demo_devices,
            uninstall_apps=self.uninstall_apps,
            factory_ops_manage_accounts=self.factory_ops_manage_accounts,
            factory_ops_view_factory_reset_codes=self.factory_ops_view_factory_reset_codes,
            sim_viewer_view_sims=self.sim_viewer_view_sims,
            sim_viewer_manage_accounts=self.sim_viewer_manage_accounts,
            sim_viewer_create_sims=self.sim_viewer_create_sims,
            modify_role_permissions=self.modify_role_permissions,
            assign_reseller_roles=self.assign_reseller_roles,
            view_members=self.view_members,
            invite_member=self.invite_member,
            create_reseller_role=self.create_reseller_role,
            delete_reseller_role=self.delete_reseller_role,
            close_failed_batch=self.close_failed_batch,
            view_failed_batch=self.view_failed_batch,
            disassociate_reseller_account=self.disassociate_reseller_account,
            delete_account_auth_factor=self.delete_account_auth_factor,
            view_enterprise_dash=self.view_enterprise_dash,
            billing_operations=self.billing_operations,
            edit_app_billing_suppression=self.edit_app_billing_suppression,
            edit_plan_billing_suppression=self.edit_plan_billing_suppression,
            edit_apps_billing_suppression=self.edit_apps_billing_suppression,
            create_reseller=self.create_reseller,
            update_rapid_deposit_rules=self.update_rapid_deposit_rules,
            view_merchant_details=self.view_merchant_details,
            move_devices_across_reseller=self.move_devices_across_reseller,
            modify_time_restrictions=self.modify_time_restrictions,
            support_remote_view_only=self.support_remote_view_only,
            request_refunds=self.request_refunds,
            modify_member_auth_factors=self.modify_member_auth_factors,
            modify_reseller=self.modify_reseller,
            edit_client_id=self.edit_client_id,
            modify_entitlements=self.modify_entitlements,
            transfer_merchants=self.transfer_merchants,
        )
