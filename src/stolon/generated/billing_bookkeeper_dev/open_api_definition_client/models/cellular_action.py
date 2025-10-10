import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CellularAction")


@_attrs_define
class CellularAction:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        billing_entity_name (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        action_date_time (Union[Unset, datetime.datetime]):
        num_units (Union[Unset, int]):
        units_in_period (Union[Unset, int]):
        basis_amount (Union[Unset, float]):
        basis_currency (Union[Unset, str]):
        reference (Union[Unset, str]):
        fee_uuid (Union[Unset, str]):
        event_uuid (Union[Unset, str]):
        request_uuid (Union[Unset, str]):
        date_to_post (Union[Unset, datetime.date]):
        posting_date (Union[Unset, datetime.date]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
        merchant_plan_uuid (Union[Unset, str]):
        iccid (Union[Unset, str]):
        carrier (Union[Unset, str]):
        cellular_action_type (Union[Unset, str]):
        cellular_action_fee_code_uuid (Union[Unset, str]):
        action_type (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    action_date_time: Union[Unset, datetime.datetime] = UNSET
    num_units: Union[Unset, int] = UNSET
    units_in_period: Union[Unset, int] = UNSET
    basis_amount: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    fee_uuid: Union[Unset, str] = UNSET
    event_uuid: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    date_to_post: Union[Unset, datetime.date] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    iccid: Union[Unset, str] = UNSET
    carrier: Union[Unset, str] = UNSET
    cellular_action_type: Union[Unset, str] = UNSET
    cellular_action_fee_code_uuid: Union[Unset, str] = UNSET
    action_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        billing_entity_name = self.billing_entity_name

        entity_uuid = self.entity_uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        action_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.action_date_time, Unset):
            action_date_time = self.action_date_time.isoformat()

        num_units = self.num_units

        units_in_period = self.units_in_period

        basis_amount = self.basis_amount

        basis_currency = self.basis_currency

        reference = self.reference

        fee_uuid = self.fee_uuid

        event_uuid = self.event_uuid

        request_uuid = self.request_uuid

        date_to_post: Union[Unset, str] = UNSET
        if not isinstance(self.date_to_post, Unset):
            date_to_post = self.date_to_post.isoformat()

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        merchant_plan_uuid = self.merchant_plan_uuid

        iccid = self.iccid

        carrier = self.carrier

        cellular_action_type = self.cellular_action_type

        cellular_action_fee_code_uuid = self.cellular_action_fee_code_uuid

        action_type = self.action_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if billing_entity_name is not UNSET:
            field_dict["billingEntityName"] = billing_entity_name
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if action_date_time is not UNSET:
            field_dict["actionDateTime"] = action_date_time
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units
        if units_in_period is not UNSET:
            field_dict["unitsInPeriod"] = units_in_period
        if basis_amount is not UNSET:
            field_dict["basisAmount"] = basis_amount
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency
        if reference is not UNSET:
            field_dict["reference"] = reference
        if fee_uuid is not UNSET:
            field_dict["feeUuid"] = fee_uuid
        if event_uuid is not UNSET:
            field_dict["eventUuid"] = event_uuid
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if date_to_post is not UNSET:
            field_dict["dateToPost"] = date_to_post
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if iccid is not UNSET:
            field_dict["iccid"] = iccid
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if cellular_action_type is not UNSET:
            field_dict["cellularActionType"] = cellular_action_type
        if cellular_action_fee_code_uuid is not UNSET:
            field_dict["cellularActionFeeCodeUuid"] = cellular_action_fee_code_uuid
        if action_type is not UNSET:
            field_dict["actionType"] = action_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        _action_date_time = d.pop("actionDateTime", UNSET)
        action_date_time: Union[Unset, datetime.datetime]
        if _action_date_time and not isinstance(_action_date_time, Unset):
            action_date_time = isoparse(_action_date_time)

        else:
            action_date_time = UNSET

        num_units = d.pop("numUnits", UNSET)

        units_in_period = d.pop("unitsInPeriod", UNSET)

        basis_amount = d.pop("basisAmount", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        reference = d.pop("reference", UNSET)

        fee_uuid = d.pop("feeUuid", UNSET)

        event_uuid = d.pop("eventUuid", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        _date_to_post = d.pop("dateToPost", UNSET)
        date_to_post: Union[Unset, datetime.date]
        if _date_to_post and not isinstance(_date_to_post, Unset):
            date_to_post = isoparse(_date_to_post).date()

        else:
            date_to_post = UNSET

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if _posting_date and not isinstance(_posting_date, Unset):
            posting_date = isoparse(_posting_date).date()

        else:
            posting_date = UNSET

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if _modified_timestamp and not isinstance(_modified_timestamp, Unset):
            modified_timestamp = isoparse(_modified_timestamp)

        else:
            modified_timestamp = UNSET

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        iccid = d.pop("iccid", UNSET)

        carrier = d.pop("carrier", UNSET)

        cellular_action_type = d.pop("cellularActionType", UNSET)

        cellular_action_fee_code_uuid = d.pop("cellularActionFeeCodeUuid", UNSET)

        action_type = d.pop("actionType", UNSET)

        cellular_action = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            billing_entity_name=billing_entity_name,
            entity_uuid=entity_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            action_date_time=action_date_time,
            num_units=num_units,
            units_in_period=units_in_period,
            basis_amount=basis_amount,
            basis_currency=basis_currency,
            reference=reference,
            fee_uuid=fee_uuid,
            event_uuid=event_uuid,
            request_uuid=request_uuid,
            date_to_post=date_to_post,
            posting_date=posting_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            merchant_plan_uuid=merchant_plan_uuid,
            iccid=iccid,
            carrier=carrier,
            cellular_action_type=cellular_action_type,
            cellular_action_fee_code_uuid=cellular_action_fee_code_uuid,
            action_type=action_type,
        )

        cellular_action.additional_properties = d
        return cellular_action

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
