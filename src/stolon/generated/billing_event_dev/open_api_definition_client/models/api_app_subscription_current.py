import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAppSubscriptionCurrent")


@_attrs_define
class ApiAppSubscriptionCurrent:
    """
    Attributes:
        uuid (Union[Unset, str]): 26-character UUID of the app subscription current record
        merchant_uuid (Union[Unset, str]): 13-character UUID from COS of the merchant
        developer_app_uuid (Union[Unset, str]): 13-character UUID from COS of the developer app
        environment (Union[Unset, str]): environment this current record is for
        app_subscription_uuid (Union[Unset, str]): 13-character UUID from COS of the current app subscription level
        app_subscription_cost (Union[Unset, float]): The cost of the app level used only for determining upgrades vs
            downgrades and does not impact amounts billed
        bundled_with_plan (Union[Unset, bool]): True if the app will not be billed because it was bundled with a plan
        trial_end_date (Union[Unset, datetime.date]): The end date of the trial if the app has a trial period
        last_advance_date (Union[Unset, datetime.date]): The date this app was last advanced.  This is used to make the
            app sub advance job as reentrant so a merchant/app will never be advanced twice on the same billing day
        created_timestamp (Union[Unset, datetime.datetime]): The date/time this current record was created
        modified_timestamp (Union[Unset, datetime.datetime]): The date/time this current record was modified
    """

    uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    app_subscription_uuid: Union[Unset, str] = UNSET
    app_subscription_cost: Union[Unset, float] = UNSET
    bundled_with_plan: Union[Unset, bool] = UNSET
    trial_end_date: Union[Unset, datetime.date] = UNSET
    last_advance_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        merchant_uuid = self.merchant_uuid

        developer_app_uuid = self.developer_app_uuid

        environment = self.environment

        app_subscription_uuid = self.app_subscription_uuid

        app_subscription_cost = self.app_subscription_cost

        bundled_with_plan = self.bundled_with_plan

        trial_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.trial_end_date, Unset):
            trial_end_date = self.trial_end_date.isoformat()

        last_advance_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_advance_date, Unset):
            last_advance_date = self.last_advance_date.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

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
        if app_subscription_uuid is not UNSET:
            field_dict["appSubscriptionUuid"] = app_subscription_uuid
        if app_subscription_cost is not UNSET:
            field_dict["appSubscriptionCost"] = app_subscription_cost
        if bundled_with_plan is not UNSET:
            field_dict["bundledWithPlan"] = bundled_with_plan
        if trial_end_date is not UNSET:
            field_dict["trialEndDate"] = trial_end_date
        if last_advance_date is not UNSET:
            field_dict["lastAdvanceDate"] = last_advance_date
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        environment = d.pop("environment", UNSET)

        app_subscription_uuid = d.pop("appSubscriptionUuid", UNSET)

        app_subscription_cost = d.pop("appSubscriptionCost", UNSET)

        bundled_with_plan = d.pop("bundledWithPlan", UNSET)

        _trial_end_date = d.pop("trialEndDate", UNSET)
        trial_end_date: Union[Unset, datetime.date]
        if isinstance(_trial_end_date, Unset):
            trial_end_date = UNSET
        else:
            trial_end_date = isoparse(_trial_end_date).date()

        _last_advance_date = d.pop("lastAdvanceDate", UNSET)
        last_advance_date: Union[Unset, datetime.date]
        if isinstance(_last_advance_date, Unset):
            last_advance_date = UNSET
        else:
            last_advance_date = isoparse(_last_advance_date).date()

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

        api_app_subscription_current = cls(
            uuid=uuid,
            merchant_uuid=merchant_uuid,
            developer_app_uuid=developer_app_uuid,
            environment=environment,
            app_subscription_uuid=app_subscription_uuid,
            app_subscription_cost=app_subscription_cost,
            bundled_with_plan=bundled_with_plan,
            trial_end_date=trial_end_date,
            last_advance_date=last_advance_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_app_subscription_current.additional_properties = d
        return api_app_subscription_current

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
