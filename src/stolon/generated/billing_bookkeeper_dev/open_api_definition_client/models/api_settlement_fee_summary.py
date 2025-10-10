import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_settlement_fee_summary_apply_type import ApiSettlementFeeSummaryApplyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_action import ApiAction


T = TypeVar("T", bound="ApiSettlementFeeSummary")


@_attrs_define
class ApiSettlementFeeSummary:
    """the fee summaries that contributed to the settlement total

    Attributes:
        fee_summary_uuid (Union[Unset, str]): 26-character UUID of the fee summary
        invoice_info_uuid (Union[Unset, str]): 26-character UUID of the invoice info that this fee summary appears on
        billing_date (Union[Unset, datetime.date]): billing date
        fee_category (Union[Unset, str]): defined fee category value
        fee_code (Union[Unset, str]): defined fee code value
        fee_short_desc (Union[Unset, str]): short description of the fee
        fee_desc (Union[Unset, str]): full description of the fee
        total_period_units (Union[Unset, float]): the total number of units billed
        total_basis_amount (Union[Unset, float]): the total basis amount billed
        total_fee_amount (Union[Unset, float]): the total fee amount billed
        currency (Union[Unset, str]): the currency of the fee summary Example: USD.
        fee_rate_uuid (Union[Unset, str]): 26-character UUID of the applied fee rate
        apply_type (Union[Unset, ApiSettlementFeeSummaryApplyType]):
        per_item_amount (Union[Unset, float]): the per-item fee rate amount
        percentage_fee_rate (Union[Unset, float]): the percentage fee rate
        fee_summary_actions (Union[Unset, list['ApiAction']]): the actions associated with this fee summary
    """

    fee_summary_uuid: Union[Unset, str] = UNSET
    invoice_info_uuid: Union[Unset, str] = UNSET
    billing_date: Union[Unset, datetime.date] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    fee_short_desc: Union[Unset, str] = UNSET
    fee_desc: Union[Unset, str] = UNSET
    total_period_units: Union[Unset, float] = UNSET
    total_basis_amount: Union[Unset, float] = UNSET
    total_fee_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    fee_rate_uuid: Union[Unset, str] = UNSET
    apply_type: Union[Unset, ApiSettlementFeeSummaryApplyType] = UNSET
    per_item_amount: Union[Unset, float] = UNSET
    percentage_fee_rate: Union[Unset, float] = UNSET
    fee_summary_actions: Union[Unset, list["ApiAction"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_summary_uuid = self.fee_summary_uuid

        invoice_info_uuid = self.invoice_info_uuid

        billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.billing_date, Unset):
            billing_date = self.billing_date.isoformat()

        fee_category = self.fee_category

        fee_code = self.fee_code

        fee_short_desc = self.fee_short_desc

        fee_desc = self.fee_desc

        total_period_units = self.total_period_units

        total_basis_amount = self.total_basis_amount

        total_fee_amount = self.total_fee_amount

        currency = self.currency

        fee_rate_uuid = self.fee_rate_uuid

        apply_type: Union[Unset, str] = UNSET
        if not isinstance(self.apply_type, Unset):
            apply_type = self.apply_type.value

        per_item_amount = self.per_item_amount

        percentage_fee_rate = self.percentage_fee_rate

        fee_summary_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_summary_actions, Unset):
            fee_summary_actions = []
            for fee_summary_actions_item_data in self.fee_summary_actions:
                fee_summary_actions_item = fee_summary_actions_item_data.to_dict()
                fee_summary_actions.append(fee_summary_actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_summary_uuid is not UNSET:
            field_dict["feeSummaryUuid"] = fee_summary_uuid
        if invoice_info_uuid is not UNSET:
            field_dict["invoiceInfoUuid"] = invoice_info_uuid
        if billing_date is not UNSET:
            field_dict["billingDate"] = billing_date
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if fee_short_desc is not UNSET:
            field_dict["feeShortDesc"] = fee_short_desc
        if fee_desc is not UNSET:
            field_dict["feeDesc"] = fee_desc
        if total_period_units is not UNSET:
            field_dict["totalPeriodUnits"] = total_period_units
        if total_basis_amount is not UNSET:
            field_dict["totalBasisAmount"] = total_basis_amount
        if total_fee_amount is not UNSET:
            field_dict["totalFeeAmount"] = total_fee_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if fee_rate_uuid is not UNSET:
            field_dict["feeRateUuid"] = fee_rate_uuid
        if apply_type is not UNSET:
            field_dict["applyType"] = apply_type
        if per_item_amount is not UNSET:
            field_dict["perItemAmount"] = per_item_amount
        if percentage_fee_rate is not UNSET:
            field_dict["percentageFeeRate"] = percentage_fee_rate
        if fee_summary_actions is not UNSET:
            field_dict["feeSummaryActions"] = fee_summary_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_action import ApiAction

        d = dict(src_dict)
        fee_summary_uuid = d.pop("feeSummaryUuid", UNSET)

        invoice_info_uuid = d.pop("invoiceInfoUuid", UNSET)

        _billing_date = d.pop("billingDate", UNSET)
        billing_date: Union[Unset, datetime.date]
        if _billing_date and not isinstance(_billing_date, Unset):
            billing_date = isoparse(_billing_date).date()

        else:
            billing_date = UNSET

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        fee_short_desc = d.pop("feeShortDesc", UNSET)

        fee_desc = d.pop("feeDesc", UNSET)

        total_period_units = d.pop("totalPeriodUnits", UNSET)

        total_basis_amount = d.pop("totalBasisAmount", UNSET)

        total_fee_amount = d.pop("totalFeeAmount", UNSET)

        currency = d.pop("currency", UNSET)

        fee_rate_uuid = d.pop("feeRateUuid", UNSET)

        _apply_type = d.pop("applyType", UNSET)
        apply_type: Union[Unset, ApiSettlementFeeSummaryApplyType]
        if _apply_type and not isinstance(_apply_type, Unset):
            apply_type = ApiSettlementFeeSummaryApplyType(_apply_type)

        else:
            apply_type = UNSET

        per_item_amount = d.pop("perItemAmount", UNSET)

        percentage_fee_rate = d.pop("percentageFeeRate", UNSET)

        fee_summary_actions = []
        _fee_summary_actions = d.pop("feeSummaryActions", UNSET)
        for fee_summary_actions_item_data in _fee_summary_actions or []:
            fee_summary_actions_item = ApiAction.from_dict(fee_summary_actions_item_data)

            fee_summary_actions.append(fee_summary_actions_item)

        api_settlement_fee_summary = cls(
            fee_summary_uuid=fee_summary_uuid,
            invoice_info_uuid=invoice_info_uuid,
            billing_date=billing_date,
            fee_category=fee_category,
            fee_code=fee_code,
            fee_short_desc=fee_short_desc,
            fee_desc=fee_desc,
            total_period_units=total_period_units,
            total_basis_amount=total_basis_amount,
            total_fee_amount=total_fee_amount,
            currency=currency,
            fee_rate_uuid=fee_rate_uuid,
            apply_type=apply_type,
            per_item_amount=per_item_amount,
            percentage_fee_rate=percentage_fee_rate,
            fee_summary_actions=fee_summary_actions,
        )

        api_settlement_fee_summary.additional_properties = d
        return api_settlement_fee_summary

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
