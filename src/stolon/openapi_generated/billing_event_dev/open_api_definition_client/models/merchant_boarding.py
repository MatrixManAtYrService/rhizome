from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerchantBoarding")


@_attrs_define
class MerchantBoarding:
    """
    Attributes:
        id (Union[Unset, str]):
        account_status (Union[Unset, str]):
        seasonal (Union[Unset, bool]):
        tax_exempt (Union[Unset, bool]):
        created_time (Union[Unset, int]):
        modified_time (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    account_status: Union[Unset, str] = UNSET
    seasonal: Union[Unset, bool] = UNSET
    tax_exempt: Union[Unset, bool] = UNSET
    created_time: Union[Unset, int] = UNSET
    modified_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_status = self.account_status

        seasonal = self.seasonal

        tax_exempt = self.tax_exempt

        created_time = self.created_time

        modified_time = self.modified_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_status is not UNSET:
            field_dict["accountStatus"] = account_status
        if seasonal is not UNSET:
            field_dict["seasonal"] = seasonal
        if tax_exempt is not UNSET:
            field_dict["taxExempt"] = tax_exempt
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        account_status = d.pop("accountStatus", UNSET)

        seasonal = d.pop("seasonal", UNSET)

        tax_exempt = d.pop("taxExempt", UNSET)

        created_time = d.pop("createdTime", UNSET)

        modified_time = d.pop("modifiedTime", UNSET)

        merchant_boarding = cls(
            id=id,
            account_status=account_status,
            seasonal=seasonal,
            tax_exempt=tax_exempt,
            created_time=created_time,
            modified_time=modified_time,
        )

        merchant_boarding.additional_properties = d
        return merchant_boarding

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
