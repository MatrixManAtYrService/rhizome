from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.specific_data_class_loader_unnamed_module_annotations_item import (
        SpecificDataClassLoaderUnnamedModuleAnnotationsItem,
    )
    from ..models.specific_data_class_loader_unnamed_module_declared_annotations_item import (
        SpecificDataClassLoaderUnnamedModuleDeclaredAnnotationsItem,
    )
    from ..models.specific_data_class_loader_unnamed_module_descriptor import (
        SpecificDataClassLoaderUnnamedModuleDescriptor,
    )
    from ..models.specific_data_class_loader_unnamed_module_layer import SpecificDataClassLoaderUnnamedModuleLayer


T = TypeVar("T", bound="SpecificDataClassLoaderUnnamedModule")


@_attrs_define
class SpecificDataClassLoaderUnnamedModule:
    """
    Attributes:
        name (Union[Unset, str]):
        descriptor (Union[Unset, SpecificDataClassLoaderUnnamedModuleDescriptor]):
        named (Union[Unset, bool]):
        annotations (Union[Unset, list['SpecificDataClassLoaderUnnamedModuleAnnotationsItem']]):
        declared_annotations (Union[Unset, list['SpecificDataClassLoaderUnnamedModuleDeclaredAnnotationsItem']]):
        packages (Union[Unset, list[str]]):
        layer (Union[Unset, SpecificDataClassLoaderUnnamedModuleLayer]):
    """

    name: Union[Unset, str] = UNSET
    descriptor: Union[Unset, "SpecificDataClassLoaderUnnamedModuleDescriptor"] = UNSET
    named: Union[Unset, bool] = UNSET
    annotations: Union[Unset, list["SpecificDataClassLoaderUnnamedModuleAnnotationsItem"]] = UNSET
    declared_annotations: Union[Unset, list["SpecificDataClassLoaderUnnamedModuleDeclaredAnnotationsItem"]] = UNSET
    packages: Union[Unset, list[str]] = UNSET
    layer: Union[Unset, "SpecificDataClassLoaderUnnamedModuleLayer"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descriptor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.descriptor, Unset):
            descriptor = self.descriptor.to_dict()

        named = self.named

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

        packages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = self.packages

        layer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.layer, Unset):
            layer = self.layer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descriptor is not UNSET:
            field_dict["descriptor"] = descriptor
        if named is not UNSET:
            field_dict["named"] = named
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if declared_annotations is not UNSET:
            field_dict["declaredAnnotations"] = declared_annotations
        if packages is not UNSET:
            field_dict["packages"] = packages
        if layer is not UNSET:
            field_dict["layer"] = layer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.specific_data_class_loader_unnamed_module_annotations_item import (
            SpecificDataClassLoaderUnnamedModuleAnnotationsItem,
        )
        from ..models.specific_data_class_loader_unnamed_module_declared_annotations_item import (
            SpecificDataClassLoaderUnnamedModuleDeclaredAnnotationsItem,
        )
        from ..models.specific_data_class_loader_unnamed_module_descriptor import (
            SpecificDataClassLoaderUnnamedModuleDescriptor,
        )
        from ..models.specific_data_class_loader_unnamed_module_layer import SpecificDataClassLoaderUnnamedModuleLayer

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _descriptor = d.pop("descriptor", UNSET)
        descriptor: Union[Unset, SpecificDataClassLoaderUnnamedModuleDescriptor]
        if _descriptor and not isinstance(_descriptor, Unset):
            descriptor = SpecificDataClassLoaderUnnamedModuleDescriptor.from_dict(_descriptor)

        else:
            descriptor = UNSET

        named = d.pop("named", UNSET)

        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = SpecificDataClassLoaderUnnamedModuleAnnotationsItem.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        declared_annotations = []
        _declared_annotations = d.pop("declaredAnnotations", UNSET)
        for declared_annotations_item_data in _declared_annotations or []:
            declared_annotations_item = SpecificDataClassLoaderUnnamedModuleDeclaredAnnotationsItem.from_dict(
                declared_annotations_item_data
            )

            declared_annotations.append(declared_annotations_item)

        packages = cast(list[str], d.pop("packages", UNSET))

        _layer = d.pop("layer", UNSET)
        layer: Union[Unset, SpecificDataClassLoaderUnnamedModuleLayer]
        if _layer and not isinstance(_layer, Unset):
            layer = SpecificDataClassLoaderUnnamedModuleLayer.from_dict(_layer)

        else:
            layer = UNSET

        specific_data_class_loader_unnamed_module = cls(
            name=name,
            descriptor=descriptor,
            named=named,
            annotations=annotations,
            declared_annotations=declared_annotations,
            packages=packages,
            layer=layer,
        )

        specific_data_class_loader_unnamed_module.additional_properties = d
        return specific_data_class_loader_unnamed_module

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
