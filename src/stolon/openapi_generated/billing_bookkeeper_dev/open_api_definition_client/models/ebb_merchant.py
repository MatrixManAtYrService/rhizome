from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ebb_address import EbbAddress
    from ..models.ebb_employee import EbbEmployee


T = TypeVar("T", bound="EbbMerchant")


@_attrs_define
class EbbMerchant:
    """
    Attributes:
        uuid (Union[Unset, str]):
        name (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        address (Union[Unset, EbbAddress]):
        owner (Union[Unset, EbbEmployee]):
        default_currency (Union[Unset, str]):
        routing_number (Union[Unset, str]):
        dda_account_number (Union[Unset, str]):
        support_phone (Union[Unset, str]):
        support_email (Union[Unset, str]):
        locale (Union[Unset, str]):
        created_time (Union[Unset, int]):
    """

    uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    reseller_uuid: Union[Unset, str] = UNSET
    address: Union[Unset, "EbbAddress"] = UNSET
    owner: Union[Unset, "EbbEmployee"] = UNSET
    default_currency: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    dda_account_number: Union[Unset, str] = UNSET
    support_phone: Union[Unset, str] = UNSET
    support_email: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    created_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        reseller_uuid = self.reseller_uuid

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        owner: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        default_currency = self.default_currency

        routing_number = self.routing_number

        dda_account_number = self.dda_account_number

        support_phone = self.support_phone

        support_email = self.support_email

        locale = self.locale

        created_time = self.created_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if reseller_uuid is not UNSET:
            field_dict["resellerUuid"] = reseller_uuid
        if address is not UNSET:
            field_dict["address"] = address
        if owner is not UNSET:
            field_dict["owner"] = owner
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if dda_account_number is not UNSET:
            field_dict["ddaAccountNumber"] = dda_account_number
        if support_phone is not UNSET:
            field_dict["supportPhone"] = support_phone
        if support_email is not UNSET:
            field_dict["supportEmail"] = support_email
        if locale is not UNSET:
            field_dict["locale"] = locale
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ebb_address import EbbAddress
        from ..models.ebb_employee import EbbEmployee

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        reseller_uuid = d.pop("resellerUuid", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, EbbAddress]
        if _address and not isinstance(_address, Unset):
            address = EbbAddress.from_dict(_address)

        else:
            address = UNSET

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, EbbEmployee]
        if _owner and not isinstance(_owner, Unset):
            owner = EbbEmployee.from_dict(_owner)

        else:
            owner = UNSET

        default_currency = d.pop("defaultCurrency", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        dda_account_number = d.pop("ddaAccountNumber", UNSET)

        support_phone = d.pop("supportPhone", UNSET)

        support_email = d.pop("supportEmail", UNSET)

        locale = d.pop("locale", UNSET)

        created_time = d.pop("createdTime", UNSET)

        ebb_merchant = cls(
            uuid=uuid,
            name=name,
            reseller_uuid=reseller_uuid,
            address=address,
            owner=owner,
            default_currency=default_currency,
            routing_number=routing_number,
            dda_account_number=dda_account_number,
            support_phone=support_phone,
            support_email=support_email,
            locale=locale,
            created_time=created_time,
        )

        ebb_merchant.additional_properties = d
        return ebb_merchant

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
