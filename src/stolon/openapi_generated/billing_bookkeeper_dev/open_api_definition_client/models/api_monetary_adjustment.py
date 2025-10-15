import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_monetary_adjustment_rule_type import ApiMonetaryAdjustmentRuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMonetaryAdjustment")


@_attrs_define
class ApiMonetaryAdjustment:
    """
    Attributes:
        id (Union[Unset, int]): ID of the monetary adjustment
        uuid (Union[Unset, str]): 26-character UUID of the monetary adjustment
        billing_entity_uuid (Union[Unset, str]): UUID of the billing entity that this monetary adjustment is for
        adjust_fee_summary_uuid (Union[Unset, str]): 26-character UUID of the monetary adjustment fee summary
        qualified_fee_summary_uuid (Union[Unset, str]): 26-character UUID of the fee summary that qualified for the
            monetary adjustment
        rule_uuid (Union[Unset, str]): 26-character UUID of the rule applied to create the monetary adjustment
        rule_criteria_uuid (Union[Unset, str]): 26-character UUID of the rule criteria that was applied to create the
            monetary adjustment
        rule_type (Union[Unset, ApiMonetaryAdjustmentRuleType]):
        request_uuid (Union[Unset, str]): 26-character UUID for the execution request that created the monetary
            adjustment
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the auto-adjust rule was created
            Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    adjust_fee_summary_uuid: Union[Unset, str] = UNSET
    qualified_fee_summary_uuid: Union[Unset, str] = UNSET
    rule_uuid: Union[Unset, str] = UNSET
    rule_criteria_uuid: Union[Unset, str] = UNSET
    rule_type: Union[Unset, ApiMonetaryAdjustmentRuleType] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        adjust_fee_summary_uuid = self.adjust_fee_summary_uuid

        qualified_fee_summary_uuid = self.qualified_fee_summary_uuid

        rule_uuid = self.rule_uuid

        rule_criteria_uuid = self.rule_criteria_uuid

        rule_type: Union[Unset, str] = UNSET
        if not isinstance(self.rule_type, Unset):
            rule_type = self.rule_type.value

        request_uuid = self.request_uuid

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if adjust_fee_summary_uuid is not UNSET:
            field_dict["adjustFeeSummaryUuid"] = adjust_fee_summary_uuid
        if qualified_fee_summary_uuid is not UNSET:
            field_dict["qualifiedFeeSummaryUuid"] = qualified_fee_summary_uuid
        if rule_uuid is not UNSET:
            field_dict["ruleUuid"] = rule_uuid
        if rule_criteria_uuid is not UNSET:
            field_dict["ruleCriteriaUuid"] = rule_criteria_uuid
        if rule_type is not UNSET:
            field_dict["ruleType"] = rule_type
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        adjust_fee_summary_uuid = d.pop("adjustFeeSummaryUuid", UNSET)

        qualified_fee_summary_uuid = d.pop("qualifiedFeeSummaryUuid", UNSET)

        rule_uuid = d.pop("ruleUuid", UNSET)

        rule_criteria_uuid = d.pop("ruleCriteriaUuid", UNSET)

        _rule_type = d.pop("ruleType", UNSET)
        rule_type: Union[Unset, ApiMonetaryAdjustmentRuleType]
        if _rule_type and not isinstance(_rule_type, Unset):
            rule_type = ApiMonetaryAdjustmentRuleType(_rule_type)

        else:
            rule_type = UNSET

        request_uuid = d.pop("requestUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_monetary_adjustment = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            adjust_fee_summary_uuid=adjust_fee_summary_uuid,
            qualified_fee_summary_uuid=qualified_fee_summary_uuid,
            rule_uuid=rule_uuid,
            rule_criteria_uuid=rule_criteria_uuid,
            rule_type=rule_type,
            request_uuid=request_uuid,
            created_timestamp=created_timestamp,
        )

        api_monetary_adjustment.additional_properties = d
        return api_monetary_adjustment

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
