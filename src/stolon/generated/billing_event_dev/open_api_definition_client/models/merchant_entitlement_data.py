from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="MerchantEntitlementData")


@_attrs_define
class MerchantEntitlementData:
    """
    Attributes:
        name (Union[Unset, str]):
        service_entitlement_number (Union[Unset, str]):
        service_type (Union[Unset, str]):
        alpha_id (Union[Unset, str]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    name: Union[Unset, str] = UNSET
    service_entitlement_number: Union[Unset, str] = UNSET
    service_type: Union[Unset, str] = UNSET
    alpha_id: Union[Unset, str] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        service_entitlement_number = self.service_entitlement_number

        service_type = self.service_type

        alpha_id = self.alpha_id

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if service_entitlement_number is not UNSET:
            field_dict["serviceEntitlementNumber"] = service_entitlement_number
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if alpha_id is not UNSET:
            field_dict["alphaId"] = alpha_id
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
        name = d.pop("name", UNSET)

        service_entitlement_number = d.pop("serviceEntitlementNumber", UNSET)

        service_type = d.pop("serviceType", UNSET)

        alpha_id = d.pop("alphaId", UNSET)

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

        merchant_entitlement_data = cls(
            name=name,
            service_entitlement_number=service_entitlement_number,
            service_type=service_type,
            alpha_id=alpha_id,
            specific_data=specific_data,
            schema=schema,
        )

        merchant_entitlement_data.additional_properties = d
        return merchant_entitlement_data

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
