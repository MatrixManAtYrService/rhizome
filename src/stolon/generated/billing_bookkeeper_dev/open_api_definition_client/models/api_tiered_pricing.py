import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTieredPricing")


@_attrs_define
class ApiTieredPricing:
    """
    Attributes:
        id (Union[Unset, int]): ID of the tiered pricing assignment
        uuid (Union[Unset, str]): 26-character UUID of the tiered pricing assignment
        billing_entity_uuid (Union[Unset, str]): UUID of the billing entity associated with this tiered pricing
            assignment
        tiered_rule_uuid (Union[Unset, str]): 26-character UUID of the tiered rule that this pricing assignment applies
            to
        effective_date (Union[Unset, datetime.date]): date that this tiered pricing assignment became effective
        deleted_date (Union[Unset, datetime.date]): date that this tiered pricing assignment is no longer applicable
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the tiered pricing assignment was
            created Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the tiered pricing assignment was last
            modified Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this tiered pricing
            assignment
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    tiered_rule_uuid: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    deleted_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        tiered_rule_uuid = self.tiered_rule_uuid

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        deleted_date: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_date, Unset):
            deleted_date = self.deleted_date.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if tiered_rule_uuid is not UNSET:
            field_dict["tieredRuleUuid"] = tiered_rule_uuid
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if deleted_date is not UNSET:
            field_dict["deletedDate"] = deleted_date
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        tiered_rule_uuid = d.pop("tieredRuleUuid", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date).date()

        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: Union[Unset, datetime.date]
        if isinstance(_deleted_date, Unset):
            deleted_date = UNSET
        else:
            deleted_date = isoparse(_deleted_date).date()

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_modified_timestamp, Unset):
            modified_timestamp = UNSET
        else:
            modified_timestamp = isoparse(_modified_timestamp)

        audit_id = d.pop("auditId", UNSET)

        api_tiered_pricing = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            tiered_rule_uuid=tiered_rule_uuid,
            effective_date=effective_date,
            deleted_date=deleted_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_tiered_pricing.additional_properties = d
        return api_tiered_pricing

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
