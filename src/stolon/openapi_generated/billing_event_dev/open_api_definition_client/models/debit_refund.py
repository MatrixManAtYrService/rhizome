from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DebitRefund")


@_attrs_define
class DebitRefund:
    """Vaulted card which can be used for subsequent transactions

    Attributes:
        debit_transaction_route_ind (Union[Unset, str]): Route that the payment transaction took, which is obtained from
            the RC response
        is_debit_transaction_refundable (Union[Unset, bool]): True, if debitTransactionRouteInd is C, else, its
            determined by the EDS entitlement rule for D/S
    """

    debit_transaction_route_ind: Union[Unset, str] = UNSET
    is_debit_transaction_refundable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debit_transaction_route_ind = self.debit_transaction_route_ind

        is_debit_transaction_refundable = self.is_debit_transaction_refundable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if debit_transaction_route_ind is not UNSET:
            field_dict["debitTransactionRouteInd"] = debit_transaction_route_ind
        if is_debit_transaction_refundable is not UNSET:
            field_dict["isDebitTransactionRefundable"] = is_debit_transaction_refundable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        debit_transaction_route_ind = d.pop("debitTransactionRouteInd", UNSET)

        is_debit_transaction_refundable = d.pop("isDebitTransactionRefundable", UNSET)

        debit_refund = cls(
            debit_transaction_route_ind=debit_transaction_route_ind,
            is_debit_transaction_refundable=is_debit_transaction_refundable,
        )

        debit_refund.additional_properties = d
        return debit_refund

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
