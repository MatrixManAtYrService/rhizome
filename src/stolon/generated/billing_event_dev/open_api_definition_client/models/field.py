from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_object_props import FieldObjectProps


T = TypeVar("T", bound="Field")


@_attrs_define
class Field:
    """
    Attributes:
        object_props (Union[Unset, FieldObjectProps]):
    """

    object_props: Union[Unset, "FieldObjectProps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_props: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_props, Unset):
            object_props = self.object_props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_props is not UNSET:
            field_dict["objectProps"] = object_props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_object_props import FieldObjectProps

        d = dict(src_dict)
        _object_props = d.pop("objectProps", UNSET)
        object_props: Union[Unset, FieldObjectProps]
        if isinstance(_object_props, Unset):
            object_props = UNSET
        else:
            object_props = FieldObjectProps.from_dict(_object_props)

        field = cls(
            object_props=object_props,
        )

        field.additional_properties = d
        return field

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
