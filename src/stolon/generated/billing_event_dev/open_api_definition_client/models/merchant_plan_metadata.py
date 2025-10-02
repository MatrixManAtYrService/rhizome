from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_plan import MerchantPlan
    from ..models.merchant_plans import MerchantPlans


T = TypeVar("T", bound="MerchantPlanMetadata")


@_attrs_define
class MerchantPlanMetadata:
    """
    Attributes:
        merchant_plans (Union[Unset, MerchantPlans]):
        current_merchant_plan (Union[Unset, MerchantPlan]):
    """

    merchant_plans: Union[Unset, "MerchantPlans"] = UNSET
    current_merchant_plan: Union[Unset, "MerchantPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant_plans: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_plans, Unset):
            merchant_plans = self.merchant_plans.to_dict()

        current_merchant_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.current_merchant_plan, Unset):
            current_merchant_plan = self.current_merchant_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant_plans is not UNSET:
            field_dict["merchantPlans"] = merchant_plans
        if current_merchant_plan is not UNSET:
            field_dict["currentMerchantPlan"] = current_merchant_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merchant_plan import MerchantPlan
        from ..models.merchant_plans import MerchantPlans

        d = dict(src_dict)
        _merchant_plans = d.pop("merchantPlans", UNSET)
        merchant_plans: Union[Unset, MerchantPlans]
        if isinstance(_merchant_plans, Unset):
            merchant_plans = UNSET
        else:
            merchant_plans = MerchantPlans.from_dict(_merchant_plans)

        _current_merchant_plan = d.pop("currentMerchantPlan", UNSET)
        current_merchant_plan: Union[Unset, MerchantPlan]
        if isinstance(_current_merchant_plan, Unset):
            current_merchant_plan = UNSET
        else:
            current_merchant_plan = MerchantPlan.from_dict(_current_merchant_plan)

        merchant_plan_metadata = cls(
            merchant_plans=merchant_plans,
            current_merchant_plan=current_merchant_plan,
        )

        merchant_plan_metadata.additional_properties = d
        return merchant_plan_metadata

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
