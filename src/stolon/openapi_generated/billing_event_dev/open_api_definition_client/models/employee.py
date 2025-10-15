from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Employee")


@_attrs_define
class Employee:
    """Employee who processed the payment

    Attributes:
        href (Union[Unset, str]): URL reference to the employee
        id (Union[Unset, str]): UUID of the employee who processed the payment
        name (Union[Unset, str]): Employee name
        nickname (Union[Unset, str]): Employee nickname
        role (Union[Unset, str]): Employee role
    """

    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        id = self.id

        name = self.name

        nickname = self.nickname

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        role = d.pop("role", UNSET)

        employee = cls(
            href=href,
            id=id,
            name=name,
            nickname=nickname,
            role=role,
        )

        employee.additional_properties = d
        return employee

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
