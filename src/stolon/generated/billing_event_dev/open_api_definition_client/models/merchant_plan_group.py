from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerchantPlanGroup")


@_attrs_define
class MerchantPlanGroup:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        enforce_assignment (Union[Unset, bool]):
        linkable (Union[Unset, bool]):
        trial_days (Union[Unset, int]):
        created_time (Union[Unset, int]):
        modified_time (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    enforce_assignment: Union[Unset, bool] = UNSET
    linkable: Union[Unset, bool] = UNSET
    trial_days: Union[Unset, int] = UNSET
    created_time: Union[Unset, int] = UNSET
    modified_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        enforce_assignment = self.enforce_assignment

        linkable = self.linkable

        trial_days = self.trial_days

        created_time = self.created_time

        modified_time = self.modified_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if enforce_assignment is not UNSET:
            field_dict["enforceAssignment"] = enforce_assignment
        if linkable is not UNSET:
            field_dict["linkable"] = linkable
        if trial_days is not UNSET:
            field_dict["trialDays"] = trial_days
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        enforce_assignment = d.pop("enforceAssignment", UNSET)

        linkable = d.pop("linkable", UNSET)

        trial_days = d.pop("trialDays", UNSET)

        created_time = d.pop("createdTime", UNSET)

        modified_time = d.pop("modifiedTime", UNSET)

        merchant_plan_group = cls(
            id=id,
            name=name,
            enforce_assignment=enforce_assignment,
            linkable=linkable,
            trial_days=trial_days,
            created_time=created_time,
            modified_time=modified_time,
        )

        merchant_plan_group.additional_properties = d
        return merchant_plan_group

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
