from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.module_module_type import ModuleModuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Module")


@_attrs_define
class Module:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        module_type (Union[Unset, ModuleModuleType]):
        config (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    module_type: Union[Unset, ModuleModuleType] = UNSET
    config: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        module_type: Union[Unset, str] = UNSET
        if not isinstance(self.module_type, Unset):
            module_type = self.module_type.value

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if module_type is not UNSET:
            field_dict["moduleType"] = module_type
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _module_type = d.pop("moduleType", UNSET)
        module_type: Union[Unset, ModuleModuleType]
        if isinstance(_module_type, Unset):
            module_type = UNSET
        else:
            module_type = ModuleModuleType(_module_type)

        config = d.pop("config", UNSET)

        module = cls(
            id=id,
            name=name,
            module_type=module_type,
            config=config,
        )

        module.additional_properties = d
        return module

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
