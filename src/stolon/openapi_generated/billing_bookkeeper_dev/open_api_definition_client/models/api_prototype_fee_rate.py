import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_prototype_fee_rate_apply_type import ApiPrototypeFeeRateApplyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPrototypeFeeRate")


@_attrs_define
class ApiPrototypeFeeRate:
    """
    Attributes:
        id (Union[Unset, int]): Id of the prototype fee rate
        uuid (Union[Unset, str]): 26-character UUID of the prototype fee rate
        prototype_fee_set_id (Union[Unset, int]): Id of the prototype fee set this prototype fee rate is in
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this rate belongs to
        fee_category (Union[Unset, str]): defined fee category value
        fee_code (Union[Unset, str]): defined fee code value
        currency (Union[Unset, str]): 3-letter currency code Example: USD.
        apply_type (Union[Unset, ApiPrototypeFeeRateApplyType]):
        per_item_amount (Union[Unset, float]): the per-item rate
        percentage (Union[Unset, float]): the percentage rate
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the prototype fee rate was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the prototype fee rate was last
            modified Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this prototype fee rate
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    prototype_fee_set_id: Union[Unset, int] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    apply_type: Union[Unset, ApiPrototypeFeeRateApplyType] = UNSET
    per_item_amount: Union[Unset, float] = UNSET
    percentage: Union[Unset, float] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        prototype_fee_set_id = self.prototype_fee_set_id

        billing_entity_uuid = self.billing_entity_uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        currency = self.currency

        apply_type: Union[Unset, str] = UNSET
        if not isinstance(self.apply_type, Unset):
            apply_type = self.apply_type.value

        per_item_amount = self.per_item_amount

        percentage = self.percentage

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
        if prototype_fee_set_id is not UNSET:
            field_dict["prototypeFeeSetId"] = prototype_fee_set_id
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if apply_type is not UNSET:
            field_dict["applyType"] = apply_type
        if per_item_amount is not UNSET:
            field_dict["perItemAmount"] = per_item_amount
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
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

        prototype_fee_set_id = d.pop("prototypeFeeSetId", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        currency = d.pop("currency", UNSET)

        _apply_type = d.pop("applyType", UNSET)
        apply_type: Union[Unset, ApiPrototypeFeeRateApplyType]
        if _apply_type and not isinstance(_apply_type, Unset):
            apply_type = ApiPrototypeFeeRateApplyType(_apply_type)

        else:
            apply_type = UNSET

        per_item_amount = d.pop("perItemAmount", UNSET)

        percentage = d.pop("percentage", UNSET)

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

        api_prototype_fee_rate = cls(
            id=id,
            uuid=uuid,
            prototype_fee_set_id=prototype_fee_set_id,
            billing_entity_uuid=billing_entity_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            apply_type=apply_type,
            per_item_amount=per_item_amount,
            percentage=percentage,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_prototype_fee_rate.additional_properties = d
        return api_prototype_fee_rate

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
