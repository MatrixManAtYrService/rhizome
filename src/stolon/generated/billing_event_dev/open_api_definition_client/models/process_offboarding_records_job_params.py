import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessOffboardingRecordsJobParams")


@_attrs_define
class ProcessOffboardingRecordsJobParams:
    """
    Attributes:
        reference_uuid (Union[Unset, str]):
        hierarchy_type (Union[Unset, str]):
        environment (Union[Unset, str]):
        cycle_date (Union[Unset, datetime.date]):
    """

    reference_uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    cycle_date: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_uuid = self.reference_uuid

        hierarchy_type = self.hierarchy_type

        environment = self.environment

        cycle_date: Union[Unset, str] = UNSET
        if not isinstance(self.cycle_date, Unset):
            cycle_date = self.cycle_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_uuid is not UNSET:
            field_dict["referenceUuid"] = reference_uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if environment is not UNSET:
            field_dict["environment"] = environment
        if cycle_date is not UNSET:
            field_dict["cycleDate"] = cycle_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_uuid = d.pop("referenceUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        environment = d.pop("environment", UNSET)

        _cycle_date = d.pop("cycleDate", UNSET)
        cycle_date: Union[Unset, datetime.date]
        if isinstance(_cycle_date, Unset):
            cycle_date = UNSET
        else:
            cycle_date = isoparse(_cycle_date).date()

        process_offboarding_records_job_params = cls(
            reference_uuid=reference_uuid,
            hierarchy_type=hierarchy_type,
            environment=environment,
            cycle_date=cycle_date,
        )

        process_offboarding_records_job_params.additional_properties = d
        return process_offboarding_records_job_params

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
