from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.i_config_data_type import IConfigDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_config_current_value import IConfigCurrentValue
    from ..models.i_config_default_value import IConfigDefaultValue


T = TypeVar("T", bound="IConfig")


@_attrs_define
class IConfig:
    """
    Attributes:
        name (Union[Unset, str]):
        default_value (Union[Unset, IConfigDefaultValue]):
        description (Union[Unset, str]):
        current_value (Union[Unset, IConfigCurrentValue]):
        default_value_as_string (Union[Unset, str]):
        data_type (Union[Unset, IConfigDataType]):
        is_nullable (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    default_value: Union[Unset, "IConfigDefaultValue"] = UNSET
    description: Union[Unset, str] = UNSET
    current_value: Union[Unset, "IConfigCurrentValue"] = UNSET
    default_value_as_string: Union[Unset, str] = UNSET
    data_type: Union[Unset, IConfigDataType] = UNSET
    is_nullable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        default_value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        description = self.description

        current_value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.current_value, Unset):
            current_value = self.current_value.to_dict()

        default_value_as_string = self.default_value_as_string

        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        is_nullable = self.is_nullable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if description is not UNSET:
            field_dict["description"] = description
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if default_value_as_string is not UNSET:
            field_dict["defaultValueAsString"] = default_value_as_string
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if is_nullable is not UNSET:
            field_dict["isNullable"] = is_nullable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_config_current_value import IConfigCurrentValue
        from ..models.i_config_default_value import IConfigDefaultValue

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _default_value = d.pop("defaultValue", UNSET)
        default_value: Union[Unset, IConfigDefaultValue]
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = IConfigDefaultValue.from_dict(_default_value)

        description = d.pop("description", UNSET)

        _current_value = d.pop("currentValue", UNSET)
        current_value: Union[Unset, IConfigCurrentValue]
        if isinstance(_current_value, Unset):
            current_value = UNSET
        else:
            current_value = IConfigCurrentValue.from_dict(_current_value)

        default_value_as_string = d.pop("defaultValueAsString", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, IConfigDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = IConfigDataType(_data_type)

        is_nullable = d.pop("isNullable", UNSET)

        i_config = cls(
            name=name,
            default_value=default_value,
            description=description,
            current_value=current_value,
            default_value_as_string=default_value_as_string,
            data_type=data_type,
            is_nullable=is_nullable,
        )

        i_config.additional_properties = d
        return i_config

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
