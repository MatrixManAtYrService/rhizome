import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAppMeteredEvent")


@_attrs_define
class ApiAppMeteredEvent:
    """
    Attributes:
        uuid (Union[Unset, str]): 26-character UUID of the app metered event
        merchant_uuid (Union[Unset, str]): 13-character UUID from COS of the merchant
        developer_app_uuid (Union[Unset, str]): 13-character UUID from COS of the developer app
        environment (Union[Unset, str]): environment this event is from
        app_metered_uuid (Union[Unset, str]): 13-character UUID from COS of the app metered
        count (Union[Unset, int]): The number of metered actions that occurred for this event
        basis_amount (Union[Unset, float]): the basis amount for the metered event
        basis_currency (Union[Unset, str]): 3-letter currency code of the basis amount Example: USD.
        action_timestamp (Union[Unset, datetime.datetime]): The date/time this event occurred
        credit_for_trial (Union[Unset, bool]): True if this event was covered under a trial period
        cos_event_uuid (Union[Unset, str]): The 13 character UUID from COS of the merchant_app or merchant_app_history
            record driving this event
        processed_timestamp (Union[Unset, datetime.datetime]): The date/time this event was processed by the app metered
            daily job
        billing_event_uuid (Union[Unset, str]): The UUID of the billing event produced for this record
        created_timestamp (Union[Unset, datetime.datetime]): The date/time this event was created
    """

    uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    app_metered_uuid: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    basis_amount: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    action_timestamp: Union[Unset, datetime.datetime] = UNSET
    credit_for_trial: Union[Unset, bool] = UNSET
    cos_event_uuid: Union[Unset, str] = UNSET
    processed_timestamp: Union[Unset, datetime.datetime] = UNSET
    billing_event_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        merchant_uuid = self.merchant_uuid

        developer_app_uuid = self.developer_app_uuid

        environment = self.environment

        app_metered_uuid = self.app_metered_uuid

        count = self.count

        basis_amount = self.basis_amount

        basis_currency = self.basis_currency

        action_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.action_timestamp, Unset):
            action_timestamp = self.action_timestamp.isoformat()

        credit_for_trial = self.credit_for_trial

        cos_event_uuid = self.cos_event_uuid

        processed_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.processed_timestamp, Unset):
            processed_timestamp = self.processed_timestamp.isoformat()

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
        if app_metered_uuid is not UNSET:
            field_dict["appMeteredUuid"] = app_metered_uuid
        if count is not UNSET:
            field_dict["count"] = count
        if basis_amount is not UNSET:
            field_dict["basisAmount"] = basis_amount
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency
        if action_timestamp is not UNSET:
            field_dict["actionTimestamp"] = action_timestamp
        if credit_for_trial is not UNSET:
            field_dict["creditForTrial"] = credit_for_trial
        if cos_event_uuid is not UNSET:
            field_dict["cosEventUuid"] = cos_event_uuid
        if processed_timestamp is not UNSET:
            field_dict["processedTimestamp"] = processed_timestamp
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

        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

        count = d.pop("count", UNSET)

        basis_amount = d.pop("basisAmount", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        _action_timestamp = d.pop("actionTimestamp", UNSET)
        action_timestamp: Union[Unset, datetime.datetime]
        if _action_timestamp and not isinstance(_action_timestamp, Unset):
            action_timestamp = isoparse(_action_timestamp)

        else:
            action_timestamp = UNSET

        credit_for_trial = d.pop("creditForTrial", UNSET)

        cos_event_uuid = d.pop("cosEventUuid", UNSET)

        _processed_timestamp = d.pop("processedTimestamp", UNSET)
        processed_timestamp: Union[Unset, datetime.datetime]
        if _processed_timestamp and not isinstance(_processed_timestamp, Unset):
            processed_timestamp = isoparse(_processed_timestamp)

        else:
            processed_timestamp = UNSET

        billing_event_uuid = d.pop("billingEventUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_app_metered_event = cls(
            uuid=uuid,
            merchant_uuid=merchant_uuid,
            developer_app_uuid=developer_app_uuid,
            environment=environment,
            app_metered_uuid=app_metered_uuid,
            count=count,
            basis_amount=basis_amount,
            basis_currency=basis_currency,
            action_timestamp=action_timestamp,
            credit_for_trial=credit_for_trial,
            cos_event_uuid=cos_event_uuid,
            processed_timestamp=processed_timestamp,
            billing_event_uuid=billing_event_uuid,
            created_timestamp=created_timestamp,
        )

        api_app_metered_event.additional_properties = d
        return api_app_metered_event

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
