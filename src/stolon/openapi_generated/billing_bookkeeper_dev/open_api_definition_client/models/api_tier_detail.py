import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTierDetail")


@_attrs_define
class ApiTierDetail:
    """
    Attributes:
        id (Union[Unset, int]): ID of the tier detail definition
        uuid (Union[Unset, str]): 26-character UUID of the tier detail definition
        tiered_rule_uuid (Union[Unset, str]): 26-character UUID of the tiered rule that this tier detail definition
            belongs to
        min_units (Union[Unset, float]): the minimum number of units needed to qualify for this tier; applied for
            QUANTITY and BOTH tiered basis
        min_amount (Union[Unset, float]): the minimum total fee amount needed to qualify for this tier; applied for
            VOLUME and BOTH tiered basis
        currency (Union[Unset, str]): 3-letter currency code Example: USD.
        rate_fee_category (Union[Unset, str]): the fee category of the fee rate to use for adjustments created for this
            pricing tier
        rate_fee_code (Union[Unset, str]): the fee code of the fee rate to use for adjustments created for this pricing
            tier
        short_desc (Union[Unset, str]): short description of this tier detail definition
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the tier detail was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the tier detail was last modified
            Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this tier detail
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    tiered_rule_uuid: Union[Unset, str] = UNSET
    min_units: Union[Unset, float] = UNSET
    min_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    rate_fee_category: Union[Unset, str] = UNSET
    rate_fee_code: Union[Unset, str] = UNSET
    short_desc: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        tiered_rule_uuid = self.tiered_rule_uuid

        min_units = self.min_units

        min_amount = self.min_amount

        currency = self.currency

        rate_fee_category = self.rate_fee_category

        rate_fee_code = self.rate_fee_code

        short_desc = self.short_desc

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if tiered_rule_uuid is not UNSET:
            field_dict["tieredRuleUuid"] = tiered_rule_uuid
        if min_units is not UNSET:
            field_dict["minUnits"] = min_units
        if min_amount is not UNSET:
            field_dict["minAmount"] = min_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if rate_fee_category is not UNSET:
            field_dict["rateFeeCategory"] = rate_fee_category
        if rate_fee_code is not UNSET:
            field_dict["rateFeeCode"] = rate_fee_code
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        tiered_rule_uuid = d.pop("tieredRuleUuid", UNSET)

        min_units = d.pop("minUnits", UNSET)

        min_amount = d.pop("minAmount", UNSET)

        currency = d.pop("currency", UNSET)

        rate_fee_category = d.pop("rateFeeCategory", UNSET)

        rate_fee_code = d.pop("rateFeeCode", UNSET)

        short_desc = d.pop("shortDesc", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if _modified_timestamp and not isinstance(_modified_timestamp, Unset):
            modified_timestamp = isoparse(_modified_timestamp)

        else:
            modified_timestamp = UNSET

        audit_id = d.pop("auditId", UNSET)

        api_tier_detail = cls(
            id=id,
            uuid=uuid,
            tiered_rule_uuid=tiered_rule_uuid,
            min_units=min_units,
            min_amount=min_amount,
            currency=currency,
            rate_fee_category=rate_fee_category,
            rate_fee_code=rate_fee_code,
            short_desc=short_desc,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_tier_detail.additional_properties = d
        return api_tier_detail

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
