import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProcessingNote")


@_attrs_define
class ApiProcessingNote:
    """
    Attributes:
        id (Union[Unset, int]): Id of the processing note
        uuid (Union[Unset, str]): 26-character UUID of the processing note
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this processing note belongs to
        process_date (Union[Unset, datetime.date]): date used by the process that created the note; may correlate to
            cycle date, billing date, settlement date, etc.
        note_code (Union[Unset, str]): the code that identifies the type of processing note
        notes (Union[Unset, str]): the free-form processing notes or details
        request_uuid (Union[Unset, str]): 26-character UUID for the execution request that created the processing note
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the processing note was created Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    process_date: Union[Unset, datetime.date] = UNSET
    note_code: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        process_date: Union[Unset, str] = UNSET
        if not isinstance(self.process_date, Unset):
            process_date = self.process_date.isoformat()

        note_code = self.note_code

        notes = self.notes

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
        if process_date is not UNSET:
            field_dict["processDate"] = process_date
        if note_code is not UNSET:
            field_dict["noteCode"] = note_code
        if notes is not UNSET:
            field_dict["notes"] = notes
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

        _process_date = d.pop("processDate", UNSET)
        process_date: Union[Unset, datetime.date]
        if isinstance(_process_date, Unset):
            process_date = UNSET
        else:
            process_date = isoparse(_process_date).date()

        note_code = d.pop("noteCode", UNSET)

        notes = d.pop("notes", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_processing_note = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            process_date=process_date,
            note_code=note_code,
            notes=notes,
            request_uuid=request_uuid,
            created_timestamp=created_timestamp,
        )

        api_processing_note.additional_properties = d
        return api_processing_note

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
