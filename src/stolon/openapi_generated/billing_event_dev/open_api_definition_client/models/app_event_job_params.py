import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppEventJobParams")


@_attrs_define
class AppEventJobParams:
    """
    Attributes:
        reference_uuid (Union[Unset, str]):
        hierarchy_type (Union[Unset, str]):
        environment (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        stop (Union[Unset, datetime.datetime]):
    """

    reference_uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    stop: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_uuid = self.reference_uuid

        hierarchy_type = self.hierarchy_type

        environment = self.environment

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        stop: Union[Unset, str] = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_uuid is not UNSET:
            field_dict["referenceUuid"] = reference_uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if environment is not UNSET:
            field_dict["environment"] = environment
        if start is not UNSET:
            field_dict["start"] = start
        if stop is not UNSET:
            field_dict["stop"] = stop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_uuid = d.pop("referenceUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        environment = d.pop("environment", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if _start and not isinstance(_start, Unset):
            start = isoparse(_start)

        else:
            start = UNSET

        _stop = d.pop("stop", UNSET)
        stop: Union[Unset, datetime.datetime]
        if _stop and not isinstance(_stop, Unset):
            stop = isoparse(_stop)

        else:
            stop = UNSET

        app_event_job_params = cls(
            reference_uuid=reference_uuid,
            hierarchy_type=hierarchy_type,
            environment=environment,
            start=start,
            stop=stop,
        )

        app_event_job_params.additional_properties = d
        return app_event_job_params

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
