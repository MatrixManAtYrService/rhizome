from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLimitJobParams")


@_attrs_define
class ApiLimitJobParams:
    """
    Attributes:
        reference_uuid (Union[Unset, str]): 13- or 26-character UUID assigned to the reference entity (or processing
            group) associated with the job execution request
        hierarchy_type (Union[Unset, str]): optional billing hierarchy type associated with the reference entity (or
            processing group)
        environment (Union[Unset, str]): optional indicators that designates the environment where the job is to be
            executed
        limit (Union[Unset, int]): optional limit that, when provided, specifies the maximum number of artifacts to
            process
    """

    reference_uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_uuid = self.reference_uuid

        hierarchy_type = self.hierarchy_type

        environment = self.environment

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_uuid is not UNSET:
            field_dict["referenceUuid"] = reference_uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if environment is not UNSET:
            field_dict["environment"] = environment
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_uuid = d.pop("referenceUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        environment = d.pop("environment", UNSET)

        limit = d.pop("limit", UNSET)

        api_limit_job_params = cls(
            reference_uuid=reference_uuid,
            hierarchy_type=hierarchy_type,
            environment=environment,
            limit=limit,
        )

        api_limit_job_params.additional_properties = d
        return api_limit_job_params

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
