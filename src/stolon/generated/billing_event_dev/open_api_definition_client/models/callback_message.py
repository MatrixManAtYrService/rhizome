from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.callback_message_clover_headers import CallbackMessageCloverHeaders
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData
    from ..models.vendor_details import VendorDetails


T = TypeVar("T", bound="CallbackMessage")


@_attrs_define
class CallbackMessage:
    """
    Attributes:
        notification_channel (Union[Unset, str]):
        status (Union[Unset, str]):
        vendor_message_id (Union[Unset, str]):
        url (Union[Unset, str]):
        clover_headers (Union[Unset, CallbackMessageCloverHeaders]):
        correlation_id (Union[Unset, str]):
        vendor_details (Union[Unset, VendorDetails]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    notification_channel: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    vendor_message_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    clover_headers: Union[Unset, "CallbackMessageCloverHeaders"] = UNSET
    correlation_id: Union[Unset, str] = UNSET
    vendor_details: Union[Unset, "VendorDetails"] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_channel = self.notification_channel

        status = self.status

        vendor_message_id = self.vendor_message_id

        url = self.url

        clover_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.clover_headers, Unset):
            clover_headers = self.clover_headers.to_dict()

        correlation_id = self.correlation_id

        vendor_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor_details, Unset):
            vendor_details = self.vendor_details.to_dict()

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_channel is not UNSET:
            field_dict["notificationChannel"] = notification_channel
        if status is not UNSET:
            field_dict["status"] = status
        if vendor_message_id is not UNSET:
            field_dict["vendorMessageId"] = vendor_message_id
        if url is not UNSET:
            field_dict["url"] = url
        if clover_headers is not UNSET:
            field_dict["cloverHeaders"] = clover_headers
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if vendor_details is not UNSET:
            field_dict["vendorDetails"] = vendor_details
        if specific_data is not UNSET:
            field_dict["specificData"] = specific_data
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.callback_message_clover_headers import CallbackMessageCloverHeaders
        from ..models.schema import Schema
        from ..models.specific_data import SpecificData
        from ..models.vendor_details import VendorDetails

        d = dict(src_dict)
        notification_channel = d.pop("notificationChannel", UNSET)

        status = d.pop("status", UNSET)

        vendor_message_id = d.pop("vendorMessageId", UNSET)

        url = d.pop("url", UNSET)

        _clover_headers = d.pop("cloverHeaders", UNSET)
        clover_headers: Union[Unset, CallbackMessageCloverHeaders]
        if _clover_headers and not isinstance(_clover_headers, Unset):
            clover_headers = CallbackMessageCloverHeaders.from_dict(_clover_headers)

        else:
            clover_headers = UNSET

        correlation_id = d.pop("correlationId", UNSET)

        _vendor_details = d.pop("vendorDetails", UNSET)
        vendor_details: Union[Unset, VendorDetails]
        if _vendor_details and not isinstance(_vendor_details, Unset):
            vendor_details = VendorDetails.from_dict(_vendor_details)

        else:
            vendor_details = UNSET

        _specific_data = d.pop("specificData", UNSET)
        specific_data: Union[Unset, SpecificData]
        if _specific_data and not isinstance(_specific_data, Unset):
            specific_data = SpecificData.from_dict(_specific_data)

        else:
            specific_data = UNSET

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, Schema]
        if _schema and not isinstance(_schema, Unset):
            schema = Schema.from_dict(_schema)

        else:
            schema = UNSET

        callback_message = cls(
            notification_channel=notification_channel,
            status=status,
            vendor_message_id=vendor_message_id,
            url=url,
            clover_headers=clover_headers,
            correlation_id=correlation_id,
            vendor_details=vendor_details,
            specific_data=specific_data,
            schema=schema,
        )

        callback_message.additional_properties = d
        return callback_message

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
