from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_fee_summary_fee_category_report_entity_type import ApiFeeSummaryFeeCategoryReportEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_fee_summary_fee_category_for_billing_date import ApiFeeSummaryFeeCategoryForBillingDate


T = TypeVar("T", bound="ApiFeeSummaryFeeCategoryReport")


@_attrs_define
class ApiFeeSummaryFeeCategoryReport:
    """
    Attributes:
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity
        billing_entity_name (Union[Unset, str]): name of the billing entity
        entity_type (Union[Unset, ApiFeeSummaryFeeCategoryReportEntityType]):
        billing_date_fee_summaries (Union[Unset, list['ApiFeeSummaryFeeCategoryForBillingDate']]):
    """

    billing_entity_uuid: Union[Unset, str] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiFeeSummaryFeeCategoryReportEntityType] = UNSET
    billing_date_fee_summaries: Union[Unset, list["ApiFeeSummaryFeeCategoryForBillingDate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_entity_uuid = self.billing_entity_uuid

        billing_entity_name = self.billing_entity_name

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        billing_date_fee_summaries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_date_fee_summaries, Unset):
            billing_date_fee_summaries = []
            for billing_date_fee_summaries_item_data in self.billing_date_fee_summaries:
                billing_date_fee_summaries_item = billing_date_fee_summaries_item_data.to_dict()
                billing_date_fee_summaries.append(billing_date_fee_summaries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if billing_entity_name is not UNSET:
            field_dict["billingEntityName"] = billing_entity_name
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if billing_date_fee_summaries is not UNSET:
            field_dict["billingDateFeeSummaries"] = billing_date_fee_summaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_fee_summary_fee_category_for_billing_date import ApiFeeSummaryFeeCategoryForBillingDate

        d = dict(src_dict)
        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, ApiFeeSummaryFeeCategoryReportEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = ApiFeeSummaryFeeCategoryReportEntityType(_entity_type)

        billing_date_fee_summaries = []
        _billing_date_fee_summaries = d.pop("billingDateFeeSummaries", UNSET)
        for billing_date_fee_summaries_item_data in _billing_date_fee_summaries or []:
            billing_date_fee_summaries_item = ApiFeeSummaryFeeCategoryForBillingDate.from_dict(
                billing_date_fee_summaries_item_data
            )

            billing_date_fee_summaries.append(billing_date_fee_summaries_item)

        api_fee_summary_fee_category_report = cls(
            billing_entity_uuid=billing_entity_uuid,
            billing_entity_name=billing_entity_name,
            entity_type=entity_type,
            billing_date_fee_summaries=billing_date_fee_summaries,
        )

        api_fee_summary_fee_category_report.additional_properties = d
        return api_fee_summary_fee_category_report

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
