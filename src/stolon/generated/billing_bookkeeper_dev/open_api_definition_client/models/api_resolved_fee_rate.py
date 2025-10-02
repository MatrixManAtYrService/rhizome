from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_fee_rate import ApiFeeRate


T = TypeVar("T", bound="ApiResolvedFeeRate")


@_attrs_define
class ApiResolvedFeeRate:
    """
    Attributes:
        based_on_prototype_fee_rate (Union[Unset, bool]): true when a prototype fee rate was used to resolve the rate
        billing_entity_fee_rate (Union[Unset, ApiFeeRate]): All fee rates for the owningBillingEntity that are used to
            build this abstraction
        applicable_fee_rate (Union[Unset, ApiFeeRate]): All fee rates for the owningBillingEntity that are used to build
            this abstraction
        missing_fee_rates (Union[Unset, list['ApiFeeRate']]): fee rates that are missing between a billing entity and a
            parent applicable fee rate
    """

    based_on_prototype_fee_rate: Union[Unset, bool] = UNSET
    billing_entity_fee_rate: Union[Unset, "ApiFeeRate"] = UNSET
    applicable_fee_rate: Union[Unset, "ApiFeeRate"] = UNSET
    missing_fee_rates: Union[Unset, list["ApiFeeRate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        based_on_prototype_fee_rate = self.based_on_prototype_fee_rate

        billing_entity_fee_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_entity_fee_rate, Unset):
            billing_entity_fee_rate = self.billing_entity_fee_rate.to_dict()

        applicable_fee_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.applicable_fee_rate, Unset):
            applicable_fee_rate = self.applicable_fee_rate.to_dict()

        missing_fee_rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.missing_fee_rates, Unset):
            missing_fee_rates = []
            for missing_fee_rates_item_data in self.missing_fee_rates:
                missing_fee_rates_item = missing_fee_rates_item_data.to_dict()
                missing_fee_rates.append(missing_fee_rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if based_on_prototype_fee_rate is not UNSET:
            field_dict["basedOnPrototypeFeeRate"] = based_on_prototype_fee_rate
        if billing_entity_fee_rate is not UNSET:
            field_dict["billingEntityFeeRate"] = billing_entity_fee_rate
        if applicable_fee_rate is not UNSET:
            field_dict["applicableFeeRate"] = applicable_fee_rate
        if missing_fee_rates is not UNSET:
            field_dict["missingFeeRates"] = missing_fee_rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_fee_rate import ApiFeeRate

        d = dict(src_dict)
        based_on_prototype_fee_rate = d.pop("basedOnPrototypeFeeRate", UNSET)

        _billing_entity_fee_rate = d.pop("billingEntityFeeRate", UNSET)
        billing_entity_fee_rate: Union[Unset, ApiFeeRate]
        if isinstance(_billing_entity_fee_rate, Unset):
            billing_entity_fee_rate = UNSET
        else:
            billing_entity_fee_rate = ApiFeeRate.from_dict(_billing_entity_fee_rate)

        _applicable_fee_rate = d.pop("applicableFeeRate", UNSET)
        applicable_fee_rate: Union[Unset, ApiFeeRate]
        if isinstance(_applicable_fee_rate, Unset):
            applicable_fee_rate = UNSET
        else:
            applicable_fee_rate = ApiFeeRate.from_dict(_applicable_fee_rate)

        missing_fee_rates = []
        _missing_fee_rates = d.pop("missingFeeRates", UNSET)
        for missing_fee_rates_item_data in _missing_fee_rates or []:
            missing_fee_rates_item = ApiFeeRate.from_dict(missing_fee_rates_item_data)

            missing_fee_rates.append(missing_fee_rates_item)

        api_resolved_fee_rate = cls(
            based_on_prototype_fee_rate=based_on_prototype_fee_rate,
            billing_entity_fee_rate=billing_entity_fee_rate,
            applicable_fee_rate=applicable_fee_rate,
            missing_fee_rates=missing_fee_rates,
        )

        api_resolved_fee_rate.additional_properties = d
        return api_resolved_fee_rate

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
