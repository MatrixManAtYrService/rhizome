import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_plan_price import ApiPlanPrice
    from ..models.api_tax_rates import ApiTaxRates


T = TypeVar("T", bound="ApiPlanPricing")


@_attrs_define
class ApiPlanPricing:
    """
    Attributes:
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the plan pricing applies
            for
        reseller_uuid (Union[Unset, str]): optional 13-character UUID of the reseller that the plan pricing is for
        merchant_uuid (Union[Unset, str]): optional 13-character UUID of the merchant that the plan pricing is for
        currency (Union[Unset, str]): 3-letter currency code for the currency that applies to all plan pricing monetary
            amounts Example: USD.
        as_of_date (Union[Unset, datetime.date]): the as-of date for the pricing quotes
        tax_rates (Union[Unset, ApiTaxRates]):
        plan_billing_method (Union[Unset, str]): method used to bill for plan SaaS fees
        plans (Union[Unset, list['ApiPlanPrice']]): collection of plans and their pricing quotes
    """

    billing_entity_uuid: Union[Unset, str] = UNSET
    reseller_uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    as_of_date: Union[Unset, datetime.date] = UNSET
    tax_rates: Union[Unset, "ApiTaxRates"] = UNSET
    plan_billing_method: Union[Unset, str] = UNSET
    plans: Union[Unset, list["ApiPlanPrice"]] = UNSET
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

        plan_billing_method = self.plan_billing_method

        plans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plans, Unset):
            plans = []
            for plans_item_data in self.plans:
                plans_item = plans_item_data.to_dict()
                plans.append(plans_item)

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
        if plan_billing_method is not UNSET:
            field_dict["planBillingMethod"] = plan_billing_method
        if plans is not UNSET:
            field_dict["plans"] = plans

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_plan_price import ApiPlanPrice
        from ..models.api_tax_rates import ApiTaxRates

        d = dict(src_dict)
        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        reseller_uuid = d.pop("resellerUuid", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        currency = d.pop("currency", UNSET)

        _as_of_date = d.pop("asOfDate", UNSET)
        as_of_date: Union[Unset, datetime.date]
        if _as_of_date and not isinstance(_as_of_date, Unset):
            as_of_date = isoparse(_as_of_date).date()

        else:
            as_of_date = UNSET

        _tax_rates = d.pop("taxRates", UNSET)
        tax_rates: Union[Unset, ApiTaxRates]
        if _tax_rates and not isinstance(_tax_rates, Unset):
            tax_rates = ApiTaxRates.from_dict(_tax_rates)

        else:
            tax_rates = UNSET

        plan_billing_method = d.pop("planBillingMethod", UNSET)

        plans = []
        _plans = d.pop("plans", UNSET)
        for plans_item_data in _plans or []:
            plans_item = ApiPlanPrice.from_dict(plans_item_data)

            plans.append(plans_item)

        api_plan_pricing = cls(
            billing_entity_uuid=billing_entity_uuid,
            reseller_uuid=reseller_uuid,
            merchant_uuid=merchant_uuid,
            currency=currency,
            as_of_date=as_of_date,
            tax_rates=tax_rates,
            plan_billing_method=plan_billing_method,
            plans=plans,
        )

        api_plan_pricing.additional_properties = d
        return api_plan_pricing

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
