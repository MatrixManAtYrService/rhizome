from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_data_activation_type import DeviceDataActivationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_data import MerchantData
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="DeviceData")


@_attrs_define
class DeviceData:
    """
    Attributes:
        merchant (Union[Unset, MerchantData]):
        serial_number (Union[Unset, str]):
        equipment_number (Union[Unset, str]):
        originating_serial_number (Union[Unset, str]):
        activation_code (Union[Unset, str]):
        provisioned_via_shipping (Union[Unset, bool]):
        activation_type (Union[Unset, DeviceDataActivationType]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant: Union[Unset, "MerchantData"] = UNSET
    serial_number: Union[Unset, str] = UNSET
    equipment_number: Union[Unset, str] = UNSET
    originating_serial_number: Union[Unset, str] = UNSET
    activation_code: Union[Unset, str] = UNSET
    provisioned_via_shipping: Union[Unset, bool] = UNSET
    activation_type: Union[Unset, DeviceDataActivationType] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        serial_number = self.serial_number

        equipment_number = self.equipment_number

        originating_serial_number = self.originating_serial_number

        activation_code = self.activation_code

        provisioned_via_shipping = self.provisioned_via_shipping

        activation_type: Union[Unset, str] = UNSET
        if not isinstance(self.activation_type, Unset):
            activation_type = self.activation_type.value

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if equipment_number is not UNSET:
            field_dict["equipmentNumber"] = equipment_number
        if originating_serial_number is not UNSET:
            field_dict["originatingSerialNumber"] = originating_serial_number
        if activation_code is not UNSET:
            field_dict["activationCode"] = activation_code
        if provisioned_via_shipping is not UNSET:
            field_dict["provisionedViaShipping"] = provisioned_via_shipping
        if activation_type is not UNSET:
            field_dict["activationType"] = activation_type
        if specific_data is not UNSET:
            field_dict["specificData"] = specific_data
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merchant_data import MerchantData
        from ..models.schema import Schema
        from ..models.specific_data import SpecificData

        d = dict(src_dict)
        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, MerchantData]
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = MerchantData.from_dict(_merchant)

        serial_number = d.pop("serialNumber", UNSET)

        equipment_number = d.pop("equipmentNumber", UNSET)

        originating_serial_number = d.pop("originatingSerialNumber", UNSET)

        activation_code = d.pop("activationCode", UNSET)

        provisioned_via_shipping = d.pop("provisionedViaShipping", UNSET)

        _activation_type = d.pop("activationType", UNSET)
        activation_type: Union[Unset, DeviceDataActivationType]
        if isinstance(_activation_type, Unset):
            activation_type = UNSET
        else:
            activation_type = DeviceDataActivationType(_activation_type)

        _specific_data = d.pop("specificData", UNSET)
        specific_data: Union[Unset, SpecificData]
        if isinstance(_specific_data, Unset):
            specific_data = UNSET
        else:
            specific_data = SpecificData.from_dict(_specific_data)

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, Schema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = Schema.from_dict(_schema)

        device_data = cls(
            merchant=merchant,
            serial_number=serial_number,
            equipment_number=equipment_number,
            originating_serial_number=originating_serial_number,
            activation_code=activation_code,
            provisioned_via_shipping=provisioned_via_shipping,
            activation_type=activation_type,
            specific_data=specific_data,
            schema=schema,
        )

        device_data.additional_properties = d
        return device_data

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
