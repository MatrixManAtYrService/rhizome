from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversion_object import ConversionObject
    from ..models.fast_reader_builder import FastReaderBuilder
    from ..models.specific_data_class_loader import SpecificDataClassLoader


T = TypeVar("T", bound="SpecificData")


@_attrs_define
class SpecificData:
    """
    Attributes:
        class_loader (Union[Unset, SpecificDataClassLoader]):
        conversions (Union[Unset, list['ConversionObject']]):
        fast_reader_enabled (Union[Unset, bool]):
        fast_reader_builder (Union[Unset, FastReaderBuilder]):
        custom_coders (Union[Unset, bool]):
    """

    class_loader: Union[Unset, "SpecificDataClassLoader"] = UNSET
    conversions: Union[Unset, list["ConversionObject"]] = UNSET
    fast_reader_enabled: Union[Unset, bool] = UNSET
    fast_reader_builder: Union[Unset, "FastReaderBuilder"] = UNSET
    custom_coders: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_loader: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.class_loader, Unset):
            class_loader = self.class_loader.to_dict()

        conversions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conversions, Unset):
            conversions = []
            for conversions_item_data in self.conversions:
                conversions_item = conversions_item_data.to_dict()
                conversions.append(conversions_item)

        fast_reader_enabled = self.fast_reader_enabled

        fast_reader_builder: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fast_reader_builder, Unset):
            fast_reader_builder = self.fast_reader_builder.to_dict()

        custom_coders = self.custom_coders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_loader is not UNSET:
            field_dict["classLoader"] = class_loader
        if conversions is not UNSET:
            field_dict["conversions"] = conversions
        if fast_reader_enabled is not UNSET:
            field_dict["fastReaderEnabled"] = fast_reader_enabled
        if fast_reader_builder is not UNSET:
            field_dict["fastReaderBuilder"] = fast_reader_builder
        if custom_coders is not UNSET:
            field_dict["customCoders"] = custom_coders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_object import ConversionObject
        from ..models.fast_reader_builder import FastReaderBuilder
        from ..models.specific_data_class_loader import SpecificDataClassLoader

        d = dict(src_dict)
        _class_loader = d.pop("classLoader", UNSET)
        class_loader: Union[Unset, SpecificDataClassLoader]
        if isinstance(_class_loader, Unset):
            class_loader = UNSET
        else:
            class_loader = SpecificDataClassLoader.from_dict(_class_loader)

        conversions = []
        _conversions = d.pop("conversions", UNSET)
        for conversions_item_data in _conversions or []:
            conversions_item = ConversionObject.from_dict(conversions_item_data)

            conversions.append(conversions_item)

        fast_reader_enabled = d.pop("fastReaderEnabled", UNSET)

        _fast_reader_builder = d.pop("fastReaderBuilder", UNSET)
        fast_reader_builder: Union[Unset, FastReaderBuilder]
        if isinstance(_fast_reader_builder, Unset):
            fast_reader_builder = UNSET
        else:
            fast_reader_builder = FastReaderBuilder.from_dict(_fast_reader_builder)

        custom_coders = d.pop("customCoders", UNSET)

        specific_data = cls(
            class_loader=class_loader,
            conversions=conversions,
            fast_reader_enabled=fast_reader_enabled,
            fast_reader_builder=fast_reader_builder,
            custom_coders=custom_coders,
        )

        specific_data.additional_properties = d
        return specific_data

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
