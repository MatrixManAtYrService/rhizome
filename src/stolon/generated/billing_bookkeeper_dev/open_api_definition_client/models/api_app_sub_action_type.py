import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAppSubActionType")


@_attrs_define
class ApiAppSubActionType:
    """
    Attributes:
        id (Union[Unset, int]): Id of the app subscription action type
        uuid (Union[Unset, str]): 26-character UUID of the app subscription action type
        app_sub_action_type (Union[Unset, str]): defined app subscription action type value
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the app subscription action type was
            created Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    app_sub_action_type: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        app_sub_action_type = self.app_sub_action_type

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if app_sub_action_type is not UNSET:
            field_dict["appSubActionType"] = app_sub_action_type
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        app_sub_action_type = d.pop("appSubActionType", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_app_sub_action_type = cls(
            id=id,
            uuid=uuid,
            app_sub_action_type=app_sub_action_type,
            created_timestamp=created_timestamp,
        )

        api_app_sub_action_type.additional_properties = d
        return api_app_sub_action_type

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
