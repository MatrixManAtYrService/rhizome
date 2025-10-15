import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_fee_ctd_extended_apply_type import ApiFeeCtdExtendedApplyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeCtdExtended")


@_attrs_define
class ApiFeeCtdExtended:
    """
    Attributes:
        id (Union[Unset, int]): Id of the current-to-date fee
        uuid (Union[Unset, str]): 26-character UUID of the current-to-date fee
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this current-to-date fee
            belongs to
        fee_category_group (Union[Unset, str]): defined fee category grouping
        fee_category (Union[Unset, str]): the fee category of the current-to-date fee
        fee_code (Union[Unset, str]): the fee code of the current-to-date fee
        short_desc (Union[Unset, str]): short description of fee code
        full_desc (Union[Unset, str]): long description for fee code
        currency (Union[Unset, str]): the currency of the current-to-date fee Example: USD.
        ctd_num_units (Union[Unset, float]): the current-to-date net number of billable units
        abs_num_units (Union[Unset, float]): the current-to-date total of the absolute value of number of billable units
        ctd_basis_amount (Union[Unset, float]): the current-to-date net basis amount
        abs_basis_amount (Union[Unset, float]): the current-to-date total of the absolute values of basis amounts
        num_actions (Union[Unset, int]): the current-to-date number of actions accumulated
        estimated_fee_amount (Union[Unset, float]): the total estimated fee amount
        fee_rate_uuid (Union[Unset, str]): 26-character UUID of the fee rate used to calculate the fee summary
        apply_type (Union[Unset, ApiFeeCtdExtendedApplyType]):
        per_item_amount (Union[Unset, float]): the per-item rate
        percentage (Union[Unset, float]): the percentage rate
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the current-to-date fee was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the current-to-date fee was last
            modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    short_desc: Union[Unset, str] = UNSET
    full_desc: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    ctd_num_units: Union[Unset, float] = UNSET
    abs_num_units: Union[Unset, float] = UNSET
    ctd_basis_amount: Union[Unset, float] = UNSET
    abs_basis_amount: Union[Unset, float] = UNSET
    num_actions: Union[Unset, int] = UNSET
    estimated_fee_amount: Union[Unset, float] = UNSET
    fee_rate_uuid: Union[Unset, str] = UNSET
    apply_type: Union[Unset, ApiFeeCtdExtendedApplyType] = UNSET
    per_item_amount: Union[Unset, float] = UNSET
    percentage: Union[Unset, float] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        fee_category_group = self.fee_category_group

        fee_category = self.fee_category

        fee_code = self.fee_code

        short_desc = self.short_desc

        full_desc = self.full_desc

        currency = self.currency

        ctd_num_units = self.ctd_num_units

        abs_num_units = self.abs_num_units

        ctd_basis_amount = self.ctd_basis_amount

        abs_basis_amount = self.abs_basis_amount

        num_actions = self.num_actions

        estimated_fee_amount = self.estimated_fee_amount

        fee_rate_uuid = self.fee_rate_uuid

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if full_desc is not UNSET:
            field_dict["fullDesc"] = full_desc
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ctd_num_units is not UNSET:
            field_dict["ctdNumUnits"] = ctd_num_units
        if abs_num_units is not UNSET:
            field_dict["absNumUnits"] = abs_num_units
        if ctd_basis_amount is not UNSET:
            field_dict["ctdBasisAmount"] = ctd_basis_amount
        if abs_basis_amount is not UNSET:
            field_dict["absBasisAmount"] = abs_basis_amount
        if num_actions is not UNSET:
            field_dict["numActions"] = num_actions
        if estimated_fee_amount is not UNSET:
            field_dict["estimatedFeeAmount"] = estimated_fee_amount
        if fee_rate_uuid is not UNSET:
            field_dict["feeRateUuid"] = fee_rate_uuid
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        short_desc = d.pop("shortDesc", UNSET)

        full_desc = d.pop("fullDesc", UNSET)

        currency = d.pop("currency", UNSET)

        ctd_num_units = d.pop("ctdNumUnits", UNSET)

        abs_num_units = d.pop("absNumUnits", UNSET)

        ctd_basis_amount = d.pop("ctdBasisAmount", UNSET)

        abs_basis_amount = d.pop("absBasisAmount", UNSET)

        num_actions = d.pop("numActions", UNSET)

        estimated_fee_amount = d.pop("estimatedFeeAmount", UNSET)

        fee_rate_uuid = d.pop("feeRateUuid", UNSET)

        _apply_type = d.pop("applyType", UNSET)
        apply_type: Union[Unset, ApiFeeCtdExtendedApplyType]
        if _apply_type and not isinstance(_apply_type, Unset):
            apply_type = ApiFeeCtdExtendedApplyType(_apply_type)

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

        api_fee_ctd_extended = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            fee_category_group=fee_category_group,
            fee_category=fee_category,
            fee_code=fee_code,
            short_desc=short_desc,
            full_desc=full_desc,
            currency=currency,
            ctd_num_units=ctd_num_units,
            abs_num_units=abs_num_units,
            ctd_basis_amount=ctd_basis_amount,
            abs_basis_amount=abs_basis_amount,
            num_actions=num_actions,
            estimated_fee_amount=estimated_fee_amount,
            fee_rate_uuid=fee_rate_uuid,
            apply_type=apply_type,
            per_item_amount=per_item_amount,
            percentage=percentage,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_fee_ctd_extended.additional_properties = d
        return api_fee_ctd_extended

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
