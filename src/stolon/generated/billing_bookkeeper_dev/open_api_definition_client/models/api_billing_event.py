import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_app_meter_event import ApiAppMeterEvent
    from ..models.api_app_rates_event import ApiAppRatesEvent
    from ..models.api_app_sub_event import ApiAppSubEvent
    from ..models.api_cellular_event import ApiCellularEvent
    from ..models.api_memo_event import ApiMemoEvent
    from ..models.api_merchant_event import ApiMerchantEvent
    from ..models.api_misc_event import ApiMiscEvent
    from ..models.api_plan_event import ApiPlanEvent
    from ..models.api_revenue_event import ApiRevenueEvent


T = TypeVar("T", bound="ApiBillingEvent")


@_attrs_define
class ApiBillingEvent:
    """
    Attributes:
        environment (Union[Unset, str]):
        event_timestamp (Union[Unset, datetime.datetime]): date and time of the billing event Example:
            2020-12-31T23:59:59.123456Z.
        event_uuid (Union[Unset, str]): 26-character UUID assigned to the event
        merchant_events (Union[Unset, list['ApiMerchantEvent']]): merchant events
        plan_events (Union[Unset, list['ApiPlanEvent']]): plan events
        app_rates_events (Union[Unset, list['ApiAppRatesEvent']]): app rates events
        app_sub_events (Union[Unset, list['ApiAppSubEvent']]): app subscription events
        app_meter_events (Union[Unset, list['ApiAppMeterEvent']]): app metered events
        cellular_events (Union[Unset, list['ApiCellularEvent']]): cellular events
        misc_events (Union[Unset, list['ApiMiscEvent']]): miscellaneous events
        revenue_events (Union[Unset, list['ApiRevenueEvent']]): revenue events
        memo_events (Union[Unset, list['ApiMemoEvent']]): memo events used to report job progress and completion
    """

    environment: Union[Unset, str] = UNSET
    event_timestamp: Union[Unset, datetime.datetime] = UNSET
    event_uuid: Union[Unset, str] = UNSET
    merchant_events: Union[Unset, list["ApiMerchantEvent"]] = UNSET
    plan_events: Union[Unset, list["ApiPlanEvent"]] = UNSET
    app_rates_events: Union[Unset, list["ApiAppRatesEvent"]] = UNSET
    app_sub_events: Union[Unset, list["ApiAppSubEvent"]] = UNSET
    app_meter_events: Union[Unset, list["ApiAppMeterEvent"]] = UNSET
    cellular_events: Union[Unset, list["ApiCellularEvent"]] = UNSET
    misc_events: Union[Unset, list["ApiMiscEvent"]] = UNSET
    revenue_events: Union[Unset, list["ApiRevenueEvent"]] = UNSET
    memo_events: Union[Unset, list["ApiMemoEvent"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment = self.environment

        event_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.event_timestamp, Unset):
            event_timestamp = self.event_timestamp.isoformat()

        event_uuid = self.event_uuid

        merchant_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.merchant_events, Unset):
            merchant_events = []
            for merchant_events_item_data in self.merchant_events:
                merchant_events_item = merchant_events_item_data.to_dict()
                merchant_events.append(merchant_events_item)

        plan_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_events, Unset):
            plan_events = []
            for plan_events_item_data in self.plan_events:
                plan_events_item = plan_events_item_data.to_dict()
                plan_events.append(plan_events_item)

        app_rates_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_rates_events, Unset):
            app_rates_events = []
            for app_rates_events_item_data in self.app_rates_events:
                app_rates_events_item = app_rates_events_item_data.to_dict()
                app_rates_events.append(app_rates_events_item)

        app_sub_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_sub_events, Unset):
            app_sub_events = []
            for app_sub_events_item_data in self.app_sub_events:
                app_sub_events_item = app_sub_events_item_data.to_dict()
                app_sub_events.append(app_sub_events_item)

        app_meter_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_meter_events, Unset):
            app_meter_events = []
            for app_meter_events_item_data in self.app_meter_events:
                app_meter_events_item = app_meter_events_item_data.to_dict()
                app_meter_events.append(app_meter_events_item)

        cellular_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cellular_events, Unset):
            cellular_events = []
            for cellular_events_item_data in self.cellular_events:
                cellular_events_item = cellular_events_item_data.to_dict()
                cellular_events.append(cellular_events_item)

        misc_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.misc_events, Unset):
            misc_events = []
            for misc_events_item_data in self.misc_events:
                misc_events_item = misc_events_item_data.to_dict()
                misc_events.append(misc_events_item)

        revenue_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revenue_events, Unset):
            revenue_events = []
            for revenue_events_item_data in self.revenue_events:
                revenue_events_item = revenue_events_item_data.to_dict()
                revenue_events.append(revenue_events_item)

        memo_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.memo_events, Unset):
            memo_events = []
            for memo_events_item_data in self.memo_events:
                memo_events_item = memo_events_item_data.to_dict()
                memo_events.append(memo_events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if environment is not UNSET:
            field_dict["environment"] = environment
        if event_timestamp is not UNSET:
            field_dict["eventTimestamp"] = event_timestamp
        if event_uuid is not UNSET:
            field_dict["eventUuid"] = event_uuid
        if merchant_events is not UNSET:
            field_dict["merchantEvents"] = merchant_events
        if plan_events is not UNSET:
            field_dict["planEvents"] = plan_events
        if app_rates_events is not UNSET:
            field_dict["appRatesEvents"] = app_rates_events
        if app_sub_events is not UNSET:
            field_dict["appSubEvents"] = app_sub_events
        if app_meter_events is not UNSET:
            field_dict["appMeterEvents"] = app_meter_events
        if cellular_events is not UNSET:
            field_dict["cellularEvents"] = cellular_events
        if misc_events is not UNSET:
            field_dict["miscEvents"] = misc_events
        if revenue_events is not UNSET:
            field_dict["revenueEvents"] = revenue_events
        if memo_events is not UNSET:
            field_dict["memoEvents"] = memo_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_app_meter_event import ApiAppMeterEvent
        from ..models.api_app_rates_event import ApiAppRatesEvent
        from ..models.api_app_sub_event import ApiAppSubEvent
        from ..models.api_cellular_event import ApiCellularEvent
        from ..models.api_memo_event import ApiMemoEvent
        from ..models.api_merchant_event import ApiMerchantEvent
        from ..models.api_misc_event import ApiMiscEvent
        from ..models.api_plan_event import ApiPlanEvent
        from ..models.api_revenue_event import ApiRevenueEvent

        d = dict(src_dict)
        environment = d.pop("environment", UNSET)

        _event_timestamp = d.pop("eventTimestamp", UNSET)
        event_timestamp: Union[Unset, datetime.datetime]
        if _event_timestamp and not isinstance(_event_timestamp, Unset):
            event_timestamp = isoparse(_event_timestamp)

        else:
            event_timestamp = UNSET

        event_uuid = d.pop("eventUuid", UNSET)

        merchant_events = []
        _merchant_events = d.pop("merchantEvents", UNSET)
        for merchant_events_item_data in _merchant_events or []:
            merchant_events_item = ApiMerchantEvent.from_dict(merchant_events_item_data)

            merchant_events.append(merchant_events_item)

        plan_events = []
        _plan_events = d.pop("planEvents", UNSET)
        for plan_events_item_data in _plan_events or []:
            plan_events_item = ApiPlanEvent.from_dict(plan_events_item_data)

            plan_events.append(plan_events_item)

        app_rates_events = []
        _app_rates_events = d.pop("appRatesEvents", UNSET)
        for app_rates_events_item_data in _app_rates_events or []:
            app_rates_events_item = ApiAppRatesEvent.from_dict(app_rates_events_item_data)

            app_rates_events.append(app_rates_events_item)

        app_sub_events = []
        _app_sub_events = d.pop("appSubEvents", UNSET)
        for app_sub_events_item_data in _app_sub_events or []:
            app_sub_events_item = ApiAppSubEvent.from_dict(app_sub_events_item_data)

            app_sub_events.append(app_sub_events_item)

        app_meter_events = []
        _app_meter_events = d.pop("appMeterEvents", UNSET)
        for app_meter_events_item_data in _app_meter_events or []:
            app_meter_events_item = ApiAppMeterEvent.from_dict(app_meter_events_item_data)

            app_meter_events.append(app_meter_events_item)

        cellular_events = []
        _cellular_events = d.pop("cellularEvents", UNSET)
        for cellular_events_item_data in _cellular_events or []:
            cellular_events_item = ApiCellularEvent.from_dict(cellular_events_item_data)

            cellular_events.append(cellular_events_item)

        misc_events = []
        _misc_events = d.pop("miscEvents", UNSET)
        for misc_events_item_data in _misc_events or []:
            misc_events_item = ApiMiscEvent.from_dict(misc_events_item_data)

            misc_events.append(misc_events_item)

        revenue_events = []
        _revenue_events = d.pop("revenueEvents", UNSET)
        for revenue_events_item_data in _revenue_events or []:
            revenue_events_item = ApiRevenueEvent.from_dict(revenue_events_item_data)

            revenue_events.append(revenue_events_item)

        memo_events = []
        _memo_events = d.pop("memoEvents", UNSET)
        for memo_events_item_data in _memo_events or []:
            memo_events_item = ApiMemoEvent.from_dict(memo_events_item_data)

            memo_events.append(memo_events_item)

        api_billing_event = cls(
            environment=environment,
            event_timestamp=event_timestamp,
            event_uuid=event_uuid,
            merchant_events=merchant_events,
            plan_events=plan_events,
            app_rates_events=app_rates_events,
            app_sub_events=app_sub_events,
            app_meter_events=app_meter_events,
            cellular_events=cellular_events,
            misc_events=misc_events,
            revenue_events=revenue_events,
            memo_events=memo_events,
        )

        api_billing_event.additional_properties = d
        return api_billing_event

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
