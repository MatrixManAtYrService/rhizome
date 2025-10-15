from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Check")


@_attrs_define
class Check:
    """
    Attributes:
        check_name (Union[Unset, str]):
        result (Union[Unset, int]):
        message (Union[Unset, str]):
    """

    check_name: Union[Unset, str] = UNSET
    result: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_name = self.check_name

        result = self.result

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_name is not UNSET:
            field_dict["checkName"] = check_name
        if result is not UNSET:
            field_dict["result"] = result
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_name = d.pop("checkName", UNSET)

        result = d.pop("result", UNSET)

        message = d.pop("message", UNSET)

        check = cls(
            check_name=check_name,
            result=result,
            message=message,
        )

        check.additional_properties = d
        return check

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
