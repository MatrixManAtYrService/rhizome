import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_fee_rate_error_report_apply_type import ApiFeeRateErrorReportApplyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeRateErrorReport")


@_attrs_define
class ApiFeeRateErrorReport:
    """
    Attributes:
        id (Union[Unset, int]): Id of the fee rate error report
        uuid (Union[Unset, str]): 26-character UUID of the fee rate error report
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the fee rate in error
            belongs to
        fee_category (Union[Unset, str]): fee category for the fee rate in error
        fee_code (Union[Unset, str]): fee code for the fee rate in error
        currency (Union[Unset, str]): 3-letter currency code for the fee rate in error Example: USD.
        resolved_status (Union[Unset, bool]): indicates whether fee rate error report has been resolved
        apply_type (Union[Unset, ApiFeeRateErrorReportApplyType]):
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the fee rate error report was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the fee rate error report was last
            modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    resolved_status: Union[Unset, bool] = UNSET
    apply_type: Union[Unset, ApiFeeRateErrorReportApplyType] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        currency = self.currency

        resolved_status = self.resolved_status

        apply_type: Union[Unset, str] = UNSET
        if not isinstance(self.apply_type, Unset):
            apply_type = self.apply_type.value

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
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if resolved_status is not UNSET:
            field_dict["resolvedStatus"] = resolved_status
        if apply_type is not UNSET:
            field_dict["applyType"] = apply_type
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

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        currency = d.pop("currency", UNSET)

        resolved_status = d.pop("resolvedStatus", UNSET)

        _apply_type = d.pop("applyType", UNSET)
        apply_type: Union[Unset, ApiFeeRateErrorReportApplyType]
        if _apply_type and not isinstance(_apply_type, Unset):
            apply_type = ApiFeeRateErrorReportApplyType(_apply_type)

        else:
            apply_type = UNSET

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

        api_fee_rate_error_report = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            resolved_status=resolved_status,
            apply_type=apply_type,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_fee_rate_error_report.additional_properties = d
        return api_fee_rate_error_report

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
