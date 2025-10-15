from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_error_status import ResponseErrorStatus


T = TypeVar("T", bound="ResponseError")


@_attrs_define
class ResponseError:
    """
    Attributes:
        message (Union[Unset, str]):
        status (Union[Unset, ResponseErrorStatus]):
    """

    message: Union[Unset, str] = UNSET
    status: Union[Unset, "ResponseErrorStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_error_status import ResponseErrorStatus

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ResponseErrorStatus]
        if _status and not isinstance(_status, Unset):
            status = ResponseErrorStatus.from_dict(_status)

        else:
            status = UNSET

        response_error = cls(
            message=message,
            status=status,
        )

        response_error.additional_properties = d
        return response_error

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
