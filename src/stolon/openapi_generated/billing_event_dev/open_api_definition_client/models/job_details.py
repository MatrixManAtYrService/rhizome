from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_details_job_parameter_values_item import JobDetailsJobParameterValuesItem
    from ..models.job_parameter import JobParameter


T = TypeVar("T", bound="JobDetails")


@_attrs_define
class JobDetails:
    """
    Attributes:
        class_name (Union[Unset, str]):
        static_field_name (Union[Unset, str]):
        method_name (Union[Unset, str]):
        job_parameters (Union[Unset, list['JobParameter']]):
        cacheable (Union[Unset, bool]):
        job_parameter_values (Union[Unset, list['JobDetailsJobParameterValuesItem']]):
    """

    class_name: Union[Unset, str] = UNSET
    static_field_name: Union[Unset, str] = UNSET
    method_name: Union[Unset, str] = UNSET
    job_parameters: Union[Unset, list["JobParameter"]] = UNSET
    cacheable: Union[Unset, bool] = UNSET
    job_parameter_values: Union[Unset, list["JobDetailsJobParameterValuesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_name = self.class_name

        static_field_name = self.static_field_name

        method_name = self.method_name

        job_parameters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.job_parameters, Unset):
            job_parameters = []
            for job_parameters_item_data in self.job_parameters:
                job_parameters_item = job_parameters_item_data.to_dict()
                job_parameters.append(job_parameters_item)

        cacheable = self.cacheable

        job_parameter_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.job_parameter_values, Unset):
            job_parameter_values = []
            for job_parameter_values_item_data in self.job_parameter_values:
                job_parameter_values_item = job_parameter_values_item_data.to_dict()
                job_parameter_values.append(job_parameter_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if static_field_name is not UNSET:
            field_dict["staticFieldName"] = static_field_name
        if method_name is not UNSET:
            field_dict["methodName"] = method_name
        if job_parameters is not UNSET:
            field_dict["jobParameters"] = job_parameters
        if cacheable is not UNSET:
            field_dict["cacheable"] = cacheable
        if job_parameter_values is not UNSET:
            field_dict["jobParameterValues"] = job_parameter_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_details_job_parameter_values_item import JobDetailsJobParameterValuesItem
        from ..models.job_parameter import JobParameter

        d = dict(src_dict)
        class_name = d.pop("className", UNSET)

        static_field_name = d.pop("staticFieldName", UNSET)

        method_name = d.pop("methodName", UNSET)

        job_parameters = []
        _job_parameters = d.pop("jobParameters", UNSET)
        for job_parameters_item_data in _job_parameters or []:
            job_parameters_item = JobParameter.from_dict(job_parameters_item_data)

            job_parameters.append(job_parameters_item)

        cacheable = d.pop("cacheable", UNSET)

        job_parameter_values = []
        _job_parameter_values = d.pop("jobParameterValues", UNSET)
        for job_parameter_values_item_data in _job_parameter_values or []:
            job_parameter_values_item = JobDetailsJobParameterValuesItem.from_dict(job_parameter_values_item_data)

            job_parameter_values.append(job_parameter_values_item)

        job_details = cls(
            class_name=class_name,
            static_field_name=static_field_name,
            method_name=method_name,
            job_parameters=job_parameters,
            cacheable=cacheable,
            job_parameter_values=job_parameter_values,
        )

        job_details.additional_properties = d
        return job_details

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
