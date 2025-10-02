from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_taxed_entity_tax import ApiTaxedEntityTax


T = TypeVar("T", bound="ApiTaxCalcResponse")


@_attrs_define
class ApiTaxCalcResponse:
    """
    Attributes:
        entities (Union[Unset, list['ApiTaxedEntityTax']]): Collection of one or more entities that tax was calculated
            for.
    """

    entities: Union[Unset, list["ApiTaxedEntityTax"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entities is not UNSET:
            field_dict["entities"] = entities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_taxed_entity_tax import ApiTaxedEntityTax

        d = dict(src_dict)
        entities = []
        _entities = d.pop("entities", UNSET)
        for entities_item_data in _entities or []:
            entities_item = ApiTaxedEntityTax.from_dict(entities_item_data)

            entities.append(entities_item)

        api_tax_calc_response = cls(
            entities=entities,
        )

        api_tax_calc_response.additional_properties = d
        return api_tax_calc_response

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
