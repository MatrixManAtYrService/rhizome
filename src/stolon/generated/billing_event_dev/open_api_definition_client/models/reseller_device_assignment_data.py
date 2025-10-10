from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="ResellerDeviceAssignmentData")


@_attrs_define
class ResellerDeviceAssignmentData:
    """
    Attributes:
        reseller_uuid (Union[Unset, str]):
        device_serial_number (Union[Unset, str]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    reseller_uuid: Union[Unset, str] = UNSET
    device_serial_number: Union[Unset, str] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reseller_uuid = self.reseller_uuid

        device_serial_number = self.device_serial_number

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reseller_uuid is not UNSET:
            field_dict["resellerUuid"] = reseller_uuid
        if device_serial_number is not UNSET:
            field_dict["deviceSerialNumber"] = device_serial_number
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
        reseller_uuid = d.pop("resellerUuid", UNSET)

        device_serial_number = d.pop("deviceSerialNumber", UNSET)

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

        reseller_device_assignment_data = cls(
            reseller_uuid=reseller_uuid,
            device_serial_number=device_serial_number,
            specific_data=specific_data,
            schema=schema,
        )

        reseller_device_assignment_data.additional_properties = d
        return reseller_device_assignment_data

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
