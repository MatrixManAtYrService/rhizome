from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Elements")


@_attrs_define
class Elements:
    """
    Attributes:
        merchant_id (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        equipment_code_desc (Union[Unset, str]):
        boarded (Union[Unset, str]):
        provisioned (Union[Unset, str]):
        provisioned_device_type (Union[Unset, str]):
        equipment_code (Union[Unset, str]):
        equipment_number (Union[Unset, str]):
        rki (Union[Unset, str]):
    """

    merchant_id: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    equipment_code_desc: Union[Unset, str] = UNSET
    boarded: Union[Unset, str] = UNSET
    provisioned: Union[Unset, str] = UNSET
    provisioned_device_type: Union[Unset, str] = UNSET
    equipment_code: Union[Unset, str] = UNSET
    equipment_number: Union[Unset, str] = UNSET
    rki: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant_id = self.merchant_id

        serial_number = self.serial_number

        equipment_code_desc = self.equipment_code_desc

        boarded = self.boarded

        provisioned = self.provisioned

        provisioned_device_type = self.provisioned_device_type

        equipment_code = self.equipment_code

        equipment_number = self.equipment_number

        rki = self.rki

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant_id is not UNSET:
            field_dict["merchantId"] = merchant_id
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if equipment_code_desc is not UNSET:
            field_dict["equipmentCodeDesc"] = equipment_code_desc
        if boarded is not UNSET:
            field_dict["boarded"] = boarded
        if provisioned is not UNSET:
            field_dict["provisioned"] = provisioned
        if provisioned_device_type is not UNSET:
            field_dict["provisionedDeviceType"] = provisioned_device_type
        if equipment_code is not UNSET:
            field_dict["equipmentCode"] = equipment_code
        if equipment_number is not UNSET:
            field_dict["equipmentNumber"] = equipment_number
        if rki is not UNSET:
            field_dict["rki"] = rki

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        merchant_id = d.pop("merchantId", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        equipment_code_desc = d.pop("equipmentCodeDesc", UNSET)

        boarded = d.pop("boarded", UNSET)

        provisioned = d.pop("provisioned", UNSET)

        provisioned_device_type = d.pop("provisionedDeviceType", UNSET)

        equipment_code = d.pop("equipmentCode", UNSET)

        equipment_number = d.pop("equipmentNumber", UNSET)

        rki = d.pop("rki", UNSET)

        elements = cls(
            merchant_id=merchant_id,
            serial_number=serial_number,
            equipment_code_desc=equipment_code_desc,
            boarded=boarded,
            provisioned=provisioned,
            provisioned_device_type=provisioned_device_type,
            equipment_code=equipment_code,
            equipment_number=equipment_number,
            rki=rki,
        )

        elements.additional_properties = d
        return elements

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
