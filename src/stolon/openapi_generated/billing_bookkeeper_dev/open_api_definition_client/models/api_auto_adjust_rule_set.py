from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_auto_adjust_qualifier import ApiAutoAdjustQualifier
    from ..models.api_auto_adjust_rule import ApiAutoAdjustRule


T = TypeVar("T", bound="ApiAutoAdjustRuleSet")


@_attrs_define
class ApiAutoAdjustRuleSet:
    """
    Attributes:
        rule (Union[Unset, ApiAutoAdjustRule]):
        qualifiers (Union[Unset, list['ApiAutoAdjustQualifier']]): qualifiers for the auto-adjust rule
    """

    rule: Union[Unset, "ApiAutoAdjustRule"] = UNSET
    qualifiers: Union[Unset, list["ApiAutoAdjustQualifier"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        qualifiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.qualifiers, Unset):
            qualifiers = []
            for qualifiers_item_data in self.qualifiers:
                qualifiers_item = qualifiers_item_data.to_dict()
                qualifiers.append(qualifiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule is not UNSET:
            field_dict["rule"] = rule
        if qualifiers is not UNSET:
            field_dict["qualifiers"] = qualifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_auto_adjust_qualifier import ApiAutoAdjustQualifier
        from ..models.api_auto_adjust_rule import ApiAutoAdjustRule

        d = dict(src_dict)
        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, ApiAutoAdjustRule]
        if _rule and not isinstance(_rule, Unset):
            rule = ApiAutoAdjustRule.from_dict(_rule)

        else:
            rule = UNSET

        qualifiers = []
        _qualifiers = d.pop("qualifiers", UNSET)
        for qualifiers_item_data in _qualifiers or []:
            qualifiers_item = ApiAutoAdjustQualifier.from_dict(qualifiers_item_data)

            qualifiers.append(qualifiers_item)

        api_auto_adjust_rule_set = cls(
            rule=rule,
            qualifiers=qualifiers,
        )

        api_auto_adjust_rule_set.additional_properties = d
        return api_auto_adjust_rule_set

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
