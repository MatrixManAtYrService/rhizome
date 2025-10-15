import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeSummary")


@_attrs_define
class ApiFeeSummary:
    """
    Attributes:
        id (Union[Unset, int]): Id of the fee summary
        uuid (Union[Unset, str]): 26-character UUID of the fee summary
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this fee summary belongs to
        billing_date (Union[Unset, datetime.date]): billing date
        fee_category (Union[Unset, str]): the fee category of the fee summary
        fee_code (Union[Unset, str]): the fee code of the fee summary
        currency (Union[Unset, str]): the currency of the fee summary Example: USD.
        total_period_units (Union[Unset, float]): the total number of units billed
        abs_period_units (Union[Unset, float]): the total of the absolute value of number of units from actions that
            were posted and billed
        total_basis_amount (Union[Unset, float]): the total basis amount billed
        abs_basis_amount (Union[Unset, float]): the total of the absolute values of basis amounts from actions that were
            posted and billed
        total_fee_amount (Union[Unset, float]): the total fee amount billed
        fee_rate_uuid (Union[Unset, str]): 26-character UUID of the fee rate used to calculate the fee summary
        request_uuid (Union[Unset, str]): 26-character UUID for the execution request that created the fee summary
        invoice_info_uuid (Union[Unset, str]): 26-character UUID for the invoice info that included the fee summary
        fee_code_ledger_account_uuid (Union[Unset, str]): 26-character UUID of the fee-code-to-ledger-account mapping
            used to apply this fee summary to the ledger
        credit_ledger_account_uuid (Union[Unset, str]): 26-character UUID of the ledger account where the credit was
            applied to the ledger
        debit_ledger_account_uuid (Union[Unset, str]): 26-character UUID of the ledger account where the debit was
            applied to the ledger
        exclude_from_invoice (Union[Unset, bool]): indicates whether the fee summary should be excluded from, or not
            presented on, an invoice; typically only applies when total fee amount is zero
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the fee summary was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the fee summary was last modified
            Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    billing_date: Union[Unset, datetime.date] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total_period_units: Union[Unset, float] = UNSET
    abs_period_units: Union[Unset, float] = UNSET
    total_basis_amount: Union[Unset, float] = UNSET
    abs_basis_amount: Union[Unset, float] = UNSET
    total_fee_amount: Union[Unset, float] = UNSET
    fee_rate_uuid: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    invoice_info_uuid: Union[Unset, str] = UNSET
    fee_code_ledger_account_uuid: Union[Unset, str] = UNSET
    credit_ledger_account_uuid: Union[Unset, str] = UNSET
    debit_ledger_account_uuid: Union[Unset, str] = UNSET
    exclude_from_invoice: Union[Unset, bool] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.billing_date, Unset):
            billing_date = self.billing_date.isoformat()

        fee_category = self.fee_category

        fee_code = self.fee_code

        currency = self.currency

        total_period_units = self.total_period_units

        abs_period_units = self.abs_period_units

        total_basis_amount = self.total_basis_amount

        abs_basis_amount = self.abs_basis_amount

        total_fee_amount = self.total_fee_amount

        fee_rate_uuid = self.fee_rate_uuid

        request_uuid = self.request_uuid

        invoice_info_uuid = self.invoice_info_uuid

        fee_code_ledger_account_uuid = self.fee_code_ledger_account_uuid

        credit_ledger_account_uuid = self.credit_ledger_account_uuid

        debit_ledger_account_uuid = self.debit_ledger_account_uuid

        exclude_from_invoice = self.exclude_from_invoice

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if billing_date is not UNSET:
            field_dict["billingDate"] = billing_date
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_period_units is not UNSET:
            field_dict["totalPeriodUnits"] = total_period_units
        if abs_period_units is not UNSET:
            field_dict["absPeriodUnits"] = abs_period_units
        if total_basis_amount is not UNSET:
            field_dict["totalBasisAmount"] = total_basis_amount
        if abs_basis_amount is not UNSET:
            field_dict["absBasisAmount"] = abs_basis_amount
        if total_fee_amount is not UNSET:
            field_dict["totalFeeAmount"] = total_fee_amount
        if fee_rate_uuid is not UNSET:
            field_dict["feeRateUuid"] = fee_rate_uuid
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if invoice_info_uuid is not UNSET:
            field_dict["invoiceInfoUuid"] = invoice_info_uuid
        if fee_code_ledger_account_uuid is not UNSET:
            field_dict["feeCodeLedgerAccountUuid"] = fee_code_ledger_account_uuid
        if credit_ledger_account_uuid is not UNSET:
            field_dict["creditLedgerAccountUuid"] = credit_ledger_account_uuid
        if debit_ledger_account_uuid is not UNSET:
            field_dict["debitLedgerAccountUuid"] = debit_ledger_account_uuid
        if exclude_from_invoice is not UNSET:
            field_dict["excludeFromInvoice"] = exclude_from_invoice
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        _billing_date = d.pop("billingDate", UNSET)
        billing_date: Union[Unset, datetime.date]
        if _billing_date and not isinstance(_billing_date, Unset):
            billing_date = isoparse(_billing_date).date()

        else:
            billing_date = UNSET

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        currency = d.pop("currency", UNSET)

        total_period_units = d.pop("totalPeriodUnits", UNSET)

        abs_period_units = d.pop("absPeriodUnits", UNSET)

        total_basis_amount = d.pop("totalBasisAmount", UNSET)

        abs_basis_amount = d.pop("absBasisAmount", UNSET)

        total_fee_amount = d.pop("totalFeeAmount", UNSET)

        fee_rate_uuid = d.pop("feeRateUuid", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        invoice_info_uuid = d.pop("invoiceInfoUuid", UNSET)

        fee_code_ledger_account_uuid = d.pop("feeCodeLedgerAccountUuid", UNSET)

        credit_ledger_account_uuid = d.pop("creditLedgerAccountUuid", UNSET)

        debit_ledger_account_uuid = d.pop("debitLedgerAccountUuid", UNSET)

        exclude_from_invoice = d.pop("excludeFromInvoice", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if _modified_timestamp and not isinstance(_modified_timestamp, Unset):
            modified_timestamp = isoparse(_modified_timestamp)

        else:
            modified_timestamp = UNSET

        api_fee_summary = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            billing_date=billing_date,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            total_period_units=total_period_units,
            abs_period_units=abs_period_units,
            total_basis_amount=total_basis_amount,
            abs_basis_amount=abs_basis_amount,
            total_fee_amount=total_fee_amount,
            fee_rate_uuid=fee_rate_uuid,
            request_uuid=request_uuid,
            invoice_info_uuid=invoice_info_uuid,
            fee_code_ledger_account_uuid=fee_code_ledger_account_uuid,
            credit_ledger_account_uuid=credit_ledger_account_uuid,
            debit_ledger_account_uuid=debit_ledger_account_uuid,
            exclude_from_invoice=exclude_from_invoice,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_fee_summary.additional_properties = d
        return api_fee_summary

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
