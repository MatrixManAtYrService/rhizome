import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_bulk_auto_adjust_advice_file_status import ApiBulkAutoAdjustAdviceFileStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBulkAutoAdjustAdvice")


@_attrs_define
class ApiBulkAutoAdjustAdvice:
    """
    Attributes:
        id (Union[Unset, int]): ID of the staging file instance containing this bulk auto-adjust advice
        uuid (Union[Unset, str]): 26-character UUID of the staging file instance
        file_def_uuid (Union[Unset, str]): Refers to the file definition for this file instance
        file_name (Union[Unset, str]): Name of the file, as processed
        process_name (Union[Unset, str]): Name of the bean, typically the class simple name, that processed the file
        request_uuid (Union[Unset, str]): Used to trace the request that called the JOB
        md_5_checksum (Union[Unset, str]): The MD5 checksum of the file contents
        file_size (Union[Unset, int]): Size of the original file in bytes; the original file typically is the file
            downloaded from the file gateway. Default is 0
        file_status (Union[Unset, ApiBulkAutoAdjustAdviceFileStatus]):
        num_records (Union[Unset, int]): Number of records in the original file, including the header and footer records
            if present
        num_attempt (Union[Unset, int]): Number of records that the job execution attempted to process
        num_success (Union[Unset, int]): Number of records that were successfully processed during the job execution.
            nullable
        num_errors (Union[Unset, int]): Number of records that failed with an error during the job execution. nullable
        num_warning (Union[Unset, int]): Number of records that contained warnings during the job execution. nullable
        num_skipped (Union[Unset, int]): Number of records that were skipped during the job execution. nullable
        reason_detail (Union[Unset, str]): Detailed description of the ERROR file status
        created_time (Union[Unset, datetime.datetime]): Date and time the row was first inserted. Default is current
            timestamp Example: 2020-12-31T23:59:59.123456Z.
        modified_time (Union[Unset, datetime.datetime]): Date and time of last update to the row Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    file_def_uuid: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    process_name: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    md_5_checksum: Union[Unset, str] = UNSET
    file_size: Union[Unset, int] = UNSET
    file_status: Union[Unset, ApiBulkAutoAdjustAdviceFileStatus] = UNSET
    num_records: Union[Unset, int] = UNSET
    num_attempt: Union[Unset, int] = UNSET
    num_success: Union[Unset, int] = UNSET
    num_errors: Union[Unset, int] = UNSET
    num_warning: Union[Unset, int] = UNSET
    num_skipped: Union[Unset, int] = UNSET
    reason_detail: Union[Unset, str] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    modified_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        file_def_uuid = self.file_def_uuid

        file_name = self.file_name

        process_name = self.process_name

        request_uuid = self.request_uuid

        md_5_checksum = self.md_5_checksum

        file_size = self.file_size

        file_status: Union[Unset, str] = UNSET
        if not isinstance(self.file_status, Unset):
            file_status = self.file_status.value

        num_records = self.num_records

        num_attempt = self.num_attempt

        num_success = self.num_success

        num_errors = self.num_errors

        num_warning = self.num_warning

        num_skipped = self.num_skipped

        reason_detail = self.reason_detail

        created_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        modified_time: Union[Unset, str] = UNSET
        if not isinstance(self.modified_time, Unset):
            modified_time = self.modified_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if file_def_uuid is not UNSET:
            field_dict["fileDefUuid"] = file_def_uuid
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if process_name is not UNSET:
            field_dict["processName"] = process_name
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if md_5_checksum is not UNSET:
            field_dict["md5Checksum"] = md_5_checksum
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if file_status is not UNSET:
            field_dict["fileStatus"] = file_status
        if num_records is not UNSET:
            field_dict["numRecords"] = num_records
        if num_attempt is not UNSET:
            field_dict["numAttempt"] = num_attempt
        if num_success is not UNSET:
            field_dict["numSuccess"] = num_success
        if num_errors is not UNSET:
            field_dict["numErrors"] = num_errors
        if num_warning is not UNSET:
            field_dict["numWarning"] = num_warning
        if num_skipped is not UNSET:
            field_dict["numSkipped"] = num_skipped
        if reason_detail is not UNSET:
            field_dict["reasonDetail"] = reason_detail
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        file_def_uuid = d.pop("fileDefUuid", UNSET)

        file_name = d.pop("fileName", UNSET)

        process_name = d.pop("processName", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        md_5_checksum = d.pop("md5Checksum", UNSET)

        file_size = d.pop("fileSize", UNSET)

        _file_status = d.pop("fileStatus", UNSET)
        file_status: Union[Unset, ApiBulkAutoAdjustAdviceFileStatus]
        if _file_status and not isinstance(_file_status, Unset):
            file_status = ApiBulkAutoAdjustAdviceFileStatus(_file_status)

        else:
            file_status = UNSET

        num_records = d.pop("numRecords", UNSET)

        num_attempt = d.pop("numAttempt", UNSET)

        num_success = d.pop("numSuccess", UNSET)

        num_errors = d.pop("numErrors", UNSET)

        num_warning = d.pop("numWarning", UNSET)

        num_skipped = d.pop("numSkipped", UNSET)

        reason_detail = d.pop("reasonDetail", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if _created_time and not isinstance(_created_time, Unset):
            created_time = isoparse(_created_time)

        else:
            created_time = UNSET

        _modified_time = d.pop("modifiedTime", UNSET)
        modified_time: Union[Unset, datetime.datetime]
        if _modified_time and not isinstance(_modified_time, Unset):
            modified_time = isoparse(_modified_time)

        else:
            modified_time = UNSET

        api_bulk_auto_adjust_advice = cls(
            id=id,
            uuid=uuid,
            file_def_uuid=file_def_uuid,
            file_name=file_name,
            process_name=process_name,
            request_uuid=request_uuid,
            md_5_checksum=md_5_checksum,
            file_size=file_size,
            file_status=file_status,
            num_records=num_records,
            num_attempt=num_attempt,
            num_success=num_success,
            num_errors=num_errors,
            num_warning=num_warning,
            num_skipped=num_skipped,
            reason_detail=reason_detail,
            created_time=created_time,
            modified_time=modified_time,
        )

        api_bulk_auto_adjust_advice.additional_properties = d
        return api_bulk_auto_adjust_advice

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
