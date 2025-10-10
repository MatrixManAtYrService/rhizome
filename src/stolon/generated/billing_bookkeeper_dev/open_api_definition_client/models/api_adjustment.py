import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAdjustment")


@_attrs_define
class ApiAdjustment:
    """
    Attributes:
        tlement_uuid (Union[Unset, ApiAdjustment]):
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the invoice belongs to
        settlement_uuid (Union[Unset, str]): 26-character UUID of the settlement request
        adjust_reason (Union[Unset, str]): reason for the adjustment action
        adjust_action_type (Union[Unset, str]): defined adjustment action type value
        adjust_amount (Union[Unset, float]): the adjustment amount
        currency (Union[Unset, str]): 3-letter currency code Example: USD.
        developer_uuid (Union[Unset, str]): 13-character UUID of the developer that the adjustment applies to; only
            applies to app-related adjustments
        developer_app_uuid (Union[Unset, str]): 13-character UUID of the developer app that the adjustment applies to;
            only applies to app-related adjustments
        reference (Union[Unset, str]): freeform comment or reference identifier for this adjustment action
        adjust_action_uuid (Union[Unset, str]): 26-character UUID of the adjustment action created
        fee_category (Union[Unset, str]): fee category assigned to the adjustment
        fee_code (Union[Unset, str]): fee code assigned to the adjustment
        action_date_time (Union[Unset, datetime.datetime]): date and time that the adjustment occurred Example:
            2020-12-31T23:59:59.123456Z.
        posting_date (Union[Unset, datetime.date]): posting date used for the adjustment
    """

    tlement_uuid: Union[Unset, "ApiAdjustment"] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    settlement_uuid: Union[Unset, str] = UNSET
    adjust_reason: Union[Unset, str] = UNSET
    adjust_action_type: Union[Unset, str] = UNSET
    adjust_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    adjust_action_uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    action_date_time: Union[Unset, datetime.datetime] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlement_uuid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_uuid, Unset):
            tlement_uuid = self.tlement_uuid.to_dict()

        billing_entity_uuid = self.billing_entity_uuid

        settlement_uuid = self.settlement_uuid

        adjust_reason = self.adjust_reason

        adjust_action_type = self.adjust_action_type

        adjust_amount = self.adjust_amount

        currency = self.currency

        developer_uuid = self.developer_uuid

        developer_app_uuid = self.developer_app_uuid

        reference = self.reference

        adjust_action_uuid = self.adjust_action_uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        action_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.action_date_time, Unset):
            action_date_time = self.action_date_time.isoformat()

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tlement_uuid is not UNSET:
            field_dict["tlementUuid"] = tlement_uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if settlement_uuid is not UNSET:
            field_dict["settlementUuid"] = settlement_uuid
        if adjust_reason is not UNSET:
            field_dict["adjustReason"] = adjust_reason
        if adjust_action_type is not UNSET:
            field_dict["adjustActionType"] = adjust_action_type
        if adjust_amount is not UNSET:
            field_dict["adjustAmount"] = adjust_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if developer_app_uuid is not UNSET:
            field_dict["developerAppUuid"] = developer_app_uuid
        if reference is not UNSET:
            field_dict["reference"] = reference
        if adjust_action_uuid is not UNSET:
            field_dict["adjustActionUuid"] = adjust_action_uuid
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if action_date_time is not UNSET:
            field_dict["actionDateTime"] = action_date_time
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tlement_uuid = d.pop("tlementUuid", UNSET)
        tlement_uuid: Union[Unset, ApiAdjustment]
        if _tlement_uuid and not isinstance(_tlement_uuid, Unset):
            tlement_uuid = ApiAdjustment.from_dict(_tlement_uuid)

        else:
            tlement_uuid = UNSET

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        settlement_uuid = d.pop("settlementUuid", UNSET)

        adjust_reason = d.pop("adjustReason", UNSET)

        adjust_action_type = d.pop("adjustActionType", UNSET)

        adjust_amount = d.pop("adjustAmount", UNSET)

        currency = d.pop("currency", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        reference = d.pop("reference", UNSET)

        adjust_action_uuid = d.pop("adjustActionUuid", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        _action_date_time = d.pop("actionDateTime", UNSET)
        action_date_time: Union[Unset, datetime.datetime]
        if _action_date_time and not isinstance(_action_date_time, Unset):
            action_date_time = isoparse(_action_date_time)

        else:
            action_date_time = UNSET

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if _posting_date and not isinstance(_posting_date, Unset):
            posting_date = isoparse(_posting_date).date()

        else:
            posting_date = UNSET

        api_adjustment = cls(
            tlement_uuid=tlement_uuid,
            billing_entity_uuid=billing_entity_uuid,
            settlement_uuid=settlement_uuid,
            adjust_reason=adjust_reason,
            adjust_action_type=adjust_action_type,
            adjust_amount=adjust_amount,
            currency=currency,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            reference=reference,
            adjust_action_uuid=adjust_action_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            action_date_time=action_date_time,
            posting_date=posting_date,
        )

        api_adjustment.additional_properties = d
        return api_adjustment

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
