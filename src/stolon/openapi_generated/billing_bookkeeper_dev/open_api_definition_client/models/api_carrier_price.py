from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_price_adjustment import ApiPriceAdjustment
    from ..models.api_price_detail import ApiPriceDetail
    from ..models.api_tier_pricing import ApiTierPricing


T = TypeVar("T", bound="ApiCarrierPrice")


@_attrs_define
class ApiCarrierPrice:
    """collection of pricing quotes by cellular carrier

    Attributes:
        carrier (Union[Unset, str]): cellular carrier, associated with the SIM, that the cellular pricing is for
        merchant_plan_uuid (Union[Unset, str]): 13-character UUID of the merchant plan that the cellular pricing is for,
            or null when applies to all plans without plan-specific pricing
        base_price (Union[Unset, ApiPriceDetail]):
        tier_pricing (Union[Unset, list['ApiTierPricing']]): tiered pricing for the current carrier's SIMs
        adjustments (Union[Unset, list['ApiPriceAdjustment']]): potential adjustments to the cellular base price
    """

    carrier: Union[Unset, str] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    base_price: Union[Unset, "ApiPriceDetail"] = UNSET
    tier_pricing: Union[Unset, list["ApiTierPricing"]] = UNSET
    adjustments: Union[Unset, list["ApiPriceAdjustment"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier = self.carrier

        merchant_plan_uuid = self.merchant_plan_uuid

        base_price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_price, Unset):
            base_price = self.base_price.to_dict()

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
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if base_price is not UNSET:
            field_dict["basePrice"] = base_price
        if tier_pricing is not UNSET:
            field_dict["tierPricing"] = tier_pricing
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_price_adjustment import ApiPriceAdjustment
        from ..models.api_price_detail import ApiPriceDetail
        from ..models.api_tier_pricing import ApiTierPricing

        d = dict(src_dict)
        carrier = d.pop("carrier", UNSET)

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        _base_price = d.pop("basePrice", UNSET)
        base_price: Union[Unset, ApiPriceDetail]
        if _base_price and not isinstance(_base_price, Unset):
            base_price = ApiPriceDetail.from_dict(_base_price)

        else:
            base_price = UNSET

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

        api_carrier_price = cls(
            carrier=carrier,
            merchant_plan_uuid=merchant_plan_uuid,
            base_price=base_price,
            tier_pricing=tier_pricing,
            adjustments=adjustments,
        )

        api_carrier_price.additional_properties = d
        return api_carrier_price

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
