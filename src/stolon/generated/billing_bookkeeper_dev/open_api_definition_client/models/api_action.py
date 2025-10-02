import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAction")


@_attrs_define
class ApiAction:
    """
    Attributes:
        id (Union[Unset, int]): Id of action
        action_uuid (Union[Unset, str]): 26-character UUID of action
        action_type (Union[Unset, str]): defined action type value
        action_source (Union[Unset, str]): source of action (action type) ex. PLAN, APP_SUB, APP_METER, CELLULAR, MISC,
            REVENUE
        fee_category (Union[Unset, str]): fee category mapped to by the action
        fee_code (Union[Unset, str]): fee code value
        num_units (Union[Unset, int]): the number of billable units for the action
        units_in_period (Union[Unset, int]): the number of billable units in the billing entity billing period
        basis_amount (Union[Unset, float]): the basis amount for the action
        basis_currency (Union[Unset, str]): 3-letter currency code
        action_date_time (Union[Unset, datetime.datetime]): date and time that the action occurred
        posting_date (Union[Unset, datetime.date]): posting date
        fee_uuid (Union[Unset, str]): 26-character UUID of the fee CTD or fee summary that this action was applied
            towards
        reference (Union[Unset, str]): freeform comment or reference identifier for this action
    """

    id: Union[Unset, int] = UNSET
    action_uuid: Union[Unset, str] = UNSET
    action_type: Union[Unset, str] = UNSET
    action_source: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    num_units: Union[Unset, int] = UNSET
    units_in_period: Union[Unset, int] = UNSET
    basis_amount: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    action_date_time: Union[Unset, datetime.datetime] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    fee_uuid: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        action_uuid = self.action_uuid

        action_type = self.action_type

        action_source = self.action_source

        fee_category = self.fee_category

        fee_code = self.fee_code

        num_units = self.num_units

        units_in_period = self.units_in_period

        basis_amount = self.basis_amount

        basis_currency = self.basis_currency

        action_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.action_date_time, Unset):
            action_date_time = self.action_date_time.isoformat()

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        fee_uuid = self.fee_uuid

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if action_uuid is not UNSET:
            field_dict["actionUuid"] = action_uuid
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if action_source is not UNSET:
            field_dict["actionSource"] = action_source
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units
        if units_in_period is not UNSET:
            field_dict["unitsInPeriod"] = units_in_period
        if basis_amount is not UNSET:
            field_dict["basisAmount"] = basis_amount
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency
        if action_date_time is not UNSET:
            field_dict["actionDateTime"] = action_date_time
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date
        if fee_uuid is not UNSET:
            field_dict["feeUuid"] = fee_uuid
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        action_uuid = d.pop("actionUuid", UNSET)

        action_type = d.pop("actionType", UNSET)

        action_source = d.pop("actionSource", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        num_units = d.pop("numUnits", UNSET)

        units_in_period = d.pop("unitsInPeriod", UNSET)

        basis_amount = d.pop("basisAmount", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        _action_date_time = d.pop("actionDateTime", UNSET)
        action_date_time: Union[Unset, datetime.datetime]
        if isinstance(_action_date_time, Unset):
            action_date_time = UNSET
        else:
            action_date_time = isoparse(_action_date_time)

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if isinstance(_posting_date, Unset):
            posting_date = UNSET
        else:
            posting_date = isoparse(_posting_date).date()

        fee_uuid = d.pop("feeUuid", UNSET)

        reference = d.pop("reference", UNSET)

        api_action = cls(
            id=id,
            action_uuid=action_uuid,
            action_type=action_type,
            action_source=action_source,
            fee_category=fee_category,
            fee_code=fee_code,
            num_units=num_units,
            units_in_period=units_in_period,
            basis_amount=basis_amount,
            basis_currency=basis_currency,
            action_date_time=action_date_time,
            posting_date=posting_date,
            fee_uuid=fee_uuid,
            reference=reference,
        )

        api_action.additional_properties = d
        return api_action

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
