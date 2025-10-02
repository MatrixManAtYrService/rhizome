from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_parameter_object import JobParameterObject


T = TypeVar("T", bound="JobParameter")


@_attrs_define
class JobParameter:
    """
    Attributes:
        class_name (Union[Unset, str]):
        actual_class_name (Union[Unset, str]):
        object_ (Union[Unset, JobParameterObject]):
    """

    class_name: Union[Unset, str] = UNSET
    actual_class_name: Union[Unset, str] = UNSET
    object_: Union[Unset, "JobParameterObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_name = self.class_name

        actual_class_name = self.actual_class_name

        object_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if actual_class_name is not UNSET:
            field_dict["actualClassName"] = actual_class_name
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_parameter_object import JobParameterObject

        d = dict(src_dict)
        class_name = d.pop("className", UNSET)

        actual_class_name = d.pop("actualClassName", UNSET)

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, JobParameterObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = JobParameterObject.from_dict(_object_)

        job_parameter = cls(
            class_name=class_name,
            actual_class_name=actual_class_name,
            object_=object_,
        )

        job_parameter.additional_properties = d
        return job_parameter

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
