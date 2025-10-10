import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_app_sub_modifier import ApiAppSubModifier


T = TypeVar("T", bound="ApiAppSubEvent")


@_attrs_define
class ApiAppSubEvent:
    """app subscription events

    Attributes:
        code (Union[Unset, str]): app subscription event code
        effective_date_time (Union[Unset, datetime.datetime]): date and time that the event is effective Example:
            2020-12-31T23:59:59.123456Z.
        merch_uuid (Union[Unset, str]): 13-character UUID assigned to the merchant
        dev_app_uuid (Union[Unset, str]): 13-character UUID assigned to the developer app
        app_sub_uuid (Union[Unset, str]): 13-character UUID assigned to the app subscription level
        merch_plan_uuid (Union[Unset, str]): 13-character UUID assigned to the merchant plan
        num_units (Union[Unset, int]): the number of billable units
        basis_units (Union[Unset, int]): the number of basis units
        basis_amt (Union[Unset, float]): the basis amount
        basis_currency (Union[Unset, str]): 3-letter currency code Example: USD.
        app_sub_mods (Union[Unset, list['ApiAppSubModifier']]): app subscription event modifiers
    """

    code: Union[Unset, str] = UNSET
    effective_date_time: Union[Unset, datetime.datetime] = UNSET
    merch_uuid: Union[Unset, str] = UNSET
    dev_app_uuid: Union[Unset, str] = UNSET
    app_sub_uuid: Union[Unset, str] = UNSET
    merch_plan_uuid: Union[Unset, str] = UNSET
    num_units: Union[Unset, int] = UNSET
    basis_units: Union[Unset, int] = UNSET
    basis_amt: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    app_sub_mods: Union[Unset, list["ApiAppSubModifier"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        effective_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date_time, Unset):
            effective_date_time = self.effective_date_time.isoformat()

        merch_uuid = self.merch_uuid

        dev_app_uuid = self.dev_app_uuid

        app_sub_uuid = self.app_sub_uuid

        merch_plan_uuid = self.merch_plan_uuid

        num_units = self.num_units

        basis_units = self.basis_units

        basis_amt = self.basis_amt

        basis_currency = self.basis_currency

        app_sub_mods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_sub_mods, Unset):
            app_sub_mods = []
            for app_sub_mods_item_data in self.app_sub_mods:
                app_sub_mods_item = app_sub_mods_item_data.to_dict()
                app_sub_mods.append(app_sub_mods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if effective_date_time is not UNSET:
            field_dict["effectiveDateTime"] = effective_date_time
        if merch_uuid is not UNSET:
            field_dict["merchUuid"] = merch_uuid
        if dev_app_uuid is not UNSET:
            field_dict["devAppUuid"] = dev_app_uuid
        if app_sub_uuid is not UNSET:
            field_dict["appSubUuid"] = app_sub_uuid
        if merch_plan_uuid is not UNSET:
            field_dict["merchPlanUuid"] = merch_plan_uuid
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units
        if basis_units is not UNSET:
            field_dict["basisUnits"] = basis_units
        if basis_amt is not UNSET:
            field_dict["basisAmt"] = basis_amt
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency
        if app_sub_mods is not UNSET:
            field_dict["appSubMods"] = app_sub_mods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_app_sub_modifier import ApiAppSubModifier

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _effective_date_time = d.pop("effectiveDateTime", UNSET)
        effective_date_time: Union[Unset, datetime.datetime]
        if _effective_date_time and not isinstance(_effective_date_time, Unset):
            effective_date_time = isoparse(_effective_date_time)

        else:
            effective_date_time = UNSET

        merch_uuid = d.pop("merchUuid", UNSET)

        dev_app_uuid = d.pop("devAppUuid", UNSET)

        app_sub_uuid = d.pop("appSubUuid", UNSET)

        merch_plan_uuid = d.pop("merchPlanUuid", UNSET)

        num_units = d.pop("numUnits", UNSET)

        basis_units = d.pop("basisUnits", UNSET)

        basis_amt = d.pop("basisAmt", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        app_sub_mods = []
        _app_sub_mods = d.pop("appSubMods", UNSET)
        for app_sub_mods_item_data in _app_sub_mods or []:
            app_sub_mods_item = ApiAppSubModifier.from_dict(app_sub_mods_item_data)

            app_sub_mods.append(app_sub_mods_item)

        api_app_sub_event = cls(
            code=code,
            effective_date_time=effective_date_time,
            merch_uuid=merch_uuid,
            dev_app_uuid=dev_app_uuid,
            app_sub_uuid=app_sub_uuid,
            merch_plan_uuid=merch_plan_uuid,
            num_units=num_units,
            basis_units=basis_units,
            basis_amt=basis_amt,
            basis_currency=basis_currency,
            app_sub_mods=app_sub_mods,
        )

        api_app_sub_event.additional_properties = d
        return api_app_sub_event

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
