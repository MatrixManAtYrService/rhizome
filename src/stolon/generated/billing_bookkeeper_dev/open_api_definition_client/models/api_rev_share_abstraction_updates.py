from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_billing_entity import ApiBillingEntity
    from ..models.api_billing_hierarchy import ApiBillingHierarchy
    from ..models.api_billing_pseudo_entity import ApiBillingPseudoEntity
    from ..models.api_fee_code import ApiFeeCode
    from ..models.api_fee_rate import ApiFeeRate
    from ..models.api_revenue_action_fee_code import ApiRevenueActionFeeCode


T = TypeVar("T", bound="ApiRevShareAbstractionUpdates")


@_attrs_define
class ApiRevShareAbstractionUpdates:
    """
    Attributes:
        fee_codes (Union[Unset, list['ApiFeeCode']]): All fee code records that will be added
        revenue_action_fee_codes (Union[Unset, list['ApiRevenueActionFeeCode']]): All revenue action fee code records
            that will be added
        billing_pseudo_entities (Union[Unset, list['ApiBillingPseudoEntity']]): All billing pseudo entity records that
            will be added
        billing_entities (Union[Unset, list['ApiBillingEntity']]): All billing entity records that will be added
        billing_hierarchies (Union[Unset, list['ApiBillingHierarchy']]): All billing hierarchy records that will be
            added
        fee_rates (Union[Unset, list['ApiFeeRate']]): All fee rate records that will be added
    """

    fee_codes: Union[Unset, list["ApiFeeCode"]] = UNSET
    revenue_action_fee_codes: Union[Unset, list["ApiRevenueActionFeeCode"]] = UNSET
    billing_pseudo_entities: Union[Unset, list["ApiBillingPseudoEntity"]] = UNSET
    billing_entities: Union[Unset, list["ApiBillingEntity"]] = UNSET
    billing_hierarchies: Union[Unset, list["ApiBillingHierarchy"]] = UNSET
    fee_rates: Union[Unset, list["ApiFeeRate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_codes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_codes, Unset):
            fee_codes = []
            for fee_codes_item_data in self.fee_codes:
                fee_codes_item = fee_codes_item_data.to_dict()
                fee_codes.append(fee_codes_item)

        revenue_action_fee_codes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revenue_action_fee_codes, Unset):
            revenue_action_fee_codes = []
            for revenue_action_fee_codes_item_data in self.revenue_action_fee_codes:
                revenue_action_fee_codes_item = revenue_action_fee_codes_item_data.to_dict()
                revenue_action_fee_codes.append(revenue_action_fee_codes_item)

        billing_pseudo_entities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_pseudo_entities, Unset):
            billing_pseudo_entities = []
            for billing_pseudo_entities_item_data in self.billing_pseudo_entities:
                billing_pseudo_entities_item = billing_pseudo_entities_item_data.to_dict()
                billing_pseudo_entities.append(billing_pseudo_entities_item)

        billing_entities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_entities, Unset):
            billing_entities = []
            for billing_entities_item_data in self.billing_entities:
                billing_entities_item = billing_entities_item_data.to_dict()
                billing_entities.append(billing_entities_item)

        billing_hierarchies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_hierarchies, Unset):
            billing_hierarchies = []
            for billing_hierarchies_item_data in self.billing_hierarchies:
                billing_hierarchies_item = billing_hierarchies_item_data.to_dict()
                billing_hierarchies.append(billing_hierarchies_item)

        fee_rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_rates, Unset):
            fee_rates = []
            for fee_rates_item_data in self.fee_rates:
                fee_rates_item = fee_rates_item_data.to_dict()
                fee_rates.append(fee_rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_codes is not UNSET:
            field_dict["feeCodes"] = fee_codes
        if revenue_action_fee_codes is not UNSET:
            field_dict["revenueActionFeeCodes"] = revenue_action_fee_codes
        if billing_pseudo_entities is not UNSET:
            field_dict["billingPseudoEntities"] = billing_pseudo_entities
        if billing_entities is not UNSET:
            field_dict["billingEntities"] = billing_entities
        if billing_hierarchies is not UNSET:
            field_dict["billingHierarchies"] = billing_hierarchies
        if fee_rates is not UNSET:
            field_dict["feeRates"] = fee_rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_billing_entity import ApiBillingEntity
        from ..models.api_billing_hierarchy import ApiBillingHierarchy
        from ..models.api_billing_pseudo_entity import ApiBillingPseudoEntity
        from ..models.api_fee_code import ApiFeeCode
        from ..models.api_fee_rate import ApiFeeRate
        from ..models.api_revenue_action_fee_code import ApiRevenueActionFeeCode

        d = dict(src_dict)
        fee_codes = []
        _fee_codes = d.pop("feeCodes", UNSET)
        for fee_codes_item_data in _fee_codes or []:
            fee_codes_item = ApiFeeCode.from_dict(fee_codes_item_data)

            fee_codes.append(fee_codes_item)

        revenue_action_fee_codes = []
        _revenue_action_fee_codes = d.pop("revenueActionFeeCodes", UNSET)
        for revenue_action_fee_codes_item_data in _revenue_action_fee_codes or []:
            revenue_action_fee_codes_item = ApiRevenueActionFeeCode.from_dict(revenue_action_fee_codes_item_data)

            revenue_action_fee_codes.append(revenue_action_fee_codes_item)

        billing_pseudo_entities = []
        _billing_pseudo_entities = d.pop("billingPseudoEntities", UNSET)
        for billing_pseudo_entities_item_data in _billing_pseudo_entities or []:
            billing_pseudo_entities_item = ApiBillingPseudoEntity.from_dict(billing_pseudo_entities_item_data)

            billing_pseudo_entities.append(billing_pseudo_entities_item)

        billing_entities = []
        _billing_entities = d.pop("billingEntities", UNSET)
        for billing_entities_item_data in _billing_entities or []:
            billing_entities_item = ApiBillingEntity.from_dict(billing_entities_item_data)

            billing_entities.append(billing_entities_item)

        billing_hierarchies = []
        _billing_hierarchies = d.pop("billingHierarchies", UNSET)
        for billing_hierarchies_item_data in _billing_hierarchies or []:
            billing_hierarchies_item = ApiBillingHierarchy.from_dict(billing_hierarchies_item_data)

            billing_hierarchies.append(billing_hierarchies_item)

        fee_rates = []
        _fee_rates = d.pop("feeRates", UNSET)
        for fee_rates_item_data in _fee_rates or []:
            fee_rates_item = ApiFeeRate.from_dict(fee_rates_item_data)

            fee_rates.append(fee_rates_item)

        api_rev_share_abstraction_updates = cls(
            fee_codes=fee_codes,
            revenue_action_fee_codes=revenue_action_fee_codes,
            billing_pseudo_entities=billing_pseudo_entities,
            billing_entities=billing_entities,
            billing_hierarchies=billing_hierarchies,
            fee_rates=fee_rates,
        )

        api_rev_share_abstraction_updates.additional_properties = d
        return api_rev_share_abstraction_updates

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
