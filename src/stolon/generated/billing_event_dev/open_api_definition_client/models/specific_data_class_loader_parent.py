from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.specific_data_class_loader_parent_defined_packages_item import (
        SpecificDataClassLoaderParentDefinedPackagesItem,
    )
    from ..models.specific_data_class_loader_parent_unnamed_module import SpecificDataClassLoaderParentUnnamedModule


T = TypeVar("T", bound="SpecificDataClassLoaderParent")


@_attrs_define
class SpecificDataClassLoaderParent:
    """
    Attributes:
        name (Union[Unset, str]):
        registered_as_parallel_capable (Union[Unset, bool]):
        unnamed_module (Union[Unset, SpecificDataClassLoaderParentUnnamedModule]):
        defined_packages (Union[Unset, list['SpecificDataClassLoaderParentDefinedPackagesItem']]):
        default_assertion_status (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    registered_as_parallel_capable: Union[Unset, bool] = UNSET
    unnamed_module: Union[Unset, "SpecificDataClassLoaderParentUnnamedModule"] = UNSET
    defined_packages: Union[Unset, list["SpecificDataClassLoaderParentDefinedPackagesItem"]] = UNSET
    default_assertion_status: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        registered_as_parallel_capable = self.registered_as_parallel_capable

        unnamed_module: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.unnamed_module, Unset):
            unnamed_module = self.unnamed_module.to_dict()

        defined_packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.defined_packages, Unset):
            defined_packages = []
            for defined_packages_item_data in self.defined_packages:
                defined_packages_item = defined_packages_item_data.to_dict()
                defined_packages.append(defined_packages_item)

        default_assertion_status = self.default_assertion_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if registered_as_parallel_capable is not UNSET:
            field_dict["registeredAsParallelCapable"] = registered_as_parallel_capable
        if unnamed_module is not UNSET:
            field_dict["unnamedModule"] = unnamed_module
        if defined_packages is not UNSET:
            field_dict["definedPackages"] = defined_packages
        if default_assertion_status is not UNSET:
            field_dict["defaultAssertionStatus"] = default_assertion_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.specific_data_class_loader_parent_defined_packages_item import (
            SpecificDataClassLoaderParentDefinedPackagesItem,
        )
        from ..models.specific_data_class_loader_parent_unnamed_module import SpecificDataClassLoaderParentUnnamedModule

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        registered_as_parallel_capable = d.pop("registeredAsParallelCapable", UNSET)

        _unnamed_module = d.pop("unnamedModule", UNSET)
        unnamed_module: Union[Unset, SpecificDataClassLoaderParentUnnamedModule]
        if _unnamed_module and not isinstance(_unnamed_module, Unset):
            unnamed_module = SpecificDataClassLoaderParentUnnamedModule.from_dict(_unnamed_module)

        else:
            unnamed_module = UNSET

        defined_packages = []
        _defined_packages = d.pop("definedPackages", UNSET)
        for defined_packages_item_data in _defined_packages or []:
            defined_packages_item = SpecificDataClassLoaderParentDefinedPackagesItem.from_dict(
                defined_packages_item_data
            )

            defined_packages.append(defined_packages_item)

        default_assertion_status = d.pop("defaultAssertionStatus", UNSET)

        specific_data_class_loader_parent = cls(
            name=name,
            registered_as_parallel_capable=registered_as_parallel_capable,
            unnamed_module=unnamed_module,
            defined_packages=defined_packages,
            default_assertion_status=default_assertion_status,
        )

        specific_data_class_loader_parent.additional_properties = d
        return specific_data_class_loader_parent

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
