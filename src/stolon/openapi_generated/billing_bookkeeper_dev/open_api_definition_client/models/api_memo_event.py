import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_memo_event_properties import ApiMemoEventProperties


T = TypeVar("T", bound="ApiMemoEvent")


@_attrs_define
class ApiMemoEvent:
    """memo events used to report job progress and completion

    Attributes:
        heading (Union[Unset, str]): memo heading
        moment (Union[Unset, datetime.date]): date/time for the memo
        properties (Union[Unset, ApiMemoEventProperties]): collection of named values associated with the memo
    """

    heading: Union[Unset, str] = UNSET
    moment: Union[Unset, datetime.date] = UNSET
    properties: Union[Unset, "ApiMemoEventProperties"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        heading = self.heading

        moment: Union[Unset, str] = UNSET
        if not isinstance(self.moment, Unset):
            moment = self.moment.isoformat()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heading is not UNSET:
            field_dict["heading"] = heading
        if moment is not UNSET:
            field_dict["moment"] = moment
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_memo_event_properties import ApiMemoEventProperties

        d = dict(src_dict)
        heading = d.pop("heading", UNSET)

        _moment = d.pop("moment", UNSET)
        moment: Union[Unset, datetime.date]
        if _moment and not isinstance(_moment, Unset):
            moment = isoparse(_moment).date()

        else:
            moment = UNSET

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, ApiMemoEventProperties]
        if _properties and not isinstance(_properties, Unset):
            properties = ApiMemoEventProperties.from_dict(_properties)

        else:
            properties = UNSET

        api_memo_event = cls(
            heading=heading,
            moment=moment,
            properties=properties,
        )

        api_memo_event.additional_properties = d
        return api_memo_event

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
