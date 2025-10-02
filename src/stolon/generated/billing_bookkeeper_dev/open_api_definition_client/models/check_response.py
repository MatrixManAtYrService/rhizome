from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check import Check


T = TypeVar("T", bound="CheckResponse")


@_attrs_define
class CheckResponse:
    """
    Attributes:
        check_name (Union[Unset, str]):
        audience (Union[Unset, str]):
        check_type (Union[Unset, str]):
        ready_for_flight (Union[Unset, bool]):
        message (Union[Unset, str]):
        checks (Union[Unset, list['Check']]):
        job_return_code (Union[Unset, int]):
        job_request_uuid (Union[Unset, str]):
        job_uuid (Union[Unset, UUID]):
    """

    check_name: Union[Unset, str] = UNSET
    audience: Union[Unset, str] = UNSET
    check_type: Union[Unset, str] = UNSET
    ready_for_flight: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    checks: Union[Unset, list["Check"]] = UNSET
    job_return_code: Union[Unset, int] = UNSET
    job_request_uuid: Union[Unset, str] = UNSET
    job_uuid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_name = self.check_name

        audience = self.audience

        check_type = self.check_type

        ready_for_flight = self.ready_for_flight

        message = self.message

        checks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.checks, Unset):
            checks = []
            for checks_item_data in self.checks:
                checks_item = checks_item_data.to_dict()
                checks.append(checks_item)

        job_return_code = self.job_return_code

        job_request_uuid = self.job_request_uuid

        job_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uuid, Unset):
            job_uuid = str(self.job_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_name is not UNSET:
            field_dict["checkName"] = check_name
        if audience is not UNSET:
            field_dict["audience"] = audience
        if check_type is not UNSET:
            field_dict["checkType"] = check_type
        if ready_for_flight is not UNSET:
            field_dict["readyForFlight"] = ready_for_flight
        if message is not UNSET:
            field_dict["message"] = message
        if checks is not UNSET:
            field_dict["checks"] = checks
        if job_return_code is not UNSET:
            field_dict["jobReturnCode"] = job_return_code
        if job_request_uuid is not UNSET:
            field_dict["jobRequestUuid"] = job_request_uuid
        if job_uuid is not UNSET:
            field_dict["jobUuid"] = job_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check import Check

        d = dict(src_dict)
        check_name = d.pop("checkName", UNSET)

        audience = d.pop("audience", UNSET)

        check_type = d.pop("checkType", UNSET)

        ready_for_flight = d.pop("readyForFlight", UNSET)

        message = d.pop("message", UNSET)

        checks = []
        _checks = d.pop("checks", UNSET)
        for checks_item_data in _checks or []:
            checks_item = Check.from_dict(checks_item_data)

            checks.append(checks_item)

        job_return_code = d.pop("jobReturnCode", UNSET)

        job_request_uuid = d.pop("jobRequestUuid", UNSET)

        _job_uuid = d.pop("jobUuid", UNSET)
        job_uuid: Union[Unset, UUID]
        if isinstance(_job_uuid, Unset):
            job_uuid = UNSET
        else:
            job_uuid = UUID(_job_uuid)

        check_response = cls(
            check_name=check_name,
            audience=audience,
            check_type=check_type,
            ready_for_flight=ready_for_flight,
            message=message,
            checks=checks,
            job_return_code=job_return_code,
            job_request_uuid=job_request_uuid,
            job_uuid=job_uuid,
        )

        check_response.additional_properties = d
        return check_response

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
