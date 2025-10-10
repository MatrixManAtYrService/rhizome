import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_monetary_rule_set_rule_rule_type import ApiMonetaryRuleSetRuleRuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMonetaryRuleSetRule")


@_attrs_define
class ApiMonetaryRuleSetRule:
    """
    Attributes:
        id (Union[Unset, int]): ID of the monetary rule set rule
        uuid (Union[Unset, str]): 26-character UUID of the monetary rule set rule
        monetary_rule_set_uuid (Union[Unset, str]): 26-character UUID of the monetary rule set that the rule belongs to
        rule_uuid (Union[Unset, str]): 26-character UUID of the rule that is part of the monetary rule set
        rule_type (Union[Unset, ApiMonetaryRuleSetRuleRuleType]):
        effective_date (Union[Unset, datetime.date]): date that this rule became part of the monetary rule set
        deleted_date (Union[Unset, datetime.date]): date that this rule is no longer included in the monetary rule set
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the monetary rule set rule was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the monetary rule set rule was last
            modified Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this monetary rule set rule
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    monetary_rule_set_uuid: Union[Unset, str] = UNSET
    rule_uuid: Union[Unset, str] = UNSET
    rule_type: Union[Unset, ApiMonetaryRuleSetRuleRuleType] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    deleted_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        monetary_rule_set_uuid = self.monetary_rule_set_uuid

        rule_uuid = self.rule_uuid

        rule_type: Union[Unset, str] = UNSET
        if not isinstance(self.rule_type, Unset):
            rule_type = self.rule_type.value

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
        if monetary_rule_set_uuid is not UNSET:
            field_dict["monetaryRuleSetUuid"] = monetary_rule_set_uuid
        if rule_uuid is not UNSET:
            field_dict["ruleUuid"] = rule_uuid
        if rule_type is not UNSET:
            field_dict["ruleType"] = rule_type
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

        monetary_rule_set_uuid = d.pop("monetaryRuleSetUuid", UNSET)

        rule_uuid = d.pop("ruleUuid", UNSET)

        _rule_type = d.pop("ruleType", UNSET)
        rule_type: Union[Unset, ApiMonetaryRuleSetRuleRuleType]
        if _rule_type and not isinstance(_rule_type, Unset):
            rule_type = ApiMonetaryRuleSetRuleRuleType(_rule_type)

        else:
            rule_type = UNSET

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if _effective_date and not isinstance(_effective_date, Unset):
            effective_date = isoparse(_effective_date).date()

        else:
            effective_date = UNSET

        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: Union[Unset, datetime.date]
        if _deleted_date and not isinstance(_deleted_date, Unset):
            deleted_date = isoparse(_deleted_date).date()

        else:
            deleted_date = UNSET

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

        api_monetary_rule_set_rule = cls(
            id=id,
            uuid=uuid,
            monetary_rule_set_uuid=monetary_rule_set_uuid,
            rule_uuid=rule_uuid,
            rule_type=rule_type,
            effective_date=effective_date,
            deleted_date=deleted_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_monetary_rule_set_rule.additional_properties = d
        return api_monetary_rule_set_rule

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
