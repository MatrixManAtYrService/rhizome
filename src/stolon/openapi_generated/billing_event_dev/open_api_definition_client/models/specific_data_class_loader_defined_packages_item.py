from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.specific_data_class_loader_defined_packages_item_annotations_item import (
        SpecificDataClassLoaderDefinedPackagesItemAnnotationsItem,
    )
    from ..models.specific_data_class_loader_defined_packages_item_declared_annotations_item import (
        SpecificDataClassLoaderDefinedPackagesItemDeclaredAnnotationsItem,
    )


T = TypeVar("T", bound="SpecificDataClassLoaderDefinedPackagesItem")


@_attrs_define
class SpecificDataClassLoaderDefinedPackagesItem:
    """
    Attributes:
        name (Union[Unset, str]):
        annotations (Union[Unset, list['SpecificDataClassLoaderDefinedPackagesItemAnnotationsItem']]):
        declared_annotations (Union[Unset, list['SpecificDataClassLoaderDefinedPackagesItemDeclaredAnnotationsItem']]):
        sealed (Union[Unset, bool]):
        specification_title (Union[Unset, str]):
        specification_version (Union[Unset, str]):
        specification_vendor (Union[Unset, str]):
        implementation_title (Union[Unset, str]):
        implementation_version (Union[Unset, str]):
        implementation_vendor (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    annotations: Union[Unset, list["SpecificDataClassLoaderDefinedPackagesItemAnnotationsItem"]] = UNSET
    declared_annotations: Union[Unset, list["SpecificDataClassLoaderDefinedPackagesItemDeclaredAnnotationsItem"]] = (
        UNSET
    )
    sealed: Union[Unset, bool] = UNSET
    specification_title: Union[Unset, str] = UNSET
    specification_version: Union[Unset, str] = UNSET
    specification_vendor: Union[Unset, str] = UNSET
    implementation_title: Union[Unset, str] = UNSET
    implementation_version: Union[Unset, str] = UNSET
    implementation_vendor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        declared_annotations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.declared_annotations, Unset):
            declared_annotations = []
            for declared_annotations_item_data in self.declared_annotations:
                declared_annotations_item = declared_annotations_item_data.to_dict()
                declared_annotations.append(declared_annotations_item)

        sealed = self.sealed

        specification_title = self.specification_title

        specification_version = self.specification_version

        specification_vendor = self.specification_vendor

        implementation_title = self.implementation_title

        implementation_version = self.implementation_version

        implementation_vendor = self.implementation_vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if declared_annotations is not UNSET:
            field_dict["declaredAnnotations"] = declared_annotations
        if sealed is not UNSET:
            field_dict["sealed"] = sealed
        if specification_title is not UNSET:
            field_dict["specificationTitle"] = specification_title
        if specification_version is not UNSET:
            field_dict["specificationVersion"] = specification_version
        if specification_vendor is not UNSET:
            field_dict["specificationVendor"] = specification_vendor
        if implementation_title is not UNSET:
            field_dict["implementationTitle"] = implementation_title
        if implementation_version is not UNSET:
            field_dict["implementationVersion"] = implementation_version
        if implementation_vendor is not UNSET:
            field_dict["implementationVendor"] = implementation_vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.specific_data_class_loader_defined_packages_item_annotations_item import (
            SpecificDataClassLoaderDefinedPackagesItemAnnotationsItem,
        )
        from ..models.specific_data_class_loader_defined_packages_item_declared_annotations_item import (
            SpecificDataClassLoaderDefinedPackagesItemDeclaredAnnotationsItem,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = SpecificDataClassLoaderDefinedPackagesItemAnnotationsItem.from_dict(
                annotations_item_data
            )

            annotations.append(annotations_item)

        declared_annotations = []
        _declared_annotations = d.pop("declaredAnnotations", UNSET)
        for declared_annotations_item_data in _declared_annotations or []:
            declared_annotations_item = SpecificDataClassLoaderDefinedPackagesItemDeclaredAnnotationsItem.from_dict(
                declared_annotations_item_data
            )

            declared_annotations.append(declared_annotations_item)

        sealed = d.pop("sealed", UNSET)

        specification_title = d.pop("specificationTitle", UNSET)

        specification_version = d.pop("specificationVersion", UNSET)

        specification_vendor = d.pop("specificationVendor", UNSET)

        implementation_title = d.pop("implementationTitle", UNSET)

        implementation_version = d.pop("implementationVersion", UNSET)

        implementation_vendor = d.pop("implementationVendor", UNSET)

        specific_data_class_loader_defined_packages_item = cls(
            name=name,
            annotations=annotations,
            declared_annotations=declared_annotations,
            sealed=sealed,
            specification_title=specification_title,
            specification_version=specification_version,
            specification_vendor=specification_vendor,
            implementation_title=implementation_title,
            implementation_version=implementation_version,
            implementation_vendor=implementation_vendor,
        )

        specific_data_class_loader_defined_packages_item.additional_properties = d
        return specific_data_class_loader_defined_packages_item

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
