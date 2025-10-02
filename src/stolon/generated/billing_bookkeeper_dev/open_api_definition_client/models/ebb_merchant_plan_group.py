from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EbbMerchantPlanGroup")


@_attrs_define
class EbbMerchantPlanGroup:
    """
    Attributes:
        uuid (Union[Unset, str]):
        trial_days (Union[Unset, int]):
    """

    uuid: Union[Unset, str] = UNSET
    trial_days: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        trial_days = self.trial_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if trial_days is not UNSET:
            field_dict["trialDays"] = trial_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        trial_days = d.pop("trialDays", UNSET)

        ebb_merchant_plan_group = cls(
            uuid=uuid,
            trial_days=trial_days,
        )

        ebb_merchant_plan_group.additional_properties = d
        return ebb_merchant_plan_group

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
