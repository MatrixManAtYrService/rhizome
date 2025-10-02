from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_shipping_device_data import DeviceShippingDeviceData
    from ..models.device_shipping_package_data import DeviceShippingPackageData
    from ..models.merchant_data import MerchantData
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="DeviceShippingData")


@_attrs_define
class DeviceShippingData:
    """
    Attributes:
        merchant (Union[Unset, MerchantData]):
        address1 (Union[Unset, str]):
        address2 (Union[Unset, str]):
        city (Union[Unset, str]):
        state (Union[Unset, str]):
        zip_ (Union[Unset, str]):
        devices (Union[Unset, list['DeviceShippingDeviceData']]):
        packages (Union[Unset, list['DeviceShippingPackageData']]):
        is_lmm (Union[Unset, bool]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant: Union[Unset, "MerchantData"] = UNSET
    address1: Union[Unset, str] = UNSET
    address2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    zip_: Union[Unset, str] = UNSET
    devices: Union[Unset, list["DeviceShippingDeviceData"]] = UNSET
    packages: Union[Unset, list["DeviceShippingPackageData"]] = UNSET
    is_lmm: Union[Unset, bool] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        address1 = self.address1

        address2 = self.address2

        city = self.city

        state = self.state

        zip_ = self.zip_

        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        is_lmm = self.is_lmm

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
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if devices is not UNSET:
            field_dict["devices"] = devices
        if packages is not UNSET:
            field_dict["packages"] = packages
        if is_lmm is not UNSET:
            field_dict["isLMM"] = is_lmm
        if specific_data is not UNSET:
            field_dict["specificData"] = specific_data
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_shipping_device_data import DeviceShippingDeviceData
        from ..models.device_shipping_package_data import DeviceShippingPackageData
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

        address1 = d.pop("address1", UNSET)

        address2 = d.pop("address2", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        zip_ = d.pop("zip", UNSET)

        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = DeviceShippingDeviceData.from_dict(devices_item_data)

            devices.append(devices_item)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = DeviceShippingPackageData.from_dict(packages_item_data)

            packages.append(packages_item)

        is_lmm = d.pop("isLMM", UNSET)

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

        device_shipping_data = cls(
            merchant=merchant,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_=zip_,
            devices=devices,
            packages=packages,
            is_lmm=is_lmm,
            specific_data=specific_data,
            schema=schema,
        )

        device_shipping_data.additional_properties = d
        return device_shipping_data

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
