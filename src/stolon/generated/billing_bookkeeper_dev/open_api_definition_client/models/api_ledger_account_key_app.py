import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLedgerAccountKeyApp")


@_attrs_define
class ApiLedgerAccountKeyApp:
    """
    Attributes:
        id (Union[Unset, int]): Id of the ledger-account-key-to-app mapping
        uuid (Union[Unset, str]): 26-character UUID of the ledger-account-key-to-app mapping
        ledger_account_key (Union[Unset, str]): the key value for the ledger account key
        developer_uuid (Union[Unset, str]): UUID of a developer that the ledger account key maps to
        developer_app_uuid (Union[Unset, str]): UUID of a developer's app that the ledger account key maps to
        app_subscription_uuid (Union[Unset, str]): UUID of the app subscription that the ledger account key maps to
        app_metered_uuid (Union[Unset, str]): UUID of the app metered event type that the ledger account key maps to
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger-account-key-to-app mapping
            was created Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger-account-key-to-app mapping
            was last modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    ledger_account_key: Union[Unset, str] = UNSET
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

        ledger_account_key = self.ledger_account_key

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
        if ledger_account_key is not UNSET:
            field_dict["ledgerAccountKey"] = ledger_account_key
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

        ledger_account_key = d.pop("ledgerAccountKey", UNSET)

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

        api_ledger_account_key_app = cls(
            id=id,
            uuid=uuid,
            ledger_account_key=ledger_account_key,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            app_subscription_uuid=app_subscription_uuid,
            app_metered_uuid=app_metered_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_ledger_account_key_app.additional_properties = d
        return api_ledger_account_key_app

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
