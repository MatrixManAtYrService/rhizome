from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_price_detail import ApiPriceDetail


T = TypeVar("T", bound="ApiPriceModifier")


@_attrs_define
class ApiPriceModifier:
    """potential modifications to the base price of the current device(s)

    Attributes:
        mod_type (Union[Unset, str]): the modifier type
        mod_price (Union[Unset, ApiPriceDetail]):
    """

    mod_type: Union[Unset, str] = UNSET
    mod_price: Union[Unset, "ApiPriceDetail"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mod_type = self.mod_type

        mod_price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mod_price, Unset):
            mod_price = self.mod_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mod_type is not UNSET:
            field_dict["modType"] = mod_type
        if mod_price is not UNSET:
            field_dict["modPrice"] = mod_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_price_detail import ApiPriceDetail

        d = dict(src_dict)
        mod_type = d.pop("modType", UNSET)

        _mod_price = d.pop("modPrice", UNSET)
        mod_price: Union[Unset, ApiPriceDetail]
        if _mod_price and not isinstance(_mod_price, Unset):
            mod_price = ApiPriceDetail.from_dict(_mod_price)

        else:
            mod_price = UNSET

        api_price_modifier = cls(
            mod_type=mod_type,
            mod_price=mod_price,
        )

        api_price_modifier.additional_properties = d
        return api_price_modifier

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
