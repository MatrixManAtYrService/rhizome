from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiJobResponse")


@_attrs_define
class ApiJobResponse:
    """
    Attributes:
        job_id (Union[Unset, str]): 36-character UUID assigned to the job Example: 5d3e53ba-a161-4d7f-8a6a-cf62f65ec1d2.
        request_uuid (Union[Unset, str]): 26-character UUID assigned to the job execution request
        return_code (Union[Unset, int]): numeric return code from the job execution
        reason_code (Union[Unset, int]): optional numeric code that indicates the inderlying reason for an assigned
            return code
        message (Union[Unset, str]): message that describes the job execution return code
    """

    job_id: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    return_code: Union[Unset, int] = UNSET
    reason_code: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        request_uuid = self.request_uuid

        return_code = self.return_code

        reason_code = self.reason_code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if return_code is not UNSET:
            field_dict["returnCode"] = return_code
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        return_code = d.pop("returnCode", UNSET)

        reason_code = d.pop("reasonCode", UNSET)

        message = d.pop("message", UNSET)

        api_job_response = cls(
            job_id=job_id,
            request_uuid=request_uuid,
            return_code=return_code,
            reason_code=reason_code,
            message=message,
        )

        api_job_response.additional_properties = d
        return api_job_response

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
