from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_info import BankInfo
    from ..models.owner import Owner


T = TypeVar("T", bound="Developer")


@_attrs_define
class Developer:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        dob (Union[Unset, str]):
        address (Union[Unset, str]): Street address
        city (Union[Unset, str]):
        state (Union[Unset, str]): State or province
        country (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        bank_info (Union[Unset, BankInfo]):
        bank_account_region (Union[Unset, str]):
        banking_system_type (Union[Unset, str]):
        bank_routing_number (Union[Unset, str]): Bank Routing Number
        business_legal_name (Union[Unset, str]):
        has_tin (Union[Unset, bool]): Indicates whether the developer has a Tax Identification Number or not
        sensitive_data (Union[Unset, str]):
        business_address (Union[Unset, str]): Street address from business address
        business_city (Union[Unset, str]): City from business address
        business_state (Union[Unset, str]): State or province from business address
        business_country (Union[Unset, str]): Country from business address
        business_postal_code (Union[Unset, str]): Postal code from business address
        billing_status (Union[Unset, str]):
        billing_status_message (Union[Unset, str]):
        approval_status (Union[Unset, str]):
        approval_status_modified_time (Union[Unset, str]):
        accepted_agreement (Union[Unset, str]):
        pr_name (Union[Unset, str]): Name of public relations contact
        pr_email (Union[Unset, str]): Email of public relations contact
        pr_phone (Union[Unset, str]): Phone of public relations contact
        website (Union[Unset, str]):
        created_time (Union[Unset, str]):
        first_submitted_time (Union[Unset, str]):
        first_approval_time (Union[Unset, str]):
        modified_time (Union[Unset, str]):
        owner (Union[Unset, Owner]):
        app_billing_system (Union[Unset, str]):
        infolease_vendor_code (Union[Unset, str]): Vendor code that identifies developer to settlement processor
        infolease_gl_code (Union[Unset, str]): General Ledger code for the developer
        rev_share (Union[Unset, int]): Revenue share percentage with 2 implied decimal places
        is_rev_share_flat_rate (Union[Unset, str]):
        rev_share_effective_time (Union[Unset, str]):
        emergency_email (Union[Unset, str]):
        developer_type (Union[Unset, str]): Indicates external third-party, second-party, Clover, and Clover-Connect
            developers
        collection_approval_status (Union[Unset, str]):
        tin_dps_uuid (Union[Unset, str]):
        vat_dps_uuid (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    dob: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    bank_info: Union[Unset, "BankInfo"] = UNSET
    bank_account_region: Union[Unset, str] = UNSET
    banking_system_type: Union[Unset, str] = UNSET
    bank_routing_number: Union[Unset, str] = UNSET
    business_legal_name: Union[Unset, str] = UNSET
    has_tin: Union[Unset, bool] = UNSET
    sensitive_data: Union[Unset, str] = UNSET
    business_address: Union[Unset, str] = UNSET
    business_city: Union[Unset, str] = UNSET
    business_state: Union[Unset, str] = UNSET
    business_country: Union[Unset, str] = UNSET
    business_postal_code: Union[Unset, str] = UNSET
    billing_status: Union[Unset, str] = UNSET
    billing_status_message: Union[Unset, str] = UNSET
    approval_status: Union[Unset, str] = UNSET
    approval_status_modified_time: Union[Unset, str] = UNSET
    accepted_agreement: Union[Unset, str] = UNSET
    pr_name: Union[Unset, str] = UNSET
    pr_email: Union[Unset, str] = UNSET
    pr_phone: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    created_time: Union[Unset, str] = UNSET
    first_submitted_time: Union[Unset, str] = UNSET
    first_approval_time: Union[Unset, str] = UNSET
    modified_time: Union[Unset, str] = UNSET
    owner: Union[Unset, "Owner"] = UNSET
    app_billing_system: Union[Unset, str] = UNSET
    infolease_vendor_code: Union[Unset, str] = UNSET
    infolease_gl_code: Union[Unset, str] = UNSET
    rev_share: Union[Unset, int] = UNSET
    is_rev_share_flat_rate: Union[Unset, str] = UNSET
    rev_share_effective_time: Union[Unset, str] = UNSET
    emergency_email: Union[Unset, str] = UNSET
    developer_type: Union[Unset, str] = UNSET
    collection_approval_status: Union[Unset, str] = UNSET
    tin_dps_uuid: Union[Unset, str] = UNSET
    vat_dps_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone = self.phone

        dob = self.dob

        address = self.address

        city = self.city

        state = self.state

        country = self.country

        postal_code = self.postal_code

        bank_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_info, Unset):
            bank_info = self.bank_info.to_dict()

        bank_account_region = self.bank_account_region

        banking_system_type = self.banking_system_type

        bank_routing_number = self.bank_routing_number

        business_legal_name = self.business_legal_name

        has_tin = self.has_tin

        sensitive_data = self.sensitive_data

        business_address = self.business_address

        business_city = self.business_city

        business_state = self.business_state

        business_country = self.business_country

        business_postal_code = self.business_postal_code

        billing_status = self.billing_status

        billing_status_message = self.billing_status_message

        approval_status = self.approval_status

        approval_status_modified_time = self.approval_status_modified_time

        accepted_agreement = self.accepted_agreement

        pr_name = self.pr_name

        pr_email = self.pr_email

        pr_phone = self.pr_phone

        website = self.website

        created_time = self.created_time

        first_submitted_time = self.first_submitted_time

        first_approval_time = self.first_approval_time

        modified_time = self.modified_time

        owner: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        app_billing_system = self.app_billing_system

        infolease_vendor_code = self.infolease_vendor_code

        infolease_gl_code = self.infolease_gl_code

        rev_share = self.rev_share

        is_rev_share_flat_rate = self.is_rev_share_flat_rate

        rev_share_effective_time = self.rev_share_effective_time

        emergency_email = self.emergency_email

        developer_type = self.developer_type

        collection_approval_status = self.collection_approval_status

        tin_dps_uuid = self.tin_dps_uuid

        vat_dps_uuid = self.vat_dps_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if dob is not UNSET:
            field_dict["dob"] = dob
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if bank_info is not UNSET:
            field_dict["bankInfo"] = bank_info
        if bank_account_region is not UNSET:
            field_dict["bankAccountRegion"] = bank_account_region
        if banking_system_type is not UNSET:
            field_dict["bankingSystemType"] = banking_system_type
        if bank_routing_number is not UNSET:
            field_dict["bankRoutingNumber"] = bank_routing_number
        if business_legal_name is not UNSET:
            field_dict["businessLegalName"] = business_legal_name
        if has_tin is not UNSET:
            field_dict["hasTin"] = has_tin
        if sensitive_data is not UNSET:
            field_dict["sensitiveData"] = sensitive_data
        if business_address is not UNSET:
            field_dict["businessAddress"] = business_address
        if business_city is not UNSET:
            field_dict["businessCity"] = business_city
        if business_state is not UNSET:
            field_dict["businessState"] = business_state
        if business_country is not UNSET:
            field_dict["businessCountry"] = business_country
        if business_postal_code is not UNSET:
            field_dict["businessPostalCode"] = business_postal_code
        if billing_status is not UNSET:
            field_dict["billingStatus"] = billing_status
        if billing_status_message is not UNSET:
            field_dict["billingStatusMessage"] = billing_status_message
        if approval_status is not UNSET:
            field_dict["approvalStatus"] = approval_status
        if approval_status_modified_time is not UNSET:
            field_dict["approvalStatusModifiedTime"] = approval_status_modified_time
        if accepted_agreement is not UNSET:
            field_dict["acceptedAgreement"] = accepted_agreement
        if pr_name is not UNSET:
            field_dict["prName"] = pr_name
        if pr_email is not UNSET:
            field_dict["prEmail"] = pr_email
        if pr_phone is not UNSET:
            field_dict["prPhone"] = pr_phone
        if website is not UNSET:
            field_dict["website"] = website
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if first_submitted_time is not UNSET:
            field_dict["firstSubmittedTime"] = first_submitted_time
        if first_approval_time is not UNSET:
            field_dict["firstApprovalTime"] = first_approval_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time
        if owner is not UNSET:
            field_dict["owner"] = owner
        if app_billing_system is not UNSET:
            field_dict["appBillingSystem"] = app_billing_system
        if infolease_vendor_code is not UNSET:
            field_dict["infoleaseVendorCode"] = infolease_vendor_code
        if infolease_gl_code is not UNSET:
            field_dict["infoleaseGlCode"] = infolease_gl_code
        if rev_share is not UNSET:
            field_dict["revShare"] = rev_share
        if is_rev_share_flat_rate is not UNSET:
            field_dict["isRevShareFlatRate"] = is_rev_share_flat_rate
        if rev_share_effective_time is not UNSET:
            field_dict["revShareEffectiveTime"] = rev_share_effective_time
        if emergency_email is not UNSET:
            field_dict["emergencyEmail"] = emergency_email
        if developer_type is not UNSET:
            field_dict["developerType"] = developer_type
        if collection_approval_status is not UNSET:
            field_dict["collectionApprovalStatus"] = collection_approval_status
        if tin_dps_uuid is not UNSET:
            field_dict["tinDpsUuid"] = tin_dps_uuid
        if vat_dps_uuid is not UNSET:
            field_dict["vatDpsUuid"] = vat_dps_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bank_info import BankInfo
        from ..models.owner import Owner

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        dob = d.pop("dob", UNSET)

        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        _bank_info = d.pop("bankInfo", UNSET)
        bank_info: Union[Unset, BankInfo]
        if _bank_info and not isinstance(_bank_info, Unset):
            bank_info = BankInfo.from_dict(_bank_info)

        else:
            bank_info = UNSET

        bank_account_region = d.pop("bankAccountRegion", UNSET)

        banking_system_type = d.pop("bankingSystemType", UNSET)

        bank_routing_number = d.pop("bankRoutingNumber", UNSET)

        business_legal_name = d.pop("businessLegalName", UNSET)

        has_tin = d.pop("hasTin", UNSET)

        sensitive_data = d.pop("sensitiveData", UNSET)

        business_address = d.pop("businessAddress", UNSET)

        business_city = d.pop("businessCity", UNSET)

        business_state = d.pop("businessState", UNSET)

        business_country = d.pop("businessCountry", UNSET)

        business_postal_code = d.pop("businessPostalCode", UNSET)

        billing_status = d.pop("billingStatus", UNSET)

        billing_status_message = d.pop("billingStatusMessage", UNSET)

        approval_status = d.pop("approvalStatus", UNSET)

        approval_status_modified_time = d.pop("approvalStatusModifiedTime", UNSET)

        accepted_agreement = d.pop("acceptedAgreement", UNSET)

        pr_name = d.pop("prName", UNSET)

        pr_email = d.pop("prEmail", UNSET)

        pr_phone = d.pop("prPhone", UNSET)

        website = d.pop("website", UNSET)

        created_time = d.pop("createdTime", UNSET)

        first_submitted_time = d.pop("firstSubmittedTime", UNSET)

        first_approval_time = d.pop("firstApprovalTime", UNSET)

        modified_time = d.pop("modifiedTime", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, Owner]
        if _owner and not isinstance(_owner, Unset):
            owner = Owner.from_dict(_owner)

        else:
            owner = UNSET

        app_billing_system = d.pop("appBillingSystem", UNSET)

        infolease_vendor_code = d.pop("infoleaseVendorCode", UNSET)

        infolease_gl_code = d.pop("infoleaseGlCode", UNSET)

        rev_share = d.pop("revShare", UNSET)

        is_rev_share_flat_rate = d.pop("isRevShareFlatRate", UNSET)

        rev_share_effective_time = d.pop("revShareEffectiveTime", UNSET)

        emergency_email = d.pop("emergencyEmail", UNSET)

        developer_type = d.pop("developerType", UNSET)

        collection_approval_status = d.pop("collectionApprovalStatus", UNSET)

        tin_dps_uuid = d.pop("tinDpsUuid", UNSET)

        vat_dps_uuid = d.pop("vatDpsUuid", UNSET)

        developer = cls(
            id=id,
            name=name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            dob=dob,
            address=address,
            city=city,
            state=state,
            country=country,
            postal_code=postal_code,
            bank_info=bank_info,
            bank_account_region=bank_account_region,
            banking_system_type=banking_system_type,
            bank_routing_number=bank_routing_number,
            business_legal_name=business_legal_name,
            has_tin=has_tin,
            sensitive_data=sensitive_data,
            business_address=business_address,
            business_city=business_city,
            business_state=business_state,
            business_country=business_country,
            business_postal_code=business_postal_code,
            billing_status=billing_status,
            billing_status_message=billing_status_message,
            approval_status=approval_status,
            approval_status_modified_time=approval_status_modified_time,
            accepted_agreement=accepted_agreement,
            pr_name=pr_name,
            pr_email=pr_email,
            pr_phone=pr_phone,
            website=website,
            created_time=created_time,
            first_submitted_time=first_submitted_time,
            first_approval_time=first_approval_time,
            modified_time=modified_time,
            owner=owner,
            app_billing_system=app_billing_system,
            infolease_vendor_code=infolease_vendor_code,
            infolease_gl_code=infolease_gl_code,
            rev_share=rev_share,
            is_rev_share_flat_rate=is_rev_share_flat_rate,
            rev_share_effective_time=rev_share_effective_time,
            emergency_email=emergency_email,
            developer_type=developer_type,
            collection_approval_status=collection_approval_status,
            tin_dps_uuid=tin_dps_uuid,
            vat_dps_uuid=vat_dps_uuid,
        )

        developer.additional_properties = d
        return developer

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
