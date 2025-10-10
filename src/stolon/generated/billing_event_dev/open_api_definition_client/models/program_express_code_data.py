from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.program_express_code_data_action import ProgramExpressCodeDataAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_data import MerchantData
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="ProgramExpressCodeData")


@_attrs_define
class ProgramExpressCodeData:
    """
    Attributes:
        merchant (Union[Unset, MerchantData]):
        action (Union[Unset, ProgramExpressCodeDataAction]):
        program_code (Union[Unset, str]):
        program_code_description (Union[Unset, str]):
        key (Union[Unset, str]):
        key_description (Union[Unset, str]):
        value (Union[Unset, str]):
        value_description (Union[Unset, str]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant: Union[Unset, "MerchantData"] = UNSET
    action: Union[Unset, ProgramExpressCodeDataAction] = UNSET
    program_code: Union[Unset, str] = UNSET
    program_code_description: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    key_description: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    value_description: Union[Unset, str] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        program_code = self.program_code

        program_code_description = self.program_code_description

        key = self.key

        key_description = self.key_description

        value = self.value

        value_description = self.value_description

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
        if action is not UNSET:
            field_dict["action"] = action
        if program_code is not UNSET:
            field_dict["programCode"] = program_code
        if program_code_description is not UNSET:
            field_dict["programCodeDescription"] = program_code_description
        if key is not UNSET:
            field_dict["key"] = key
        if key_description is not UNSET:
            field_dict["keyDescription"] = key_description
        if value is not UNSET:
            field_dict["value"] = value
        if value_description is not UNSET:
            field_dict["valueDescription"] = value_description
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

        _action = d.pop("action", UNSET)
        action: Union[Unset, ProgramExpressCodeDataAction]
        if _action and not isinstance(_action, Unset):
            action = ProgramExpressCodeDataAction(_action)

        else:
            action = UNSET

        program_code = d.pop("programCode", UNSET)

        program_code_description = d.pop("programCodeDescription", UNSET)

        key = d.pop("key", UNSET)

        key_description = d.pop("keyDescription", UNSET)

        value = d.pop("value", UNSET)

        value_description = d.pop("valueDescription", UNSET)

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

        program_express_code_data = cls(
            merchant=merchant,
            action=action,
            program_code=program_code,
            program_code_description=program_code_description,
            key=key,
            key_description=key_description,
            value=value,
            value_description=value_description,
            specific_data=specific_data,
            schema=schema,
        )

        program_express_code_data.additional_properties = d
        return program_express_code_data

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
