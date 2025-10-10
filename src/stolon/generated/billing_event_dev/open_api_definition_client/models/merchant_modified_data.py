from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delta_value import DeltaValue
    from ..models.merchant_data import MerchantData
    from ..models.program_express_code_data_element import ProgramExpressCodeDataElement
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="MerchantModifiedData")


@_attrs_define
class MerchantModifiedData:
    """
    Attributes:
        merchant (Union[Unset, MerchantData]):
        region_changed (Union[Unset, bool]):
        gateway_config_mutation (Union[Unset, list['DeltaValue']]):
        owner_mobile_phone_number (Union[Unset, str]):
        program_express_codes (Union[Unset, list['ProgramExpressCodeDataElement']]):
        source_system (Union[Unset, str]):
        fdgg_merchant (Union[Unset, bool]):
        legacy_merchant_migration (Union[Unset, bool]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant: Union[Unset, "MerchantData"] = UNSET
    region_changed: Union[Unset, bool] = UNSET
    gateway_config_mutation: Union[Unset, list["DeltaValue"]] = UNSET
    owner_mobile_phone_number: Union[Unset, str] = UNSET
    program_express_codes: Union[Unset, list["ProgramExpressCodeDataElement"]] = UNSET
    source_system: Union[Unset, str] = UNSET
    fdgg_merchant: Union[Unset, bool] = UNSET
    legacy_merchant_migration: Union[Unset, bool] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        region_changed = self.region_changed

        gateway_config_mutation: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.gateway_config_mutation, Unset):
            gateway_config_mutation = []
            for gateway_config_mutation_item_data in self.gateway_config_mutation:
                gateway_config_mutation_item = gateway_config_mutation_item_data.to_dict()
                gateway_config_mutation.append(gateway_config_mutation_item)

        owner_mobile_phone_number = self.owner_mobile_phone_number

        program_express_codes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_express_codes, Unset):
            program_express_codes = []
            for program_express_codes_item_data in self.program_express_codes:
                program_express_codes_item = program_express_codes_item_data.to_dict()
                program_express_codes.append(program_express_codes_item)

        source_system = self.source_system

        fdgg_merchant = self.fdgg_merchant

        legacy_merchant_migration = self.legacy_merchant_migration

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
        if region_changed is not UNSET:
            field_dict["regionChanged"] = region_changed
        if gateway_config_mutation is not UNSET:
            field_dict["gatewayConfigMutation"] = gateway_config_mutation
        if owner_mobile_phone_number is not UNSET:
            field_dict["ownerMobilePhoneNumber"] = owner_mobile_phone_number
        if program_express_codes is not UNSET:
            field_dict["programExpressCodes"] = program_express_codes
        if source_system is not UNSET:
            field_dict["sourceSystem"] = source_system
        if fdgg_merchant is not UNSET:
            field_dict["fdggMerchant"] = fdgg_merchant
        if legacy_merchant_migration is not UNSET:
            field_dict["legacyMerchantMigration"] = legacy_merchant_migration
        if specific_data is not UNSET:
            field_dict["specificData"] = specific_data
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delta_value import DeltaValue
        from ..models.merchant_data import MerchantData
        from ..models.program_express_code_data_element import ProgramExpressCodeDataElement
        from ..models.schema import Schema
        from ..models.specific_data import SpecificData

        d = dict(src_dict)
        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, MerchantData]
        if _merchant and not isinstance(_merchant, Unset):
            merchant = MerchantData.from_dict(_merchant)

        else:
            merchant = UNSET

        region_changed = d.pop("regionChanged", UNSET)

        gateway_config_mutation = []
        _gateway_config_mutation = d.pop("gatewayConfigMutation", UNSET)
        for gateway_config_mutation_item_data in _gateway_config_mutation or []:
            gateway_config_mutation_item = DeltaValue.from_dict(gateway_config_mutation_item_data)

            gateway_config_mutation.append(gateway_config_mutation_item)

        owner_mobile_phone_number = d.pop("ownerMobilePhoneNumber", UNSET)

        program_express_codes = []
        _program_express_codes = d.pop("programExpressCodes", UNSET)
        for program_express_codes_item_data in _program_express_codes or []:
            program_express_codes_item = ProgramExpressCodeDataElement.from_dict(program_express_codes_item_data)

            program_express_codes.append(program_express_codes_item)

        source_system = d.pop("sourceSystem", UNSET)

        fdgg_merchant = d.pop("fdggMerchant", UNSET)

        legacy_merchant_migration = d.pop("legacyMerchantMigration", UNSET)

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

        merchant_modified_data = cls(
            merchant=merchant,
            region_changed=region_changed,
            gateway_config_mutation=gateway_config_mutation,
            owner_mobile_phone_number=owner_mobile_phone_number,
            program_express_codes=program_express_codes,
            source_system=source_system,
            fdgg_merchant=fdgg_merchant,
            legacy_merchant_migration=legacy_merchant_migration,
            specific_data=specific_data,
            schema=schema,
        )

        merchant_modified_data.additional_properties = d
        return merchant_modified_data

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
