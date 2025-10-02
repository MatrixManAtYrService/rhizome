import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMiscEvent")


@_attrs_define
class ApiMiscEvent:
    """miscellaneous events

    Attributes:
        code (Union[Unset, str]): miscellaneous event code
        effective_date_time (Union[Unset, datetime.datetime]): date and time that the event is effective Example:
            2020-12-31T23:59:59.123456Z.
        entity_uuid (Union[Unset, str]): 13-character UUID assigned to the entity
        specifier (Union[Unset, str]): uniquely specifies the subtype of misc event
        ref (Union[Unset, str]): reference
        num_units (Union[Unset, int]): the number of billable units
        basis_units (Union[Unset, int]): the number of basis units
        basis_amt (Union[Unset, float]): the basis amount
        basis_currency (Union[Unset, str]): 3-letter currency code Example: USD.
    """

    code: Union[Unset, str] = UNSET
    effective_date_time: Union[Unset, datetime.datetime] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    specifier: Union[Unset, str] = UNSET
    ref: Union[Unset, str] = UNSET
    num_units: Union[Unset, int] = UNSET
    basis_units: Union[Unset, int] = UNSET
    basis_amt: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        effective_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date_time, Unset):
            effective_date_time = self.effective_date_time.isoformat()

        entity_uuid = self.entity_uuid

        specifier = self.specifier

        ref = self.ref

        num_units = self.num_units

        basis_units = self.basis_units

        basis_amt = self.basis_amt

        basis_currency = self.basis_currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if effective_date_time is not UNSET:
            field_dict["effectiveDateTime"] = effective_date_time
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if specifier is not UNSET:
            field_dict["specifier"] = specifier
        if ref is not UNSET:
            field_dict["ref"] = ref
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units
        if basis_units is not UNSET:
            field_dict["basisUnits"] = basis_units
        if basis_amt is not UNSET:
            field_dict["basisAmt"] = basis_amt
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _effective_date_time = d.pop("effectiveDateTime", UNSET)
        effective_date_time: Union[Unset, datetime.datetime]
        if isinstance(_effective_date_time, Unset):
            effective_date_time = UNSET
        else:
            effective_date_time = isoparse(_effective_date_time)

        entity_uuid = d.pop("entityUuid", UNSET)

        specifier = d.pop("specifier", UNSET)

        ref = d.pop("ref", UNSET)

        num_units = d.pop("numUnits", UNSET)

        basis_units = d.pop("basisUnits", UNSET)

        basis_amt = d.pop("basisAmt", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        api_misc_event = cls(
            code=code,
            effective_date_time=effective_date_time,
            entity_uuid=entity_uuid,
            specifier=specifier,
            ref=ref,
            num_units=num_units,
            basis_units=basis_units,
            basis_amt=basis_amt,
            basis_currency=basis_currency,
        )

        api_misc_event.additional_properties = d
        return api_misc_event

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
