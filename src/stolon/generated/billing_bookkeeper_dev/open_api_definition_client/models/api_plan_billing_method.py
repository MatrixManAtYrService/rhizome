from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPlanBillingMethod")


@_attrs_define
class ApiPlanBillingMethod:
    """
    Attributes:
        plan_billing_method (Union[Unset, str]): plan billing method value
        valid_hierarchy_types (Union[Unset, list[str]]): billing hierarchy types where the plan billing method is valid
    """

    plan_billing_method: Union[Unset, str] = UNSET
    valid_hierarchy_types: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_billing_method = self.plan_billing_method

        valid_hierarchy_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.valid_hierarchy_types, Unset):
            valid_hierarchy_types = self.valid_hierarchy_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_billing_method is not UNSET:
            field_dict["planBillingMethod"] = plan_billing_method
        if valid_hierarchy_types is not UNSET:
            field_dict["validHierarchyTypes"] = valid_hierarchy_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan_billing_method = d.pop("planBillingMethod", UNSET)

        valid_hierarchy_types = cast(list[str], d.pop("validHierarchyTypes", UNSET))

        api_plan_billing_method = cls(
            plan_billing_method=plan_billing_method,
            valid_hierarchy_types=valid_hierarchy_types,
        )

        api_plan_billing_method.additional_properties = d
        return api_plan_billing_method

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
