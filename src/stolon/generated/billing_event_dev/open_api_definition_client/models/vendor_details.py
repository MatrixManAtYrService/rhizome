from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="VendorDetails")


@_attrs_define
class VendorDetails:
    """
    Attributes:
        vendor_name (Union[Unset, str]):
        vendor_status_code (Union[Unset, str]):
        vendor_message_id (Union[Unset, str]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    vendor_name: Union[Unset, str] = UNSET
    vendor_status_code: Union[Unset, str] = UNSET
    vendor_message_id: Union[Unset, str] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vendor_name = self.vendor_name

        vendor_status_code = self.vendor_status_code

        vendor_message_id = self.vendor_message_id

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vendor_name is not UNSET:
            field_dict["vendorName"] = vendor_name
        if vendor_status_code is not UNSET:
            field_dict["vendorStatusCode"] = vendor_status_code
        if vendor_message_id is not UNSET:
            field_dict["vendorMessageId"] = vendor_message_id
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
        vendor_name = d.pop("vendorName", UNSET)

        vendor_status_code = d.pop("vendorStatusCode", UNSET)

        vendor_message_id = d.pop("vendorMessageId", UNSET)

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

        vendor_details = cls(
            vendor_name=vendor_name,
            vendor_status_code=vendor_status_code,
            vendor_message_id=vendor_message_id,
            specific_data=specific_data,
            schema=schema,
        )

        vendor_details.additional_properties = d
        return vendor_details

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
