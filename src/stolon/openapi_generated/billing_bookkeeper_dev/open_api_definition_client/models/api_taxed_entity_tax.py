import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_taxed_entity_tax_entity_type import ApiTaxedEntityTaxEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_product_tax import ApiProductTax


T = TypeVar("T", bound="ApiTaxedEntityTax")


@_attrs_define
class ApiTaxedEntityTax:
    """Collection of one or more entities that tax was calculated for.

    Attributes:
        billing_entity_uuid (Union[Unset, str]): The 26-character UUID of the EBB billing entity that the calculations
            are being done for.
        entity_uuid (Union[Unset, str]): The 13-character COS UUID of the actual entity that the tax calculations are
            being done for.
        entity_type (Union[Unset, ApiTaxedEntityTaxEntityType]):
        transaction_date (Union[Unset, datetime.date]): The date of the transaction being taxed; the date that the
            applied tax rates are effective. Example: 2020-12-31.
        products (Union[Unset, list['ApiProductTax']]): Collection of products and services that tax was calculated for.
    """

    billing_entity_uuid: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiTaxedEntityTaxEntityType] = UNSET
    transaction_date: Union[Unset, datetime.date] = UNSET
    products: Union[Unset, list["ApiProductTax"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_entity_uuid = self.billing_entity_uuid

        entity_uuid = self.entity_uuid

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if transaction_date is not UNSET:
            field_dict["transactionDate"] = transaction_date
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_product_tax import ApiProductTax

        d = dict(src_dict)
        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, ApiTaxedEntityTaxEntityType]
        if _entity_type and not isinstance(_entity_type, Unset):
            entity_type = ApiTaxedEntityTaxEntityType(_entity_type)

        else:
            entity_type = UNSET

        _transaction_date = d.pop("transactionDate", UNSET)
        transaction_date: Union[Unset, datetime.date]
        if _transaction_date and not isinstance(_transaction_date, Unset):
            transaction_date = isoparse(_transaction_date).date()

        else:
            transaction_date = UNSET

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = ApiProductTax.from_dict(products_item_data)

            products.append(products_item)

        api_taxed_entity_tax = cls(
            billing_entity_uuid=billing_entity_uuid,
            entity_uuid=entity_uuid,
            entity_type=entity_type,
            transaction_date=transaction_date,
            products=products,
        )

        api_taxed_entity_tax.additional_properties = d
        return api_taxed_entity_tax

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
