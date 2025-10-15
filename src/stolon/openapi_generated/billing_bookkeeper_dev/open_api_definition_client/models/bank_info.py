from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BankInfo")


@_attrs_define
class BankInfo:
    """
    Attributes:
        bank_account_last_four (Union[Unset, str]):
        dps_dda_guid (Union[Unset, str]):
        bank_account_region (Union[Unset, str]):
        account_type (Union[Unset, str]):
        banking_system (Union[Unset, str]):
        modified_time (Union[Unset, str]):
    """

    bank_account_last_four: Union[Unset, str] = UNSET
    dps_dda_guid: Union[Unset, str] = UNSET
    bank_account_region: Union[Unset, str] = UNSET
    account_type: Union[Unset, str] = UNSET
    banking_system: Union[Unset, str] = UNSET
    modified_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bank_account_last_four = self.bank_account_last_four

        dps_dda_guid = self.dps_dda_guid

        bank_account_region = self.bank_account_region

        account_type = self.account_type

        banking_system = self.banking_system

        modified_time = self.modified_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_account_last_four is not UNSET:
            field_dict["bankAccountLastFour"] = bank_account_last_four
        if dps_dda_guid is not UNSET:
            field_dict["dpsDdaGuid"] = dps_dda_guid
        if bank_account_region is not UNSET:
            field_dict["bankAccountRegion"] = bank_account_region
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if banking_system is not UNSET:
            field_dict["bankingSystem"] = banking_system
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bank_account_last_four = d.pop("bankAccountLastFour", UNSET)

        dps_dda_guid = d.pop("dpsDdaGuid", UNSET)

        bank_account_region = d.pop("bankAccountRegion", UNSET)

        account_type = d.pop("accountType", UNSET)

        banking_system = d.pop("bankingSystem", UNSET)

        modified_time = d.pop("modifiedTime", UNSET)

        bank_info = cls(
            bank_account_last_four=bank_account_last_four,
            dps_dda_guid=dps_dda_guid,
            bank_account_region=bank_account_region,
            account_type=account_type,
            banking_system=banking_system,
            modified_time=modified_time,
        )

        bank_info.additional_properties = d
        return bank_info

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
