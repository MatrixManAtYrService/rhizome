from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_meter_action import AppMeterAction
    from ..models.app_sub_action import AppSubAction
    from ..models.cellular_action import CellularAction
    from ..models.misc_action import MiscAction
    from ..models.plan_action import PlanAction
    from ..models.revenue_action import RevenueAction


T = TypeVar("T", bound="Actions")


@_attrs_define
class Actions:
    """
    Attributes:
        plan_actions (Union[Unset, list['PlanAction']]):
        cellular_actions (Union[Unset, list['CellularAction']]):
        app_sub_actions (Union[Unset, list['AppSubAction']]):
        app_meter_actions (Union[Unset, list['AppMeterAction']]):
        misc_actions (Union[Unset, list['MiscAction']]):
        revenue_actions (Union[Unset, list['RevenueAction']]):
    """

    plan_actions: Union[Unset, list["PlanAction"]] = UNSET
    cellular_actions: Union[Unset, list["CellularAction"]] = UNSET
    app_sub_actions: Union[Unset, list["AppSubAction"]] = UNSET
    app_meter_actions: Union[Unset, list["AppMeterAction"]] = UNSET
    misc_actions: Union[Unset, list["MiscAction"]] = UNSET
    revenue_actions: Union[Unset, list["RevenueAction"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_actions, Unset):
            plan_actions = []
            for plan_actions_item_data in self.plan_actions:
                plan_actions_item = plan_actions_item_data.to_dict()
                plan_actions.append(plan_actions_item)

        cellular_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cellular_actions, Unset):
            cellular_actions = []
            for cellular_actions_item_data in self.cellular_actions:
                cellular_actions_item = cellular_actions_item_data.to_dict()
                cellular_actions.append(cellular_actions_item)

        app_sub_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_sub_actions, Unset):
            app_sub_actions = []
            for app_sub_actions_item_data in self.app_sub_actions:
                app_sub_actions_item = app_sub_actions_item_data.to_dict()
                app_sub_actions.append(app_sub_actions_item)

        app_meter_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_meter_actions, Unset):
            app_meter_actions = []
            for app_meter_actions_item_data in self.app_meter_actions:
                app_meter_actions_item = app_meter_actions_item_data.to_dict()
                app_meter_actions.append(app_meter_actions_item)

        misc_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.misc_actions, Unset):
            misc_actions = []
            for misc_actions_item_data in self.misc_actions:
                misc_actions_item = misc_actions_item_data.to_dict()
                misc_actions.append(misc_actions_item)

        revenue_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revenue_actions, Unset):
            revenue_actions = []
            for revenue_actions_item_data in self.revenue_actions:
                revenue_actions_item = revenue_actions_item_data.to_dict()
                revenue_actions.append(revenue_actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_actions is not UNSET:
            field_dict["planActions"] = plan_actions
        if cellular_actions is not UNSET:
            field_dict["cellularActions"] = cellular_actions
        if app_sub_actions is not UNSET:
            field_dict["appSubActions"] = app_sub_actions
        if app_meter_actions is not UNSET:
            field_dict["appMeterActions"] = app_meter_actions
        if misc_actions is not UNSET:
            field_dict["miscActions"] = misc_actions
        if revenue_actions is not UNSET:
            field_dict["revenueActions"] = revenue_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_meter_action import AppMeterAction
        from ..models.app_sub_action import AppSubAction
        from ..models.cellular_action import CellularAction
        from ..models.misc_action import MiscAction
        from ..models.plan_action import PlanAction
        from ..models.revenue_action import RevenueAction

        d = dict(src_dict)
        plan_actions = []
        _plan_actions = d.pop("planActions", UNSET)
        for plan_actions_item_data in _plan_actions or []:
            plan_actions_item = PlanAction.from_dict(plan_actions_item_data)

            plan_actions.append(plan_actions_item)

        cellular_actions = []
        _cellular_actions = d.pop("cellularActions", UNSET)
        for cellular_actions_item_data in _cellular_actions or []:
            cellular_actions_item = CellularAction.from_dict(cellular_actions_item_data)

            cellular_actions.append(cellular_actions_item)

        app_sub_actions = []
        _app_sub_actions = d.pop("appSubActions", UNSET)
        for app_sub_actions_item_data in _app_sub_actions or []:
            app_sub_actions_item = AppSubAction.from_dict(app_sub_actions_item_data)

            app_sub_actions.append(app_sub_actions_item)

        app_meter_actions = []
        _app_meter_actions = d.pop("appMeterActions", UNSET)
        for app_meter_actions_item_data in _app_meter_actions or []:
            app_meter_actions_item = AppMeterAction.from_dict(app_meter_actions_item_data)

            app_meter_actions.append(app_meter_actions_item)

        misc_actions = []
        _misc_actions = d.pop("miscActions", UNSET)
        for misc_actions_item_data in _misc_actions or []:
            misc_actions_item = MiscAction.from_dict(misc_actions_item_data)

            misc_actions.append(misc_actions_item)

        revenue_actions = []
        _revenue_actions = d.pop("revenueActions", UNSET)
        for revenue_actions_item_data in _revenue_actions or []:
            revenue_actions_item = RevenueAction.from_dict(revenue_actions_item_data)

            revenue_actions.append(revenue_actions_item)

        actions = cls(
            plan_actions=plan_actions,
            cellular_actions=cellular_actions,
            app_sub_actions=app_sub_actions,
            app_meter_actions=app_meter_actions,
            misc_actions=misc_actions,
            revenue_actions=revenue_actions,
        )

        actions.additional_properties = d
        return actions

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
