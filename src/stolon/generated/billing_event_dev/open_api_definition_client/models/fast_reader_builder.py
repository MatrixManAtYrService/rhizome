from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FastReaderBuilder")


@_attrs_define
class FastReaderBuilder:
    """
    Attributes:
        key_class_enabled (Union[Unset, bool]):
        class_prop_enabled (Union[Unset, bool]):
    """

    key_class_enabled: Union[Unset, bool] = UNSET
    class_prop_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_class_enabled = self.key_class_enabled

        class_prop_enabled = self.class_prop_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_class_enabled is not UNSET:
            field_dict["keyClassEnabled"] = key_class_enabled
        if class_prop_enabled is not UNSET:
            field_dict["classPropEnabled"] = class_prop_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_class_enabled = d.pop("keyClassEnabled", UNSET)

        class_prop_enabled = d.pop("classPropEnabled", UNSET)

        fast_reader_builder = cls(
            key_class_enabled=key_class_enabled,
            class_prop_enabled=class_prop_enabled,
        )

        fast_reader_builder.additional_properties = d
        return fast_reader_builder

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
