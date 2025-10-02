from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.merchant_accoun_status_change_data_source import MerchantAccounStatusChangeDataSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_data import MerchantData
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="MerchantAccounStatusChangeData")


@_attrs_define
class MerchantAccounStatusChangeData:
    """
    Attributes:
        merchant (Union[Unset, MerchantData]):
        new_account_status (Union[Unset, str]):
        previous_account_status (Union[Unset, str]):
        source (Union[Unset, MerchantAccounStatusChangeDataSource]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant: Union[Unset, "MerchantData"] = UNSET
    new_account_status: Union[Unset, str] = UNSET
    previous_account_status: Union[Unset, str] = UNSET
    source: Union[Unset, MerchantAccounStatusChangeDataSource] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        new_account_status = self.new_account_status

        previous_account_status = self.previous_account_status

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

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
        if new_account_status is not UNSET:
            field_dict["newAccountStatus"] = new_account_status
        if previous_account_status is not UNSET:
            field_dict["previousAccountStatus"] = previous_account_status
        if source is not UNSET:
            field_dict["source"] = source
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

        new_account_status = d.pop("newAccountStatus", UNSET)

        previous_account_status = d.pop("previousAccountStatus", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, MerchantAccounStatusChangeDataSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = MerchantAccounStatusChangeDataSource(_source)

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

        merchant_accoun_status_change_data = cls(
            merchant=merchant,
            new_account_status=new_account_status,
            previous_account_status=previous_account_status,
            source=source,
            specific_data=specific_data,
            schema=schema,
        )

        merchant_accoun_status_change_data.additional_properties = d
        return merchant_accoun_status_change_data

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
