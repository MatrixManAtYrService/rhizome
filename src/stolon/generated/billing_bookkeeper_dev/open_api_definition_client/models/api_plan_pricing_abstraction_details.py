from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_billing_entity import ApiBillingEntity
    from ..models.api_billing_hierarchy import ApiBillingHierarchy
    from ..models.api_fee_rate import ApiFeeRate
    from ..models.api_plan_action_fee_code import ApiPlanActionFeeCode


T = TypeVar("T", bound="ApiPlanPricingAbstractionDetails")


@_attrs_define
class ApiPlanPricingAbstractionDetails:
    """
    Attributes:
        plan_action_fee_codes (Union[Unset, list['ApiPlanActionFeeCode']]): All plan action fee code records used by
            this plan pricing abstraction
        owning_billing_entity (Union[Unset, ApiBillingEntity]):
        owning_billing_hierarchy (Union[Unset, ApiBillingHierarchy]):
        fee_rates (Union[Unset, list['ApiFeeRate']]): All fee rates for the owningBillingEntity that are used to build
            this abstraction
        validation_errors (Union[Unset, list[str]]): Validation errors.  Errors must be corrected manually in the
            database before the abstraction can be updated.
        validation_warnings (Union[Unset, list[str]]): Validation warnings.  Warnings should automatically be corrected
            when the abstraction is next updated.
    """

    plan_action_fee_codes: Union[Unset, list["ApiPlanActionFeeCode"]] = UNSET
    owning_billing_entity: Union[Unset, "ApiBillingEntity"] = UNSET
    owning_billing_hierarchy: Union[Unset, "ApiBillingHierarchy"] = UNSET
    fee_rates: Union[Unset, list["ApiFeeRate"]] = UNSET
    validation_errors: Union[Unset, list[str]] = UNSET
    validation_warnings: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_action_fee_codes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_action_fee_codes, Unset):
            plan_action_fee_codes = []
            for plan_action_fee_codes_item_data in self.plan_action_fee_codes:
                plan_action_fee_codes_item = plan_action_fee_codes_item_data.to_dict()
                plan_action_fee_codes.append(plan_action_fee_codes_item)

        owning_billing_entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.owning_billing_entity, Unset):
            owning_billing_entity = self.owning_billing_entity.to_dict()

        owning_billing_hierarchy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.owning_billing_hierarchy, Unset):
            owning_billing_hierarchy = self.owning_billing_hierarchy.to_dict()

        fee_rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_rates, Unset):
            fee_rates = []
            for fee_rates_item_data in self.fee_rates:
                fee_rates_item = fee_rates_item_data.to_dict()
                fee_rates.append(fee_rates_item)

        validation_errors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.validation_errors, Unset):
            validation_errors = self.validation_errors

        validation_warnings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.validation_warnings, Unset):
            validation_warnings = self.validation_warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_action_fee_codes is not UNSET:
            field_dict["planActionFeeCodes"] = plan_action_fee_codes
        if owning_billing_entity is not UNSET:
            field_dict["owningBillingEntity"] = owning_billing_entity
        if owning_billing_hierarchy is not UNSET:
            field_dict["owningBillingHierarchy"] = owning_billing_hierarchy
        if fee_rates is not UNSET:
            field_dict["feeRates"] = fee_rates
        if validation_errors is not UNSET:
            field_dict["validationErrors"] = validation_errors
        if validation_warnings is not UNSET:
            field_dict["validationWarnings"] = validation_warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_billing_entity import ApiBillingEntity
        from ..models.api_billing_hierarchy import ApiBillingHierarchy
        from ..models.api_fee_rate import ApiFeeRate
        from ..models.api_plan_action_fee_code import ApiPlanActionFeeCode

        d = dict(src_dict)
        plan_action_fee_codes = []
        _plan_action_fee_codes = d.pop("planActionFeeCodes", UNSET)
        for plan_action_fee_codes_item_data in _plan_action_fee_codes or []:
            plan_action_fee_codes_item = ApiPlanActionFeeCode.from_dict(plan_action_fee_codes_item_data)

            plan_action_fee_codes.append(plan_action_fee_codes_item)

        _owning_billing_entity = d.pop("owningBillingEntity", UNSET)
        owning_billing_entity: Union[Unset, ApiBillingEntity]
        if isinstance(_owning_billing_entity, Unset):
            owning_billing_entity = UNSET
        else:
            owning_billing_entity = ApiBillingEntity.from_dict(_owning_billing_entity)

        _owning_billing_hierarchy = d.pop("owningBillingHierarchy", UNSET)
        owning_billing_hierarchy: Union[Unset, ApiBillingHierarchy]
        if isinstance(_owning_billing_hierarchy, Unset):
            owning_billing_hierarchy = UNSET
        else:
            owning_billing_hierarchy = ApiBillingHierarchy.from_dict(_owning_billing_hierarchy)

        fee_rates = []
        _fee_rates = d.pop("feeRates", UNSET)
        for fee_rates_item_data in _fee_rates or []:
            fee_rates_item = ApiFeeRate.from_dict(fee_rates_item_data)

            fee_rates.append(fee_rates_item)

        validation_errors = cast(list[str], d.pop("validationErrors", UNSET))

        validation_warnings = cast(list[str], d.pop("validationWarnings", UNSET))

        api_plan_pricing_abstraction_details = cls(
            plan_action_fee_codes=plan_action_fee_codes,
            owning_billing_entity=owning_billing_entity,
            owning_billing_hierarchy=owning_billing_hierarchy,
            fee_rates=fee_rates,
            validation_errors=validation_errors,
            validation_warnings=validation_warnings,
        )

        api_plan_pricing_abstraction_details.additional_properties = d
        return api_plan_pricing_abstraction_details

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
