from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_fee_estimate_entity_type import ApiFeeEstimateEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_currency_amount import ApiCurrencyAmount
    from ..models.api_fee_summary_estimate import ApiFeeSummaryEstimate


T = TypeVar("T", bound="ApiFeeEstimate")


@_attrs_define
class ApiFeeEstimate:
    """
    Attributes:
        is_successful (Union[Unset, bool]): indicates whether fee estimate computation was successful or not
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this rate belongs to
        entity_uuid (Union[Unset, str]): 13-character UUID of the actual entity that this billing entity represents
        entity_type (Union[Unset, ApiFeeEstimateEntityType]):
        fee_totals (Union[Unset, list['ApiCurrencyAmount']]): estimated fee totals by currency
        fee_summaries (Union[Unset, list['ApiFeeSummaryEstimate']]): fee summaries for estimated fees
        messages (Union[Unset, list[str]]): error messages, if any
    """

    is_successful: Union[Unset, bool] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiFeeEstimateEntityType] = UNSET
    fee_totals: Union[Unset, list["ApiCurrencyAmount"]] = UNSET
    fee_summaries: Union[Unset, list["ApiFeeSummaryEstimate"]] = UNSET
    messages: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_successful = self.is_successful

        billing_entity_uuid = self.billing_entity_uuid

        entity_uuid = self.entity_uuid

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        fee_totals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_totals, Unset):
            fee_totals = []
            for fee_totals_item_data in self.fee_totals:
                fee_totals_item = fee_totals_item_data.to_dict()
                fee_totals.append(fee_totals_item)

        fee_summaries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_summaries, Unset):
            fee_summaries = []
            for fee_summaries_item_data in self.fee_summaries:
                fee_summaries_item = fee_summaries_item_data.to_dict()
                fee_summaries.append(fee_summaries_item)

        messages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_successful is not UNSET:
            field_dict["isSuccessful"] = is_successful
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if fee_totals is not UNSET:
            field_dict["feeTotals"] = fee_totals
        if fee_summaries is not UNSET:
            field_dict["feeSummaries"] = fee_summaries
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_currency_amount import ApiCurrencyAmount
        from ..models.api_fee_summary_estimate import ApiFeeSummaryEstimate

        d = dict(src_dict)
        is_successful = d.pop("isSuccessful", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, ApiFeeEstimateEntityType]
        if _entity_type and not isinstance(_entity_type, Unset):
            entity_type = ApiFeeEstimateEntityType(_entity_type)

        else:
            entity_type = UNSET

        fee_totals = []
        _fee_totals = d.pop("feeTotals", UNSET)
        for fee_totals_item_data in _fee_totals or []:
            fee_totals_item = ApiCurrencyAmount.from_dict(fee_totals_item_data)

            fee_totals.append(fee_totals_item)

        fee_summaries = []
        _fee_summaries = d.pop("feeSummaries", UNSET)
        for fee_summaries_item_data in _fee_summaries or []:
            fee_summaries_item = ApiFeeSummaryEstimate.from_dict(fee_summaries_item_data)

            fee_summaries.append(fee_summaries_item)

        messages = cast(list[str], d.pop("messages", UNSET))

        api_fee_estimate = cls(
            is_successful=is_successful,
            billing_entity_uuid=billing_entity_uuid,
            entity_uuid=entity_uuid,
            entity_type=entity_type,
            fee_totals=fee_totals,
            fee_summaries=fee_summaries,
            messages=messages,
        )

        api_fee_estimate.additional_properties = d
        return api_fee_estimate

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
