import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_fee_rate_report_action_error_action_type import ApiFeeRateReportActionErrorActionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeRateReportActionError")


@_attrs_define
class ApiFeeRateReportActionError:
    """
    Attributes:
        id (Union[Unset, int]): Id of the fee rate report action error
        uuid (Union[Unset, str]): 26-character UUID of the fee rate report action error
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the action with a fee rate
            error belongs to
        fee_rate_error_report_uuid (Union[Unset, str]): 26-character UUID of the fee rate error report this fee rate
            report action error is associated with
        action_error_uuid (Union[Unset, str]): 26-character UUID of the fee-specific action error
        action_type (Union[Unset, ApiFeeRateReportActionErrorActionType]):
        action_uuid (Union[Unset, str]): 26-character UUID of the specific action that failed to post
        posting_attempts (Union[Unset, int]): number of attempts to post the action
        posting_date (Union[Unset, datetime.date]): date of the most recent attempt to post the action
        original_posting_date (Union[Unset, datetime.date]): date of the first attempt to post the action
        error_details (Union[Unset, str]): posting error message and details
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the fee rate report action error was
            created Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    fee_rate_error_report_uuid: Union[Unset, str] = UNSET
    action_error_uuid: Union[Unset, str] = UNSET
    action_type: Union[Unset, ApiFeeRateReportActionErrorActionType] = UNSET
    action_uuid: Union[Unset, str] = UNSET
    posting_attempts: Union[Unset, int] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    original_posting_date: Union[Unset, datetime.date] = UNSET
    error_details: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        fee_rate_error_report_uuid = self.fee_rate_error_report_uuid

        action_error_uuid = self.action_error_uuid

        action_type: Union[Unset, str] = UNSET
        if not isinstance(self.action_type, Unset):
            action_type = self.action_type.value

        action_uuid = self.action_uuid

        posting_attempts = self.posting_attempts

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        original_posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.original_posting_date, Unset):
            original_posting_date = self.original_posting_date.isoformat()

        error_details = self.error_details

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
        if fee_rate_error_report_uuid is not UNSET:
            field_dict["feeRateErrorReportUuid"] = fee_rate_error_report_uuid
        if action_error_uuid is not UNSET:
            field_dict["actionErrorUuid"] = action_error_uuid
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if action_uuid is not UNSET:
            field_dict["actionUuid"] = action_uuid
        if posting_attempts is not UNSET:
            field_dict["postingAttempts"] = posting_attempts
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date
        if original_posting_date is not UNSET:
            field_dict["originalPostingDate"] = original_posting_date
        if error_details is not UNSET:
            field_dict["errorDetails"] = error_details
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        fee_rate_error_report_uuid = d.pop("feeRateErrorReportUuid", UNSET)

        action_error_uuid = d.pop("actionErrorUuid", UNSET)

        _action_type = d.pop("actionType", UNSET)
        action_type: Union[Unset, ApiFeeRateReportActionErrorActionType]
        if isinstance(_action_type, Unset):
            action_type = UNSET
        else:
            action_type = ApiFeeRateReportActionErrorActionType(_action_type)

        action_uuid = d.pop("actionUuid", UNSET)

        posting_attempts = d.pop("postingAttempts", UNSET)

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if isinstance(_posting_date, Unset):
            posting_date = UNSET
        else:
            posting_date = isoparse(_posting_date).date()

        _original_posting_date = d.pop("originalPostingDate", UNSET)
        original_posting_date: Union[Unset, datetime.date]
        if isinstance(_original_posting_date, Unset):
            original_posting_date = UNSET
        else:
            original_posting_date = isoparse(_original_posting_date).date()

        error_details = d.pop("errorDetails", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_fee_rate_report_action_error = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            fee_rate_error_report_uuid=fee_rate_error_report_uuid,
            action_error_uuid=action_error_uuid,
            action_type=action_type,
            action_uuid=action_uuid,
            posting_attempts=posting_attempts,
            posting_date=posting_date,
            original_posting_date=original_posting_date,
            error_details=error_details,
            created_timestamp=created_timestamp,
        )

        api_fee_rate_report_action_error.additional_properties = d
        return api_fee_rate_report_action_error

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
