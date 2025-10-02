import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeCodeApp")


@_attrs_define
class ApiFeeCodeApp:
    """
    Attributes:
        id (Union[Unset, int]): Id of the fee-code-to-app mapping
        uuid (Union[Unset, str]): 26-character UUID of the fee-code-to-app mapping
        fee_category (Union[Unset, str]): defined fee category value
        fee_code (Union[Unset, str]): defined fee code value
        developer_uuid (Union[Unset, str]): UUID of a developer
        developer_app_uuid (Union[Unset, str]): UUID of a developer's app
        app_subscription_uuid (Union[Unset, str]): UUID of the app subscription
        app_metered_uuid (Union[Unset, str]): UUID of the app metered event type
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the fee-code-to-app was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the fee-code-to-app was last modified
            Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    app_subscription_uuid: Union[Unset, str] = UNSET
    app_metered_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        developer_uuid = self.developer_uuid

        developer_app_uuid = self.developer_app_uuid

        app_subscription_uuid = self.app_subscription_uuid

        app_metered_uuid = self.app_metered_uuid

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
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if developer_app_uuid is not UNSET:
            field_dict["developerAppUuid"] = developer_app_uuid
        if app_subscription_uuid is not UNSET:
            field_dict["appSubscriptionUuid"] = app_subscription_uuid
        if app_metered_uuid is not UNSET:
            field_dict["appMeteredUuid"] = app_metered_uuid
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

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        app_subscription_uuid = d.pop("appSubscriptionUuid", UNSET)

        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_modified_timestamp, Unset):
            modified_timestamp = UNSET
        else:
            modified_timestamp = isoparse(_modified_timestamp)

        api_fee_code_app = cls(
            id=id,
            uuid=uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            app_subscription_uuid=app_subscription_uuid,
            app_metered_uuid=app_metered_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_fee_code_app.additional_properties = d
        return api_fee_code_app

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
