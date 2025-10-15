import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_as_of_merchant_device import ApiAsOfMerchantDevice
    from ..models.api_as_of_merchant_plan import ApiAsOfMerchantPlan


T = TypeVar("T", bound="ApiAsOfMerchant")


@_attrs_define
class ApiAsOfMerchant:
    """
    Attributes:
        id (Union[Unset, int]): ID of the merchant's as-of date break
        uuid (Union[Unset, str]): 26-character UUID for the merchant's as-of date break
        merchant_uuid (Union[Unset, str]): 13-character COS UUID for the merchant
        as_of_timestamp (Union[Unset, datetime.datetime]): date and time for the merchant's as-of date break Example:
            2020-12-31T23:59:59.123456Z.
        event_datetime (Union[Unset, datetime.datetime]): date and time of the event that triggered the as-of date break
            Example: 2020-12-31T23:59:59.123456Z.
        billing_event_uuid (Union[Unset, str]): 26-character UUID for the billing event associated with the as-of date
            break
        request_uuid (Union[Unset, str]): 26-character UUID for the job execution request associated with the as-of date
            break
        created_timestamp (Union[Unset, datetime.datetime]): timestamp for when the merchant evolution data was first
            created Example: 2020-12-31T23:59:59.123456Z.
        plan (Union[Unset, ApiAsOfMerchantPlan]):
        devices (Union[Unset, list['ApiAsOfMerchantDevice']]): devices belonging to the merchant for the as-of date
            break
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    as_of_timestamp: Union[Unset, datetime.datetime] = UNSET
    event_datetime: Union[Unset, datetime.datetime] = UNSET
    billing_event_uuid: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    plan: Union[Unset, "ApiAsOfMerchantPlan"] = UNSET
    devices: Union[Unset, list["ApiAsOfMerchantDevice"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        merchant_uuid = self.merchant_uuid

        as_of_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.as_of_timestamp, Unset):
            as_of_timestamp = self.as_of_timestamp.isoformat()

        event_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.event_datetime, Unset):
            event_datetime = self.event_datetime.isoformat()

        billing_event_uuid = self.billing_event_uuid

        request_uuid = self.request_uuid

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if as_of_timestamp is not UNSET:
            field_dict["asOfTimestamp"] = as_of_timestamp
        if event_datetime is not UNSET:
            field_dict["eventDatetime"] = event_datetime
        if billing_event_uuid is not UNSET:
            field_dict["billingEventUuid"] = billing_event_uuid
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if plan is not UNSET:
            field_dict["plan"] = plan
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_as_of_merchant_device import ApiAsOfMerchantDevice
        from ..models.api_as_of_merchant_plan import ApiAsOfMerchantPlan

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        _as_of_timestamp = d.pop("asOfTimestamp", UNSET)
        as_of_timestamp: Union[Unset, datetime.datetime]
        if _as_of_timestamp and not isinstance(_as_of_timestamp, Unset):
            as_of_timestamp = isoparse(_as_of_timestamp)

        else:
            as_of_timestamp = UNSET

        _event_datetime = d.pop("eventDatetime", UNSET)
        event_datetime: Union[Unset, datetime.datetime]
        if _event_datetime and not isinstance(_event_datetime, Unset):
            event_datetime = isoparse(_event_datetime)

        else:
            event_datetime = UNSET

        billing_event_uuid = d.pop("billingEventUuid", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, ApiAsOfMerchantPlan]
        if _plan and not isinstance(_plan, Unset):
            plan = ApiAsOfMerchantPlan.from_dict(_plan)

        else:
            plan = UNSET

        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = ApiAsOfMerchantDevice.from_dict(devices_item_data)

            devices.append(devices_item)

        api_as_of_merchant = cls(
            id=id,
            uuid=uuid,
            merchant_uuid=merchant_uuid,
            as_of_timestamp=as_of_timestamp,
            event_datetime=event_datetime,
            billing_event_uuid=billing_event_uuid,
            request_uuid=request_uuid,
            created_timestamp=created_timestamp,
            plan=plan,
            devices=devices,
        )

        api_as_of_merchant.additional_properties = d
        return api_as_of_merchant

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
