from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMigrateMerchantsJobParams")


@_attrs_define
class ApiMigrateMerchantsJobParams:
    """
    Attributes:
        reference_uuid (Union[Unset, str]): 13-character UUID assigned to the reference entity (or reseller uuid)
            associated with the job execution request
        processing_group_uuid (Union[Unset, str]): 26-character UUID of the processing group that will be used for this
            reseller.  This is required for app migration.
        hierarchy_type (Union[Unset, str]): optional billing hierarchy type associated with the reference entity (or
            reseller uuid)
        environment (Union[Unset, str]): optional indicators that designates the environment where the job is to be
            executed
        bypass_capture_event_play (Union[Unset, bool]): When true, this will bypass playing captured events as part of
            the migration.  This generally should not be used except in the case of migration of very simple merchants with
            single plans and no devices.
        bypass_capture_validation_check (Union[Unset, bool]): When true, this will ignore the results of the validation
            check to make sure the target reseller has been capturing events since the beginning of the month.  This should
            generally not be used.
        bypass_app_migration (Union[Unset, bool]): When true, this will bypass migration of apps.  Default is false.
        run_in_test_mode (Union[Unset, bool]): When true, merchants will not be added to the EBB merchant group in COS
            and a managed item filter will not created.  This would be used to migrate merchants in prod for shadowing.
    """

    reference_uuid: Union[Unset, str] = UNSET
    processing_group_uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    bypass_capture_event_play: Union[Unset, bool] = UNSET
    bypass_capture_validation_check: Union[Unset, bool] = UNSET
    bypass_app_migration: Union[Unset, bool] = UNSET
    run_in_test_mode: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_uuid = self.reference_uuid

        processing_group_uuid = self.processing_group_uuid

        hierarchy_type = self.hierarchy_type

        environment = self.environment

        bypass_capture_event_play = self.bypass_capture_event_play

        bypass_capture_validation_check = self.bypass_capture_validation_check

        bypass_app_migration = self.bypass_app_migration

        run_in_test_mode = self.run_in_test_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_uuid is not UNSET:
            field_dict["referenceUuid"] = reference_uuid
        if processing_group_uuid is not UNSET:
            field_dict["processingGroupUuid"] = processing_group_uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if environment is not UNSET:
            field_dict["environment"] = environment
        if bypass_capture_event_play is not UNSET:
            field_dict["bypassCaptureEventPlay"] = bypass_capture_event_play
        if bypass_capture_validation_check is not UNSET:
            field_dict["bypassCaptureValidationCheck"] = bypass_capture_validation_check
        if bypass_app_migration is not UNSET:
            field_dict["bypassAppMigration"] = bypass_app_migration
        if run_in_test_mode is not UNSET:
            field_dict["runInTestMode"] = run_in_test_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference_uuid = d.pop("referenceUuid", UNSET)

        processing_group_uuid = d.pop("processingGroupUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        environment = d.pop("environment", UNSET)

        bypass_capture_event_play = d.pop("bypassCaptureEventPlay", UNSET)

        bypass_capture_validation_check = d.pop("bypassCaptureValidationCheck", UNSET)

        bypass_app_migration = d.pop("bypassAppMigration", UNSET)

        run_in_test_mode = d.pop("runInTestMode", UNSET)

        api_migrate_merchants_job_params = cls(
            reference_uuid=reference_uuid,
            processing_group_uuid=processing_group_uuid,
            hierarchy_type=hierarchy_type,
            environment=environment,
            bypass_capture_event_play=bypass_capture_event_play,
            bypass_capture_validation_check=bypass_capture_validation_check,
            bypass_app_migration=bypass_app_migration,
            run_in_test_mode=run_in_test_mode,
        )

        api_migrate_merchants_job_params.additional_properties = d
        return api_migrate_merchants_job_params

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
