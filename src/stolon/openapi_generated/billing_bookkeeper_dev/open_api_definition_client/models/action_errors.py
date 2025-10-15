from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_meter_action_error import AppMeterActionError
    from ..models.app_sub_action_error import AppSubActionError
    from ..models.cellular_action_error import CellularActionError
    from ..models.misc_action_error import MiscActionError
    from ..models.plan_action_error import PlanActionError
    from ..models.revenue_action_error import RevenueActionError


T = TypeVar("T", bound="ActionErrors")


@_attrs_define
class ActionErrors:
    """
    Attributes:
        plan_action_errors (Union[Unset, list['PlanActionError']]):
        cellular_action_errors (Union[Unset, list['CellularActionError']]):
        app_sub_action_errors (Union[Unset, list['AppSubActionError']]):
        app_meter_action_errors (Union[Unset, list['AppMeterActionError']]):
        misc_action_errors (Union[Unset, list['MiscActionError']]):
        revenue_action_errors (Union[Unset, list['RevenueActionError']]):
    """

    plan_action_errors: Union[Unset, list["PlanActionError"]] = UNSET
    cellular_action_errors: Union[Unset, list["CellularActionError"]] = UNSET
    app_sub_action_errors: Union[Unset, list["AppSubActionError"]] = UNSET
    app_meter_action_errors: Union[Unset, list["AppMeterActionError"]] = UNSET
    misc_action_errors: Union[Unset, list["MiscActionError"]] = UNSET
    revenue_action_errors: Union[Unset, list["RevenueActionError"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_action_errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_action_errors, Unset):
            plan_action_errors = []
            for plan_action_errors_item_data in self.plan_action_errors:
                plan_action_errors_item = plan_action_errors_item_data.to_dict()
                plan_action_errors.append(plan_action_errors_item)

        cellular_action_errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cellular_action_errors, Unset):
            cellular_action_errors = []
            for cellular_action_errors_item_data in self.cellular_action_errors:
                cellular_action_errors_item = cellular_action_errors_item_data.to_dict()
                cellular_action_errors.append(cellular_action_errors_item)

        app_sub_action_errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_sub_action_errors, Unset):
            app_sub_action_errors = []
            for app_sub_action_errors_item_data in self.app_sub_action_errors:
                app_sub_action_errors_item = app_sub_action_errors_item_data.to_dict()
                app_sub_action_errors.append(app_sub_action_errors_item)

        app_meter_action_errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_meter_action_errors, Unset):
            app_meter_action_errors = []
            for app_meter_action_errors_item_data in self.app_meter_action_errors:
                app_meter_action_errors_item = app_meter_action_errors_item_data.to_dict()
                app_meter_action_errors.append(app_meter_action_errors_item)

        misc_action_errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.misc_action_errors, Unset):
            misc_action_errors = []
            for misc_action_errors_item_data in self.misc_action_errors:
                misc_action_errors_item = misc_action_errors_item_data.to_dict()
                misc_action_errors.append(misc_action_errors_item)

        revenue_action_errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revenue_action_errors, Unset):
            revenue_action_errors = []
            for revenue_action_errors_item_data in self.revenue_action_errors:
                revenue_action_errors_item = revenue_action_errors_item_data.to_dict()
                revenue_action_errors.append(revenue_action_errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_action_errors is not UNSET:
            field_dict["planActionErrors"] = plan_action_errors
        if cellular_action_errors is not UNSET:
            field_dict["cellularActionErrors"] = cellular_action_errors
        if app_sub_action_errors is not UNSET:
            field_dict["appSubActionErrors"] = app_sub_action_errors
        if app_meter_action_errors is not UNSET:
            field_dict["appMeterActionErrors"] = app_meter_action_errors
        if misc_action_errors is not UNSET:
            field_dict["miscActionErrors"] = misc_action_errors
        if revenue_action_errors is not UNSET:
            field_dict["revenueActionErrors"] = revenue_action_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_meter_action_error import AppMeterActionError
        from ..models.app_sub_action_error import AppSubActionError
        from ..models.cellular_action_error import CellularActionError
        from ..models.misc_action_error import MiscActionError
        from ..models.plan_action_error import PlanActionError
        from ..models.revenue_action_error import RevenueActionError

        d = dict(src_dict)
        plan_action_errors = []
        _plan_action_errors = d.pop("planActionErrors", UNSET)
        for plan_action_errors_item_data in _plan_action_errors or []:
            plan_action_errors_item = PlanActionError.from_dict(plan_action_errors_item_data)

            plan_action_errors.append(plan_action_errors_item)

        cellular_action_errors = []
        _cellular_action_errors = d.pop("cellularActionErrors", UNSET)
        for cellular_action_errors_item_data in _cellular_action_errors or []:
            cellular_action_errors_item = CellularActionError.from_dict(cellular_action_errors_item_data)

            cellular_action_errors.append(cellular_action_errors_item)

        app_sub_action_errors = []
        _app_sub_action_errors = d.pop("appSubActionErrors", UNSET)
        for app_sub_action_errors_item_data in _app_sub_action_errors or []:
            app_sub_action_errors_item = AppSubActionError.from_dict(app_sub_action_errors_item_data)

            app_sub_action_errors.append(app_sub_action_errors_item)

        app_meter_action_errors = []
        _app_meter_action_errors = d.pop("appMeterActionErrors", UNSET)
        for app_meter_action_errors_item_data in _app_meter_action_errors or []:
            app_meter_action_errors_item = AppMeterActionError.from_dict(app_meter_action_errors_item_data)

            app_meter_action_errors.append(app_meter_action_errors_item)

        misc_action_errors = []
        _misc_action_errors = d.pop("miscActionErrors", UNSET)
        for misc_action_errors_item_data in _misc_action_errors or []:
            misc_action_errors_item = MiscActionError.from_dict(misc_action_errors_item_data)

            misc_action_errors.append(misc_action_errors_item)

        revenue_action_errors = []
        _revenue_action_errors = d.pop("revenueActionErrors", UNSET)
        for revenue_action_errors_item_data in _revenue_action_errors or []:
            revenue_action_errors_item = RevenueActionError.from_dict(revenue_action_errors_item_data)

            revenue_action_errors.append(revenue_action_errors_item)

        action_errors = cls(
            plan_action_errors=plan_action_errors,
            cellular_action_errors=cellular_action_errors,
            app_sub_action_errors=app_sub_action_errors,
            app_meter_action_errors=app_meter_action_errors,
            misc_action_errors=misc_action_errors,
            revenue_action_errors=revenue_action_errors,
        )

        action_errors.additional_properties = d
        return action_errors

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
