import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_monetary_rule_alias_rule_type import ApiMonetaryRuleAliasRuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMonetaryRuleAlias")


@_attrs_define
class ApiMonetaryRuleAlias:
    """
    Attributes:
        id (Union[Unset, int]): ID of the monetary rule alias
        uuid (Union[Unset, str]): 26-character UUID of the monetary rule alias
        rule_alias (Union[Unset, str]): the alias for a monetary rule
        rule_type (Union[Unset, ApiMonetaryRuleAliasRuleType]):
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the monetary rule alias was created
            Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    rule_alias: Union[Unset, str] = UNSET
    rule_type: Union[Unset, ApiMonetaryRuleAliasRuleType] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        rule_alias = self.rule_alias

        rule_type: Union[Unset, str] = UNSET
        if not isinstance(self.rule_type, Unset):
            rule_type = self.rule_type.value

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if rule_alias is not UNSET:
            field_dict["ruleAlias"] = rule_alias
        if rule_type is not UNSET:
            field_dict["ruleType"] = rule_type
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        rule_alias = d.pop("ruleAlias", UNSET)

        _rule_type = d.pop("ruleType", UNSET)
        rule_type: Union[Unset, ApiMonetaryRuleAliasRuleType]
        if isinstance(_rule_type, Unset):
            rule_type = UNSET
        else:
            rule_type = ApiMonetaryRuleAliasRuleType(_rule_type)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_monetary_rule_alias = cls(
            id=id,
            uuid=uuid,
            rule_alias=rule_alias,
            rule_type=rule_type,
            created_timestamp=created_timestamp,
        )

        api_monetary_rule_alias.additional_properties = d
        return api_monetary_rule_alias

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
