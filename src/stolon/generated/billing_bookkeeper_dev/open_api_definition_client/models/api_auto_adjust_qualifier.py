import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutoAdjustQualifier")


@_attrs_define
class ApiAutoAdjustQualifier:
    """
    Attributes:
        id (Union[Unset, int]): ID of the auto-adjust rule qualifier
        uuid (Union[Unset, str]): 26-character UUID of the auto-adjust rule qualifier
        auto_adjust_rule_uuid (Union[Unset, str]): 26-character UUID of the auto-adjust rule that this qualifier applies
            to
        fee_category (Union[Unset, str]): the fee category that qualifies for the auto-adjust rule
        fee_code (Union[Unset, str]): the fee code that qualifies for the auto-adjust rule
        disqualify (Union[Unset, bool]): true indicates a fee category and fee code match disqualifies rather than
            qualifies
        negate_fee_summary (Union[Unset, bool]): indicates whether to negate the unit and amount totals from qualified
            fee summaries
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the auto-adjust rule qualifier was
            created Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this auto-adjust qualifier
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    auto_adjust_rule_uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    disqualify: Union[Unset, bool] = UNSET
    negate_fee_summary: Union[Unset, bool] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        auto_adjust_rule_uuid = self.auto_adjust_rule_uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        disqualify = self.disqualify

        negate_fee_summary = self.negate_fee_summary

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        audit_id = self.audit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if auto_adjust_rule_uuid is not UNSET:
            field_dict["autoAdjustRuleUuid"] = auto_adjust_rule_uuid
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if disqualify is not UNSET:
            field_dict["disqualify"] = disqualify
        if negate_fee_summary is not UNSET:
            field_dict["negateFeeSummary"] = negate_fee_summary
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        auto_adjust_rule_uuid = d.pop("autoAdjustRuleUuid", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        disqualify = d.pop("disqualify", UNSET)

        negate_fee_summary = d.pop("negateFeeSummary", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        audit_id = d.pop("auditId", UNSET)

        api_auto_adjust_qualifier = cls(
            id=id,
            uuid=uuid,
            auto_adjust_rule_uuid=auto_adjust_rule_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            disqualify=disqualify,
            negate_fee_summary=negate_fee_summary,
            created_timestamp=created_timestamp,
            audit_id=audit_id,
        )

        api_auto_adjust_qualifier.additional_properties = d
        return api_auto_adjust_qualifier

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
