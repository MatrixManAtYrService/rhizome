import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_prototype_fee_set_disposition import ApiPrototypeFeeSetDisposition
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPrototypeFeeSet")


@_attrs_define
class ApiPrototypeFeeSet:
    """
    Attributes:
        id (Union[Unset, int]): Id of the prototype fee set
        uuid (Union[Unset, str]): 26-character UUID of the prototype fee set
        name (Union[Unset, str]): The name of the prototype fee set
        description (Union[Unset, str]): A description of the prototype fee set
        disposition (Union[Unset, ApiPrototypeFeeSetDisposition]):
        effective_date (Union[Unset, datetime.date]): effective date
        disposition_date_time (Union[Unset, datetime.datetime]): date and time when the prototype fee set was
            dispositioned Example: 2020-12-31T23:59:59.123456Z.
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the prototype fee rate was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the prototype fee rate was last
            modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    disposition: Union[Unset, ApiPrototypeFeeSetDisposition] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    disposition_date_time: Union[Unset, datetime.datetime] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        name = self.name

        description = self.description

        disposition: Union[Unset, str] = UNSET
        if not isinstance(self.disposition, Unset):
            disposition = self.disposition.value

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        disposition_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.disposition_date_time, Unset):
            disposition_date_time = self.disposition_date_time.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if disposition is not UNSET:
            field_dict["disposition"] = disposition
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if disposition_date_time is not UNSET:
            field_dict["dispositionDateTime"] = disposition_date_time
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _disposition = d.pop("disposition", UNSET)
        disposition: Union[Unset, ApiPrototypeFeeSetDisposition]
        if _disposition and not isinstance(_disposition, Unset):
            disposition = ApiPrototypeFeeSetDisposition(_disposition)

        else:
            disposition = UNSET

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if _effective_date and not isinstance(_effective_date, Unset):
            effective_date = isoparse(_effective_date).date()

        else:
            effective_date = UNSET

        _disposition_date_time = d.pop("dispositionDateTime", UNSET)
        disposition_date_time: Union[Unset, datetime.datetime]
        if _disposition_date_time and not isinstance(_disposition_date_time, Unset):
            disposition_date_time = isoparse(_disposition_date_time)

        else:
            disposition_date_time = UNSET

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if _modified_timestamp and not isinstance(_modified_timestamp, Unset):
            modified_timestamp = isoparse(_modified_timestamp)

        else:
            modified_timestamp = UNSET

        api_prototype_fee_set = cls(
            id=id,
            uuid=uuid,
            name=name,
            description=description,
            disposition=disposition,
            effective_date=effective_date,
            disposition_date_time=disposition_date_time,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_prototype_fee_set.additional_properties = d
        return api_prototype_fee_set

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
