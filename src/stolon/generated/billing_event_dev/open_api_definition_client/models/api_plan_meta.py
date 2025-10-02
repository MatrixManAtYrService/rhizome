from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_plan_meta_plan_type import ApiPlanMetaPlanType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPlanMeta")


@_attrs_define
class ApiPlanMeta:
    """
    Attributes:
        bundle_model (Union[Unset, str]):
        excluded_devices (Union[Unset, list[str]]):
        excluded_include_first_devices (Union[Unset, list[str]]):
        excluded_plan_trial_devices (Union[Unset, list[str]]):
        supported_bundle_indicators (Union[Unset, list[str]]):
        country (Union[Unset, str]):
        plan_type (Union[Unset, ApiPlanMetaPlanType]):
        plan_uuid (Union[Unset, str]):
    """

    bundle_model: Union[Unset, str] = UNSET
    excluded_devices: Union[Unset, list[str]] = UNSET
    excluded_include_first_devices: Union[Unset, list[str]] = UNSET
    excluded_plan_trial_devices: Union[Unset, list[str]] = UNSET
    supported_bundle_indicators: Union[Unset, list[str]] = UNSET
    country: Union[Unset, str] = UNSET
    plan_type: Union[Unset, ApiPlanMetaPlanType] = UNSET
    plan_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundle_model = self.bundle_model

        excluded_devices: Union[Unset, list[str]] = UNSET
        if not isinstance(self.excluded_devices, Unset):
            excluded_devices = self.excluded_devices

        excluded_include_first_devices: Union[Unset, list[str]] = UNSET
        if not isinstance(self.excluded_include_first_devices, Unset):
            excluded_include_first_devices = self.excluded_include_first_devices

        excluded_plan_trial_devices: Union[Unset, list[str]] = UNSET
        if not isinstance(self.excluded_plan_trial_devices, Unset):
            excluded_plan_trial_devices = self.excluded_plan_trial_devices

        supported_bundle_indicators: Union[Unset, list[str]] = UNSET
        if not isinstance(self.supported_bundle_indicators, Unset):
            supported_bundle_indicators = self.supported_bundle_indicators

        country = self.country

        plan_type: Union[Unset, str] = UNSET
        if not isinstance(self.plan_type, Unset):
            plan_type = self.plan_type.value

        plan_uuid = self.plan_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bundle_model is not UNSET:
            field_dict["bundleModel"] = bundle_model
        if excluded_devices is not UNSET:
            field_dict["excludedDevices"] = excluded_devices
        if excluded_include_first_devices is not UNSET:
            field_dict["excludedIncludeFirstDevices"] = excluded_include_first_devices
        if excluded_plan_trial_devices is not UNSET:
            field_dict["excludedPlanTrialDevices"] = excluded_plan_trial_devices
        if supported_bundle_indicators is not UNSET:
            field_dict["supportedBundleIndicators"] = supported_bundle_indicators
        if country is not UNSET:
            field_dict["country"] = country
        if plan_type is not UNSET:
            field_dict["planType"] = plan_type
        if plan_uuid is not UNSET:
            field_dict["planUuid"] = plan_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bundle_model = d.pop("bundleModel", UNSET)

        excluded_devices = cast(list[str], d.pop("excludedDevices", UNSET))

        excluded_include_first_devices = cast(list[str], d.pop("excludedIncludeFirstDevices", UNSET))

        excluded_plan_trial_devices = cast(list[str], d.pop("excludedPlanTrialDevices", UNSET))

        supported_bundle_indicators = cast(list[str], d.pop("supportedBundleIndicators", UNSET))

        country = d.pop("country", UNSET)

        _plan_type = d.pop("planType", UNSET)
        plan_type: Union[Unset, ApiPlanMetaPlanType]
        if isinstance(_plan_type, Unset):
            plan_type = UNSET
        else:
            plan_type = ApiPlanMetaPlanType(_plan_type)

        plan_uuid = d.pop("planUuid", UNSET)

        api_plan_meta = cls(
            bundle_model=bundle_model,
            excluded_devices=excluded_devices,
            excluded_include_first_devices=excluded_include_first_devices,
            excluded_plan_trial_devices=excluded_plan_trial_devices,
            supported_bundle_indicators=supported_bundle_indicators,
            country=country,
            plan_type=plan_type,
            plan_uuid=plan_uuid,
        )

        api_plan_meta.additional_properties = d
        return api_plan_meta

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
