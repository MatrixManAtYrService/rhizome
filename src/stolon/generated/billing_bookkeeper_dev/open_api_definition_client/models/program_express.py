from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProgramExpress")


@_attrs_define
class ProgramExpress:
    """
    Attributes:
        key (Union[Unset, str]):
        program_code (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    key: Union[Unset, str] = UNSET
    program_code: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        program_code = self.program_code

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if program_code is not UNSET:
            field_dict["programCode"] = program_code
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        program_code = d.pop("programCode", UNSET)

        value = d.pop("value", UNSET)

        program_express = cls(
            key=key,
            program_code=program_code,
            value=value,
        )

        program_express.additional_properties = d
        return program_express

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
