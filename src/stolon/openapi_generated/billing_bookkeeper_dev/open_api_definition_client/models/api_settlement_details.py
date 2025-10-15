from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_settlement_details_entity_type import ApiSettlementDetailsEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_settlement_fees import ApiSettlementFees


T = TypeVar("T", bound="ApiSettlementDetails")


@_attrs_define
class ApiSettlementDetails:
    """
    Attributes:
        tlements (Union[Unset, ApiSettlementDetails]):
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the invoice belongs to
        billing_entity_name (Union[Unset, str]): name of the billing entity
        entity_uuid (Union[Unset, str]): 13-character COS UUID of the billing entity
        entity_type (Union[Unset, ApiSettlementDetailsEntityType]):
        settlements (Union[Unset, list['ApiSettlementFees']]): settlement requests for the billing entity
    """

    tlements: Union[Unset, "ApiSettlementDetails"] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiSettlementDetailsEntityType] = UNSET
    settlements: Union[Unset, list["ApiSettlementFees"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlements: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlements, Unset):
            tlements = self.tlements.to_dict()

        billing_entity_uuid = self.billing_entity_uuid

        billing_entity_name = self.billing_entity_name

        entity_uuid = self.entity_uuid

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        settlements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.settlements, Unset):
            settlements = []
            for settlements_item_data in self.settlements:
                settlements_item = settlements_item_data.to_dict()
                settlements.append(settlements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tlements is not UNSET:
            field_dict["tlements"] = tlements
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if billing_entity_name is not UNSET:
            field_dict["billingEntityName"] = billing_entity_name
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if settlements is not UNSET:
            field_dict["settlements"] = settlements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_settlement_fees import ApiSettlementFees

        d = dict(src_dict)
        _tlements = d.pop("tlements", UNSET)
        tlements: Union[Unset, ApiSettlementDetails]
        if _tlements and not isinstance(_tlements, Unset):
            tlements = ApiSettlementDetails.from_dict(_tlements)

        else:
            tlements = UNSET

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, ApiSettlementDetailsEntityType]
        if _entity_type and not isinstance(_entity_type, Unset):
            entity_type = ApiSettlementDetailsEntityType(_entity_type)

        else:
            entity_type = UNSET

        settlements = []
        _settlements = d.pop("settlements", UNSET)
        for settlements_item_data in _settlements or []:
            settlements_item = ApiSettlementFees.from_dict(settlements_item_data)

            settlements.append(settlements_item)

        api_settlement_details = cls(
            tlements=tlements,
            billing_entity_uuid=billing_entity_uuid,
            billing_entity_name=billing_entity_name,
            entity_uuid=entity_uuid,
            entity_type=entity_type,
            settlements=settlements,
        )

        api_settlement_details.additional_properties = d
        return api_settlement_details

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
