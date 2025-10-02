from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_tier_detail import ApiTierDetail
    from ..models.api_tiered_qualifier import ApiTieredQualifier
    from ..models.api_tiered_rule import ApiTieredRule


T = TypeVar("T", bound="ApiTieredRuleSet")


@_attrs_define
class ApiTieredRuleSet:
    """
    Attributes:
        rule (Union[Unset, ApiTieredRule]):
        tiers (Union[Unset, list['ApiTierDetail']]): tier details for the tiered rule
        qualifiers (Union[Unset, list['ApiTieredQualifier']]): qualifiers for the tiered rule
    """

    rule: Union[Unset, "ApiTieredRule"] = UNSET
    tiers: Union[Unset, list["ApiTierDetail"]] = UNSET
    qualifiers: Union[Unset, list["ApiTieredQualifier"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        tiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

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
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if qualifiers is not UNSET:
            field_dict["qualifiers"] = qualifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_tier_detail import ApiTierDetail
        from ..models.api_tiered_qualifier import ApiTieredQualifier
        from ..models.api_tiered_rule import ApiTieredRule

        d = dict(src_dict)
        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, ApiTieredRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = ApiTieredRule.from_dict(_rule)

        tiers = []
        _tiers = d.pop("tiers", UNSET)
        for tiers_item_data in _tiers or []:
            tiers_item = ApiTierDetail.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        qualifiers = []
        _qualifiers = d.pop("qualifiers", UNSET)
        for qualifiers_item_data in _qualifiers or []:
            qualifiers_item = ApiTieredQualifier.from_dict(qualifiers_item_data)

            qualifiers.append(qualifiers_item)

        api_tiered_rule_set = cls(
            rule=rule,
            tiers=tiers,
            qualifiers=qualifiers,
        )

        api_tiered_rule_set.additional_properties = d
        return api_tiered_rule_set

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
