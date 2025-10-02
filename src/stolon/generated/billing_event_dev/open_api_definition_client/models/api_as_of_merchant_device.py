import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAsOfMerchantDevice")


@_attrs_define
class ApiAsOfMerchantDevice:
    """devices belonging to the merchant for the as-of date break

    Attributes:
        id (Union[Unset, int]): ID of the merchant's device data associated with an as-of date break
        uuid (Union[Unset, str]): 26-character UUID for the merchant's device data associated with an as-of date break
        as_of_merchant_uuid (Union[Unset, str]): 26-character UUID for the merchant's as-of date break
        serial_number (Union[Unset, str]): serial number for a merchant's device that was included for the date break
        device_type (Union[Unset, str]): type of device that this as-of-merchant-device is for based on the serial
            number
        bundle_indicator (Union[Unset, str]): bundle indicator of the device when the device is bundled as part of a
            plan
        modifier1 (Union[Unset, str]): first billing modifier assigned to the device for the date break
        modifier2 (Union[Unset, str]): second billing modifier assigned to the device for the date break
        created_timestamp (Union[Unset, datetime.datetime]): timestamp for when the merchant's device data associated
            with an as-of date break was first created Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    as_of_merchant_uuid: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    bundle_indicator: Union[Unset, str] = UNSET
    modifier1: Union[Unset, str] = UNSET
    modifier2: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        as_of_merchant_uuid = self.as_of_merchant_uuid

        serial_number = self.serial_number

        device_type = self.device_type

        bundle_indicator = self.bundle_indicator

        modifier1 = self.modifier1

        modifier2 = self.modifier2

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if as_of_merchant_uuid is not UNSET:
            field_dict["asOfMerchantUuid"] = as_of_merchant_uuid
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if bundle_indicator is not UNSET:
            field_dict["bundleIndicator"] = bundle_indicator
        if modifier1 is not UNSET:
            field_dict["modifier1"] = modifier1
        if modifier2 is not UNSET:
            field_dict["modifier2"] = modifier2
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        as_of_merchant_uuid = d.pop("asOfMerchantUuid", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        device_type = d.pop("deviceType", UNSET)

        bundle_indicator = d.pop("bundleIndicator", UNSET)

        modifier1 = d.pop("modifier1", UNSET)

        modifier2 = d.pop("modifier2", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_as_of_merchant_device = cls(
            id=id,
            uuid=uuid,
            as_of_merchant_uuid=as_of_merchant_uuid,
            serial_number=serial_number,
            device_type=device_type,
            bundle_indicator=bundle_indicator,
            modifier1=modifier1,
            modifier2=modifier2,
            created_timestamp=created_timestamp,
        )

        api_as_of_merchant_device.additional_properties = d
        return api_as_of_merchant_device

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
