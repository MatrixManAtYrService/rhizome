from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_data import MerchantData
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="MerchantShellCreatedData")


@_attrs_define
class MerchantShellCreatedData:
    """
    Attributes:
        merchant (Union[Unset, MerchantData]):
        mcc_code (Union[Unset, str]):
        new_plan_type (Union[Unset, str]):
        new_plan_uuid (Union[Unset, str]):
        source_system (Union[Unset, str]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant: Union[Unset, "MerchantData"] = UNSET
    mcc_code: Union[Unset, str] = UNSET
    new_plan_type: Union[Unset, str] = UNSET
    new_plan_uuid: Union[Unset, str] = UNSET
    source_system: Union[Unset, str] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        mcc_code = self.mcc_code

        new_plan_type = self.new_plan_type

        new_plan_uuid = self.new_plan_uuid

        source_system = self.source_system

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
        if mcc_code is not UNSET:
            field_dict["mccCode"] = mcc_code
        if new_plan_type is not UNSET:
            field_dict["newPlanType"] = new_plan_type
        if new_plan_uuid is not UNSET:
            field_dict["newPlanUuid"] = new_plan_uuid
        if source_system is not UNSET:
            field_dict["sourceSystem"] = source_system
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
        if _merchant and not isinstance(_merchant, Unset):
            merchant = MerchantData.from_dict(_merchant)

        else:
            merchant = UNSET

        mcc_code = d.pop("mccCode", UNSET)

        new_plan_type = d.pop("newPlanType", UNSET)

        new_plan_uuid = d.pop("newPlanUuid", UNSET)

        source_system = d.pop("sourceSystem", UNSET)

        _specific_data = d.pop("specificData", UNSET)
        specific_data: Union[Unset, SpecificData]
        if _specific_data and not isinstance(_specific_data, Unset):
            specific_data = SpecificData.from_dict(_specific_data)

        else:
            specific_data = UNSET

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, Schema]
        if _schema and not isinstance(_schema, Unset):
            schema = Schema.from_dict(_schema)

        else:
            schema = UNSET

        merchant_shell_created_data = cls(
            merchant=merchant,
            mcc_code=mcc_code,
            new_plan_type=new_plan_type,
            new_plan_uuid=new_plan_uuid,
            source_system=source_system,
            specific_data=specific_data,
            schema=schema,
        )

        merchant_shell_created_data.additional_properties = d
        return merchant_shell_created_data

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
