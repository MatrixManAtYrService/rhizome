from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_device_price import ApiDevicePrice
    from ..models.api_price_adjustment import ApiPriceAdjustment
    from ..models.api_price_detail import ApiPriceDetail


T = TypeVar("T", bound="ApiPlanPrice")


@_attrs_define
class ApiPlanPrice:
    """collection of plans and their pricing quotes

    Attributes:
        merchant_plan_uuid (Union[Unset, str]): 13-character UUID of the merchant plan that the pricing is for
        base_price (Union[Unset, ApiPriceDetail]):
        trial_price (Union[Unset, ApiPriceDetail]):
        adjustments (Union[Unset, list['ApiPriceAdjustment']]): potential adjustments to the base price of the plan
        devices (Union[Unset, list['ApiDevicePrice']]): qualifiers for the tiered rule
    """

    merchant_plan_uuid: Union[Unset, str] = UNSET
    base_price: Union[Unset, "ApiPriceDetail"] = UNSET
    trial_price: Union[Unset, "ApiPriceDetail"] = UNSET
    adjustments: Union[Unset, list["ApiPriceAdjustment"]] = UNSET
    devices: Union[Unset, list["ApiDevicePrice"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant_plan_uuid = self.merchant_plan_uuid

        base_price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_price, Unset):
            base_price = self.base_price.to_dict()

        trial_price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trial_price, Unset):
            trial_price = self.trial_price.to_dict()

        adjustments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.adjustments, Unset):
            adjustments = []
            for adjustments_item_data in self.adjustments:
                adjustments_item = adjustments_item_data.to_dict()
                adjustments.append(adjustments_item)

        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if base_price is not UNSET:
            field_dict["basePrice"] = base_price
        if trial_price is not UNSET:
            field_dict["trialPrice"] = trial_price
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_device_price import ApiDevicePrice
        from ..models.api_price_adjustment import ApiPriceAdjustment
        from ..models.api_price_detail import ApiPriceDetail

        d = dict(src_dict)
        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

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

        adjustments = []
        _adjustments = d.pop("adjustments", UNSET)
        for adjustments_item_data in _adjustments or []:
            adjustments_item = ApiPriceAdjustment.from_dict(adjustments_item_data)

            adjustments.append(adjustments_item)

        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = ApiDevicePrice.from_dict(devices_item_data)

            devices.append(devices_item)

        api_plan_price = cls(
            merchant_plan_uuid=merchant_plan_uuid,
            base_price=base_price,
            trial_price=trial_price,
            adjustments=adjustments,
            devices=devices,
        )

        api_plan_price.additional_properties = d
        return api_plan_price

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
