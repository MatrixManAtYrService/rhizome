from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_data import MerchantData
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="MerchantPlanChangeData")


@_attrs_define
class MerchantPlanChangeData:
    """
    Attributes:
        merchant (Union[Unset, MerchantData]):
        old_plan_type (Union[Unset, str]):
        old_plan_uuid (Union[Unset, str]):
        new_plan_type (Union[Unset, str]):
        new_plan_uuid (Union[Unset, str]):
        previous_service_plan (Union[Unset, str]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant: Union[Unset, "MerchantData"] = UNSET
    old_plan_type: Union[Unset, str] = UNSET
    old_plan_uuid: Union[Unset, str] = UNSET
    new_plan_type: Union[Unset, str] = UNSET
    new_plan_uuid: Union[Unset, str] = UNSET
    previous_service_plan: Union[Unset, str] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        old_plan_type = self.old_plan_type

        old_plan_uuid = self.old_plan_uuid

        new_plan_type = self.new_plan_type

        new_plan_uuid = self.new_plan_uuid

        previous_service_plan = self.previous_service_plan

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if old_plan_type is not UNSET:
            field_dict["oldPlanType"] = old_plan_type
        if old_plan_uuid is not UNSET:
            field_dict["oldPlanUuid"] = old_plan_uuid
        if new_plan_type is not UNSET:
            field_dict["newPlanType"] = new_plan_type
        if new_plan_uuid is not UNSET:
            field_dict["newPlanUuid"] = new_plan_uuid
        if previous_service_plan is not UNSET:
            field_dict["previousServicePlan"] = previous_service_plan
        if specific_data is not UNSET:
            field_dict["specificData"] = specific_data
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merchant_data import MerchantData
        from ..models.schema import Schema
        from ..models.specific_data import SpecificData

        d = dict(src_dict)
        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, MerchantData]
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = MerchantData.from_dict(_merchant)

        old_plan_type = d.pop("oldPlanType", UNSET)

        old_plan_uuid = d.pop("oldPlanUuid", UNSET)

        new_plan_type = d.pop("newPlanType", UNSET)

        new_plan_uuid = d.pop("newPlanUuid", UNSET)

        previous_service_plan = d.pop("previousServicePlan", UNSET)

        _specific_data = d.pop("specificData", UNSET)
        specific_data: Union[Unset, SpecificData]
        if isinstance(_specific_data, Unset):
            specific_data = UNSET
        else:
            specific_data = SpecificData.from_dict(_specific_data)

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, Schema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = Schema.from_dict(_schema)

        merchant_plan_change_data = cls(
            merchant=merchant,
            old_plan_type=old_plan_type,
            old_plan_uuid=old_plan_uuid,
            new_plan_type=new_plan_type,
            new_plan_uuid=new_plan_uuid,
            previous_service_plan=previous_service_plan,
            specific_data=specific_data,
            schema=schema,
        )

        merchant_plan_change_data.additional_properties = d
        return merchant_plan_change_data

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
