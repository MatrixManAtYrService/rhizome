import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_merchant_offboarding_step import ApiMerchantOffboardingStep
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMerchantOffboarding")


@_attrs_define
class ApiMerchantOffboarding:
    """
    Attributes:
        id (Union[Unset, int]): Id of the offboarding
        merchant_uuid (Union[Unset, str]): 13-character merchant ID of the offboarding
        uuid (Union[Unset, str]): 26-character uuid for offboarding
        environment (Union[Unset, str]):
        step (Union[Unset, ApiMerchantOffboardingStep]):
        due_date (Union[Unset, datetime.date]): date of the for offboarding to be entered into queue
        offboard_timestamp (Union[Unset, datetime.datetime]):  Example: 2020-12-31T23:59:59.123456Z.
        created_timestamp (Union[Unset, datetime.datetime]): offboarding created timestamp Example:
            2020-12-31T23:59:59.123456Z.
        deleted_timestamp (Union[Unset, datetime.datetime]): offboarding end timestamp Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    step: Union[Unset, ApiMerchantOffboardingStep] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    offboard_timestamp: Union[Unset, datetime.datetime] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    deleted_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        merchant_uuid = self.merchant_uuid

        uuid = self.uuid

        environment = self.environment

        step: Union[Unset, str] = UNSET
        if not isinstance(self.step, Unset):
            step = self.step.value

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        offboard_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.offboard_timestamp, Unset):
            offboard_timestamp = self.offboard_timestamp.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        deleted_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_timestamp, Unset):
            deleted_timestamp = self.deleted_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if environment is not UNSET:
            field_dict["environment"] = environment
        if step is not UNSET:
            field_dict["step"] = step
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if offboard_timestamp is not UNSET:
            field_dict["offboardTimestamp"] = offboard_timestamp
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if deleted_timestamp is not UNSET:
            field_dict["deletedTimestamp"] = deleted_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        uuid = d.pop("uuid", UNSET)

        environment = d.pop("environment", UNSET)

        _step = d.pop("step", UNSET)
        step: Union[Unset, ApiMerchantOffboardingStep]
        if _step and not isinstance(_step, Unset):
            step = ApiMerchantOffboardingStep(_step)

        else:
            step = UNSET

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if _due_date and not isinstance(_due_date, Unset):
            due_date = isoparse(_due_date).date()

        else:
            due_date = UNSET

        _offboard_timestamp = d.pop("offboardTimestamp", UNSET)
        offboard_timestamp: Union[Unset, datetime.datetime]
        if _offboard_timestamp and not isinstance(_offboard_timestamp, Unset):
            offboard_timestamp = isoparse(_offboard_timestamp)

        else:
            offboard_timestamp = UNSET

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _deleted_timestamp = d.pop("deletedTimestamp", UNSET)
        deleted_timestamp: Union[Unset, datetime.datetime]
        if _deleted_timestamp and not isinstance(_deleted_timestamp, Unset):
            deleted_timestamp = isoparse(_deleted_timestamp)

        else:
            deleted_timestamp = UNSET

        api_merchant_offboarding = cls(
            id=id,
            merchant_uuid=merchant_uuid,
            uuid=uuid,
            environment=environment,
            step=step,
            due_date=due_date,
            offboard_timestamp=offboard_timestamp,
            created_timestamp=created_timestamp,
            deleted_timestamp=deleted_timestamp,
        )

        api_merchant_offboarding.additional_properties = d
        return api_merchant_offboarding

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
