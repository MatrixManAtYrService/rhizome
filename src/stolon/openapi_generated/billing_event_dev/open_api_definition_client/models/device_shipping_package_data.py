import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="DeviceShippingPackageData")


@_attrs_define
class DeviceShippingPackageData:
    """
    Attributes:
        tracking_number (Union[Unset, str]):
        tracking_url (Union[Unset, str]):
        shipper (Union[Unset, str]):
        shipped_date (Union[Unset, datetime.datetime]):
        shipped_service (Union[Unset, str]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    tracking_number: Union[Unset, str] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    shipper: Union[Unset, str] = UNSET
    shipped_date: Union[Unset, datetime.datetime] = UNSET
    shipped_service: Union[Unset, str] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracking_number = self.tracking_number

        tracking_url = self.tracking_url

        shipper = self.shipper

        shipped_date: Union[Unset, str] = UNSET
        if not isinstance(self.shipped_date, Unset):
            shipped_date = self.shipped_date.isoformat()

        shipped_service = self.shipped_service

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if tracking_url is not UNSET:
            field_dict["trackingUrl"] = tracking_url
        if shipper is not UNSET:
            field_dict["shipper"] = shipper
        if shipped_date is not UNSET:
            field_dict["shippedDate"] = shipped_date
        if shipped_service is not UNSET:
            field_dict["shippedService"] = shipped_service
        if specific_data is not UNSET:
            field_dict["specificData"] = specific_data
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema import Schema
        from ..models.specific_data import SpecificData

        d = dict(src_dict)
        tracking_number = d.pop("trackingNumber", UNSET)

        tracking_url = d.pop("trackingUrl", UNSET)

        shipper = d.pop("shipper", UNSET)

        _shipped_date = d.pop("shippedDate", UNSET)
        shipped_date: Union[Unset, datetime.datetime]
        if _shipped_date and not isinstance(_shipped_date, Unset):
            shipped_date = isoparse(_shipped_date)

        else:
            shipped_date = UNSET

        shipped_service = d.pop("shippedService", UNSET)

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

        device_shipping_package_data = cls(
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            shipper=shipper,
            shipped_date=shipped_date,
            shipped_service=shipped_service,
            specific_data=specific_data,
            schema=schema,
        )

        device_shipping_package_data.additional_properties = d
        return device_shipping_package_data

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
