import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_carrier_price import ApiCarrierPrice
    from ..models.api_tax_rates import ApiTaxRates


T = TypeVar("T", bound="ApiCellularPricing")


@_attrs_define
class ApiCellularPricing:
    """
    Attributes:
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the cellular pricing
            applies for
        reseller_uuid (Union[Unset, str]): optional 13-character UUID of the reseller that the cellular pricing is for
        merchant_uuid (Union[Unset, str]): optional 13-character UUID of the merchant that the cellular pricing is for
        currency (Union[Unset, str]): 3-letter currency code for the currency that applies to all cellular pricing
            monetary amounts Example: USD.
        as_of_date (Union[Unset, datetime.date]): the as-of date for the pricing quotes
        tax_rates (Union[Unset, ApiTaxRates]):
        cellular_billing_method (Union[Unset, str]): method used to bill for cellular fees
        carriers (Union[Unset, list['ApiCarrierPrice']]): collection of pricing quotes by cellular carrier
    """

    billing_entity_uuid: Union[Unset, str] = UNSET
    reseller_uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    as_of_date: Union[Unset, datetime.date] = UNSET
    tax_rates: Union[Unset, "ApiTaxRates"] = UNSET
    cellular_billing_method: Union[Unset, str] = UNSET
    carriers: Union[Unset, list["ApiCarrierPrice"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_entity_uuid = self.billing_entity_uuid

        reseller_uuid = self.reseller_uuid

        merchant_uuid = self.merchant_uuid

        currency = self.currency

        as_of_date: Union[Unset, str] = UNSET
        if not isinstance(self.as_of_date, Unset):
            as_of_date = self.as_of_date.isoformat()

        tax_rates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_rates, Unset):
            tax_rates = self.tax_rates.to_dict()

        cellular_billing_method = self.cellular_billing_method

        carriers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.carriers, Unset):
            carriers = []
            for carriers_item_data in self.carriers:
                carriers_item = carriers_item_data.to_dict()
                carriers.append(carriers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if reseller_uuid is not UNSET:
            field_dict["resellerUuid"] = reseller_uuid
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if currency is not UNSET:
            field_dict["currency"] = currency
        if as_of_date is not UNSET:
            field_dict["asOfDate"] = as_of_date
        if tax_rates is not UNSET:
            field_dict["taxRates"] = tax_rates
        if cellular_billing_method is not UNSET:
            field_dict["cellularBillingMethod"] = cellular_billing_method
        if carriers is not UNSET:
            field_dict["carriers"] = carriers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_carrier_price import ApiCarrierPrice
        from ..models.api_tax_rates import ApiTaxRates

        d = dict(src_dict)
        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        reseller_uuid = d.pop("resellerUuid", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        currency = d.pop("currency", UNSET)

        _as_of_date = d.pop("asOfDate", UNSET)
        as_of_date: Union[Unset, datetime.date]
        if isinstance(_as_of_date, Unset):
            as_of_date = UNSET
        else:
            as_of_date = isoparse(_as_of_date).date()

        _tax_rates = d.pop("taxRates", UNSET)
        tax_rates: Union[Unset, ApiTaxRates]
        if isinstance(_tax_rates, Unset):
            tax_rates = UNSET
        else:
            tax_rates = ApiTaxRates.from_dict(_tax_rates)

        cellular_billing_method = d.pop("cellularBillingMethod", UNSET)

        carriers = []
        _carriers = d.pop("carriers", UNSET)
        for carriers_item_data in _carriers or []:
            carriers_item = ApiCarrierPrice.from_dict(carriers_item_data)

            carriers.append(carriers_item)

        api_cellular_pricing = cls(
            billing_entity_uuid=billing_entity_uuid,
            reseller_uuid=reseller_uuid,
            merchant_uuid=merchant_uuid,
            currency=currency,
            as_of_date=as_of_date,
            tax_rates=tax_rates,
            cellular_billing_method=cellular_billing_method,
            carriers=carriers,
        )

        api_cellular_pricing.additional_properties = d
        return api_cellular_pricing

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
