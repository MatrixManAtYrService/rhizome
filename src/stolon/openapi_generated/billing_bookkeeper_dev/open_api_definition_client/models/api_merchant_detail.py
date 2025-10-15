import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMerchantDetail")


@_attrs_define
class ApiMerchantDetail:
    """
    Attributes:
        id (Union[Unset, int]): ID of the merchant detail
        uuid (Union[Unset, str]): 26-character UUID of the merchant detail
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this merchant detail belongs to
        seasonal (Union[Unset, bool]): true indicates the merchant is seasonal and only does business for a portion of
            the year; false indicates the merchant does business all year
        tax_exempt (Union[Unset, bool]): indicates whether the merchant is exempt from paying taxes
        verified_terms_acceptance (Union[Unset, bool]): true indicates that billing terms acceptance has been verified;
            false indicates that terms acceptance needs to be checked/verified
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the merchant detail was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the merchant detail was last modified
            Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this merchant detail
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    seasonal: Union[Unset, bool] = UNSET
    tax_exempt: Union[Unset, bool] = UNSET
    verified_terms_acceptance: Union[Unset, bool] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        seasonal = self.seasonal

        tax_exempt = self.tax_exempt

        verified_terms_acceptance = self.verified_terms_acceptance

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if seasonal is not UNSET:
            field_dict["seasonal"] = seasonal
        if tax_exempt is not UNSET:
            field_dict["taxExempt"] = tax_exempt
        if verified_terms_acceptance is not UNSET:
            field_dict["verifiedTermsAcceptance"] = verified_terms_acceptance
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        seasonal = d.pop("seasonal", UNSET)

        tax_exempt = d.pop("taxExempt", UNSET)

        verified_terms_acceptance = d.pop("verifiedTermsAcceptance", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if _modified_timestamp and not isinstance(_modified_timestamp, Unset):
            modified_timestamp = isoparse(_modified_timestamp)

        else:
            modified_timestamp = UNSET

        audit_id = d.pop("auditId", UNSET)

        api_merchant_detail = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            seasonal=seasonal,
            tax_exempt=tax_exempt,
            verified_terms_acceptance=verified_terms_acceptance,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_merchant_detail.additional_properties = d
        return api_merchant_detail

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
