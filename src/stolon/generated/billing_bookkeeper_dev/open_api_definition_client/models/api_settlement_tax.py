from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSettlementTax")


@_attrs_define
class ApiSettlementTax:
    """
    Attributes:
        uuid (Union[Unset, str]): 26-character UUID of the settlement request
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the settlement request is
            for
        currency (Union[Unset, str]): the currency of the settlement request amount Example: USD.
        total_amount (Union[Unset, float]): the total amount being settled by the settlement request
        fee_amount (Union[Unset, float]): the portion of the total settlement amount that is for fees
        tax_1_amount (Union[Unset, float]): the portion of the total settlement amount that is for tax 1, typically
            Federal tax, GST, or VAT
        tax_2_amount (Union[Unset, float]): the portion of the total settlement amount that is for tax 2, typically
            state or province tax
        tax_3_amount (Union[Unset, float]): the portion of the total settlement amount that is for tax 3, typically
            county tax
        tax_4_amount (Union[Unset, float]): the portion of the total settlement amount that is for tax 4, typically city
            or local tax
    """

    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    fee_amount: Union[Unset, float] = UNSET
    tax_1_amount: Union[Unset, float] = UNSET
    tax_2_amount: Union[Unset, float] = UNSET
    tax_3_amount: Union[Unset, float] = UNSET
    tax_4_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        currency = self.currency

        total_amount = self.total_amount

        fee_amount = self.fee_amount

        tax_1_amount = self.tax_1_amount

        tax_2_amount = self.tax_2_amount

        tax_3_amount = self.tax_3_amount

        tax_4_amount = self.tax_4_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if fee_amount is not UNSET:
            field_dict["feeAmount"] = fee_amount
        if tax_1_amount is not UNSET:
            field_dict["tax1Amount"] = tax_1_amount
        if tax_2_amount is not UNSET:
            field_dict["tax2Amount"] = tax_2_amount
        if tax_3_amount is not UNSET:
            field_dict["tax3Amount"] = tax_3_amount
        if tax_4_amount is not UNSET:
            field_dict["tax4Amount"] = tax_4_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        currency = d.pop("currency", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        fee_amount = d.pop("feeAmount", UNSET)

        tax_1_amount = d.pop("tax1Amount", UNSET)

        tax_2_amount = d.pop("tax2Amount", UNSET)

        tax_3_amount = d.pop("tax3Amount", UNSET)

        tax_4_amount = d.pop("tax4Amount", UNSET)

        api_settlement_tax = cls(
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            currency=currency,
            total_amount=total_amount,
            fee_amount=fee_amount,
            tax_1_amount=tax_1_amount,
            tax_2_amount=tax_2_amount,
            tax_3_amount=tax_3_amount,
            tax_4_amount=tax_4_amount,
        )

        api_settlement_tax.additional_properties = d
        return api_settlement_tax

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
