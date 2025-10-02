from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tender")


@_attrs_define
class Tender:
    """The tender type associated with this payment, e.g. credit card, cash, etc.

    Attributes:
        id (Union[Unset, str]): UUID for the tender type associated with the payment
        editable (Union[Unset, bool]): Indicates whether this merchant tender is editable
        label_key (Union[Unset, str]): I18n key for the label for this merchant tender
        label (Union[Unset, str]): Label value
        opens_cash_drawer (Union[Unset, bool]): Indicates whether this tender opens the cash drawer
        supports_tipping (Union[Unset, bool]): Indicates whether tipping is allowed on payment from tender
        enabled (Union[Unset, bool]): Indicates whether the merchant tender is enabled
        visible (Union[Unset, bool]): Indicates whether the merchant tender is visible
        instructions (Union[Unset, str]): Instructions
    """

    id: Union[Unset, str] = UNSET
    editable: Union[Unset, bool] = UNSET
    label_key: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    opens_cash_drawer: Union[Unset, bool] = UNSET
    supports_tipping: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    visible: Union[Unset, bool] = UNSET
    instructions: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        editable = self.editable

        label_key = self.label_key

        label = self.label

        opens_cash_drawer = self.opens_cash_drawer

        supports_tipping = self.supports_tipping

        enabled = self.enabled

        visible = self.visible

        instructions = self.instructions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if editable is not UNSET:
            field_dict["editable"] = editable
        if label_key is not UNSET:
            field_dict["labelKey"] = label_key
        if label is not UNSET:
            field_dict["label"] = label
        if opens_cash_drawer is not UNSET:
            field_dict["opensCashDrawer"] = opens_cash_drawer
        if supports_tipping is not UNSET:
            field_dict["supportsTipping"] = supports_tipping
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if visible is not UNSET:
            field_dict["visible"] = visible
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        editable = d.pop("editable", UNSET)

        label_key = d.pop("labelKey", UNSET)

        label = d.pop("label", UNSET)

        opens_cash_drawer = d.pop("opensCashDrawer", UNSET)

        supports_tipping = d.pop("supportsTipping", UNSET)

        enabled = d.pop("enabled", UNSET)

        visible = d.pop("visible", UNSET)

        instructions = d.pop("instructions", UNSET)

        tender = cls(
            id=id,
            editable=editable,
            label_key=label_key,
            label=label,
            opens_cash_drawer=opens_cash_drawer,
            supports_tipping=supports_tipping,
            enabled=enabled,
            visible=visible,
            instructions=instructions,
        )

        tender.additional_properties = d
        return tender

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
