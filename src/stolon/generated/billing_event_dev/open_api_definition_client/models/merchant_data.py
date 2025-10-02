from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merchant_address_data import MerchantAddressData
    from ..models.merchant_entitlement_data import MerchantEntitlementData
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="MerchantData")


@_attrs_define
class MerchantData:
    """
    Attributes:
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        name (Union[Unset, str]):
        mid (Union[Unset, str]):
        bemid (Union[Unset, str]):
        tid (Union[Unset, str]):
        gateway_config (Union[Unset, str]):
        owner (Union[Unset, str]):
        service_plan (Union[Unset, str]):
        contains_station (Union[Unset, bool]):
        address (Union[Unset, MerchantAddressData]):
        business_level (Union[Unset, str]):
        bank (Union[Unset, str]):
        bank_marker (Union[Unset, str]):
        account_status (Union[Unset, str]):
        entitlements (Union[Unset, list['MerchantEntitlementData']]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    merchant_uuid: Union[Unset, str] = UNSET
    reseller_uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    mid: Union[Unset, str] = UNSET
    bemid: Union[Unset, str] = UNSET
    tid: Union[Unset, str] = UNSET
    gateway_config: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    service_plan: Union[Unset, str] = UNSET
    contains_station: Union[Unset, bool] = UNSET
    address: Union[Unset, "MerchantAddressData"] = UNSET
    business_level: Union[Unset, str] = UNSET
    bank: Union[Unset, str] = UNSET
    bank_marker: Union[Unset, str] = UNSET
    account_status: Union[Unset, str] = UNSET
    entitlements: Union[Unset, list["MerchantEntitlementData"]] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant_uuid = self.merchant_uuid

        reseller_uuid = self.reseller_uuid

        name = self.name

        mid = self.mid

        bemid = self.bemid

        tid = self.tid

        gateway_config = self.gateway_config

        owner = self.owner

        service_plan = self.service_plan

        contains_station = self.contains_station

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        business_level = self.business_level

        bank = self.bank

        bank_marker = self.bank_marker

        account_status = self.account_status

        entitlements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entitlements, Unset):
            entitlements = []
            for entitlements_item_data in self.entitlements:
                entitlements_item = entitlements_item_data.to_dict()
                entitlements.append(entitlements_item)

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if reseller_uuid is not UNSET:
            field_dict["resellerUuid"] = reseller_uuid
        if name is not UNSET:
            field_dict["name"] = name
        if mid is not UNSET:
            field_dict["mid"] = mid
        if bemid is not UNSET:
            field_dict["bemid"] = bemid
        if tid is not UNSET:
            field_dict["tid"] = tid
        if gateway_config is not UNSET:
            field_dict["gatewayConfig"] = gateway_config
        if owner is not UNSET:
            field_dict["owner"] = owner
        if service_plan is not UNSET:
            field_dict["servicePlan"] = service_plan
        if contains_station is not UNSET:
            field_dict["containsStation"] = contains_station
        if address is not UNSET:
            field_dict["address"] = address
        if business_level is not UNSET:
            field_dict["businessLevel"] = business_level
        if bank is not UNSET:
            field_dict["bank"] = bank
        if bank_marker is not UNSET:
            field_dict["bankMarker"] = bank_marker
        if account_status is not UNSET:
            field_dict["accountStatus"] = account_status
        if entitlements is not UNSET:
            field_dict["entitlements"] = entitlements
        if specific_data is not UNSET:
            field_dict["specificData"] = specific_data
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merchant_address_data import MerchantAddressData
        from ..models.merchant_entitlement_data import MerchantEntitlementData
        from ..models.schema import Schema
        from ..models.specific_data import SpecificData

        d = dict(src_dict)
        merchant_uuid = d.pop("merchantUuid", UNSET)

        reseller_uuid = d.pop("resellerUuid", UNSET)

        name = d.pop("name", UNSET)

        mid = d.pop("mid", UNSET)

        bemid = d.pop("bemid", UNSET)

        tid = d.pop("tid", UNSET)

        gateway_config = d.pop("gatewayConfig", UNSET)

        owner = d.pop("owner", UNSET)

        service_plan = d.pop("servicePlan", UNSET)

        contains_station = d.pop("containsStation", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, MerchantAddressData]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = MerchantAddressData.from_dict(_address)

        business_level = d.pop("businessLevel", UNSET)

        bank = d.pop("bank", UNSET)

        bank_marker = d.pop("bankMarker", UNSET)

        account_status = d.pop("accountStatus", UNSET)

        entitlements = []
        _entitlements = d.pop("entitlements", UNSET)
        for entitlements_item_data in _entitlements or []:
            entitlements_item = MerchantEntitlementData.from_dict(entitlements_item_data)

            entitlements.append(entitlements_item)

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

        merchant_data = cls(
            merchant_uuid=merchant_uuid,
            reseller_uuid=reseller_uuid,
            name=name,
            mid=mid,
            bemid=bemid,
            tid=tid,
            gateway_config=gateway_config,
            owner=owner,
            service_plan=service_plan,
            contains_station=contains_station,
            address=address,
            business_level=business_level,
            bank=bank,
            bank_marker=bank_marker,
            account_status=account_status,
            entitlements=entitlements,
            specific_data=specific_data,
            schema=schema,
        )

        merchant_data.additional_properties = d
        return merchant_data

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
