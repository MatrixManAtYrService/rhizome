import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.monetary_adjustment_rule_type import MonetaryAdjustmentRuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonetaryAdjustment")


@_attrs_define
class MonetaryAdjustment:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        adjust_fee_summary_uuid (Union[Unset, str]):
        qualified_fee_summary_uuid (Union[Unset, str]):
        rule_uuid (Union[Unset, str]):
        rule_criteria_uuid (Union[Unset, str]):
        rule_type (Union[Unset, MonetaryAdjustmentRuleType]):
        request_uuid (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    adjust_fee_summary_uuid: Union[Unset, str] = UNSET
    qualified_fee_summary_uuid: Union[Unset, str] = UNSET
    rule_uuid: Union[Unset, str] = UNSET
    rule_criteria_uuid: Union[Unset, str] = UNSET
    rule_type: Union[Unset, MonetaryAdjustmentRuleType] = UNSET
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
        rule_type: Union[Unset, MonetaryAdjustmentRuleType]
        if isinstance(_rule_type, Unset):
            rule_type = UNSET
        else:
            rule_type = MonetaryAdjustmentRuleType(_rule_type)

        request_uuid = d.pop("requestUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        monetary_adjustment = cls(
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

        monetary_adjustment.additional_properties = d
        return monetary_adjustment

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
