import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingEntityConfig")


@_attrs_define
class BillingEntityConfig:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        hierarchy_type (Union[Unset, str]):
        effective_date (Union[Unset, datetime.date]):
        post_method (Union[Unset, str]):
        plan_billing_method (Union[Unset, str]):
        invoice_method (Union[Unset, str]):
        settlement_method (Union[Unset, str]):
        seasonal_rule_set_uuid (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
        audit_id (Union[Unset, str]):
        revenue_share_group (Union[Unset, str]):
        invoice_number_format (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    post_method: Union[Unset, str] = UNSET
    plan_billing_method: Union[Unset, str] = UNSET
    invoice_method: Union[Unset, str] = UNSET
    settlement_method: Union[Unset, str] = UNSET
    seasonal_rule_set_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    revenue_share_group: Union[Unset, str] = UNSET
    invoice_number_format: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        hierarchy_type = self.hierarchy_type

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        post_method = self.post_method

        plan_billing_method = self.plan_billing_method

        invoice_method = self.invoice_method

        settlement_method = self.settlement_method

        seasonal_rule_set_uuid = self.seasonal_rule_set_uuid

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        revenue_share_group = self.revenue_share_group

        invoice_number_format = self.invoice_number_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if post_method is not UNSET:
            field_dict["postMethod"] = post_method
        if plan_billing_method is not UNSET:
            field_dict["planBillingMethod"] = plan_billing_method
        if invoice_method is not UNSET:
            field_dict["invoiceMethod"] = invoice_method
        if settlement_method is not UNSET:
            field_dict["settlementMethod"] = settlement_method
        if seasonal_rule_set_uuid is not UNSET:
            field_dict["seasonalRuleSetUuid"] = seasonal_rule_set_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id
        if revenue_share_group is not UNSET:
            field_dict["revenueShareGroup"] = revenue_share_group
        if invoice_number_format is not UNSET:
            field_dict["invoiceNumberFormat"] = invoice_number_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if _effective_date and not isinstance(_effective_date, Unset):
            effective_date = isoparse(_effective_date).date()

        else:
            effective_date = UNSET

        post_method = d.pop("postMethod", UNSET)

        plan_billing_method = d.pop("planBillingMethod", UNSET)

        invoice_method = d.pop("invoiceMethod", UNSET)

        settlement_method = d.pop("settlementMethod", UNSET)

        seasonal_rule_set_uuid = d.pop("seasonalRuleSetUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if _modified_timestamp and not isinstance(_modified_timestamp, Unset):
            modified_timestamp = isoparse(_modified_timestamp)

        else:
            modified_timestamp = UNSET

        audit_id = d.pop("auditId", UNSET)

        revenue_share_group = d.pop("revenueShareGroup", UNSET)

        invoice_number_format = d.pop("invoiceNumberFormat", UNSET)

        billing_entity_config = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            hierarchy_type=hierarchy_type,
            effective_date=effective_date,
            post_method=post_method,
            plan_billing_method=plan_billing_method,
            invoice_method=invoice_method,
            settlement_method=settlement_method,
            seasonal_rule_set_uuid=seasonal_rule_set_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
            revenue_share_group=revenue_share_group,
            invoice_number_format=invoice_number_format,
        )

        billing_entity_config.additional_properties = d
        return billing_entity_config

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
