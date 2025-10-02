from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_data import MerchantData
    from ..models.program_express_code_data_element import ProgramExpressCodeDataElement
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="MerchantCreatedData")


@_attrs_define
class MerchantCreatedData:
    """
    Attributes:
        merchant (Union[Unset, MerchantData]):
        contact (Union[Unset, str]):
        num_devices (Union[Unset, int]):
        mcc_code (Union[Unset, str]):
        new_plan_type (Union[Unset, str]):
        new_plan_uuid (Union[Unset, str]):
        previous_service_plan (Union[Unset, str]):
        owner_mobile_phone_number (Union[Unset, str]):
        program_express_codes (Union[Unset, list['ProgramExpressCodeDataElement']]):
        payeezy_merchant (Union[Unset, bool]):
        source_system (Union[Unset, str]):
        legacy (Union[Unset, bool]):
        fdgg_merchant (Union[Unset, bool]):
        legacy_merchant_migration (Union[Unset, bool]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant: Union[Unset, "MerchantData"] = UNSET
    contact: Union[Unset, str] = UNSET
    num_devices: Union[Unset, int] = UNSET
    mcc_code: Union[Unset, str] = UNSET
    new_plan_type: Union[Unset, str] = UNSET
    new_plan_uuid: Union[Unset, str] = UNSET
    previous_service_plan: Union[Unset, str] = UNSET
    owner_mobile_phone_number: Union[Unset, str] = UNSET
    program_express_codes: Union[Unset, list["ProgramExpressCodeDataElement"]] = UNSET
    payeezy_merchant: Union[Unset, bool] = UNSET
    source_system: Union[Unset, str] = UNSET
    legacy: Union[Unset, bool] = UNSET
    fdgg_merchant: Union[Unset, bool] = UNSET
    legacy_merchant_migration: Union[Unset, bool] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        contact = self.contact

        num_devices = self.num_devices

        mcc_code = self.mcc_code

        new_plan_type = self.new_plan_type

        new_plan_uuid = self.new_plan_uuid

        previous_service_plan = self.previous_service_plan

        owner_mobile_phone_number = self.owner_mobile_phone_number

        program_express_codes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_express_codes, Unset):
            program_express_codes = []
            for program_express_codes_item_data in self.program_express_codes:
                program_express_codes_item = program_express_codes_item_data.to_dict()
                program_express_codes.append(program_express_codes_item)

        payeezy_merchant = self.payeezy_merchant

        source_system = self.source_system

        legacy = self.legacy

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
        if contact is not UNSET:
            field_dict["contact"] = contact
        if num_devices is not UNSET:
            field_dict["numDevices"] = num_devices
        if mcc_code is not UNSET:
            field_dict["mccCode"] = mcc_code
        if new_plan_type is not UNSET:
            field_dict["newPlanType"] = new_plan_type
        if new_plan_uuid is not UNSET:
            field_dict["newPlanUuid"] = new_plan_uuid
        if previous_service_plan is not UNSET:
            field_dict["previousServicePlan"] = previous_service_plan
        if owner_mobile_phone_number is not UNSET:
            field_dict["ownerMobilePhoneNumber"] = owner_mobile_phone_number
        if program_express_codes is not UNSET:
            field_dict["programExpressCodes"] = program_express_codes
        if payeezy_merchant is not UNSET:
            field_dict["payeezyMerchant"] = payeezy_merchant
        if source_system is not UNSET:
            field_dict["sourceSystem"] = source_system
        if legacy is not UNSET:
            field_dict["legacy"] = legacy
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
        from ..models.merchant_data import MerchantData
        from ..models.program_express_code_data_element import ProgramExpressCodeDataElement
        from ..models.schema import Schema
        from ..models.specific_data import SpecificData

        d = dict(src_dict)
        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, MerchantData]
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = MerchantData.from_dict(_merchant)

        contact = d.pop("contact", UNSET)

        num_devices = d.pop("numDevices", UNSET)

        mcc_code = d.pop("mccCode", UNSET)

        new_plan_type = d.pop("newPlanType", UNSET)

        new_plan_uuid = d.pop("newPlanUuid", UNSET)

        previous_service_plan = d.pop("previousServicePlan", UNSET)

        owner_mobile_phone_number = d.pop("ownerMobilePhoneNumber", UNSET)

        program_express_codes = []
        _program_express_codes = d.pop("programExpressCodes", UNSET)
        for program_express_codes_item_data in _program_express_codes or []:
            program_express_codes_item = ProgramExpressCodeDataElement.from_dict(program_express_codes_item_data)

            program_express_codes.append(program_express_codes_item)

        payeezy_merchant = d.pop("payeezyMerchant", UNSET)

        source_system = d.pop("sourceSystem", UNSET)

        legacy = d.pop("legacy", UNSET)

        fdgg_merchant = d.pop("fdggMerchant", UNSET)

        legacy_merchant_migration = d.pop("legacyMerchantMigration", UNSET)

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

        merchant_created_data = cls(
            merchant=merchant,
            contact=contact,
            num_devices=num_devices,
            mcc_code=mcc_code,
            new_plan_type=new_plan_type,
            new_plan_uuid=new_plan_uuid,
            previous_service_plan=previous_service_plan,
            owner_mobile_phone_number=owner_mobile_phone_number,
            program_express_codes=program_express_codes,
            payeezy_merchant=payeezy_merchant,
            source_system=source_system,
            legacy=legacy,
            fdgg_merchant=fdgg_merchant,
            legacy_merchant_migration=legacy_merchant_migration,
            specific_data=specific_data,
            schema=schema,
        )

        merchant_created_data.additional_properties = d
        return merchant_created_data

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
