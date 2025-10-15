from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EbbMerchantBoarding")


@_attrs_define
class EbbMerchantBoarding:
    """
    Attributes:
        database_id (Union[Unset, int]):
        seasonal (Union[Unset, bool]):
        account_status (Union[Unset, str]):
        tax_exempt (Union[Unset, bool]):
    """

    database_id: Union[Unset, int] = UNSET
    seasonal: Union[Unset, bool] = UNSET
    account_status: Union[Unset, str] = UNSET
    tax_exempt: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_id = self.database_id

        seasonal = self.seasonal

        account_status = self.account_status

        tax_exempt = self.tax_exempt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_id is not UNSET:
            field_dict["databaseId"] = database_id
        if seasonal is not UNSET:
            field_dict["seasonal"] = seasonal
        if account_status is not UNSET:
            field_dict["accountStatus"] = account_status
        if tax_exempt is not UNSET:
            field_dict["taxExempt"] = tax_exempt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database_id = d.pop("databaseId", UNSET)

        seasonal = d.pop("seasonal", UNSET)

        account_status = d.pop("accountStatus", UNSET)

        tax_exempt = d.pop("taxExempt", UNSET)

        ebb_merchant_boarding = cls(
            database_id=database_id,
            seasonal=seasonal,
            account_status=account_status,
            tax_exempt=tax_exempt,
        )

        ebb_merchant_boarding.additional_properties = d
        return ebb_merchant_boarding

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
