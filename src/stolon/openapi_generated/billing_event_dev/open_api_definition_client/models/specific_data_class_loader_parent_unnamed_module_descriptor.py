from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpecificDataClassLoaderParentUnnamedModuleDescriptor")


@_attrs_define
class SpecificDataClassLoaderParentUnnamedModuleDescriptor:
    """
    Attributes:
        open_ (Union[Unset, bool]):
        automatic (Union[Unset, bool]):
    """

    open_: Union[Unset, bool] = UNSET
    automatic: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        automatic = self.automatic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_ is not UNSET:
            field_dict["open"] = open_
        if automatic is not UNSET:
            field_dict["automatic"] = automatic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_ = d.pop("open", UNSET)

        automatic = d.pop("automatic", UNSET)

        specific_data_class_loader_parent_unnamed_module_descriptor = cls(
            open_=open_,
            automatic=automatic,
        )

        specific_data_class_loader_parent_unnamed_module_descriptor.additional_properties = d
        return specific_data_class_loader_parent_unnamed_module_descriptor

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
