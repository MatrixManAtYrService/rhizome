import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_fee_summary_total_by_fee_category_group import ApiFeeSummaryTotalByFeeCategoryGroup


T = TypeVar("T", bound="ApiFeeSummaryFeeCategoryForBillingDate")


@_attrs_define
class ApiFeeSummaryFeeCategoryForBillingDate:
    """
    Attributes:
        billing_date (Union[Unset, datetime.date]): billing date
        invoice_number (Union[Unset, str]): invoice number assigned to the invoice
        invoice_uuid (Union[Unset, str]): 26-character UUID of the invoice document
        fee_category_fee_summary_totals (Union[Unset, list['ApiFeeSummaryTotalByFeeCategoryGroup']]): the fee details
            belonging to the fee category grouping
    """

    billing_date: Union[Unset, datetime.date] = UNSET
    invoice_number: Union[Unset, str] = UNSET
    invoice_uuid: Union[Unset, str] = UNSET
    fee_category_fee_summary_totals: Union[Unset, list["ApiFeeSummaryTotalByFeeCategoryGroup"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.billing_date, Unset):
            billing_date = self.billing_date.isoformat()

        invoice_number = self.invoice_number

        invoice_uuid = self.invoice_uuid

        fee_category_fee_summary_totals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_category_fee_summary_totals, Unset):
            fee_category_fee_summary_totals = []
            for fee_category_fee_summary_totals_item_data in self.fee_category_fee_summary_totals:
                fee_category_fee_summary_totals_item = fee_category_fee_summary_totals_item_data.to_dict()
                fee_category_fee_summary_totals.append(fee_category_fee_summary_totals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_date is not UNSET:
            field_dict["billingDate"] = billing_date
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if invoice_uuid is not UNSET:
            field_dict["invoiceUuid"] = invoice_uuid
        if fee_category_fee_summary_totals is not UNSET:
            field_dict["feeCategoryFeeSummaryTotals"] = fee_category_fee_summary_totals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_fee_summary_total_by_fee_category_group import ApiFeeSummaryTotalByFeeCategoryGroup

        d = dict(src_dict)
        _billing_date = d.pop("billingDate", UNSET)
        billing_date: Union[Unset, datetime.date]
        if isinstance(_billing_date, Unset):
            billing_date = UNSET
        else:
            billing_date = isoparse(_billing_date).date()

        invoice_number = d.pop("invoiceNumber", UNSET)

        invoice_uuid = d.pop("invoiceUuid", UNSET)

        fee_category_fee_summary_totals = []
        _fee_category_fee_summary_totals = d.pop("feeCategoryFeeSummaryTotals", UNSET)
        for fee_category_fee_summary_totals_item_data in _fee_category_fee_summary_totals or []:
            fee_category_fee_summary_totals_item = ApiFeeSummaryTotalByFeeCategoryGroup.from_dict(
                fee_category_fee_summary_totals_item_data
            )

            fee_category_fee_summary_totals.append(fee_category_fee_summary_totals_item)

        api_fee_summary_fee_category_for_billing_date = cls(
            billing_date=billing_date,
            invoice_number=invoice_number,
            invoice_uuid=invoice_uuid,
            fee_category_fee_summary_totals=fee_category_fee_summary_totals,
        )

        api_fee_summary_fee_category_for_billing_date.additional_properties = d
        return api_fee_summary_fee_category_for_billing_date

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
