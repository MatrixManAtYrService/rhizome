from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_tier_pricing_tiered_basis import ApiTierPricingTieredBasis
from ..models.api_tier_pricing_tiered_model import ApiTierPricingTieredModel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_price_tier import ApiPriceTier


T = TypeVar("T", bound="ApiTierPricing")


@_attrs_define
class ApiTierPricing:
    """tiered pricing for the current carrier's SIMs

    Attributes:
        tiered_rule_uuid (Union[Unset, str]): 26-character UUID of the tiered rule applicable for the billing entity
        rule_alias (Union[Unset, str]): commonly known alias assigned to the tiered rule
        rule_short_desc (Union[Unset, str]): short description of the tiered rule
        tiered_basis (Union[Unset, ApiTierPricingTieredBasis]):
        tiered_model (Union[Unset, ApiTierPricingTieredModel]):
        tiers (Union[Unset, list['ApiPriceTier']]): details for devices for which this device pricing data applies
    """

    tiered_rule_uuid: Union[Unset, str] = UNSET
    rule_alias: Union[Unset, str] = UNSET
    rule_short_desc: Union[Unset, str] = UNSET
    tiered_basis: Union[Unset, ApiTierPricingTieredBasis] = UNSET
    tiered_model: Union[Unset, ApiTierPricingTieredModel] = UNSET
    tiers: Union[Unset, list["ApiPriceTier"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tiered_rule_uuid = self.tiered_rule_uuid

        rule_alias = self.rule_alias

        rule_short_desc = self.rule_short_desc

        tiered_basis: Union[Unset, str] = UNSET
        if not isinstance(self.tiered_basis, Unset):
            tiered_basis = self.tiered_basis.value

        tiered_model: Union[Unset, str] = UNSET
        if not isinstance(self.tiered_model, Unset):
            tiered_model = self.tiered_model.value

        tiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tiered_rule_uuid is not UNSET:
            field_dict["tieredRuleUuid"] = tiered_rule_uuid
        if rule_alias is not UNSET:
            field_dict["ruleAlias"] = rule_alias
        if rule_short_desc is not UNSET:
            field_dict["ruleShortDesc"] = rule_short_desc
        if tiered_basis is not UNSET:
            field_dict["tieredBasis"] = tiered_basis
        if tiered_model is not UNSET:
            field_dict["tieredModel"] = tiered_model
        if tiers is not UNSET:
            field_dict["tiers"] = tiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_price_tier import ApiPriceTier

        d = dict(src_dict)
        tiered_rule_uuid = d.pop("tieredRuleUuid", UNSET)

        rule_alias = d.pop("ruleAlias", UNSET)

        rule_short_desc = d.pop("ruleShortDesc", UNSET)

        _tiered_basis = d.pop("tieredBasis", UNSET)
        tiered_basis: Union[Unset, ApiTierPricingTieredBasis]
        if _tiered_basis and not isinstance(_tiered_basis, Unset):
            tiered_basis = ApiTierPricingTieredBasis(_tiered_basis)

        else:
            tiered_basis = UNSET

        _tiered_model = d.pop("tieredModel", UNSET)
        tiered_model: Union[Unset, ApiTierPricingTieredModel]
        if _tiered_model and not isinstance(_tiered_model, Unset):
            tiered_model = ApiTierPricingTieredModel(_tiered_model)

        else:
            tiered_model = UNSET

        tiers = []
        _tiers = d.pop("tiers", UNSET)
        for tiers_item_data in _tiers or []:
            tiers_item = ApiPriceTier.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        api_tier_pricing = cls(
            tiered_rule_uuid=tiered_rule_uuid,
            rule_alias=rule_alias,
            rule_short_desc=rule_short_desc,
            tiered_basis=tiered_basis,
            tiered_model=tiered_model,
            tiers=tiers,
        )

        api_tier_pricing.additional_properties = d
        return api_tier_pricing

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
