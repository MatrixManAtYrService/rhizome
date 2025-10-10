import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAppSubscriptionEvent")


@_attrs_define
class ApiAppSubscriptionEvent:
    """
    Attributes:
        uuid (Union[Unset, str]): 26-character UUID of the app subscription event
        merchant_uuid (Union[Unset, str]): 13-character UUID from COS of the merchant
        developer_app_uuid (Union[Unset, str]): 13-character UUID from COS of the developer app
        environment (Union[Unset, str]): environment this event is from
        action_type (Union[Unset, str]): the type of subscription action (INSTALL, UNINSTALL, SUBSCRIPTION_CHANGE)
        app_subscription_uuid (Union[Unset, str]): 13-character UUID from COS of the app subscription
        app_subscription_cost (Union[Unset, float]): The cost of the app used only for determining upgrades vs
            downgrades and does not impact amounts billed
        bundled_with_plan (Union[Unset, bool]): True if the app will not be billed because it was bundled with a plan
        trial_end_date (Union[Unset, datetime.date]): The end date of the trial if the app has a trial period
        is_hidden_or_sys_app (Union[Unset, bool]): True if the app is hidden or is a system app
        cos_event_uuid (Union[Unset, str]): The 13 character UUID from COS of the merchant_app or merchant_app_history
            record driving this event
        action_timestamp (Union[Unset, datetime.datetime]): The date/time this event occurred
        processed_timestamp (Union[Unset, datetime.datetime]): The date/time this event was processed by the app
            subscription daily job
        app_subscription_daily_uuid (Union[Unset, str]): The UUID of the app subscription daily record that this event
            was included on
        created_timestamp (Union[Unset, datetime.datetime]): The date/time this event was created
    """

    uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    action_type: Union[Unset, str] = UNSET
    app_subscription_uuid: Union[Unset, str] = UNSET
    app_subscription_cost: Union[Unset, float] = UNSET
    bundled_with_plan: Union[Unset, bool] = UNSET
    trial_end_date: Union[Unset, datetime.date] = UNSET
    is_hidden_or_sys_app: Union[Unset, bool] = UNSET
    cos_event_uuid: Union[Unset, str] = UNSET
    action_timestamp: Union[Unset, datetime.datetime] = UNSET
    processed_timestamp: Union[Unset, datetime.datetime] = UNSET
    app_subscription_daily_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        merchant_uuid = self.merchant_uuid

        developer_app_uuid = self.developer_app_uuid

        environment = self.environment

        action_type = self.action_type

        app_subscription_uuid = self.app_subscription_uuid

        app_subscription_cost = self.app_subscription_cost

        bundled_with_plan = self.bundled_with_plan

        trial_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.trial_end_date, Unset):
            trial_end_date = self.trial_end_date.isoformat()

        is_hidden_or_sys_app = self.is_hidden_or_sys_app

        cos_event_uuid = self.cos_event_uuid

        action_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.action_timestamp, Unset):
            action_timestamp = self.action_timestamp.isoformat()

        processed_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.processed_timestamp, Unset):
            processed_timestamp = self.processed_timestamp.isoformat()

        app_subscription_daily_uuid = self.app_subscription_daily_uuid

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
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if app_subscription_uuid is not UNSET:
            field_dict["appSubscriptionUuid"] = app_subscription_uuid
        if app_subscription_cost is not UNSET:
            field_dict["appSubscriptionCost"] = app_subscription_cost
        if bundled_with_plan is not UNSET:
            field_dict["bundledWithPlan"] = bundled_with_plan
        if trial_end_date is not UNSET:
            field_dict["trialEndDate"] = trial_end_date
        if is_hidden_or_sys_app is not UNSET:
            field_dict["isHiddenOrSysApp"] = is_hidden_or_sys_app
        if cos_event_uuid is not UNSET:
            field_dict["cosEventUuid"] = cos_event_uuid
        if action_timestamp is not UNSET:
            field_dict["actionTimestamp"] = action_timestamp
        if processed_timestamp is not UNSET:
            field_dict["processedTimestamp"] = processed_timestamp
        if app_subscription_daily_uuid is not UNSET:
            field_dict["appSubscriptionDailyUuid"] = app_subscription_daily_uuid
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

        action_type = d.pop("actionType", UNSET)

        app_subscription_uuid = d.pop("appSubscriptionUuid", UNSET)

        app_subscription_cost = d.pop("appSubscriptionCost", UNSET)

        bundled_with_plan = d.pop("bundledWithPlan", UNSET)

        _trial_end_date = d.pop("trialEndDate", UNSET)
        trial_end_date: Union[Unset, datetime.date]
        if _trial_end_date and not isinstance(_trial_end_date, Unset):
            trial_end_date = isoparse(_trial_end_date).date()

        else:
            trial_end_date = UNSET

        is_hidden_or_sys_app = d.pop("isHiddenOrSysApp", UNSET)

        cos_event_uuid = d.pop("cosEventUuid", UNSET)

        _action_timestamp = d.pop("actionTimestamp", UNSET)
        action_timestamp: Union[Unset, datetime.datetime]
        if _action_timestamp and not isinstance(_action_timestamp, Unset):
            action_timestamp = isoparse(_action_timestamp)

        else:
            action_timestamp = UNSET

        _processed_timestamp = d.pop("processedTimestamp", UNSET)
        processed_timestamp: Union[Unset, datetime.datetime]
        if _processed_timestamp and not isinstance(_processed_timestamp, Unset):
            processed_timestamp = isoparse(_processed_timestamp)

        else:
            processed_timestamp = UNSET

        app_subscription_daily_uuid = d.pop("appSubscriptionDailyUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_app_subscription_event = cls(
            uuid=uuid,
            merchant_uuid=merchant_uuid,
            developer_app_uuid=developer_app_uuid,
            environment=environment,
            action_type=action_type,
            app_subscription_uuid=app_subscription_uuid,
            app_subscription_cost=app_subscription_cost,
            bundled_with_plan=bundled_with_plan,
            trial_end_date=trial_end_date,
            is_hidden_or_sys_app=is_hidden_or_sys_app,
            cos_event_uuid=cos_event_uuid,
            action_timestamp=action_timestamp,
            processed_timestamp=processed_timestamp,
            app_subscription_daily_uuid=app_subscription_daily_uuid,
            created_timestamp=created_timestamp,
        )

        api_app_subscription_event.additional_properties = d
        return api_app_subscription_event

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
