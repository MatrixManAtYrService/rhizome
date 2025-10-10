import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeSummaryEstimate")


@_attrs_define
class ApiFeeSummaryEstimate:
    """fee summaries for estimated fees

    Attributes:
        billing_date (Union[Unset, datetime.date]): billing date
        fee_category (Union[Unset, str]): the fee category of the fee summary
        fee_code (Union[Unset, str]): the fee code of the fee summary
        currency (Union[Unset, str]): the currency of the fee summary Example: USD.
        total_period_units (Union[Unset, float]): the total number of units billed
        total_basis_amount (Union[Unset, float]): the total basis amount billed
        total_fee_amount (Union[Unset, float]): the total fee amount billed
        total_tax_amount (Union[Unset, float]): the total tax amount
        tax_1_amount (Union[Unset, float]): the portion of the total tax amount that is for tax 1, typically Federal
            tax, GST, or VAT
        tax_2_amount (Union[Unset, float]): the portion of the total tax amount that is for tax 2, typically state or
            province tax
        tax_3_amount (Union[Unset, float]): the portion of the total tax amount that is for tax 3, typically county tax
        tax_4_amount (Union[Unset, float]): the portion of the total tax amount that is for tax 4, typically city or
            local tax
        total_amount (Union[Unset, float]): the total amount including the fee amount and taxes
        fee_rate_uuid (Union[Unset, str]): 26-character UUID of the fee rate used to calculate the fee summary
    """

    billing_date: Union[Unset, datetime.date] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total_period_units: Union[Unset, float] = UNSET
    total_basis_amount: Union[Unset, float] = UNSET
    total_fee_amount: Union[Unset, float] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    tax_1_amount: Union[Unset, float] = UNSET
    tax_2_amount: Union[Unset, float] = UNSET
    tax_3_amount: Union[Unset, float] = UNSET
    tax_4_amount: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    fee_rate_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.billing_date, Unset):
            billing_date = self.billing_date.isoformat()

        fee_category = self.fee_category

        fee_code = self.fee_code

        currency = self.currency

        total_period_units = self.total_period_units

        total_basis_amount = self.total_basis_amount

        total_fee_amount = self.total_fee_amount

        total_tax_amount = self.total_tax_amount

        tax_1_amount = self.tax_1_amount

        tax_2_amount = self.tax_2_amount

        tax_3_amount = self.tax_3_amount

        tax_4_amount = self.tax_4_amount

        total_amount = self.total_amount

        fee_rate_uuid = self.fee_rate_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_date is not UNSET:
            field_dict["billingDate"] = billing_date
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_period_units is not UNSET:
            field_dict["totalPeriodUnits"] = total_period_units
        if total_basis_amount is not UNSET:
            field_dict["totalBasisAmount"] = total_basis_amount
        if total_fee_amount is not UNSET:
            field_dict["totalFeeAmount"] = total_fee_amount
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
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if fee_rate_uuid is not UNSET:
            field_dict["feeRateUuid"] = fee_rate_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _billing_date = d.pop("billingDate", UNSET)
        billing_date: Union[Unset, datetime.date]
        if _billing_date and not isinstance(_billing_date, Unset):
            billing_date = isoparse(_billing_date).date()

        else:
            billing_date = UNSET

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        currency = d.pop("currency", UNSET)

        total_period_units = d.pop("totalPeriodUnits", UNSET)

        total_basis_amount = d.pop("totalBasisAmount", UNSET)

        total_fee_amount = d.pop("totalFeeAmount", UNSET)

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        tax_1_amount = d.pop("tax1Amount", UNSET)

        tax_2_amount = d.pop("tax2Amount", UNSET)

        tax_3_amount = d.pop("tax3Amount", UNSET)

        tax_4_amount = d.pop("tax4Amount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        fee_rate_uuid = d.pop("feeRateUuid", UNSET)

        api_fee_summary_estimate = cls(
            billing_date=billing_date,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            total_period_units=total_period_units,
            total_basis_amount=total_basis_amount,
            total_fee_amount=total_fee_amount,
            total_tax_amount=total_tax_amount,
            tax_1_amount=tax_1_amount,
            tax_2_amount=tax_2_amount,
            tax_3_amount=tax_3_amount,
            tax_4_amount=tax_4_amount,
            total_amount=total_amount,
            fee_rate_uuid=fee_rate_uuid,
        )

        api_fee_summary_estimate.additional_properties = d
        return api_fee_summary_estimate

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
