import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_cellular_modifier import ApiCellularModifier
    from ..models.api_sim import ApiSim


T = TypeVar("T", bound="ApiCellularEvent")


@_attrs_define
class ApiCellularEvent:
    """cellular events

    Attributes:
        code (Union[Unset, str]): cellular event code
        effective_date_time (Union[Unset, datetime.datetime]): date and time that the event is effective Example:
            2020-12-31T23:59:59.123456Z.
        merch_uuid (Union[Unset, str]): 13-character UUID assigned to the merchant
        merch_plan_uuid (Union[Unset, str]): 13-character UUID assigned to the merchant plan
        cellular_mods (Union[Unset, list['ApiCellularModifier']]): cellular event modifiers
        sims (Union[Unset, list['ApiSim']]): devices
    """

    code: Union[Unset, str] = UNSET
    effective_date_time: Union[Unset, datetime.datetime] = UNSET
    merch_uuid: Union[Unset, str] = UNSET
    merch_plan_uuid: Union[Unset, str] = UNSET
    cellular_mods: Union[Unset, list["ApiCellularModifier"]] = UNSET
    sims: Union[Unset, list["ApiSim"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        effective_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date_time, Unset):
            effective_date_time = self.effective_date_time.isoformat()

        merch_uuid = self.merch_uuid

        merch_plan_uuid = self.merch_plan_uuid

        cellular_mods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cellular_mods, Unset):
            cellular_mods = []
            for cellular_mods_item_data in self.cellular_mods:
                cellular_mods_item = cellular_mods_item_data.to_dict()
                cellular_mods.append(cellular_mods_item)

        sims: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sims, Unset):
            sims = []
            for sims_item_data in self.sims:
                sims_item = sims_item_data.to_dict()
                sims.append(sims_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if effective_date_time is not UNSET:
            field_dict["effectiveDateTime"] = effective_date_time
        if merch_uuid is not UNSET:
            field_dict["merchUuid"] = merch_uuid
        if merch_plan_uuid is not UNSET:
            field_dict["merchPlanUuid"] = merch_plan_uuid
        if cellular_mods is not UNSET:
            field_dict["cellularMods"] = cellular_mods
        if sims is not UNSET:
            field_dict["sims"] = sims

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_cellular_modifier import ApiCellularModifier
        from ..models.api_sim import ApiSim

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _effective_date_time = d.pop("effectiveDateTime", UNSET)
        effective_date_time: Union[Unset, datetime.datetime]
        if _effective_date_time and not isinstance(_effective_date_time, Unset):
            effective_date_time = isoparse(_effective_date_time)

        else:
            effective_date_time = UNSET

        merch_uuid = d.pop("merchUuid", UNSET)

        merch_plan_uuid = d.pop("merchPlanUuid", UNSET)

        cellular_mods = []
        _cellular_mods = d.pop("cellularMods", UNSET)
        for cellular_mods_item_data in _cellular_mods or []:
            cellular_mods_item = ApiCellularModifier.from_dict(cellular_mods_item_data)

            cellular_mods.append(cellular_mods_item)

        sims = []
        _sims = d.pop("sims", UNSET)
        for sims_item_data in _sims or []:
            sims_item = ApiSim.from_dict(sims_item_data)

            sims.append(sims_item)

        api_cellular_event = cls(
            code=code,
            effective_date_time=effective_date_time,
            merch_uuid=merch_uuid,
            merch_plan_uuid=merch_plan_uuid,
            cellular_mods=cellular_mods,
            sims=sims,
        )

        api_cellular_event.additional_properties = d
        return api_cellular_event

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
