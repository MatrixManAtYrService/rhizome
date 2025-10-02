from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ebb_merchant_plan_group import EbbMerchantPlanGroup


T = TypeVar("T", bound="EbbMerchantPlan")


@_attrs_define
class EbbMerchantPlan:
    """
    Attributes:
        uuid (Union[Unset, str]):
        type_ (Union[Unset, str]):
        trial_days (Union[Unset, int]):
        trial_remaining_days (Union[Unset, int]):
        merchant_plan_group (Union[Unset, EbbMerchantPlanGroup]):
    """

    uuid: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    trial_days: Union[Unset, int] = UNSET
    trial_remaining_days: Union[Unset, int] = UNSET
    merchant_plan_group: Union[Unset, "EbbMerchantPlanGroup"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        type_ = self.type_

        trial_days = self.trial_days

        trial_remaining_days = self.trial_remaining_days

        merchant_plan_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_plan_group, Unset):
            merchant_plan_group = self.merchant_plan_group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if trial_days is not UNSET:
            field_dict["trialDays"] = trial_days
        if trial_remaining_days is not UNSET:
            field_dict["trialRemainingDays"] = trial_remaining_days
        if merchant_plan_group is not UNSET:
            field_dict["merchantPlanGroup"] = merchant_plan_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ebb_merchant_plan_group import EbbMerchantPlanGroup

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        type_ = d.pop("type", UNSET)

        trial_days = d.pop("trialDays", UNSET)

        trial_remaining_days = d.pop("trialRemainingDays", UNSET)

        _merchant_plan_group = d.pop("merchantPlanGroup", UNSET)
        merchant_plan_group: Union[Unset, EbbMerchantPlanGroup]
        if isinstance(_merchant_plan_group, Unset):
            merchant_plan_group = UNSET
        else:
            merchant_plan_group = EbbMerchantPlanGroup.from_dict(_merchant_plan_group)

        ebb_merchant_plan = cls(
            uuid=uuid,
            type_=type_,
            trial_days=trial_days,
            trial_remaining_days=trial_remaining_days,
            merchant_plan_group=merchant_plan_group,
        )

        ebb_merchant_plan.additional_properties = d
        return ebb_merchant_plan

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
