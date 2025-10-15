from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_adjust_advice import AutoAdjustAdvice
    from ..models.monetary_adjustment import MonetaryAdjustment
    from ..models.tiered_pricing import TieredPricing


T = TypeVar("T", bound="Monetary")


@_attrs_define
class Monetary:
    """
    Attributes:
        auto_adjust_advices (Union[Unset, list['AutoAdjustAdvice']]):
        tiered_pricings (Union[Unset, list['TieredPricing']]):
        monetary_adjustments (Union[Unset, list['MonetaryAdjustment']]):
    """

    auto_adjust_advices: Union[Unset, list["AutoAdjustAdvice"]] = UNSET
    tiered_pricings: Union[Unset, list["TieredPricing"]] = UNSET
    monetary_adjustments: Union[Unset, list["MonetaryAdjustment"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_adjust_advices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.auto_adjust_advices, Unset):
            auto_adjust_advices = []
            for auto_adjust_advices_item_data in self.auto_adjust_advices:
                auto_adjust_advices_item = auto_adjust_advices_item_data.to_dict()
                auto_adjust_advices.append(auto_adjust_advices_item)

        tiered_pricings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tiered_pricings, Unset):
            tiered_pricings = []
            for tiered_pricings_item_data in self.tiered_pricings:
                tiered_pricings_item = tiered_pricings_item_data.to_dict()
                tiered_pricings.append(tiered_pricings_item)

        monetary_adjustments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.monetary_adjustments, Unset):
            monetary_adjustments = []
            for monetary_adjustments_item_data in self.monetary_adjustments:
                monetary_adjustments_item = monetary_adjustments_item_data.to_dict()
                monetary_adjustments.append(monetary_adjustments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_adjust_advices is not UNSET:
            field_dict["autoAdjustAdvices"] = auto_adjust_advices
        if tiered_pricings is not UNSET:
            field_dict["tieredPricings"] = tiered_pricings
        if monetary_adjustments is not UNSET:
            field_dict["monetaryAdjustments"] = monetary_adjustments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_adjust_advice import AutoAdjustAdvice
        from ..models.monetary_adjustment import MonetaryAdjustment
        from ..models.tiered_pricing import TieredPricing

        d = dict(src_dict)
        auto_adjust_advices = []
        _auto_adjust_advices = d.pop("autoAdjustAdvices", UNSET)
        for auto_adjust_advices_item_data in _auto_adjust_advices or []:
            auto_adjust_advices_item = AutoAdjustAdvice.from_dict(auto_adjust_advices_item_data)

            auto_adjust_advices.append(auto_adjust_advices_item)

        tiered_pricings = []
        _tiered_pricings = d.pop("tieredPricings", UNSET)
        for tiered_pricings_item_data in _tiered_pricings or []:
            tiered_pricings_item = TieredPricing.from_dict(tiered_pricings_item_data)

            tiered_pricings.append(tiered_pricings_item)

        monetary_adjustments = []
        _monetary_adjustments = d.pop("monetaryAdjustments", UNSET)
        for monetary_adjustments_item_data in _monetary_adjustments or []:
            monetary_adjustments_item = MonetaryAdjustment.from_dict(monetary_adjustments_item_data)

            monetary_adjustments.append(monetary_adjustments_item)

        monetary = cls(
            auto_adjust_advices=auto_adjust_advices,
            tiered_pricings=tiered_pricings,
            monetary_adjustments=monetary_adjustments,
        )

        monetary.additional_properties = d
        return monetary

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
