import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.server_config_data_type import ServerConfigDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_config import IConfig


T = TypeVar("T", bound="ServerConfig")


@_attrs_define
class ServerConfig:
    """
    Attributes:
        id (Union[Unset, int]):
        key (Union[Unset, str]):
        value (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
        audit_id (Union[Unset, str]):
        data_type (Union[Unset, ServerConfigDataType]):
        description (Union[Unset, str]):
        nullable (Union[Unset, int]):
        transient_data_from_config (Union[Unset, IConfig]):
    """

    id: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    data_type: Union[Unset, ServerConfigDataType] = UNSET
    description: Union[Unset, str] = UNSET
    nullable: Union[Unset, int] = UNSET
    transient_data_from_config: Union[Unset, "IConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        value = self.value

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        description = self.description

        nullable = self.nullable

        transient_data_from_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transient_data_from_config, Unset):
            transient_data_from_config = self.transient_data_from_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if description is not UNSET:
            field_dict["description"] = description
        if nullable is not UNSET:
            field_dict["nullable"] = nullable
        if transient_data_from_config is not UNSET:
            field_dict["transientDataFromConfig"] = transient_data_from_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_config import IConfig

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

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

        audit_id = d.pop("auditId", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, ServerConfigDataType]
        if _data_type and not isinstance(_data_type, Unset):
            data_type = ServerConfigDataType(_data_type)

        else:
            data_type = UNSET

        description = d.pop("description", UNSET)

        nullable = d.pop("nullable", UNSET)

        _transient_data_from_config = d.pop("transientDataFromConfig", UNSET)
        transient_data_from_config: Union[Unset, IConfig]
        if _transient_data_from_config and not isinstance(_transient_data_from_config, Unset):
            transient_data_from_config = IConfig.from_dict(_transient_data_from_config)

        else:
            transient_data_from_config = UNSET

        server_config = cls(
            id=id,
            key=key,
            value=value,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
            data_type=data_type,
            description=description,
            nullable=nullable,
            transient_data_from_config=transient_data_from_config,
        )

        server_config.additional_properties = d
        return server_config

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
