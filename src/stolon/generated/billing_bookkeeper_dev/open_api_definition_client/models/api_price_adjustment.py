from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_price_detail import ApiPriceDetail


T = TypeVar("T", bound="ApiPriceAdjustment")


@_attrs_define
class ApiPriceAdjustment:
    """potential adjustments to the cellular base price

    Attributes:
        advice_uuid (Union[Unset, str]): 26-character UUID of the auto-adjustment advice that assigns an auto-adjustment
            rule to the billing entity
        auto_adjust_rule_uuid (Union[Unset, str]): 26-character UUID of the auto-adjustment rule assigned to the billing
            entity
        rule_alias (Union[Unset, str]): commonly known alias assigned to the auto-adjustment rule
        rule_short_desc (Union[Unset, str]): short description of the auto-adjustment rule
        total_periods (Union[Unset, int]): the total number of billing periods that this auto-adjust advice and
            associated rule should be evaluated
        evaluated_periods (Union[Unset, int]): the total number of billing periods that this auto-adjust advice and
            associated rule have been evaluated
        applied_periods (Union[Unset, int]): the total number of billing periods where this auto-adjust advice and
            associated rule applied an adjustment
        max_units (Union[Unset, float]): the maximum total number of units from qualified fee summaries that can be used
            to create an auto-adjustment
        max_amount (Union[Unset, float]): the maximum total of fee amount from qualified fee summaries that can be used
            to create an auto-adjustment
        adjust_price (Union[Unset, ApiPriceDetail]):
    """

    advice_uuid: Union[Unset, str] = UNSET
    auto_adjust_rule_uuid: Union[Unset, str] = UNSET
    rule_alias: Union[Unset, str] = UNSET
    rule_short_desc: Union[Unset, str] = UNSET
    total_periods: Union[Unset, int] = UNSET
    evaluated_periods: Union[Unset, int] = UNSET
    applied_periods: Union[Unset, int] = UNSET
    max_units: Union[Unset, float] = UNSET
    max_amount: Union[Unset, float] = UNSET
    adjust_price: Union[Unset, "ApiPriceDetail"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advice_uuid = self.advice_uuid

        auto_adjust_rule_uuid = self.auto_adjust_rule_uuid

        rule_alias = self.rule_alias

        rule_short_desc = self.rule_short_desc

        total_periods = self.total_periods

        evaluated_periods = self.evaluated_periods

        applied_periods = self.applied_periods

        max_units = self.max_units

        max_amount = self.max_amount

        adjust_price: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.adjust_price, Unset):
            adjust_price = self.adjust_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advice_uuid is not UNSET:
            field_dict["adviceUuid"] = advice_uuid
        if auto_adjust_rule_uuid is not UNSET:
            field_dict["autoAdjustRuleUuid"] = auto_adjust_rule_uuid
        if rule_alias is not UNSET:
            field_dict["ruleAlias"] = rule_alias
        if rule_short_desc is not UNSET:
            field_dict["ruleShortDesc"] = rule_short_desc
        if total_periods is not UNSET:
            field_dict["totalPeriods"] = total_periods
        if evaluated_periods is not UNSET:
            field_dict["evaluatedPeriods"] = evaluated_periods
        if applied_periods is not UNSET:
            field_dict["appliedPeriods"] = applied_periods
        if max_units is not UNSET:
            field_dict["maxUnits"] = max_units
        if max_amount is not UNSET:
            field_dict["maxAmount"] = max_amount
        if adjust_price is not UNSET:
            field_dict["adjustPrice"] = adjust_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_price_detail import ApiPriceDetail

        d = dict(src_dict)
        advice_uuid = d.pop("adviceUuid", UNSET)

        auto_adjust_rule_uuid = d.pop("autoAdjustRuleUuid", UNSET)

        rule_alias = d.pop("ruleAlias", UNSET)

        rule_short_desc = d.pop("ruleShortDesc", UNSET)

        total_periods = d.pop("totalPeriods", UNSET)

        evaluated_periods = d.pop("evaluatedPeriods", UNSET)

        applied_periods = d.pop("appliedPeriods", UNSET)

        max_units = d.pop("maxUnits", UNSET)

        max_amount = d.pop("maxAmount", UNSET)

        _adjust_price = d.pop("adjustPrice", UNSET)
        adjust_price: Union[Unset, ApiPriceDetail]
        if isinstance(_adjust_price, Unset):
            adjust_price = UNSET
        else:
            adjust_price = ApiPriceDetail.from_dict(_adjust_price)

        api_price_adjustment = cls(
            advice_uuid=advice_uuid,
            auto_adjust_rule_uuid=auto_adjust_rule_uuid,
            rule_alias=rule_alias,
            rule_short_desc=rule_short_desc,
            total_periods=total_periods,
            evaluated_periods=evaluated_periods,
            applied_periods=applied_periods,
            max_units=max_units,
            max_amount=max_amount,
            adjust_price=adjust_price,
        )

        api_price_adjustment.additional_properties = d
        return api_price_adjustment

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
