import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_plan_pricing_abstraction_plan_pricing_abstraction_type import (
    ApiPlanPricingAbstractionPlanPricingAbstractionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPlanPricingAbstraction")


@_attrs_define
class ApiPlanPricingAbstraction:
    """
    Attributes:
        as_of_date (Union[Unset, datetime.date]): date of the abstraction used to find records effective as of
        plan_pricing_abstraction_type (Union[Unset, ApiPlanPricingAbstractionPlanPricingAbstractionType]):
        currency (Union[Unset, str]): 3-letter currency code for fee rates Example: USD.
        custom_plan_uuid (Union[Unset, str]): When planPricingAbstractionType = CUSTOM, this is the uuid of the plan
            this pricing abstraction is for.  Otherwise, this should be null.
        plan_uuids (Union[Unset, list[str]]): A list of plan UUIDs (13 character plan UUIDs from COS) that this
            abstraction is associated with
        owning_billing_entity_uuid (Union[Unset, str]): The billing entity UUID of the reseller (or pseudo) where these
            rates are defined.  This is the highest level in the MERCHANT_FEE_RATE hierarchy where the rates are defined.
        owning_billing_entity_name (Union[Unset, str]): The name of the reseller (or pseudo) where these rates are
            defined.  This is read-only from the GET.  When saving, the owningBillingEntityUuid is used.
        owning_billing_entity_cos_uuid (Union[Unset, str]): The 13 character UUID of the reseller (or pseudo) from COS
            where these rates are defined.  This is read-only from the GET.  When saving, the owningBillingEntityUuid is
            used.
        plan_cost (Union[Unset, float]): The cost of the plan
        device_cost (Union[Unset, float]): The cost of each device
        kitchen_display_cost (Union[Unset, float]): The per device cost of Kitchen Display devices.  This is a device
            price shared by all plans across all abstractions.  When null, Kitchen Display pricing will fall under the
            standard deviceCost.
        kitchen_display_24_cost (Union[Unset, float]): The per device cost of Kitchen Display 24 devices.  This is a
            device price shared by all plans across all abstractions.  When null, Kitchen Display 24 pricing will fall under
            the standard deviceCost.
        kiosk_cost (Union[Unset, float]): The per device cost of Kiosk devices.  This is a device price shared by all
            plans across all abstractions.  When null, Kiosk pricing will fall under the standard deviceCost.
        supports_trial (Union[Unset, bool]): Indicates if fee codes and rates exist to support trials
        supports_include_first_device (Union[Unset, bool]): Indicates if fee codes and rates exist to support including
            the 1st device with the plan
        supports_non_billable_devices (Union[Unset, bool]): Indicates if fee codes and rates exist to support non-
            billable devices
        supports_bundled_devices (Union[Unset, bool]): Indicates if fee codes and rates exist to support bundled devices
        supports_bogo_devices (Union[Unset, bool]): Indicates if fee codes and rates exist to support bogo devices
        override_billing_entity_uuids (Union[Unset, list[str]]): A list of billing entity uuids which are children of
            the owningBillingEntity in the MERCHANT_FEE_RATE hierarchy and have custom pricing specified for these plans.
            This is read only from the GET.
        has_validation_errors (Union[Unset, bool]): This is read-only from the GET.  The abstraction is invalid because
            of validation errors.  Errors must be corrected manually in the database before the abstraction can be updated.
        has_validation_warnings (Union[Unset, bool]): This is read-only from the GET.  The abstraction is invalid
            because of validation warnings.  Warnings should automatically be corrected when the abstraction is next
            updated.
    """

    as_of_date: Union[Unset, datetime.date] = UNSET
    plan_pricing_abstraction_type: Union[Unset, ApiPlanPricingAbstractionPlanPricingAbstractionType] = UNSET
    currency: Union[Unset, str] = UNSET
    custom_plan_uuid: Union[Unset, str] = UNSET
    plan_uuids: Union[Unset, list[str]] = UNSET
    owning_billing_entity_uuid: Union[Unset, str] = UNSET
    owning_billing_entity_name: Union[Unset, str] = UNSET
    owning_billing_entity_cos_uuid: Union[Unset, str] = UNSET
    plan_cost: Union[Unset, float] = UNSET
    device_cost: Union[Unset, float] = UNSET
    kitchen_display_cost: Union[Unset, float] = UNSET
    kitchen_display_24_cost: Union[Unset, float] = UNSET
    kiosk_cost: Union[Unset, float] = UNSET
    supports_trial: Union[Unset, bool] = UNSET
    supports_include_first_device: Union[Unset, bool] = UNSET
    supports_non_billable_devices: Union[Unset, bool] = UNSET
    supports_bundled_devices: Union[Unset, bool] = UNSET
    supports_bogo_devices: Union[Unset, bool] = UNSET
    override_billing_entity_uuids: Union[Unset, list[str]] = UNSET
    has_validation_errors: Union[Unset, bool] = UNSET
    has_validation_warnings: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of_date: Union[Unset, str] = UNSET
        if not isinstance(self.as_of_date, Unset):
            as_of_date = self.as_of_date.isoformat()

        plan_pricing_abstraction_type: Union[Unset, str] = UNSET
        if not isinstance(self.plan_pricing_abstraction_type, Unset):
            plan_pricing_abstraction_type = self.plan_pricing_abstraction_type.value

        currency = self.currency

        custom_plan_uuid = self.custom_plan_uuid

        plan_uuids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.plan_uuids, Unset):
            plan_uuids = self.plan_uuids

        owning_billing_entity_uuid = self.owning_billing_entity_uuid

        owning_billing_entity_name = self.owning_billing_entity_name

        owning_billing_entity_cos_uuid = self.owning_billing_entity_cos_uuid

        plan_cost = self.plan_cost

        device_cost = self.device_cost

        kitchen_display_cost = self.kitchen_display_cost

        kitchen_display_24_cost = self.kitchen_display_24_cost

        kiosk_cost = self.kiosk_cost

        supports_trial = self.supports_trial

        supports_include_first_device = self.supports_include_first_device

        supports_non_billable_devices = self.supports_non_billable_devices

        supports_bundled_devices = self.supports_bundled_devices

        supports_bogo_devices = self.supports_bogo_devices

        override_billing_entity_uuids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.override_billing_entity_uuids, Unset):
            override_billing_entity_uuids = self.override_billing_entity_uuids

        has_validation_errors = self.has_validation_errors

        has_validation_warnings = self.has_validation_warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_of_date is not UNSET:
            field_dict["asOfDate"] = as_of_date
        if plan_pricing_abstraction_type is not UNSET:
            field_dict["planPricingAbstractionType"] = plan_pricing_abstraction_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if custom_plan_uuid is not UNSET:
            field_dict["customPlanUuid"] = custom_plan_uuid
        if plan_uuids is not UNSET:
            field_dict["planUuids"] = plan_uuids
        if owning_billing_entity_uuid is not UNSET:
            field_dict["owningBillingEntityUuid"] = owning_billing_entity_uuid
        if owning_billing_entity_name is not UNSET:
            field_dict["owningBillingEntityName"] = owning_billing_entity_name
        if owning_billing_entity_cos_uuid is not UNSET:
            field_dict["owningBillingEntityCosUuid"] = owning_billing_entity_cos_uuid
        if plan_cost is not UNSET:
            field_dict["planCost"] = plan_cost
        if device_cost is not UNSET:
            field_dict["deviceCost"] = device_cost
        if kitchen_display_cost is not UNSET:
            field_dict["kitchenDisplayCost"] = kitchen_display_cost
        if kitchen_display_24_cost is not UNSET:
            field_dict["kitchenDisplay24Cost"] = kitchen_display_24_cost
        if kiosk_cost is not UNSET:
            field_dict["kioskCost"] = kiosk_cost
        if supports_trial is not UNSET:
            field_dict["supportsTrial"] = supports_trial
        if supports_include_first_device is not UNSET:
            field_dict["supportsIncludeFirstDevice"] = supports_include_first_device
        if supports_non_billable_devices is not UNSET:
            field_dict["supportsNonBillableDevices"] = supports_non_billable_devices
        if supports_bundled_devices is not UNSET:
            field_dict["supportsBundledDevices"] = supports_bundled_devices
        if supports_bogo_devices is not UNSET:
            field_dict["supportsBogoDevices"] = supports_bogo_devices
        if override_billing_entity_uuids is not UNSET:
            field_dict["overrideBillingEntityUuids"] = override_billing_entity_uuids
        if has_validation_errors is not UNSET:
            field_dict["hasValidationErrors"] = has_validation_errors
        if has_validation_warnings is not UNSET:
            field_dict["hasValidationWarnings"] = has_validation_warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _as_of_date = d.pop("asOfDate", UNSET)
        as_of_date: Union[Unset, datetime.date]
        if _as_of_date and not isinstance(_as_of_date, Unset):
            as_of_date = isoparse(_as_of_date).date()

        else:
            as_of_date = UNSET

        _plan_pricing_abstraction_type = d.pop("planPricingAbstractionType", UNSET)
        plan_pricing_abstraction_type: Union[Unset, ApiPlanPricingAbstractionPlanPricingAbstractionType]
        if _plan_pricing_abstraction_type and not isinstance(_plan_pricing_abstraction_type, Unset):
            plan_pricing_abstraction_type = ApiPlanPricingAbstractionPlanPricingAbstractionType(
                _plan_pricing_abstraction_type
            )

        else:
            plan_pricing_abstraction_type = UNSET

        currency = d.pop("currency", UNSET)

        custom_plan_uuid = d.pop("customPlanUuid", UNSET)

        plan_uuids = cast(list[str], d.pop("planUuids", UNSET))

        owning_billing_entity_uuid = d.pop("owningBillingEntityUuid", UNSET)

        owning_billing_entity_name = d.pop("owningBillingEntityName", UNSET)

        owning_billing_entity_cos_uuid = d.pop("owningBillingEntityCosUuid", UNSET)

        plan_cost = d.pop("planCost", UNSET)

        device_cost = d.pop("deviceCost", UNSET)

        kitchen_display_cost = d.pop("kitchenDisplayCost", UNSET)

        kitchen_display_24_cost = d.pop("kitchenDisplay24Cost", UNSET)

        kiosk_cost = d.pop("kioskCost", UNSET)

        supports_trial = d.pop("supportsTrial", UNSET)

        supports_include_first_device = d.pop("supportsIncludeFirstDevice", UNSET)

        supports_non_billable_devices = d.pop("supportsNonBillableDevices", UNSET)

        supports_bundled_devices = d.pop("supportsBundledDevices", UNSET)

        supports_bogo_devices = d.pop("supportsBogoDevices", UNSET)

        override_billing_entity_uuids = cast(list[str], d.pop("overrideBillingEntityUuids", UNSET))

        has_validation_errors = d.pop("hasValidationErrors", UNSET)

        has_validation_warnings = d.pop("hasValidationWarnings", UNSET)

        api_plan_pricing_abstraction = cls(
            as_of_date=as_of_date,
            plan_pricing_abstraction_type=plan_pricing_abstraction_type,
            currency=currency,
            custom_plan_uuid=custom_plan_uuid,
            plan_uuids=plan_uuids,
            owning_billing_entity_uuid=owning_billing_entity_uuid,
            owning_billing_entity_name=owning_billing_entity_name,
            owning_billing_entity_cos_uuid=owning_billing_entity_cos_uuid,
            plan_cost=plan_cost,
            device_cost=device_cost,
            kitchen_display_cost=kitchen_display_cost,
            kitchen_display_24_cost=kitchen_display_24_cost,
            kiosk_cost=kiosk_cost,
            supports_trial=supports_trial,
            supports_include_first_device=supports_include_first_device,
            supports_non_billable_devices=supports_non_billable_devices,
            supports_bundled_devices=supports_bundled_devices,
            supports_bogo_devices=supports_bogo_devices,
            override_billing_entity_uuids=override_billing_entity_uuids,
            has_validation_errors=has_validation_errors,
            has_validation_warnings=has_validation_warnings,
        )

        api_plan_pricing_abstraction.additional_properties = d
        return api_plan_pricing_abstraction

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
