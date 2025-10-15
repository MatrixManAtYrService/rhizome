import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_merchant_acceptance_action import ApiMerchantAcceptanceAction
from ..models.api_merchant_acceptance_agreement_event_type import ApiMerchantAcceptanceAgreementEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMerchantAcceptance")


@_attrs_define
class ApiMerchantAcceptance:
    """
    Attributes:
        id (Union[Unset, int]): ID of the merchant acceptance
        uuid (Union[Unset, str]): 26-character UUID assigned to the merchant acceptance
        merchant_uuid (Union[Unset, str]): 13-character COS UUID for the merchant that the acceptance belongs to
        account_id (Union[Unset, str]): 13-character COS UUID for the account owner
        acceptance_id (Union[Unset, str]): the ID assigned to the acceptance by the Agreement service
        agreement_id (Union[Unset, str]): the ID assigned to the agreement by the Agreement service
        agreement_type (Union[Unset, str]): the type of agreement that was accepted
        agreement_event_type (Union[Unset, ApiMerchantAcceptanceAgreementEventType]):
        action (Union[Unset, ApiMerchantAcceptanceAction]):
        acceptance_created_datetime (Union[Unset, datetime.datetime]): date and time when the acceptance was created in
            the Agreement service Example: 2020-12-31T23:59:59.123456Z.
        acceptance_modified_datetime (Union[Unset, datetime.datetime]): date and time when the acceptance was most
            recently modified in the Agreement service Example: 2020-12-31T23:59:59.123456Z.
        acceptance_deleted_datetime (Union[Unset, datetime.datetime]): date and time when the acceptance was soft-
            deleted in the Agreement service Example: 2020-12-31T23:59:59.123456Z.
        acceptance_expiration_datetime (Union[Unset, datetime.datetime]): date and time when the acceptance expired (or
            became stale) in the Agreement service Example: 2020-12-31T23:59:59.123456Z.
        serial_number (Union[Unset, str]): serial number for a merchant's device that was included for the date break
        iccid (Union[Unset, str]): the integrated circuit card identifier (ICCID) for the SIM associated with the device
            serial number
        is_oobe (Union[Unset, bool]): was the acceptance created during OOBE
        created_timestamp (Union[Unset, datetime.datetime]): timestamp for when the merchant acceptance was first
            created in the scratchpad Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): timestamp for when the merchant acceptance data was most
            recently modified in the scratchpad Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    acceptance_id: Union[Unset, str] = UNSET
    agreement_id: Union[Unset, str] = UNSET
    agreement_type: Union[Unset, str] = UNSET
    agreement_event_type: Union[Unset, ApiMerchantAcceptanceAgreementEventType] = UNSET
    action: Union[Unset, ApiMerchantAcceptanceAction] = UNSET
    acceptance_created_datetime: Union[Unset, datetime.datetime] = UNSET
    acceptance_modified_datetime: Union[Unset, datetime.datetime] = UNSET
    acceptance_deleted_datetime: Union[Unset, datetime.datetime] = UNSET
    acceptance_expiration_datetime: Union[Unset, datetime.datetime] = UNSET
    serial_number: Union[Unset, str] = UNSET
    iccid: Union[Unset, str] = UNSET
    is_oobe: Union[Unset, bool] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        merchant_uuid = self.merchant_uuid

        account_id = self.account_id

        acceptance_id = self.acceptance_id

        agreement_id = self.agreement_id

        agreement_type = self.agreement_type

        agreement_event_type: Union[Unset, str] = UNSET
        if not isinstance(self.agreement_event_type, Unset):
            agreement_event_type = self.agreement_event_type.value

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        acceptance_created_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.acceptance_created_datetime, Unset):
            acceptance_created_datetime = self.acceptance_created_datetime.isoformat()

        acceptance_modified_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.acceptance_modified_datetime, Unset):
            acceptance_modified_datetime = self.acceptance_modified_datetime.isoformat()

        acceptance_deleted_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.acceptance_deleted_datetime, Unset):
            acceptance_deleted_datetime = self.acceptance_deleted_datetime.isoformat()

        acceptance_expiration_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.acceptance_expiration_datetime, Unset):
            acceptance_expiration_datetime = self.acceptance_expiration_datetime.isoformat()

        serial_number = self.serial_number

        iccid = self.iccid

        is_oobe = self.is_oobe

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if acceptance_id is not UNSET:
            field_dict["acceptanceId"] = acceptance_id
        if agreement_id is not UNSET:
            field_dict["agreementId"] = agreement_id
        if agreement_type is not UNSET:
            field_dict["agreementType"] = agreement_type
        if agreement_event_type is not UNSET:
            field_dict["agreementEventType"] = agreement_event_type
        if action is not UNSET:
            field_dict["action"] = action
        if acceptance_created_datetime is not UNSET:
            field_dict["acceptanceCreatedDatetime"] = acceptance_created_datetime
        if acceptance_modified_datetime is not UNSET:
            field_dict["acceptanceModifiedDatetime"] = acceptance_modified_datetime
        if acceptance_deleted_datetime is not UNSET:
            field_dict["acceptanceDeletedDatetime"] = acceptance_deleted_datetime
        if acceptance_expiration_datetime is not UNSET:
            field_dict["acceptanceExpirationDatetime"] = acceptance_expiration_datetime
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if iccid is not UNSET:
            field_dict["iccid"] = iccid
        if is_oobe is not UNSET:
            field_dict["isOobe"] = is_oobe
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        account_id = d.pop("accountId", UNSET)

        acceptance_id = d.pop("acceptanceId", UNSET)

        agreement_id = d.pop("agreementId", UNSET)

        agreement_type = d.pop("agreementType", UNSET)

        _agreement_event_type = d.pop("agreementEventType", UNSET)
        agreement_event_type: Union[Unset, ApiMerchantAcceptanceAgreementEventType]
        if _agreement_event_type and not isinstance(_agreement_event_type, Unset):
            agreement_event_type = ApiMerchantAcceptanceAgreementEventType(_agreement_event_type)

        else:
            agreement_event_type = UNSET

        _action = d.pop("action", UNSET)
        action: Union[Unset, ApiMerchantAcceptanceAction]
        if _action and not isinstance(_action, Unset):
            action = ApiMerchantAcceptanceAction(_action)

        else:
            action = UNSET

        _acceptance_created_datetime = d.pop("acceptanceCreatedDatetime", UNSET)
        acceptance_created_datetime: Union[Unset, datetime.datetime]
        if _acceptance_created_datetime and not isinstance(_acceptance_created_datetime, Unset):
            acceptance_created_datetime = isoparse(_acceptance_created_datetime)

        else:
            acceptance_created_datetime = UNSET

        _acceptance_modified_datetime = d.pop("acceptanceModifiedDatetime", UNSET)
        acceptance_modified_datetime: Union[Unset, datetime.datetime]
        if _acceptance_modified_datetime and not isinstance(_acceptance_modified_datetime, Unset):
            acceptance_modified_datetime = isoparse(_acceptance_modified_datetime)

        else:
            acceptance_modified_datetime = UNSET

        _acceptance_deleted_datetime = d.pop("acceptanceDeletedDatetime", UNSET)
        acceptance_deleted_datetime: Union[Unset, datetime.datetime]
        if _acceptance_deleted_datetime and not isinstance(_acceptance_deleted_datetime, Unset):
            acceptance_deleted_datetime = isoparse(_acceptance_deleted_datetime)

        else:
            acceptance_deleted_datetime = UNSET

        _acceptance_expiration_datetime = d.pop("acceptanceExpirationDatetime", UNSET)
        acceptance_expiration_datetime: Union[Unset, datetime.datetime]
        if _acceptance_expiration_datetime and not isinstance(_acceptance_expiration_datetime, Unset):
            acceptance_expiration_datetime = isoparse(_acceptance_expiration_datetime)

        else:
            acceptance_expiration_datetime = UNSET

        serial_number = d.pop("serialNumber", UNSET)

        iccid = d.pop("iccid", UNSET)

        is_oobe = d.pop("isOobe", UNSET)

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

        api_merchant_acceptance = cls(
            id=id,
            uuid=uuid,
            merchant_uuid=merchant_uuid,
            account_id=account_id,
            acceptance_id=acceptance_id,
            agreement_id=agreement_id,
            agreement_type=agreement_type,
            agreement_event_type=agreement_event_type,
            action=action,
            acceptance_created_datetime=acceptance_created_datetime,
            acceptance_modified_datetime=acceptance_modified_datetime,
            acceptance_deleted_datetime=acceptance_deleted_datetime,
            acceptance_expiration_datetime=acceptance_expiration_datetime,
            serial_number=serial_number,
            iccid=iccid,
            is_oobe=is_oobe,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_merchant_acceptance.additional_properties = d
        return api_merchant_acceptance

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
