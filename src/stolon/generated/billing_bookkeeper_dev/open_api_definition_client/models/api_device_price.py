from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_device_info import ApiDeviceInfo
    from ..models.api_price_adjustment import ApiPriceAdjustment
    from ..models.api_price_detail import ApiPriceDetail
    from ..models.api_price_modifier import ApiPriceModifier
    from ..models.api_tier_pricing import ApiTierPricing


T = TypeVar("T", bound="ApiDevicePrice")


@_attrs_define
class ApiDevicePrice:
    """qualifiers for the tiered rule

    Attributes:
        device_info (Union[Unset, list['ApiDeviceInfo']]): details for devices for which this device pricing data
            applies
        base_price (Union[Unset, ApiPriceDetail]):
        trial_price (Union[Unset, ApiPriceDetail]):
        modifiers (Union[Unset, list['ApiPriceModifier']]): potential modifications to the base price of the current
            device(s)
        tier_pricing (Union[Unset, list['ApiTierPricing']]): tiered pricing for the current device(s)
        adjustments (Union[Unset, list['ApiPriceAdjustment']]): potential adjustments to the base price of the plan
    """

    device_info: Union[Unset, list["ApiDeviceInfo"]] = UNSET
    base_price: Union[Unset, "ApiPriceDetail"] = UNSET
    trial_price: Union[Unset, "ApiPriceDetail"] = UNSET
    modifiers: Union[Unset, list["ApiPriceModifier"]] = UNSET
    tier_pricing: Union[Unset, list["ApiTierPricing"]] = UNSET
    adjustments: Union[Unset, list["ApiPriceAdjustment"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = []
            for device_info_item_data in self.device_info:
                device_info_item = device_info_item_data.to_dict()
                device_info.append(device_info_item)

        base_price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_price, Unset):
            base_price = self.base_price.to_dict()

        trial_price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trial_price, Unset):
            trial_price = self.trial_price.to_dict()

        modifiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.modifiers, Unset):
            modifiers = []
            for modifiers_item_data in self.modifiers:
                modifiers_item = modifiers_item_data.to_dict()
                modifiers.append(modifiers_item)

        tier_pricing: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tier_pricing, Unset):
            tier_pricing = []
            for tier_pricing_item_data in self.tier_pricing:
                tier_pricing_item = tier_pricing_item_data.to_dict()
                tier_pricing.append(tier_pricing_item)

        adjustments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.adjustments, Unset):
            adjustments = []
            for adjustments_item_data in self.adjustments:
                adjustments_item = adjustments_item_data.to_dict()
                adjustments.append(adjustments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_info is not UNSET:
            field_dict["deviceInfo"] = device_info
        if base_price is not UNSET:
            field_dict["basePrice"] = base_price
        if trial_price is not UNSET:
            field_dict["trialPrice"] = trial_price
        if modifiers is not UNSET:
            field_dict["modifiers"] = modifiers
        if tier_pricing is not UNSET:
            field_dict["tierPricing"] = tier_pricing
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_device_info import ApiDeviceInfo
        from ..models.api_price_adjustment import ApiPriceAdjustment
        from ..models.api_price_detail import ApiPriceDetail
        from ..models.api_price_modifier import ApiPriceModifier
        from ..models.api_tier_pricing import ApiTierPricing

        d = dict(src_dict)
        device_info = []
        _device_info = d.pop("deviceInfo", UNSET)
        for device_info_item_data in _device_info or []:
            device_info_item = ApiDeviceInfo.from_dict(device_info_item_data)

            device_info.append(device_info_item)

        _base_price = d.pop("basePrice", UNSET)
        base_price: Union[Unset, ApiPriceDetail]
        if isinstance(_base_price, Unset):
            base_price = UNSET
        else:
            base_price = ApiPriceDetail.from_dict(_base_price)

        _trial_price = d.pop("trialPrice", UNSET)
        trial_price: Union[Unset, ApiPriceDetail]
        if isinstance(_trial_price, Unset):
            trial_price = UNSET
        else:
            trial_price = ApiPriceDetail.from_dict(_trial_price)

        modifiers = []
        _modifiers = d.pop("modifiers", UNSET)
        for modifiers_item_data in _modifiers or []:
            modifiers_item = ApiPriceModifier.from_dict(modifiers_item_data)

            modifiers.append(modifiers_item)

        tier_pricing = []
        _tier_pricing = d.pop("tierPricing", UNSET)
        for tier_pricing_item_data in _tier_pricing or []:
            tier_pricing_item = ApiTierPricing.from_dict(tier_pricing_item_data)

            tier_pricing.append(tier_pricing_item)

        adjustments = []
        _adjustments = d.pop("adjustments", UNSET)
        for adjustments_item_data in _adjustments or []:
            adjustments_item = ApiPriceAdjustment.from_dict(adjustments_item_data)

            adjustments.append(adjustments_item)

        api_device_price = cls(
            device_info=device_info,
            base_price=base_price,
            trial_price=trial_price,
            modifiers=modifiers,
            tier_pricing=tier_pricing,
            adjustments=adjustments,
        )

        api_device_price.additional_properties = d
        return api_device_price

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
