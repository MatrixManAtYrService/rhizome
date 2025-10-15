from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="AdditionalChargeAmount")


@_attrs_define
class AdditionalChargeAmount:
    """
    Attributes:
        id (Union[Unset, str]): Clover UUID for the additional charge
        amount (Union[Unset, int]): Amount of the additional charge with 2 implied decimal places
        rate (Union[Unset, int]): Percent rate of the additional charge with 4 implied decimal places (1% = 10000)
        pretax (Union[Unset, bool]): True if this charge was applied pretax
        type_ (Union[Unset, str]): Type of additional charge
        payment (Union[Unset, Reference]):
        refund (Union[Unset, Reference]):
        incremental_auth (Union[Unset, Reference]):
    """

    id: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    rate: Union[Unset, int] = UNSET
    pretax: Union[Unset, bool] = UNSET
    type_: Union[Unset, str] = UNSET
    payment: Union[Unset, "Reference"] = UNSET
    refund: Union[Unset, "Reference"] = UNSET
    incremental_auth: Union[Unset, "Reference"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount = self.amount

        rate = self.rate

        pretax = self.pretax

        type_ = self.type_

        payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        refund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.refund, Unset):
            refund = self.refund.to_dict()

        incremental_auth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.incremental_auth, Unset):
            incremental_auth = self.incremental_auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if rate is not UNSET:
            field_dict["rate"] = rate
        if pretax is not UNSET:
            field_dict["pretax"] = pretax
        if type_ is not UNSET:
            field_dict["type"] = type_
        if payment is not UNSET:
            field_dict["payment"] = payment
        if refund is not UNSET:
            field_dict["refund"] = refund
        if incremental_auth is not UNSET:
            field_dict["incrementalAuth"] = incremental_auth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reference import Reference

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        rate = d.pop("rate", UNSET)

        pretax = d.pop("pretax", UNSET)

        type_ = d.pop("type", UNSET)

        _payment = d.pop("payment", UNSET)
        payment: Union[Unset, Reference]
        if _payment and not isinstance(_payment, Unset):
            payment = Reference.from_dict(_payment)

        else:
            payment = UNSET

        _refund = d.pop("refund", UNSET)
        refund: Union[Unset, Reference]
        if _refund and not isinstance(_refund, Unset):
            refund = Reference.from_dict(_refund)

        else:
            refund = UNSET

        _incremental_auth = d.pop("incrementalAuth", UNSET)
        incremental_auth: Union[Unset, Reference]
        if _incremental_auth and not isinstance(_incremental_auth, Unset):
            incremental_auth = Reference.from_dict(_incremental_auth)

        else:
            incremental_auth = UNSET

        additional_charge_amount = cls(
            id=id,
            amount=amount,
            rate=rate,
            pretax=pretax,
            type_=type_,
            payment=payment,
            refund=refund,
            incremental_auth=incremental_auth,
        )

        additional_charge_amount.additional_properties = d
        return additional_charge_amount

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
