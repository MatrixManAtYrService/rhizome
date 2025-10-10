from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_price_detail_apply_type import ApiPriceDetailApplyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPriceDetail")


@_attrs_define
class ApiPriceDetail:
    """
    Attributes:
        fee_category (Union[Unset, str]): defined fee category value
        fee_code (Union[Unset, str]): defined fee code value
        fee_rate_uuid (Union[Unset, str]): 26-character UUID of the applicable fee rate
        apply_type (Union[Unset, ApiPriceDetailApplyType]):
        rate_amount (Union[Unset, float]): the per-item amount or flat-fee amount from the fee rate
        rate_percentage (Union[Unset, float]): the percentage rate from the fee rate
        net_fee_amount (Union[Unset, float]): the net fee amount that would be billed
        tax_amount (Union[Unset, float]): the tax amount for the net fee amount
        net_amount (Union[Unset, float]): the total of the net fee amount and the tax amount
    """

    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    fee_rate_uuid: Union[Unset, str] = UNSET
    apply_type: Union[Unset, ApiPriceDetailApplyType] = UNSET
    rate_amount: Union[Unset, float] = UNSET
    rate_percentage: Union[Unset, float] = UNSET
    net_fee_amount: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    net_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_category = self.fee_category

        fee_code = self.fee_code

        fee_rate_uuid = self.fee_rate_uuid

        apply_type: Union[Unset, str] = UNSET
        if not isinstance(self.apply_type, Unset):
            apply_type = self.apply_type.value

        rate_amount = self.rate_amount

        rate_percentage = self.rate_percentage

        net_fee_amount = self.net_fee_amount

        tax_amount = self.tax_amount

        net_amount = self.net_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if fee_rate_uuid is not UNSET:
            field_dict["feeRateUuid"] = fee_rate_uuid
        if apply_type is not UNSET:
            field_dict["applyType"] = apply_type
        if rate_amount is not UNSET:
            field_dict["rateAmount"] = rate_amount
        if rate_percentage is not UNSET:
            field_dict["ratePercentage"] = rate_percentage
        if net_fee_amount is not UNSET:
            field_dict["netFeeAmount"] = net_fee_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        fee_rate_uuid = d.pop("feeRateUuid", UNSET)

        _apply_type = d.pop("applyType", UNSET)
        apply_type: Union[Unset, ApiPriceDetailApplyType]
        if _apply_type and not isinstance(_apply_type, Unset):
            apply_type = ApiPriceDetailApplyType(_apply_type)

        else:
            apply_type = UNSET

        rate_amount = d.pop("rateAmount", UNSET)

        rate_percentage = d.pop("ratePercentage", UNSET)

        net_fee_amount = d.pop("netFeeAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        net_amount = d.pop("netAmount", UNSET)

        api_price_detail = cls(
            fee_category=fee_category,
            fee_code=fee_code,
            fee_rate_uuid=fee_rate_uuid,
            apply_type=apply_type,
            rate_amount=rate_amount,
            rate_percentage=rate_percentage,
            net_fee_amount=net_fee_amount,
            tax_amount=tax_amount,
            net_amount=net_amount,
        )

        api_price_detail.additional_properties = d
        return api_price_detail

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
