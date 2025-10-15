from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activation_rule import ActivationRule
    from ..models.base_rule import BaseRule
    from ..models.conditional_rule import ConditionalRule
    from ..models.simple_rule import SimpleRule
    from ..models.unit_rule import UnitRule


T = TypeVar("T", bound="AllRules")


@_attrs_define
class AllRules:
    """
    Attributes:
        simple_rules (Union[Unset, list['SimpleRule']]):
        unit_rules (Union[Unset, list['UnitRule']]):
        activation_rules (Union[Unset, list['ActivationRule']]):
        conditional_rules (Union[Unset, list['ConditionalRule']]):
        first (Union[Unset, BaseRule]):
        initialized (Union[Unset, bool]):
    """

    simple_rules: Union[Unset, list["SimpleRule"]] = UNSET
    unit_rules: Union[Unset, list["UnitRule"]] = UNSET
    activation_rules: Union[Unset, list["ActivationRule"]] = UNSET
    conditional_rules: Union[Unset, list["ConditionalRule"]] = UNSET
    first: Union[Unset, "BaseRule"] = UNSET
    initialized: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        simple_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.simple_rules, Unset):
            simple_rules = []
            for simple_rules_item_data in self.simple_rules:
                simple_rules_item = simple_rules_item_data.to_dict()
                simple_rules.append(simple_rules_item)

        unit_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.unit_rules, Unset):
            unit_rules = []
            for unit_rules_item_data in self.unit_rules:
                unit_rules_item = unit_rules_item_data.to_dict()
                unit_rules.append(unit_rules_item)

        activation_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.activation_rules, Unset):
            activation_rules = []
            for activation_rules_item_data in self.activation_rules:
                activation_rules_item = activation_rules_item_data.to_dict()
                activation_rules.append(activation_rules_item)

        conditional_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditional_rules, Unset):
            conditional_rules = []
            for conditional_rules_item_data in self.conditional_rules:
                conditional_rules_item = conditional_rules_item_data.to_dict()
                conditional_rules.append(conditional_rules_item)

        first: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.to_dict()

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if simple_rules is not UNSET:
            field_dict["simpleRules"] = simple_rules
        if unit_rules is not UNSET:
            field_dict["unitRules"] = unit_rules
        if activation_rules is not UNSET:
            field_dict["activationRules"] = activation_rules
        if conditional_rules is not UNSET:
            field_dict["conditionalRules"] = conditional_rules
        if first is not UNSET:
            field_dict["first"] = first
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activation_rule import ActivationRule
        from ..models.base_rule import BaseRule
        from ..models.conditional_rule import ConditionalRule
        from ..models.simple_rule import SimpleRule
        from ..models.unit_rule import UnitRule

        d = dict(src_dict)
        simple_rules = []
        _simple_rules = d.pop("simpleRules", UNSET)
        for simple_rules_item_data in _simple_rules or []:
            simple_rules_item = SimpleRule.from_dict(simple_rules_item_data)

            simple_rules.append(simple_rules_item)

        unit_rules = []
        _unit_rules = d.pop("unitRules", UNSET)
        for unit_rules_item_data in _unit_rules or []:
            unit_rules_item = UnitRule.from_dict(unit_rules_item_data)

            unit_rules.append(unit_rules_item)

        activation_rules = []
        _activation_rules = d.pop("activationRules", UNSET)
        for activation_rules_item_data in _activation_rules or []:
            activation_rules_item = ActivationRule.from_dict(activation_rules_item_data)

            activation_rules.append(activation_rules_item)

        conditional_rules = []
        _conditional_rules = d.pop("conditionalRules", UNSET)
        for conditional_rules_item_data in _conditional_rules or []:
            conditional_rules_item = ConditionalRule.from_dict(conditional_rules_item_data)

            conditional_rules.append(conditional_rules_item)

        _first = d.pop("first", UNSET)
        first: Union[Unset, BaseRule]
        if _first and not isinstance(_first, Unset):
            first = BaseRule.from_dict(_first)

        else:
            first = UNSET

        initialized = d.pop("initialized", UNSET)

        all_rules = cls(
            simple_rules=simple_rules,
            unit_rules=unit_rules,
            activation_rules=activation_rules,
            conditional_rules=conditional_rules,
            first=first,
            initialized=initialized,
        )

        all_rules.additional_properties = d
        return all_rules

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
