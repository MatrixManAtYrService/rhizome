from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lexi_attr_intent_intent_type import LexiAttrIntentIntentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lexi_attribute_dto import LexiAttributeDTO


T = TypeVar("T", bound="LexiAttrIntent")


@_attrs_define
class LexiAttrIntent:
    """
    Attributes:
        lexi_attribute (Union[Unset, LexiAttributeDTO]):
        intent_type (Union[Unset, LexiAttrIntentIntentType]):
    """

    lexi_attribute: Union[Unset, "LexiAttributeDTO"] = UNSET
    intent_type: Union[Unset, LexiAttrIntentIntentType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lexi_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.lexi_attribute, Unset):
            lexi_attribute = self.lexi_attribute.to_dict()

        intent_type: Union[Unset, str] = UNSET
        if not isinstance(self.intent_type, Unset):
            intent_type = self.intent_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lexi_attribute is not UNSET:
            field_dict["lexiAttribute"] = lexi_attribute
        if intent_type is not UNSET:
            field_dict["intentType"] = intent_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lexi_attribute_dto import LexiAttributeDTO

        d = dict(src_dict)
        _lexi_attribute = d.pop("lexiAttribute", UNSET)
        lexi_attribute: Union[Unset, LexiAttributeDTO]
        if _lexi_attribute and not isinstance(_lexi_attribute, Unset):
            lexi_attribute = LexiAttributeDTO.from_dict(_lexi_attribute)

        else:
            lexi_attribute = UNSET

        _intent_type = d.pop("intentType", UNSET)
        intent_type: Union[Unset, LexiAttrIntentIntentType]
        if _intent_type and not isinstance(_intent_type, Unset):
            intent_type = LexiAttrIntentIntentType(_intent_type)

        else:
            intent_type = UNSET

        lexi_attr_intent = cls(
            lexi_attribute=lexi_attribute,
            intent_type=intent_type,
        )

        lexi_attr_intent.additional_properties = d
        return lexi_attr_intent

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
