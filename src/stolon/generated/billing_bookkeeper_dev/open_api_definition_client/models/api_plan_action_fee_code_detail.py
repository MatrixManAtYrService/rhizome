from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_plan_action_fee_description import ApiPlanActionFeeDescription
    from ..models.api_plan_action_fee_rate_summary import ApiPlanActionFeeRateSummary


T = TypeVar("T", bound="ApiPlanActionFeeCodeDetail")


@_attrs_define
class ApiPlanActionFeeCodeDetail:
    """
    Attributes:
        name (Union[Unset, str]): Name of the merchant plan.
        uuid (Union[Unset, str]): 13-character UUID of the merchant plan
        plan_action_fee_rate_summary_list (Union[Unset, list['ApiPlanActionFeeRateSummary']]): Summary list
        plan_action_fee_description_list (Union[Unset, list['ApiPlanActionFeeDescription']]): Description list
    """

    name: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    plan_action_fee_rate_summary_list: Union[Unset, list["ApiPlanActionFeeRateSummary"]] = UNSET
    plan_action_fee_description_list: Union[Unset, list["ApiPlanActionFeeDescription"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uuid = self.uuid

        plan_action_fee_rate_summary_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_action_fee_rate_summary_list, Unset):
            plan_action_fee_rate_summary_list = []
            for plan_action_fee_rate_summary_list_item_data in self.plan_action_fee_rate_summary_list:
                plan_action_fee_rate_summary_list_item = plan_action_fee_rate_summary_list_item_data.to_dict()
                plan_action_fee_rate_summary_list.append(plan_action_fee_rate_summary_list_item)

        plan_action_fee_description_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_action_fee_description_list, Unset):
            plan_action_fee_description_list = []
            for plan_action_fee_description_list_item_data in self.plan_action_fee_description_list:
                plan_action_fee_description_list_item = plan_action_fee_description_list_item_data.to_dict()
                plan_action_fee_description_list.append(plan_action_fee_description_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if plan_action_fee_rate_summary_list is not UNSET:
            field_dict["planActionFeeRateSummaryList"] = plan_action_fee_rate_summary_list
        if plan_action_fee_description_list is not UNSET:
            field_dict["planActionFeeDescriptionList"] = plan_action_fee_description_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_plan_action_fee_description import ApiPlanActionFeeDescription
        from ..models.api_plan_action_fee_rate_summary import ApiPlanActionFeeRateSummary

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        uuid = d.pop("uuid", UNSET)

        plan_action_fee_rate_summary_list = []
        _plan_action_fee_rate_summary_list = d.pop("planActionFeeRateSummaryList", UNSET)
        for plan_action_fee_rate_summary_list_item_data in _plan_action_fee_rate_summary_list or []:
            plan_action_fee_rate_summary_list_item = ApiPlanActionFeeRateSummary.from_dict(
                plan_action_fee_rate_summary_list_item_data
            )

            plan_action_fee_rate_summary_list.append(plan_action_fee_rate_summary_list_item)

        plan_action_fee_description_list = []
        _plan_action_fee_description_list = d.pop("planActionFeeDescriptionList", UNSET)
        for plan_action_fee_description_list_item_data in _plan_action_fee_description_list or []:
            plan_action_fee_description_list_item = ApiPlanActionFeeDescription.from_dict(
                plan_action_fee_description_list_item_data
            )

            plan_action_fee_description_list.append(plan_action_fee_description_list_item)

        api_plan_action_fee_code_detail = cls(
            name=name,
            uuid=uuid,
            plan_action_fee_rate_summary_list=plan_action_fee_rate_summary_list,
            plan_action_fee_description_list=plan_action_fee_description_list,
        )

        api_plan_action_fee_code_detail.additional_properties = d
        return api_plan_action_fee_code_detail

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
