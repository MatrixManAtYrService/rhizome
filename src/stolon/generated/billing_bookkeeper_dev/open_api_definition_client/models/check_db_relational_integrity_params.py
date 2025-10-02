from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_execution_param import ApiExecutionParam


T = TypeVar("T", bound="CheckDbRelationalIntegrityParams")


@_attrs_define
class CheckDbRelationalIntegrityParams:
    """
    Attributes:
        reference_uuid (Union[Unset, str]):
        hierarchy_type (Union[Unset, str]):
        environment (Union[Unset, str]):
        checks_to_exclude (Union[Unset, str]):
        row_limit (Union[Unset, int]):
        as_job_params (Union[Unset, list['ApiExecutionParam']]):
    """

    reference_uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    checks_to_exclude: Union[Unset, str] = UNSET
    row_limit: Union[Unset, int] = UNSET
    as_job_params: Union[Unset, list["ApiExecutionParam"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_uuid = self.reference_uuid

        hierarchy_type = self.hierarchy_type

        environment = self.environment

        checks_to_exclude = self.checks_to_exclude

        row_limit = self.row_limit

        as_job_params: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.as_job_params, Unset):
            as_job_params = []
            for as_job_params_item_data in self.as_job_params:
                as_job_params_item = as_job_params_item_data.to_dict()
                as_job_params.append(as_job_params_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_uuid is not UNSET:
            field_dict["referenceUuid"] = reference_uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if environment is not UNSET:
            field_dict["environment"] = environment
        if checks_to_exclude is not UNSET:
            field_dict["checksToExclude"] = checks_to_exclude
        if row_limit is not UNSET:
            field_dict["rowLimit"] = row_limit
        if as_job_params is not UNSET:
            field_dict["asJobParams"] = as_job_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_execution_param import ApiExecutionParam

        d = dict(src_dict)
        reference_uuid = d.pop("referenceUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        environment = d.pop("environment", UNSET)

        checks_to_exclude = d.pop("checksToExclude", UNSET)

        row_limit = d.pop("rowLimit", UNSET)

        as_job_params = []
        _as_job_params = d.pop("asJobParams", UNSET)
        for as_job_params_item_data in _as_job_params or []:
            as_job_params_item = ApiExecutionParam.from_dict(as_job_params_item_data)

            as_job_params.append(as_job_params_item)

        check_db_relational_integrity_params = cls(
            reference_uuid=reference_uuid,
            hierarchy_type=hierarchy_type,
            environment=environment,
            checks_to_exclude=checks_to_exclude,
            row_limit=row_limit,
            as_job_params=as_job_params,
        )

        check_db_relational_integrity_params.additional_properties = d
        return check_db_relational_integrity_params

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
