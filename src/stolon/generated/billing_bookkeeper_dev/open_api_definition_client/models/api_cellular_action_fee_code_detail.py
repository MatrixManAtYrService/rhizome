from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_cellular_action_fee_description import ApiCellularActionFeeDescription
    from ..models.api_cellular_action_fee_rate_summary import ApiCellularActionFeeRateSummary


T = TypeVar("T", bound="ApiCellularActionFeeCodeDetail")


@_attrs_define
class ApiCellularActionFeeCodeDetail:
    """
    Attributes:
        name (Union[Unset, str]): Name of the merchant cellular plan.
        uuid (Union[Unset, str]): 13-character UUID of the merchant cellular plan
        cellular_fee_rate_summary_list (Union[Unset, list['ApiCellularActionFeeRateSummary']]): Summary list
        cellular_fee_description_list (Union[Unset, list['ApiCellularActionFeeDescription']]): Description list
    """

    name: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    cellular_fee_rate_summary_list: Union[Unset, list["ApiCellularActionFeeRateSummary"]] = UNSET
    cellular_fee_description_list: Union[Unset, list["ApiCellularActionFeeDescription"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uuid = self.uuid

        cellular_fee_rate_summary_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cellular_fee_rate_summary_list, Unset):
            cellular_fee_rate_summary_list = []
            for cellular_fee_rate_summary_list_item_data in self.cellular_fee_rate_summary_list:
                cellular_fee_rate_summary_list_item = cellular_fee_rate_summary_list_item_data.to_dict()
                cellular_fee_rate_summary_list.append(cellular_fee_rate_summary_list_item)

        cellular_fee_description_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cellular_fee_description_list, Unset):
            cellular_fee_description_list = []
            for cellular_fee_description_list_item_data in self.cellular_fee_description_list:
                cellular_fee_description_list_item = cellular_fee_description_list_item_data.to_dict()
                cellular_fee_description_list.append(cellular_fee_description_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if cellular_fee_rate_summary_list is not UNSET:
            field_dict["cellularFeeRateSummaryList"] = cellular_fee_rate_summary_list
        if cellular_fee_description_list is not UNSET:
            field_dict["cellularFeeDescriptionList"] = cellular_fee_description_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_cellular_action_fee_description import ApiCellularActionFeeDescription
        from ..models.api_cellular_action_fee_rate_summary import ApiCellularActionFeeRateSummary

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        uuid = d.pop("uuid", UNSET)

        cellular_fee_rate_summary_list = []
        _cellular_fee_rate_summary_list = d.pop("cellularFeeRateSummaryList", UNSET)
        for cellular_fee_rate_summary_list_item_data in _cellular_fee_rate_summary_list or []:
            cellular_fee_rate_summary_list_item = ApiCellularActionFeeRateSummary.from_dict(
                cellular_fee_rate_summary_list_item_data
            )

            cellular_fee_rate_summary_list.append(cellular_fee_rate_summary_list_item)

        cellular_fee_description_list = []
        _cellular_fee_description_list = d.pop("cellularFeeDescriptionList", UNSET)
        for cellular_fee_description_list_item_data in _cellular_fee_description_list or []:
            cellular_fee_description_list_item = ApiCellularActionFeeDescription.from_dict(
                cellular_fee_description_list_item_data
            )

            cellular_fee_description_list.append(cellular_fee_description_list_item)

        api_cellular_action_fee_code_detail = cls(
            name=name,
            uuid=uuid,
            cellular_fee_rate_summary_list=cellular_fee_rate_summary_list,
            cellular_fee_description_list=cellular_fee_description_list,
        )

        api_cellular_action_fee_code_detail.additional_properties = d
        return api_cellular_action_fee_code_detail

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
