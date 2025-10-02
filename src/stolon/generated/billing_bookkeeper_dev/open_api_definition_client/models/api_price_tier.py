from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_price_detail import ApiPriceDetail


T = TypeVar("T", bound="ApiPriceTier")


@_attrs_define
class ApiPriceTier:
    """details for devices for which this device pricing data applies

    Attributes:
        tier_uuid (Union[Unset, str]): 26-character UUID of the tier detail definition
        tier_short_desc (Union[Unset, str]): short description of the tier
        min_units (Union[Unset, float]): the minimum number of units needed to qualify for the tier; applied for
            QUANTITY and BOTH tiered basis
        min_amount (Union[Unset, float]): the minimum total fee amount needed to qualify for the tier; applied for
            VOLUME and BOTH tiered basis
        tier_price (Union[Unset, ApiPriceDetail]):
    """

    tier_uuid: Union[Unset, str] = UNSET
    tier_short_desc: Union[Unset, str] = UNSET
    min_units: Union[Unset, float] = UNSET
    min_amount: Union[Unset, float] = UNSET
    tier_price: Union[Unset, "ApiPriceDetail"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier_uuid = self.tier_uuid

        tier_short_desc = self.tier_short_desc

        min_units = self.min_units

        min_amount = self.min_amount

        tier_price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tier_price, Unset):
            tier_price = self.tier_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tier_uuid is not UNSET:
            field_dict["tierUuid"] = tier_uuid
        if tier_short_desc is not UNSET:
            field_dict["tierShortDesc"] = tier_short_desc
        if min_units is not UNSET:
            field_dict["minUnits"] = min_units
        if min_amount is not UNSET:
            field_dict["minAmount"] = min_amount
        if tier_price is not UNSET:
            field_dict["tierPrice"] = tier_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_price_detail import ApiPriceDetail

        d = dict(src_dict)
        tier_uuid = d.pop("tierUuid", UNSET)

        tier_short_desc = d.pop("tierShortDesc", UNSET)

        min_units = d.pop("minUnits", UNSET)

        min_amount = d.pop("minAmount", UNSET)

        _tier_price = d.pop("tierPrice", UNSET)
        tier_price: Union[Unset, ApiPriceDetail]
        if isinstance(_tier_price, Unset):
            tier_price = UNSET
        else:
            tier_price = ApiPriceDetail.from_dict(_tier_price)

        api_price_tier = cls(
            tier_uuid=tier_uuid,
            tier_short_desc=tier_short_desc,
            min_units=min_units,
            min_amount=min_amount,
            tier_price=tier_price,
        )

        api_price_tier.additional_properties = d
        return api_price_tier

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
