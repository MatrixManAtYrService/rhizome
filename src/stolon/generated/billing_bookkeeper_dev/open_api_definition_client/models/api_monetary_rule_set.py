import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_monetary_rule_set_rule_status import ApiMonetaryRuleSetRuleStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_monetary_rule_set_rule import ApiMonetaryRuleSetRule


T = TypeVar("T", bound="ApiMonetaryRuleSet")


@_attrs_define
class ApiMonetaryRuleSet:
    """
    Attributes:
        id (Union[Unset, int]): ID of the monetary rule set
        uuid (Union[Unset, str]): 26-character UUID of the monetary rule set
        rule_status (Union[Unset, ApiMonetaryRuleSetRuleStatus]):
        short_desc (Union[Unset, str]): short description of monetary rule set
        full_desc (Union[Unset, str]): full description of monetary rule set
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the monetary rule set was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the monetary rule set was last modified
            Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this monetary rule set
        rules (Union[Unset, list['ApiMonetaryRuleSetRule']]): rules belonging to the monetary rule set
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    rule_status: Union[Unset, ApiMonetaryRuleSetRuleStatus] = UNSET
    short_desc: Union[Unset, str] = UNSET
    full_desc: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    rules: Union[Unset, list["ApiMonetaryRuleSetRule"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        rule_status: Union[Unset, str] = UNSET
        if not isinstance(self.rule_status, Unset):
            rule_status = self.rule_status.value

        short_desc = self.short_desc

        full_desc = self.full_desc

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if rule_status is not UNSET:
            field_dict["ruleStatus"] = rule_status
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if full_desc is not UNSET:
            field_dict["fullDesc"] = full_desc
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_monetary_rule_set_rule import ApiMonetaryRuleSetRule

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        _rule_status = d.pop("ruleStatus", UNSET)
        rule_status: Union[Unset, ApiMonetaryRuleSetRuleStatus]
        if isinstance(_rule_status, Unset):
            rule_status = UNSET
        else:
            rule_status = ApiMonetaryRuleSetRuleStatus(_rule_status)

        short_desc = d.pop("shortDesc", UNSET)

        full_desc = d.pop("fullDesc", UNSET)

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

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = ApiMonetaryRuleSetRule.from_dict(rules_item_data)

            rules.append(rules_item)

        api_monetary_rule_set = cls(
            id=id,
            uuid=uuid,
            rule_status=rule_status,
            short_desc=short_desc,
            full_desc=full_desc,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
            rules=rules,
        )

        api_monetary_rule_set.additional_properties = d
        return api_monetary_rule_set

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
