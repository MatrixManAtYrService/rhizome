import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_billing_entity_config import ApiBillingEntityConfig


T = TypeVar("T", bound="ApiResolvedBillingEntityConfig")


@_attrs_define
class ApiResolvedBillingEntityConfig:
    """
    Attributes:
        tlement_method_be_uuid (Union[Unset, ApiResolvedBillingEntityConfig]):
        tlement_method (Union[Unset, ApiResolvedBillingEntityConfig]):
        billing_entity_config (Union[Unset, ApiBillingEntityConfig]):
        as_of_date (Union[Unset, datetime.date]): the as-of date for the configuration
        revenue_share_group (Union[Unset, str]): group that the billing entity's partner belongs to for revenue share
            splits
        revenue_share_group_be_uuid (Union[Unset, str]): UUID of the billing entity that provided the resolved revenue
            share group value
        post_method (Union[Unset, str]): method used to post actions
        post_method_be_uuid (Union[Unset, str]): UUID of the billing entity that provided the resolved post method value
        plan_billing_method (Union[Unset, str]): method used to bill for plan fees
        plan_billing_method_be_uuid (Union[Unset, str]): UUID of the billing entity that provided the resolved plan
            billing method value
        invoice_method (Union[Unset, str]): method used to produce invoice
        invoice_method_be_uuid (Union[Unset, str]): UUID of the billing entity that provided the resolved invoice method
            value
        invoice_number_format (Union[Unset, str]): format used for invoice number
        invoice_number_format_be_uuid (Union[Unset, str]): UUID of the billing entity that provided the resolved invoice
            number format value
        settlement_method (Union[Unset, str]): method used to settle
        settlement_method_be_uuid (Union[Unset, str]): UUID of the billing entity that provided the resolved settlement
            method value
        seasonal_rule_set_uuid (Union[Unset, str]): UUID of the monetary rule set used to apply seasonal processing
            rules
        seasonal_rule_set_uuid_be_uuid (Union[Unset, str]): UUID of the billing entity that provided the resolved
            seasonal rule set UUID value
    """

    tlement_method_be_uuid: Union[Unset, "ApiResolvedBillingEntityConfig"] = UNSET
    tlement_method: Union[Unset, "ApiResolvedBillingEntityConfig"] = UNSET
    billing_entity_config: Union[Unset, "ApiBillingEntityConfig"] = UNSET
    as_of_date: Union[Unset, datetime.date] = UNSET
    revenue_share_group: Union[Unset, str] = UNSET
    revenue_share_group_be_uuid: Union[Unset, str] = UNSET
    post_method: Union[Unset, str] = UNSET
    post_method_be_uuid: Union[Unset, str] = UNSET
    plan_billing_method: Union[Unset, str] = UNSET
    plan_billing_method_be_uuid: Union[Unset, str] = UNSET
    invoice_method: Union[Unset, str] = UNSET
    invoice_method_be_uuid: Union[Unset, str] = UNSET
    invoice_number_format: Union[Unset, str] = UNSET
    invoice_number_format_be_uuid: Union[Unset, str] = UNSET
    settlement_method: Union[Unset, str] = UNSET
    settlement_method_be_uuid: Union[Unset, str] = UNSET
    seasonal_rule_set_uuid: Union[Unset, str] = UNSET
    seasonal_rule_set_uuid_be_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlement_method_be_uuid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_method_be_uuid, Unset):
            tlement_method_be_uuid = self.tlement_method_be_uuid.to_dict()

        tlement_method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_method, Unset):
            tlement_method = self.tlement_method.to_dict()

        billing_entity_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_entity_config, Unset):
            billing_entity_config = self.billing_entity_config.to_dict()

        as_of_date: Union[Unset, str] = UNSET
        if not isinstance(self.as_of_date, Unset):
            as_of_date = self.as_of_date.isoformat()

        revenue_share_group = self.revenue_share_group

        revenue_share_group_be_uuid = self.revenue_share_group_be_uuid

        post_method = self.post_method

        post_method_be_uuid = self.post_method_be_uuid

        plan_billing_method = self.plan_billing_method

        plan_billing_method_be_uuid = self.plan_billing_method_be_uuid

        invoice_method = self.invoice_method

        invoice_method_be_uuid = self.invoice_method_be_uuid

        invoice_number_format = self.invoice_number_format

        invoice_number_format_be_uuid = self.invoice_number_format_be_uuid

        settlement_method = self.settlement_method

        settlement_method_be_uuid = self.settlement_method_be_uuid

        seasonal_rule_set_uuid = self.seasonal_rule_set_uuid

        seasonal_rule_set_uuid_be_uuid = self.seasonal_rule_set_uuid_be_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tlement_method_be_uuid is not UNSET:
            field_dict["tlementMethodBeUuid"] = tlement_method_be_uuid
        if tlement_method is not UNSET:
            field_dict["tlementMethod"] = tlement_method
        if billing_entity_config is not UNSET:
            field_dict["billingEntityConfig"] = billing_entity_config
        if as_of_date is not UNSET:
            field_dict["asOfDate"] = as_of_date
        if revenue_share_group is not UNSET:
            field_dict["revenueShareGroup"] = revenue_share_group
        if revenue_share_group_be_uuid is not UNSET:
            field_dict["revenueShareGroupBeUuid"] = revenue_share_group_be_uuid
        if post_method is not UNSET:
            field_dict["postMethod"] = post_method
        if post_method_be_uuid is not UNSET:
            field_dict["postMethodBeUuid"] = post_method_be_uuid
        if plan_billing_method is not UNSET:
            field_dict["planBillingMethod"] = plan_billing_method
        if plan_billing_method_be_uuid is not UNSET:
            field_dict["planBillingMethodBeUuid"] = plan_billing_method_be_uuid
        if invoice_method is not UNSET:
            field_dict["invoiceMethod"] = invoice_method
        if invoice_method_be_uuid is not UNSET:
            field_dict["invoiceMethodBeUuid"] = invoice_method_be_uuid
        if invoice_number_format is not UNSET:
            field_dict["invoiceNumberFormat"] = invoice_number_format
        if invoice_number_format_be_uuid is not UNSET:
            field_dict["invoiceNumberFormatBeUuid"] = invoice_number_format_be_uuid
        if settlement_method is not UNSET:
            field_dict["settlementMethod"] = settlement_method
        if settlement_method_be_uuid is not UNSET:
            field_dict["settlementMethodBeUuid"] = settlement_method_be_uuid
        if seasonal_rule_set_uuid is not UNSET:
            field_dict["seasonalRuleSetUuid"] = seasonal_rule_set_uuid
        if seasonal_rule_set_uuid_be_uuid is not UNSET:
            field_dict["seasonalRuleSetUuidBeUuid"] = seasonal_rule_set_uuid_be_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_billing_entity_config import ApiBillingEntityConfig

        d = dict(src_dict)
        _tlement_method_be_uuid = d.pop("tlementMethodBeUuid", UNSET)
        tlement_method_be_uuid: Union[Unset, ApiResolvedBillingEntityConfig]
        if _tlement_method_be_uuid and not isinstance(_tlement_method_be_uuid, Unset):
            tlement_method_be_uuid = ApiResolvedBillingEntityConfig.from_dict(_tlement_method_be_uuid)

        else:
            tlement_method_be_uuid = UNSET

        _tlement_method = d.pop("tlementMethod", UNSET)
        tlement_method: Union[Unset, ApiResolvedBillingEntityConfig]
        if _tlement_method and not isinstance(_tlement_method, Unset):
            tlement_method = ApiResolvedBillingEntityConfig.from_dict(_tlement_method)

        else:
            tlement_method = UNSET

        _billing_entity_config = d.pop("billingEntityConfig", UNSET)
        billing_entity_config: Union[Unset, ApiBillingEntityConfig]
        if _billing_entity_config and not isinstance(_billing_entity_config, Unset):
            billing_entity_config = ApiBillingEntityConfig.from_dict(_billing_entity_config)

        else:
            billing_entity_config = UNSET

        _as_of_date = d.pop("asOfDate", UNSET)
        as_of_date: Union[Unset, datetime.date]
        if _as_of_date and not isinstance(_as_of_date, Unset):
            as_of_date = isoparse(_as_of_date).date()

        else:
            as_of_date = UNSET

        revenue_share_group = d.pop("revenueShareGroup", UNSET)

        revenue_share_group_be_uuid = d.pop("revenueShareGroupBeUuid", UNSET)

        post_method = d.pop("postMethod", UNSET)

        post_method_be_uuid = d.pop("postMethodBeUuid", UNSET)

        plan_billing_method = d.pop("planBillingMethod", UNSET)

        plan_billing_method_be_uuid = d.pop("planBillingMethodBeUuid", UNSET)

        invoice_method = d.pop("invoiceMethod", UNSET)

        invoice_method_be_uuid = d.pop("invoiceMethodBeUuid", UNSET)

        invoice_number_format = d.pop("invoiceNumberFormat", UNSET)

        invoice_number_format_be_uuid = d.pop("invoiceNumberFormatBeUuid", UNSET)

        settlement_method = d.pop("settlementMethod", UNSET)

        settlement_method_be_uuid = d.pop("settlementMethodBeUuid", UNSET)

        seasonal_rule_set_uuid = d.pop("seasonalRuleSetUuid", UNSET)

        seasonal_rule_set_uuid_be_uuid = d.pop("seasonalRuleSetUuidBeUuid", UNSET)

        api_resolved_billing_entity_config = cls(
            tlement_method_be_uuid=tlement_method_be_uuid,
            tlement_method=tlement_method,
            billing_entity_config=billing_entity_config,
            as_of_date=as_of_date,
            revenue_share_group=revenue_share_group,
            revenue_share_group_be_uuid=revenue_share_group_be_uuid,
            post_method=post_method,
            post_method_be_uuid=post_method_be_uuid,
            plan_billing_method=plan_billing_method,
            plan_billing_method_be_uuid=plan_billing_method_be_uuid,
            invoice_method=invoice_method,
            invoice_method_be_uuid=invoice_method_be_uuid,
            invoice_number_format=invoice_number_format,
            invoice_number_format_be_uuid=invoice_number_format_be_uuid,
            settlement_method=settlement_method,
            settlement_method_be_uuid=settlement_method_be_uuid,
            seasonal_rule_set_uuid=seasonal_rule_set_uuid,
            seasonal_rule_set_uuid_be_uuid=seasonal_rule_set_uuid_be_uuid,
        )

        api_resolved_billing_entity_config.additional_properties = d
        return api_resolved_billing_entity_config

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
