import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RevenueActionError")


@_attrs_define
class RevenueActionError:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        request_uuid (Union[Unset, str]):
        posting_date (Union[Unset, datetime.date]):
        original_request_uuid (Union[Unset, str]):
        original_posting_date (Union[Unset, datetime.date]):
        posting_attempts (Union[Unset, int]):
        error_code (Union[Unset, str]):
        error_details (Union[Unset, str]):
        resolved (Union[Unset, int]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
        billing_entity_uuid (Union[Unset, str]):
        revenue_action_uuid (Union[Unset, str]):
        action_uuid (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    original_request_uuid: Union[Unset, str] = UNSET
    original_posting_date: Union[Unset, datetime.date] = UNSET
    posting_attempts: Union[Unset, int] = UNSET
    error_code: Union[Unset, str] = UNSET
    error_details: Union[Unset, str] = UNSET
    resolved: Union[Unset, int] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    revenue_action_uuid: Union[Unset, str] = UNSET
    action_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        request_uuid = self.request_uuid

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        original_request_uuid = self.original_request_uuid

        original_posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.original_posting_date, Unset):
            original_posting_date = self.original_posting_date.isoformat()

        posting_attempts = self.posting_attempts

        error_code = self.error_code

        error_details = self.error_details

        resolved = self.resolved

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        billing_entity_uuid = self.billing_entity_uuid

        revenue_action_uuid = self.revenue_action_uuid

        action_uuid = self.action_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date
        if original_request_uuid is not UNSET:
            field_dict["originalRequestUuid"] = original_request_uuid
        if original_posting_date is not UNSET:
            field_dict["originalPostingDate"] = original_posting_date
        if posting_attempts is not UNSET:
            field_dict["postingAttempts"] = posting_attempts
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_details is not UNSET:
            field_dict["errorDetails"] = error_details
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if revenue_action_uuid is not UNSET:
            field_dict["revenueActionUuid"] = revenue_action_uuid
        if action_uuid is not UNSET:
            field_dict["actionUuid"] = action_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if _posting_date and not isinstance(_posting_date, Unset):
            posting_date = isoparse(_posting_date).date()

        else:
            posting_date = UNSET

        original_request_uuid = d.pop("originalRequestUuid", UNSET)

        _original_posting_date = d.pop("originalPostingDate", UNSET)
        original_posting_date: Union[Unset, datetime.date]
        if _original_posting_date and not isinstance(_original_posting_date, Unset):
            original_posting_date = isoparse(_original_posting_date).date()

        else:
            original_posting_date = UNSET

        posting_attempts = d.pop("postingAttempts", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_details = d.pop("errorDetails", UNSET)

        resolved = d.pop("resolved", UNSET)

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

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        revenue_action_uuid = d.pop("revenueActionUuid", UNSET)

        action_uuid = d.pop("actionUuid", UNSET)

        revenue_action_error = cls(
            id=id,
            uuid=uuid,
            request_uuid=request_uuid,
            posting_date=posting_date,
            original_request_uuid=original_request_uuid,
            original_posting_date=original_posting_date,
            posting_attempts=posting_attempts,
            error_code=error_code,
            error_details=error_details,
            resolved=resolved,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            billing_entity_uuid=billing_entity_uuid,
            revenue_action_uuid=revenue_action_uuid,
            action_uuid=action_uuid,
        )

        revenue_action_error.additional_properties = d
        return revenue_action_error

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
