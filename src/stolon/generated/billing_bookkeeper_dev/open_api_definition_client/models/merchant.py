from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.compliances import Compliances
    from ..models.equipment import Equipment
    from ..models.gateway import Gateway
    from ..models.logo_elements import LogoElements
    from ..models.merchant_boarding import MerchantBoarding
    from ..models.merchant_owner import MerchantOwner
    from ..models.merchant_plan import MerchantPlan
    from ..models.merchant_reseller import MerchantReseller
    from ..models.program_expresses import ProgramExpresses
    from ..models.properties import Properties
    from ..models.tip_suggestions import TipSuggestions


T = TypeVar("T", bound="Merchant")


@_attrs_define
class Merchant:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        properties (Union[Unset, Properties]):
        tip_suggestions (Union[Unset, TipSuggestions]):
        owner (Union[Unset, MerchantOwner]):
        reseller (Union[Unset, MerchantReseller]):
        phone_number (Union[Unset, str]):
        website (Union[Unset, str]):
        logos (Union[Unset, LogoElements]):
        customer_contact_email (Union[Unset, str]):
        compliances (Union[Unset, Compliances]):
        gateway (Union[Unset, Gateway]):
        merchant_plan (Union[Unset, MerchantPlan]):
        merchant_boarding (Union[Unset, MerchantBoarding]):
        created_time (Union[Unset, int]):
        equipment (Union[Unset, Equipment]):
        program_expresses (Union[Unset, ProgramExpresses]):
        address (Union[Unset, Address]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    properties: Union[Unset, "Properties"] = UNSET
    tip_suggestions: Union[Unset, "TipSuggestions"] = UNSET
    owner: Union[Unset, "MerchantOwner"] = UNSET
    reseller: Union[Unset, "MerchantReseller"] = UNSET
    phone_number: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    logos: Union[Unset, "LogoElements"] = UNSET
    customer_contact_email: Union[Unset, str] = UNSET
    compliances: Union[Unset, "Compliances"] = UNSET
    gateway: Union[Unset, "Gateway"] = UNSET
    merchant_plan: Union[Unset, "MerchantPlan"] = UNSET
    merchant_boarding: Union[Unset, "MerchantBoarding"] = UNSET
    created_time: Union[Unset, int] = UNSET
    equipment: Union[Unset, "Equipment"] = UNSET
    program_expresses: Union[Unset, "ProgramExpresses"] = UNSET
    address: Union[Unset, "Address"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        tip_suggestions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tip_suggestions, Unset):
            tip_suggestions = self.tip_suggestions.to_dict()

        owner: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        reseller: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reseller, Unset):
            reseller = self.reseller.to_dict()

        phone_number = self.phone_number

        website = self.website

        logos: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.logos, Unset):
            logos = self.logos.to_dict()

        customer_contact_email = self.customer_contact_email

        compliances: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.compliances, Unset):
            compliances = self.compliances.to_dict()

        gateway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.to_dict()

        merchant_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_plan, Unset):
            merchant_plan = self.merchant_plan.to_dict()

        merchant_boarding: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_boarding, Unset):
            merchant_boarding = self.merchant_boarding.to_dict()

        created_time = self.created_time

        equipment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.equipment, Unset):
            equipment = self.equipment.to_dict()

        program_expresses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_expresses, Unset):
            program_expresses = self.program_expresses.to_dict()

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if properties is not UNSET:
            field_dict["properties"] = properties
        if tip_suggestions is not UNSET:
            field_dict["tipSuggestions"] = tip_suggestions
        if owner is not UNSET:
            field_dict["owner"] = owner
        if reseller is not UNSET:
            field_dict["reseller"] = reseller
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if website is not UNSET:
            field_dict["website"] = website
        if logos is not UNSET:
            field_dict["logos"] = logos
        if customer_contact_email is not UNSET:
            field_dict["customerContactEmail"] = customer_contact_email
        if compliances is not UNSET:
            field_dict["compliances"] = compliances
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if merchant_plan is not UNSET:
            field_dict["merchantPlan"] = merchant_plan
        if merchant_boarding is not UNSET:
            field_dict["merchantBoarding"] = merchant_boarding
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if program_expresses is not UNSET:
            field_dict["programExpresses"] = program_expresses
        if address is not UNSET:
            field_dict["Address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.compliances import Compliances
        from ..models.equipment import Equipment
        from ..models.gateway import Gateway
        from ..models.logo_elements import LogoElements
        from ..models.merchant_boarding import MerchantBoarding
        from ..models.merchant_owner import MerchantOwner
        from ..models.merchant_plan import MerchantPlan
        from ..models.merchant_reseller import MerchantReseller
        from ..models.program_expresses import ProgramExpresses
        from ..models.properties import Properties
        from ..models.tip_suggestions import TipSuggestions

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, Properties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = Properties.from_dict(_properties)

        _tip_suggestions = d.pop("tipSuggestions", UNSET)
        tip_suggestions: Union[Unset, TipSuggestions]
        if isinstance(_tip_suggestions, Unset):
            tip_suggestions = UNSET
        else:
            tip_suggestions = TipSuggestions.from_dict(_tip_suggestions)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, MerchantOwner]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = MerchantOwner.from_dict(_owner)

        _reseller = d.pop("reseller", UNSET)
        reseller: Union[Unset, MerchantReseller]
        if isinstance(_reseller, Unset):
            reseller = UNSET
        else:
            reseller = MerchantReseller.from_dict(_reseller)

        phone_number = d.pop("phoneNumber", UNSET)

        website = d.pop("website", UNSET)

        _logos = d.pop("logos", UNSET)
        logos: Union[Unset, LogoElements]
        if isinstance(_logos, Unset):
            logos = UNSET
        else:
            logos = LogoElements.from_dict(_logos)

        customer_contact_email = d.pop("customerContactEmail", UNSET)

        _compliances = d.pop("compliances", UNSET)
        compliances: Union[Unset, Compliances]
        if isinstance(_compliances, Unset):
            compliances = UNSET
        else:
            compliances = Compliances.from_dict(_compliances)

        _gateway = d.pop("gateway", UNSET)
        gateway: Union[Unset, Gateway]
        if isinstance(_gateway, Unset):
            gateway = UNSET
        else:
            gateway = Gateway.from_dict(_gateway)

        _merchant_plan = d.pop("merchantPlan", UNSET)
        merchant_plan: Union[Unset, MerchantPlan]
        if isinstance(_merchant_plan, Unset):
            merchant_plan = UNSET
        else:
            merchant_plan = MerchantPlan.from_dict(_merchant_plan)

        _merchant_boarding = d.pop("merchantBoarding", UNSET)
        merchant_boarding: Union[Unset, MerchantBoarding]
        if isinstance(_merchant_boarding, Unset):
            merchant_boarding = UNSET
        else:
            merchant_boarding = MerchantBoarding.from_dict(_merchant_boarding)

        created_time = d.pop("createdTime", UNSET)

        _equipment = d.pop("equipment", UNSET)
        equipment: Union[Unset, Equipment]
        if isinstance(_equipment, Unset):
            equipment = UNSET
        else:
            equipment = Equipment.from_dict(_equipment)

        _program_expresses = d.pop("programExpresses", UNSET)
        program_expresses: Union[Unset, ProgramExpresses]
        if isinstance(_program_expresses, Unset):
            program_expresses = UNSET
        else:
            program_expresses = ProgramExpresses.from_dict(_program_expresses)

        _address = d.pop("Address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        merchant = cls(
            id=id,
            name=name,
            properties=properties,
            tip_suggestions=tip_suggestions,
            owner=owner,
            reseller=reseller,
            phone_number=phone_number,
            website=website,
            logos=logos,
            customer_contact_email=customer_contact_email,
            compliances=compliances,
            gateway=gateway,
            merchant_plan=merchant_plan,
            merchant_boarding=merchant_boarding,
            created_time=created_time,
            equipment=equipment,
            program_expresses=program_expresses,
            address=address,
        )

        merchant.additional_properties = d
        return merchant

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
