from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_plan import MerchantPlan


T = TypeVar("T", bound="PlanChange")


@_attrs_define
class PlanChange:
    """
    Attributes:
        changed_time (Union[Unset, int]):
        old_plan (Union[Unset, MerchantPlan]):
        new_plan (Union[Unset, MerchantPlan]):
    """

    changed_time: Union[Unset, int] = UNSET
    old_plan: Union[Unset, "MerchantPlan"] = UNSET
    new_plan: Union[Unset, "MerchantPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed_time = self.changed_time

        old_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.old_plan, Unset):
            old_plan = self.old_plan.to_dict()

        new_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.new_plan, Unset):
            new_plan = self.new_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed_time is not UNSET:
            field_dict["changedTime"] = changed_time
        if old_plan is not UNSET:
            field_dict["oldPlan"] = old_plan
        if new_plan is not UNSET:
            field_dict["newPlan"] = new_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merchant_plan import MerchantPlan

        d = dict(src_dict)
        changed_time = d.pop("changedTime", UNSET)

        _old_plan = d.pop("oldPlan", UNSET)
        old_plan: Union[Unset, MerchantPlan]
        if _old_plan and not isinstance(_old_plan, Unset):
            old_plan = MerchantPlan.from_dict(_old_plan)

        else:
            old_plan = UNSET

        _new_plan = d.pop("newPlan", UNSET)
        new_plan: Union[Unset, MerchantPlan]
        if _new_plan and not isinstance(_new_plan, Unset):
            new_plan = MerchantPlan.from_dict(_new_plan)

        else:
            new_plan = UNSET

        plan_change = cls(
            changed_time=changed_time,
            old_plan=old_plan,
            new_plan=new_plan,
        )

        plan_change.additional_properties = d
        return plan_change

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
