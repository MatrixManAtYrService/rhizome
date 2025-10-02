import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_settlement_adjust_info_entity_type import ApiSettlementAdjustInfoEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSettlementAdjustInfo")


@_attrs_define
class ApiSettlementAdjustInfo:
    """
    Attributes:
        tlement_tax_amount (Union[Unset, ApiSettlementAdjustInfo]):
        tlement_fee_amount (Union[Unset, ApiSettlementAdjustInfo]):
        tlement_uuid (Union[Unset, ApiSettlementAdjustInfo]):
        tlement_date (Union[Unset, ApiSettlementAdjustInfo]):
        settlement_uuid (Union[Unset, str]): 26-character UUID of the settlement request
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the settlement belongs to
        billing_entity_name (Union[Unset, str]): name of the billing entity
        entity_uuid (Union[Unset, str]): 13-character COS UUID of the billing entity
        entity_type (Union[Unset, ApiSettlementAdjustInfoEntityType]):
        settlement_date (Union[Unset, datetime.date]): settlement date of the settlement request
        settlement_fee_amount (Union[Unset, float]): the total fee amount of the settlement request, does not include
            taxes
        settlement_tax_amount (Union[Unset, float]): the total of tax amounts for the settlement request
        total_settlement_amount (Union[Unset, float]): the total amount of the settlement request including fees and
            taxes
        total_fee_amount_settled (Union[Unset, float]): the total fee amount currently settled, does not include taxes
        total_fee_amount_adjusted (Union[Unset, float]): the total fee amount adjusted against the settlement amount,
            does not include taxes
        refundable_amount (Union[Unset, float]): the total amount that is refundable
        currency (Union[Unset, str]): the currency of the settlement amounts Example: USD.
        ledger_account_key (Union[Unset, str]): the ledger account key for the ledger account that fee summaries were
            initially posted to for settlement
        adjust_action_type (Union[Unset, str]): the adjustment action type that applies to this settlement
        fee_category_group (Union[Unset, str]): the fee category grouping for the settlement fees
        revenue_group (Union[Unset, str]): the revenue group for the settlement fees, if applicable
        error_message (Union[Unset, str]): an error message indicating why the settlement and adjustment info could not
            be returned
    """

    tlement_tax_amount: Union[Unset, "ApiSettlementAdjustInfo"] = UNSET
    tlement_fee_amount: Union[Unset, "ApiSettlementAdjustInfo"] = UNSET
    tlement_uuid: Union[Unset, "ApiSettlementAdjustInfo"] = UNSET
    tlement_date: Union[Unset, "ApiSettlementAdjustInfo"] = UNSET
    settlement_uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiSettlementAdjustInfoEntityType] = UNSET
    settlement_date: Union[Unset, datetime.date] = UNSET
    settlement_fee_amount: Union[Unset, float] = UNSET
    settlement_tax_amount: Union[Unset, float] = UNSET
    total_settlement_amount: Union[Unset, float] = UNSET
    total_fee_amount_settled: Union[Unset, float] = UNSET
    total_fee_amount_adjusted: Union[Unset, float] = UNSET
    refundable_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    ledger_account_key: Union[Unset, str] = UNSET
    adjust_action_type: Union[Unset, str] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    revenue_group: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlement_tax_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_tax_amount, Unset):
            tlement_tax_amount = self.tlement_tax_amount.to_dict()

        tlement_fee_amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_fee_amount, Unset):
            tlement_fee_amount = self.tlement_fee_amount.to_dict()

        tlement_uuid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_uuid, Unset):
            tlement_uuid = self.tlement_uuid.to_dict()

        tlement_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_date, Unset):
            tlement_date = self.tlement_date.to_dict()

        settlement_uuid = self.settlement_uuid

        billing_entity_uuid = self.billing_entity_uuid

        billing_entity_name = self.billing_entity_name

        entity_uuid = self.entity_uuid

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        settlement_date: Union[Unset, str] = UNSET
        if not isinstance(self.settlement_date, Unset):
            settlement_date = self.settlement_date.isoformat()

        settlement_fee_amount = self.settlement_fee_amount

        settlement_tax_amount = self.settlement_tax_amount

        total_settlement_amount = self.total_settlement_amount

        total_fee_amount_settled = self.total_fee_amount_settled

        total_fee_amount_adjusted = self.total_fee_amount_adjusted

        refundable_amount = self.refundable_amount

        currency = self.currency

        ledger_account_key = self.ledger_account_key

        adjust_action_type = self.adjust_action_type

        fee_category_group = self.fee_category_group

        revenue_group = self.revenue_group

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tlement_tax_amount is not UNSET:
            field_dict["tlementTaxAmount"] = tlement_tax_amount
        if tlement_fee_amount is not UNSET:
            field_dict["tlementFeeAmount"] = tlement_fee_amount
        if tlement_uuid is not UNSET:
            field_dict["tlementUuid"] = tlement_uuid
        if tlement_date is not UNSET:
            field_dict["tlementDate"] = tlement_date
        if settlement_uuid is not UNSET:
            field_dict["settlementUuid"] = settlement_uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if billing_entity_name is not UNSET:
            field_dict["billingEntityName"] = billing_entity_name
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if settlement_date is not UNSET:
            field_dict["settlementDate"] = settlement_date
        if settlement_fee_amount is not UNSET:
            field_dict["settlementFeeAmount"] = settlement_fee_amount
        if settlement_tax_amount is not UNSET:
            field_dict["settlementTaxAmount"] = settlement_tax_amount
        if total_settlement_amount is not UNSET:
            field_dict["totalSettlementAmount"] = total_settlement_amount
        if total_fee_amount_settled is not UNSET:
            field_dict["totalFeeAmountSettled"] = total_fee_amount_settled
        if total_fee_amount_adjusted is not UNSET:
            field_dict["totalFeeAmountAdjusted"] = total_fee_amount_adjusted
        if refundable_amount is not UNSET:
            field_dict["refundableAmount"] = refundable_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ledger_account_key is not UNSET:
            field_dict["ledgerAccountKey"] = ledger_account_key
        if adjust_action_type is not UNSET:
            field_dict["adjustActionType"] = adjust_action_type
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if revenue_group is not UNSET:
            field_dict["revenueGroup"] = revenue_group
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tlement_tax_amount = d.pop("tlementTaxAmount", UNSET)
        tlement_tax_amount: Union[Unset, ApiSettlementAdjustInfo]
        if isinstance(_tlement_tax_amount, Unset):
            tlement_tax_amount = UNSET
        else:
            tlement_tax_amount = ApiSettlementAdjustInfo.from_dict(_tlement_tax_amount)

        _tlement_fee_amount = d.pop("tlementFeeAmount", UNSET)
        tlement_fee_amount: Union[Unset, ApiSettlementAdjustInfo]
        if isinstance(_tlement_fee_amount, Unset):
            tlement_fee_amount = UNSET
        else:
            tlement_fee_amount = ApiSettlementAdjustInfo.from_dict(_tlement_fee_amount)

        _tlement_uuid = d.pop("tlementUuid", UNSET)
        tlement_uuid: Union[Unset, ApiSettlementAdjustInfo]
        if isinstance(_tlement_uuid, Unset):
            tlement_uuid = UNSET
        else:
            tlement_uuid = ApiSettlementAdjustInfo.from_dict(_tlement_uuid)

        _tlement_date = d.pop("tlementDate", UNSET)
        tlement_date: Union[Unset, ApiSettlementAdjustInfo]
        if isinstance(_tlement_date, Unset):
            tlement_date = UNSET
        else:
            tlement_date = ApiSettlementAdjustInfo.from_dict(_tlement_date)

        settlement_uuid = d.pop("settlementUuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, ApiSettlementAdjustInfoEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = ApiSettlementAdjustInfoEntityType(_entity_type)

        _settlement_date = d.pop("settlementDate", UNSET)
        settlement_date: Union[Unset, datetime.date]
        if isinstance(_settlement_date, Unset):
            settlement_date = UNSET
        else:
            settlement_date = isoparse(_settlement_date).date()

        settlement_fee_amount = d.pop("settlementFeeAmount", UNSET)

        settlement_tax_amount = d.pop("settlementTaxAmount", UNSET)

        total_settlement_amount = d.pop("totalSettlementAmount", UNSET)

        total_fee_amount_settled = d.pop("totalFeeAmountSettled", UNSET)

        total_fee_amount_adjusted = d.pop("totalFeeAmountAdjusted", UNSET)

        refundable_amount = d.pop("refundableAmount", UNSET)

        currency = d.pop("currency", UNSET)

        ledger_account_key = d.pop("ledgerAccountKey", UNSET)

        adjust_action_type = d.pop("adjustActionType", UNSET)

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        revenue_group = d.pop("revenueGroup", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        api_settlement_adjust_info = cls(
            tlement_tax_amount=tlement_tax_amount,
            tlement_fee_amount=tlement_fee_amount,
            tlement_uuid=tlement_uuid,
            tlement_date=tlement_date,
            settlement_uuid=settlement_uuid,
            billing_entity_uuid=billing_entity_uuid,
            billing_entity_name=billing_entity_name,
            entity_uuid=entity_uuid,
            entity_type=entity_type,
            settlement_date=settlement_date,
            settlement_fee_amount=settlement_fee_amount,
            settlement_tax_amount=settlement_tax_amount,
            total_settlement_amount=total_settlement_amount,
            total_fee_amount_settled=total_fee_amount_settled,
            total_fee_amount_adjusted=total_fee_amount_adjusted,
            refundable_amount=refundable_amount,
            currency=currency,
            ledger_account_key=ledger_account_key,
            adjust_action_type=adjust_action_type,
            fee_category_group=fee_category_group,
            revenue_group=revenue_group,
            error_message=error_message,
        )

        api_settlement_adjust_info.additional_properties = d
        return api_settlement_adjust_info

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
