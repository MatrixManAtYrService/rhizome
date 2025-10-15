from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProductTax")


@_attrs_define
class ApiProductTax:
    """Collection of products and services that tax was calculated for.

    Attributes:
        correlation_id (Union[Unset, str]): Client-assigned product identifier from the request that is returned with
            the corresponding product in response.
        product_code (Union[Unset, str]): The code that identifies the product or service that tax was calculated for.
        base_amount (Union[Unset, float]): The base amount that tax was calculated for.
        currency (Union[Unset, str]): The currency of the base and tax amounts. Example: USD.
        total_tax_amount (Union[Unset, float]): The total of the calculated tax amounts.
        tax_1_amount (Union[Unset, float]): The portion of the total tax amount that is for tax 1, typically Federal
            tax, GST, or VAT.
        tax_2_amount (Union[Unset, float]): The portion of the total tax amount that is for tax 2, typically state or
            province tax.
        tax_3_amount (Union[Unset, float]): The portion of the total tax amount that is for tax 3, typically county tax.
        tax_4_amount (Union[Unset, float]): The portion of the total tax amount that is for tax 4, typically city or
            local tax.
        total_tax_rate (Union[Unset, float]): The total of the tax rates applied.
        tax_1_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 1, typically Federal tax,
            GST, or VAT.
        tax_2_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 2, typically state or
            province tax.
        tax_3_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 3, typically county tax.
        tax_4_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 4, typically city or local
            tax.
        is_tax_exempt (Union[Unset, bool]): Indicates whether the entity and/or product or service is exempt from tax.
    """

    correlation_id: Union[Unset, str] = UNSET
    product_code: Union[Unset, str] = UNSET
    base_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    tax_1_amount: Union[Unset, float] = UNSET
    tax_2_amount: Union[Unset, float] = UNSET
    tax_3_amount: Union[Unset, float] = UNSET
    tax_4_amount: Union[Unset, float] = UNSET
    total_tax_rate: Union[Unset, float] = UNSET
    tax_1_rate: Union[Unset, float] = UNSET
    tax_2_rate: Union[Unset, float] = UNSET
    tax_3_rate: Union[Unset, float] = UNSET
    tax_4_rate: Union[Unset, float] = UNSET
    is_tax_exempt: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        correlation_id = self.correlation_id

        product_code = self.product_code

        base_amount = self.base_amount

        currency = self.currency

        total_tax_amount = self.total_tax_amount

        tax_1_amount = self.tax_1_amount

        tax_2_amount = self.tax_2_amount

        tax_3_amount = self.tax_3_amount

        tax_4_amount = self.tax_4_amount

        total_tax_rate = self.total_tax_rate

        tax_1_rate = self.tax_1_rate

        tax_2_rate = self.tax_2_rate

        tax_3_rate = self.tax_3_rate

        tax_4_rate = self.tax_4_rate

        is_tax_exempt = self.is_tax_exempt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if product_code is not UNSET:
            field_dict["productCode"] = product_code
        if base_amount is not UNSET:
            field_dict["baseAmount"] = base_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_tax_amount is not UNSET:
            field_dict["totalTaxAmount"] = total_tax_amount
        if tax_1_amount is not UNSET:
            field_dict["tax1Amount"] = tax_1_amount
        if tax_2_amount is not UNSET:
            field_dict["tax2Amount"] = tax_2_amount
        if tax_3_amount is not UNSET:
            field_dict["tax3Amount"] = tax_3_amount
        if tax_4_amount is not UNSET:
            field_dict["tax4Amount"] = tax_4_amount
        if total_tax_rate is not UNSET:
            field_dict["totalTaxRate"] = total_tax_rate
        if tax_1_rate is not UNSET:
            field_dict["tax1Rate"] = tax_1_rate
        if tax_2_rate is not UNSET:
            field_dict["tax2Rate"] = tax_2_rate
        if tax_3_rate is not UNSET:
            field_dict["tax3Rate"] = tax_3_rate
        if tax_4_rate is not UNSET:
            field_dict["tax4Rate"] = tax_4_rate
        if is_tax_exempt is not UNSET:
            field_dict["isTaxExempt"] = is_tax_exempt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        correlation_id = d.pop("correlationId", UNSET)

        product_code = d.pop("productCode", UNSET)

        base_amount = d.pop("baseAmount", UNSET)

        currency = d.pop("currency", UNSET)

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        tax_1_amount = d.pop("tax1Amount", UNSET)

        tax_2_amount = d.pop("tax2Amount", UNSET)

        tax_3_amount = d.pop("tax3Amount", UNSET)

        tax_4_amount = d.pop("tax4Amount", UNSET)

        total_tax_rate = d.pop("totalTaxRate", UNSET)

        tax_1_rate = d.pop("tax1Rate", UNSET)

        tax_2_rate = d.pop("tax2Rate", UNSET)

        tax_3_rate = d.pop("tax3Rate", UNSET)

        tax_4_rate = d.pop("tax4Rate", UNSET)

        is_tax_exempt = d.pop("isTaxExempt", UNSET)

        api_product_tax = cls(
            correlation_id=correlation_id,
            product_code=product_code,
            base_amount=base_amount,
            currency=currency,
            total_tax_amount=total_tax_amount,
            tax_1_amount=tax_1_amount,
            tax_2_amount=tax_2_amount,
            tax_3_amount=tax_3_amount,
            tax_4_amount=tax_4_amount,
            total_tax_rate=total_tax_rate,
            tax_1_rate=tax_1_rate,
            tax_2_rate=tax_2_rate,
            tax_3_rate=tax_3_rate,
            tax_4_rate=tax_4_rate,
            is_tax_exempt=is_tax_exempt,
        )

        api_product_tax.additional_properties = d
        return api_product_tax

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
