from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference import Reference


T = TypeVar("T", bound="ServiceCharge")


@_attrs_define
class ServiceCharge:
    """Amount recorded as a service charge

    Attributes:
        id (Union[Unset, str]): Clover UUID
        name (Union[Unset, str]): Refund with which the card transaction is associated
        amount (Union[Unset, int]): Service charge amount with 2 implied decimal places
        payment_ref (Union[Unset, Reference]):
        refund_ref (Union[Unset, Reference]):
        percentage (Union[Unset, int]): Percentage of the service charge with 4 implied decimal places (1% = 10000)
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    payment_ref: Union[Unset, "Reference"] = UNSET
    refund_ref: Union[Unset, "Reference"] = UNSET
    percentage: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        amount = self.amount

        payment_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_ref, Unset):
            payment_ref = self.payment_ref.to_dict()

        refund_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.refund_ref, Unset):
            refund_ref = self.refund_ref.to_dict()

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payment_ref is not UNSET:
            field_dict["paymentRef"] = payment_ref
        if refund_ref is not UNSET:
            field_dict["refundRef"] = refund_ref
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reference import Reference

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        amount = d.pop("amount", UNSET)

        _payment_ref = d.pop("paymentRef", UNSET)
        payment_ref: Union[Unset, Reference]
        if isinstance(_payment_ref, Unset):
            payment_ref = UNSET
        else:
            payment_ref = Reference.from_dict(_payment_ref)

        _refund_ref = d.pop("refundRef", UNSET)
        refund_ref: Union[Unset, Reference]
        if isinstance(_refund_ref, Unset):
            refund_ref = UNSET
        else:
            refund_ref = Reference.from_dict(_refund_ref)

        percentage = d.pop("percentage", UNSET)

        service_charge = cls(
            id=id,
            name=name,
            amount=amount,
            payment_ref=payment_ref,
            refund_ref=refund_ref,
            percentage=percentage,
        )

        service_charge.additional_properties = d
        return service_charge

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
