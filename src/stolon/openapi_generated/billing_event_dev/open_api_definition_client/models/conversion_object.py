from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema import Schema


T = TypeVar("T", bound="ConversionObject")


@_attrs_define
class ConversionObject:
    """
    Attributes:
        recommended_schema (Union[Unset, Schema]):
        logical_type_name (Union[Unset, str]):
    """

    recommended_schema: Union[Unset, "Schema"] = UNSET
    logical_type_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recommended_schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recommended_schema, Unset):
            recommended_schema = self.recommended_schema.to_dict()

        logical_type_name = self.logical_type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recommended_schema is not UNSET:
            field_dict["recommendedSchema"] = recommended_schema
        if logical_type_name is not UNSET:
            field_dict["logicalTypeName"] = logical_type_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema import Schema

        d = dict(src_dict)
        _recommended_schema = d.pop("recommendedSchema", UNSET)
        recommended_schema: Union[Unset, Schema]
        if _recommended_schema and not isinstance(_recommended_schema, Unset):
            recommended_schema = Schema.from_dict(_recommended_schema)

        else:
            recommended_schema = UNSET

        logical_type_name = d.pop("logicalTypeName", UNSET)

        conversion_object = cls(
            recommended_schema=recommended_schema,
            logical_type_name=logical_type_name,
        )

        conversion_object.additional_properties = d
        return conversion_object

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
