from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EbbGateway")


@_attrs_define
class EbbGateway:
    """
    Attributes:
        database_id (Union[Unset, int]):
        production (Union[Unset, bool]):
        mid (Union[Unset, str]):
        bemid (Union[Unset, str]):
        acquiring_back_end (Union[Unset, str]):
    """

    database_id: Union[Unset, int] = UNSET
    production: Union[Unset, bool] = UNSET
    mid: Union[Unset, str] = UNSET
    bemid: Union[Unset, str] = UNSET
    acquiring_back_end: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_id = self.database_id

        production = self.production

        mid = self.mid

        bemid = self.bemid

        acquiring_back_end = self.acquiring_back_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_id is not UNSET:
            field_dict["databaseId"] = database_id
        if production is not UNSET:
            field_dict["production"] = production
        if mid is not UNSET:
            field_dict["mid"] = mid
        if bemid is not UNSET:
            field_dict["bemid"] = bemid
        if acquiring_back_end is not UNSET:
            field_dict["acquiringBackEnd"] = acquiring_back_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database_id = d.pop("databaseId", UNSET)

        production = d.pop("production", UNSET)

        mid = d.pop("mid", UNSET)

        bemid = d.pop("bemid", UNSET)

        acquiring_back_end = d.pop("acquiringBackEnd", UNSET)

        ebb_gateway = cls(
            database_id=database_id,
            production=production,
            mid=mid,
            bemid=bemid,
            acquiring_back_end=acquiring_back_end,
        )

        ebb_gateway.additional_properties = d
        return ebb_gateway

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
