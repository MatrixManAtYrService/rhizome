import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_rev_share_abstraction_revenue_share_type import ApiRevShareAbstractionRevenueShareType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRevShareAbstraction")


@_attrs_define
class ApiRevShareAbstraction:
    """
    Attributes:
        as_of_date (Union[Unset, datetime.date]): effective date for the rev share action
        revenue_share_group (Union[Unset, str]): Used to identify the collective revenue share split percentages for
            resellers, developers, and Clover.
        revenue_share_type (Union[Unset, ApiRevShareAbstractionRevenueShareType]):
        currency (Union[Unset, str]): 3-letter currency code for fee rates Example: USD.
        developer_uuid (Union[Unset, str]): When revenueShareType = DEV_CUSTOM, this is the uuid of the developer the
            rev share is for.  Otherwise, this should be null.
        developer_app_uuid (Union[Unset, str]): When revenueShareType = APP_CUSTOM, this is the uuid of the app the rev
            share is for.  Otherwise, this should be null.
        developer_percent (Union[Unset, float]): The percentage of the total revenue paid to the developer.
        developer_per_item_rate (Union[Unset, float]): The per item rate paid to the developer.
        reseller_percent (Union[Unset, float]): The percentage of the total revenue paid to the reseller.
        reseller_per_item_rate (Union[Unset, float]): The per item rate paid to the reseller.
        clover_remaining_percent (Union[Unset, float]): This is read-only from the GET.  The remaining percent of the
            total that is left to clover.  Does not account for flat rates.
        fee_code (Union[Unset, str]): This is read-only from the GET but assuming a single fee code is used for rev
            share rates (which would usually be the case), this is the fee code.
        has_validation_errors (Union[Unset, bool]): This is read-only from the GET.  The abstraction is invalid because
            of validation errors.  Errors must be corrected manually in the database before the abstraction can be updated.
        has_validation_warnings (Union[Unset, bool]): This is read-only from the GET.  The abstraction is invalid
            because of validation warnings.  Warnings should automatically be corrected when the abstraction is next
            updated.
    """

    as_of_date: Union[Unset, datetime.date] = UNSET
    revenue_share_group: Union[Unset, str] = UNSET
    revenue_share_type: Union[Unset, ApiRevShareAbstractionRevenueShareType] = UNSET
    currency: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    developer_percent: Union[Unset, float] = UNSET
    developer_per_item_rate: Union[Unset, float] = UNSET
    reseller_percent: Union[Unset, float] = UNSET
    reseller_per_item_rate: Union[Unset, float] = UNSET
    clover_remaining_percent: Union[Unset, float] = UNSET
    fee_code: Union[Unset, str] = UNSET
    has_validation_errors: Union[Unset, bool] = UNSET
    has_validation_warnings: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of_date: Union[Unset, str] = UNSET
        if not isinstance(self.as_of_date, Unset):
            as_of_date = self.as_of_date.isoformat()

        revenue_share_group = self.revenue_share_group

        revenue_share_type: Union[Unset, str] = UNSET
        if not isinstance(self.revenue_share_type, Unset):
            revenue_share_type = self.revenue_share_type.value

        currency = self.currency

        developer_uuid = self.developer_uuid

        developer_app_uuid = self.developer_app_uuid

        developer_percent = self.developer_percent

        developer_per_item_rate = self.developer_per_item_rate

        reseller_percent = self.reseller_percent

        reseller_per_item_rate = self.reseller_per_item_rate

        clover_remaining_percent = self.clover_remaining_percent

        fee_code = self.fee_code

        has_validation_errors = self.has_validation_errors

        has_validation_warnings = self.has_validation_warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_of_date is not UNSET:
            field_dict["asOfDate"] = as_of_date
        if revenue_share_group is not UNSET:
            field_dict["revenueShareGroup"] = revenue_share_group
        if revenue_share_type is not UNSET:
            field_dict["revenueShareType"] = revenue_share_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if developer_app_uuid is not UNSET:
            field_dict["developerAppUuid"] = developer_app_uuid
        if developer_percent is not UNSET:
            field_dict["developerPercent"] = developer_percent
        if developer_per_item_rate is not UNSET:
            field_dict["developerPerItemRate"] = developer_per_item_rate
        if reseller_percent is not UNSET:
            field_dict["resellerPercent"] = reseller_percent
        if reseller_per_item_rate is not UNSET:
            field_dict["resellerPerItemRate"] = reseller_per_item_rate
        if clover_remaining_percent is not UNSET:
            field_dict["cloverRemainingPercent"] = clover_remaining_percent
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if has_validation_errors is not UNSET:
            field_dict["hasValidationErrors"] = has_validation_errors
        if has_validation_warnings is not UNSET:
            field_dict["hasValidationWarnings"] = has_validation_warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _as_of_date = d.pop("asOfDate", UNSET)
        as_of_date: Union[Unset, datetime.date]
        if isinstance(_as_of_date, Unset):
            as_of_date = UNSET
        else:
            as_of_date = isoparse(_as_of_date).date()

        revenue_share_group = d.pop("revenueShareGroup", UNSET)

        _revenue_share_type = d.pop("revenueShareType", UNSET)
        revenue_share_type: Union[Unset, ApiRevShareAbstractionRevenueShareType]
        if isinstance(_revenue_share_type, Unset):
            revenue_share_type = UNSET
        else:
            revenue_share_type = ApiRevShareAbstractionRevenueShareType(_revenue_share_type)

        currency = d.pop("currency", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        developer_percent = d.pop("developerPercent", UNSET)

        developer_per_item_rate = d.pop("developerPerItemRate", UNSET)

        reseller_percent = d.pop("resellerPercent", UNSET)

        reseller_per_item_rate = d.pop("resellerPerItemRate", UNSET)

        clover_remaining_percent = d.pop("cloverRemainingPercent", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        has_validation_errors = d.pop("hasValidationErrors", UNSET)

        has_validation_warnings = d.pop("hasValidationWarnings", UNSET)

        api_rev_share_abstraction = cls(
            as_of_date=as_of_date,
            revenue_share_group=revenue_share_group,
            revenue_share_type=revenue_share_type,
            currency=currency,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            developer_percent=developer_percent,
            developer_per_item_rate=developer_per_item_rate,
            reseller_percent=reseller_percent,
            reseller_per_item_rate=reseller_per_item_rate,
            clover_remaining_percent=clover_remaining_percent,
            fee_code=fee_code,
            has_validation_errors=has_validation_errors,
            has_validation_warnings=has_validation_warnings,
        )

        api_rev_share_abstraction.additional_properties = d
        return api_rev_share_abstraction

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
