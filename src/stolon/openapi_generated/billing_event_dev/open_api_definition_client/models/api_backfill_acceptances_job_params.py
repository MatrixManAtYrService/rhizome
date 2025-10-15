from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_backfill_acceptance import ApiBackfillAcceptance


T = TypeVar("T", bound="ApiBackfillAcceptancesJobParams")


@_attrs_define
class ApiBackfillAcceptancesJobParams:
    """
    Attributes:
        reference_uuid (Union[Unset, str]): 13-character UUID assigned to the reference entity (or reseller uuid)
            associated with the job execution request
        environment (Union[Unset, str]): optional indicators that designates the environment where the job is to be
            executed
        backfill_acceptances (Union[Unset, list['ApiBackfillAcceptance']]): Array of backfill acceptances to create
    """

    reference_uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    backfill_acceptances: Union[Unset, list["ApiBackfillAcceptance"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_uuid = self.reference_uuid

        environment = self.environment

        backfill_acceptances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.backfill_acceptances, Unset):
            backfill_acceptances = []
            for backfill_acceptances_item_data in self.backfill_acceptances:
                backfill_acceptances_item = backfill_acceptances_item_data.to_dict()
                backfill_acceptances.append(backfill_acceptances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_uuid is not UNSET:
            field_dict["referenceUuid"] = reference_uuid
        if environment is not UNSET:
            field_dict["environment"] = environment
        if backfill_acceptances is not UNSET:
            field_dict["backfillAcceptances"] = backfill_acceptances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_backfill_acceptance import ApiBackfillAcceptance

        d = dict(src_dict)
        reference_uuid = d.pop("referenceUuid", UNSET)

        environment = d.pop("environment", UNSET)

        backfill_acceptances = []
        _backfill_acceptances = d.pop("backfillAcceptances", UNSET)
        for backfill_acceptances_item_data in _backfill_acceptances or []:
            backfill_acceptances_item = ApiBackfillAcceptance.from_dict(backfill_acceptances_item_data)

            backfill_acceptances.append(backfill_acceptances_item)

        api_backfill_acceptances_job_params = cls(
            reference_uuid=reference_uuid,
            environment=environment,
            backfill_acceptances=backfill_acceptances,
        )

        api_backfill_acceptances_job_params.additional_properties = d
        return api_backfill_acceptances_job_params

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
