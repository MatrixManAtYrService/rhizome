from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDeveloperBillingEntity")


@_attrs_define
class ApiDeveloperBillingEntity:
    """
    Attributes:
        entity_uuid (Union[Unset, str]): 13-character UUID of the actual entity that this billing entity represents
        name (Union[Unset, str]): name of billing entity
    """

    entity_uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_uuid = self.entity_uuid

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_uuid = d.pop("entityUuid", UNSET)

        name = d.pop("name", UNSET)

        api_developer_billing_entity = cls(
            entity_uuid=entity_uuid,
            name=name,
        )

        api_developer_billing_entity.additional_properties = d
        return api_developer_billing_entity

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
