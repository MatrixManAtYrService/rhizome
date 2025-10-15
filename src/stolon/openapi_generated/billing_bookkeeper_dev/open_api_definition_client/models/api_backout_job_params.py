from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_backout_job_params_mode import ApiBackoutJobParamsMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBackoutJobParams")


@_attrs_define
class ApiBackoutJobParams:
    """
    Attributes:
        reference_uuid (Union[Unset, str]): 13- or 26-character UUID assigned to the reference entity (or processing
            group) associated with the job execution request
        hierarchy_type (Union[Unset, str]): optional billing hierarchy type associated with the reference entity (or
            processing group)
        environment (Union[Unset, str]): optional indicators that designates the environment where the job is to be
            executed
        request_uuid (Union[Unset, str]): 26-character UUID assigned to the job execution request of the job being
            backed out
        mode (Union[Unset, ApiBackoutJobParamsMode]):
        verbose (Union[Unset, bool]): indicates whether to include specific update/delete details in logging (true), or
            only routine summary logging (false/default)
        billing_entity_uuids (Union[Unset, list[str]]):
    """

    reference_uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    mode: Union[Unset, ApiBackoutJobParamsMode] = UNSET
    verbose: Union[Unset, bool] = UNSET
    billing_entity_uuids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_uuid = self.reference_uuid

        hierarchy_type = self.hierarchy_type

        environment = self.environment

        request_uuid = self.request_uuid

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        verbose = self.verbose

        billing_entity_uuids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.billing_entity_uuids, Unset):
            billing_entity_uuids = self.billing_entity_uuids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_uuid is not UNSET:
            field_dict["referenceUuid"] = reference_uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if environment is not UNSET:
            field_dict["environment"] = environment
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if mode is not UNSET:
            field_dict["mode"] = mode
        if verbose is not UNSET:
            field_dict["verbose"] = verbose
        if billing_entity_uuids is not UNSET:
            field_dict["billingEntityUuids"] = billing_entity_uuids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_uuid = d.pop("referenceUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        environment = d.pop("environment", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, ApiBackoutJobParamsMode]
        if _mode and not isinstance(_mode, Unset):
            mode = ApiBackoutJobParamsMode(_mode)

        else:
            mode = UNSET

        verbose = d.pop("verbose", UNSET)

        billing_entity_uuids = cast(list[str], d.pop("billingEntityUuids", UNSET))

        api_backout_job_params = cls(
            reference_uuid=reference_uuid,
            hierarchy_type=hierarchy_type,
            environment=environment,
            request_uuid=request_uuid,
            mode=mode,
            verbose=verbose,
            billing_entity_uuids=billing_entity_uuids,
        )

        api_backout_job_params.additional_properties = d
        return api_backout_job_params

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
