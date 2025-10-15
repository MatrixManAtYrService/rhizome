from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_sim_modifier import ApiSimModifier


T = TypeVar("T", bound="ApiSim")


@_attrs_define
class ApiSim:
    """devices

    Attributes:
        iccid (Union[Unset, str]): integrated circuit card identifier
        carrier (Union[Unset, str]): cellular carrier or service provider
        sim_mods (Union[Unset, list['ApiSimModifier']]): SIM modifiers
    """

    iccid: Union[Unset, str] = UNSET
    carrier: Union[Unset, str] = UNSET
    sim_mods: Union[Unset, list["ApiSimModifier"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iccid = self.iccid

        carrier = self.carrier

        sim_mods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sim_mods, Unset):
            sim_mods = []
            for sim_mods_item_data in self.sim_mods:
                sim_mods_item = sim_mods_item_data.to_dict()
                sim_mods.append(sim_mods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iccid is not UNSET:
            field_dict["iccid"] = iccid
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if sim_mods is not UNSET:
            field_dict["simMods"] = sim_mods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_sim_modifier import ApiSimModifier

        d = dict(src_dict)
        iccid = d.pop("iccid", UNSET)

        carrier = d.pop("carrier", UNSET)

        sim_mods = []
        _sim_mods = d.pop("simMods", UNSET)
        for sim_mods_item_data in _sim_mods or []:
            sim_mods_item = ApiSimModifier.from_dict(sim_mods_item_data)

            sim_mods.append(sim_mods_item)

        api_sim = cls(
            iccid=iccid,
            carrier=carrier,
            sim_mods=sim_mods,
        )

        api_sim.additional_properties = d
        return api_sim

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
