from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acceptance_sort_sort_by import AcceptanceSortSortBy
from ..models.acceptance_sort_sort_direction import AcceptanceSortSortDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptanceSort")


@_attrs_define
class AcceptanceSort:
    """
    Attributes:
        sort_by (Union[Unset, AcceptanceSortSortBy]):
        sort_direction (Union[Unset, AcceptanceSortSortDirection]):
    """

    sort_by: Union[Unset, AcceptanceSortSortBy] = UNSET
    sort_direction: Union[Unset, AcceptanceSortSortDirection] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sort_by: Union[Unset, str] = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by.value

        sort_direction: Union[Unset, str] = UNSET
        if not isinstance(self.sort_direction, Unset):
            sort_direction = self.sort_direction.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if sort_direction is not UNSET:
            field_dict["sortDirection"] = sort_direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sort_by = d.pop("sortBy", UNSET)
        sort_by: Union[Unset, AcceptanceSortSortBy]
        if _sort_by and not isinstance(_sort_by, Unset):
            sort_by = AcceptanceSortSortBy(_sort_by)

        else:
            sort_by = UNSET

        _sort_direction = d.pop("sortDirection", UNSET)
        sort_direction: Union[Unset, AcceptanceSortSortDirection]
        if _sort_direction and not isinstance(_sort_direction, Unset):
            sort_direction = AcceptanceSortSortDirection(_sort_direction)

        else:
            sort_direction = UNSET

        acceptance_sort = cls(
            sort_by=sort_by,
            sort_direction=sort_direction,
        )

        acceptance_sort.additional_properties = d
        return acceptance_sort

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
