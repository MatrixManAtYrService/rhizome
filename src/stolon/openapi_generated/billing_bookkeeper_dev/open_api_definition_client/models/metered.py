from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metered_countries import MeteredCountries


T = TypeVar("T", bound="Metered")


@_attrs_define
class Metered:
    """
    Attributes:
        id (Union[Unset, str]):
        label (Union[Unset, str]): App metered event label
        active (Union[Unset, bool]): True if the event is active
        metered_countries (Union[Unset, MeteredCountries]):
    """

    id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    metered_countries: Union[Unset, "MeteredCountries"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        active = self.active

        metered_countries: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metered_countries, Unset):
            metered_countries = self.metered_countries.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if active is not UNSET:
            field_dict["active"] = active
        if metered_countries is not UNSET:
            field_dict["meteredCountries"] = metered_countries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metered_countries import MeteredCountries

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        active = d.pop("active", UNSET)

        _metered_countries = d.pop("meteredCountries", UNSET)
        metered_countries: Union[Unset, MeteredCountries]
        if _metered_countries and not isinstance(_metered_countries, Unset):
            metered_countries = MeteredCountries.from_dict(_metered_countries)

        else:
            metered_countries = UNSET

        metered = cls(
            id=id,
            label=label,
            active=active,
            metered_countries=metered_countries,
        )

        metered.additional_properties = d
        return metered

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
