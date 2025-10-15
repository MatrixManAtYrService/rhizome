from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPostMethod")


@_attrs_define
class ApiPostMethod:
    """
    Attributes:
        post_method (Union[Unset, str]): post method value
        valid_hierarchy_types (Union[Unset, list[str]]): billing hierarchy types where the post method is valid
    """

    post_method: Union[Unset, str] = UNSET
    valid_hierarchy_types: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_method = self.post_method

        valid_hierarchy_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.valid_hierarchy_types, Unset):
            valid_hierarchy_types = self.valid_hierarchy_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_method is not UNSET:
            field_dict["postMethod"] = post_method
        if valid_hierarchy_types is not UNSET:
            field_dict["validHierarchyTypes"] = valid_hierarchy_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_method = d.pop("postMethod", UNSET)

        valid_hierarchy_types = cast(list[str], d.pop("validHierarchyTypes", UNSET))

        api_post_method = cls(
            post_method=post_method,
            valid_hierarchy_types=valid_hierarchy_types,
        )

        api_post_method.additional_properties = d
        return api_post_method

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
