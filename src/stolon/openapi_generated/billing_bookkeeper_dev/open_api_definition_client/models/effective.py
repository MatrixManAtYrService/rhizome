from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_hierarchy import BillingHierarchy
    from ..models.billing_hierarchy_cycle import BillingHierarchyCycle
    from ..models.billing_schedule import BillingSchedule
    from ..models.processing_group_dates import ProcessingGroupDates


T = TypeVar("T", bound="Effective")


@_attrs_define
class Effective:
    """
    Attributes:
        effective_billing_schedule (Union[Unset, BillingSchedule]):
        effective_billing_hierarchies (Union[Unset, list['BillingHierarchy']]):
        effective_billing_hierarchy_cycle (Union[Unset, BillingHierarchyCycle]):
        processing_group_dates (Union[Unset, ProcessingGroupDates]):
    """

    effective_billing_schedule: Union[Unset, "BillingSchedule"] = UNSET
    effective_billing_hierarchies: Union[Unset, list["BillingHierarchy"]] = UNSET
    effective_billing_hierarchy_cycle: Union[Unset, "BillingHierarchyCycle"] = UNSET
    processing_group_dates: Union[Unset, "ProcessingGroupDates"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_billing_schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.effective_billing_schedule, Unset):
            effective_billing_schedule = self.effective_billing_schedule.to_dict()

        effective_billing_hierarchies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.effective_billing_hierarchies, Unset):
            effective_billing_hierarchies = []
            for effective_billing_hierarchies_item_data in self.effective_billing_hierarchies:
                effective_billing_hierarchies_item = effective_billing_hierarchies_item_data.to_dict()
                effective_billing_hierarchies.append(effective_billing_hierarchies_item)

        effective_billing_hierarchy_cycle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.effective_billing_hierarchy_cycle, Unset):
            effective_billing_hierarchy_cycle = self.effective_billing_hierarchy_cycle.to_dict()

        processing_group_dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.processing_group_dates, Unset):
            processing_group_dates = self.processing_group_dates.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if effective_billing_schedule is not UNSET:
            field_dict["effectiveBillingSchedule"] = effective_billing_schedule
        if effective_billing_hierarchies is not UNSET:
            field_dict["effectiveBillingHierarchies"] = effective_billing_hierarchies
        if effective_billing_hierarchy_cycle is not UNSET:
            field_dict["effectiveBillingHierarchyCycle"] = effective_billing_hierarchy_cycle
        if processing_group_dates is not UNSET:
            field_dict["processingGroupDates"] = processing_group_dates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_hierarchy import BillingHierarchy
        from ..models.billing_hierarchy_cycle import BillingHierarchyCycle
        from ..models.billing_schedule import BillingSchedule
        from ..models.processing_group_dates import ProcessingGroupDates

        d = dict(src_dict)
        _effective_billing_schedule = d.pop("effectiveBillingSchedule", UNSET)
        effective_billing_schedule: Union[Unset, BillingSchedule]
        if _effective_billing_schedule and not isinstance(_effective_billing_schedule, Unset):
            effective_billing_schedule = BillingSchedule.from_dict(_effective_billing_schedule)

        else:
            effective_billing_schedule = UNSET

        effective_billing_hierarchies = []
        _effective_billing_hierarchies = d.pop("effectiveBillingHierarchies", UNSET)
        for effective_billing_hierarchies_item_data in _effective_billing_hierarchies or []:
            effective_billing_hierarchies_item = BillingHierarchy.from_dict(effective_billing_hierarchies_item_data)

            effective_billing_hierarchies.append(effective_billing_hierarchies_item)

        _effective_billing_hierarchy_cycle = d.pop("effectiveBillingHierarchyCycle", UNSET)
        effective_billing_hierarchy_cycle: Union[Unset, BillingHierarchyCycle]
        if _effective_billing_hierarchy_cycle and not isinstance(_effective_billing_hierarchy_cycle, Unset):
            effective_billing_hierarchy_cycle = BillingHierarchyCycle.from_dict(_effective_billing_hierarchy_cycle)

        else:
            effective_billing_hierarchy_cycle = UNSET

        _processing_group_dates = d.pop("processingGroupDates", UNSET)
        processing_group_dates: Union[Unset, ProcessingGroupDates]
        if _processing_group_dates and not isinstance(_processing_group_dates, Unset):
            processing_group_dates = ProcessingGroupDates.from_dict(_processing_group_dates)

        else:
            processing_group_dates = UNSET

        effective = cls(
            effective_billing_schedule=effective_billing_schedule,
            effective_billing_hierarchies=effective_billing_hierarchies,
            effective_billing_hierarchy_cycle=effective_billing_hierarchy_cycle,
            processing_group_dates=processing_group_dates,
        )

        effective.additional_properties = d
        return effective

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
