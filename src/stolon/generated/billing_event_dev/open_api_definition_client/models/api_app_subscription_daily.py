import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAppSubscriptionDaily")


@_attrs_define
class ApiAppSubscriptionDaily:
    """
    Attributes:
        uuid (Union[Unset, str]): 26-character UUID of the app subscription daily
        merchant_uuid (Union[Unset, str]): 13-character UUID from COS of the merchant
        developer_app_uuid (Union[Unset, str]): 13-character UUID from COS of the developer app
        environment (Union[Unset, str]): environment this daily is for
        event_date (Union[Unset, datetime.date]): The date the daily record is for
        starting_app_subscription_uuid (Union[Unset, str]): 13-character UUID from COS of the app subscription level at
            the beginning of the day
        ending_app_subscription_uuid (Union[Unset, str]): 13-character UUID from COS of the app subscription level at
            the end of the day
        highest_app_subscription_uuid (Union[Unset, str]): 13-character UUID from COS of the app subscription level that
            was the most expensive during the day
        billing_event_uuid (Union[Unset, str]): The UUID of the billing event that was produced for this daily record
        created_timestamp (Union[Unset, datetime.datetime]): The date/time this daily record was created
    """

    uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    event_date: Union[Unset, datetime.date] = UNSET
    starting_app_subscription_uuid: Union[Unset, str] = UNSET
    ending_app_subscription_uuid: Union[Unset, str] = UNSET
    highest_app_subscription_uuid: Union[Unset, str] = UNSET
    billing_event_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        merchant_uuid = self.merchant_uuid

        developer_app_uuid = self.developer_app_uuid

        environment = self.environment

        event_date: Union[Unset, str] = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.isoformat()

        starting_app_subscription_uuid = self.starting_app_subscription_uuid

        ending_app_subscription_uuid = self.ending_app_subscription_uuid

        highest_app_subscription_uuid = self.highest_app_subscription_uuid

        billing_event_uuid = self.billing_event_uuid

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if developer_app_uuid is not UNSET:
            field_dict["developerAppUuid"] = developer_app_uuid
        if environment is not UNSET:
            field_dict["environment"] = environment
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if starting_app_subscription_uuid is not UNSET:
            field_dict["startingAppSubscriptionUuid"] = starting_app_subscription_uuid
        if ending_app_subscription_uuid is not UNSET:
            field_dict["endingAppSubscriptionUuid"] = ending_app_subscription_uuid
        if highest_app_subscription_uuid is not UNSET:
            field_dict["highestAppSubscriptionUuid"] = highest_app_subscription_uuid
        if billing_event_uuid is not UNSET:
            field_dict["billingEventUuid"] = billing_event_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        environment = d.pop("environment", UNSET)

        _event_date = d.pop("eventDate", UNSET)
        event_date: Union[Unset, datetime.date]
        if isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = isoparse(_event_date).date()

        starting_app_subscription_uuid = d.pop("startingAppSubscriptionUuid", UNSET)

        ending_app_subscription_uuid = d.pop("endingAppSubscriptionUuid", UNSET)

        highest_app_subscription_uuid = d.pop("highestAppSubscriptionUuid", UNSET)

        billing_event_uuid = d.pop("billingEventUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_app_subscription_daily = cls(
            uuid=uuid,
            merchant_uuid=merchant_uuid,
            developer_app_uuid=developer_app_uuid,
            environment=environment,
            event_date=event_date,
            starting_app_subscription_uuid=starting_app_subscription_uuid,
            ending_app_subscription_uuid=ending_app_subscription_uuid,
            highest_app_subscription_uuid=highest_app_subscription_uuid,
            billing_event_uuid=billing_event_uuid,
            created_timestamp=created_timestamp,
        )

        api_app_subscription_daily.additional_properties = d
        return api_app_subscription_daily

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
