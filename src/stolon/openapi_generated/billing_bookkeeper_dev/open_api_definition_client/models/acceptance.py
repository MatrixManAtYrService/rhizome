import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.acceptance_action import AcceptanceAction
from ..models.acceptance_source import AcceptanceSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acceptance_metadata import AcceptanceMetadata
    from ..models.acceptance_template_parameters import AcceptanceTemplateParameters


T = TypeVar("T", bound="Acceptance")


@_attrs_define
class Acceptance:
    """
    Attributes:
        id (Union[Unset, UUID]):
        merchant_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        agreement_type (Union[Unset, str]):
        current (Union[Unset, bool]):
        version (Union[Unset, str]):
        agreement_id (Union[Unset, UUID]):
        signer_name (Union[Unset, str]):
        signer_signature (Union[Unset, str]):
        source (Union[Unset, AcceptanceSource]):
        origin_device_serial (Union[Unset, str]):
        device_serial_number (Union[Unset, str]):
        template_parameters (Union[Unset, AcceptanceTemplateParameters]):
        metadata (Union[Unset, AcceptanceMetadata]):
        created_time (Union[Unset, datetime.datetime]):
        expiration_date (Union[Unset, datetime.datetime]):
        deleted_time (Union[Unset, datetime.datetime]):
        modified_time (Union[Unset, datetime.datetime]):
        action (Union[Unset, AcceptanceAction]):
    """

    id: Union[Unset, UUID] = UNSET
    merchant_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    agreement_type: Union[Unset, str] = UNSET
    current: Union[Unset, bool] = UNSET
    version: Union[Unset, str] = UNSET
    agreement_id: Union[Unset, UUID] = UNSET
    signer_name: Union[Unset, str] = UNSET
    signer_signature: Union[Unset, str] = UNSET
    source: Union[Unset, AcceptanceSource] = UNSET
    origin_device_serial: Union[Unset, str] = UNSET
    device_serial_number: Union[Unset, str] = UNSET
    template_parameters: Union[Unset, "AcceptanceTemplateParameters"] = UNSET
    metadata: Union[Unset, "AcceptanceMetadata"] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    deleted_time: Union[Unset, datetime.datetime] = UNSET
    modified_time: Union[Unset, datetime.datetime] = UNSET
    action: Union[Unset, AcceptanceAction] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        merchant_id = self.merchant_id

        account_id = self.account_id

        agreement_type = self.agreement_type

        current = self.current

        version = self.version

        agreement_id: Union[Unset, str] = UNSET
        if not isinstance(self.agreement_id, Unset):
            agreement_id = str(self.agreement_id)

        signer_name = self.signer_name

        signer_signature = self.signer_signature

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        origin_device_serial = self.origin_device_serial

        device_serial_number = self.device_serial_number

        template_parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.template_parameters, Unset):
            template_parameters = self.template_parameters.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        created_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        deleted_time: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_time, Unset):
            deleted_time = self.deleted_time.isoformat()

        modified_time: Union[Unset, str] = UNSET
        if not isinstance(self.modified_time, Unset):
            modified_time = self.modified_time.isoformat()

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if merchant_id is not UNSET:
            field_dict["merchantId"] = merchant_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if agreement_type is not UNSET:
            field_dict["agreementType"] = agreement_type
        if current is not UNSET:
            field_dict["current"] = current
        if version is not UNSET:
            field_dict["version"] = version
        if agreement_id is not UNSET:
            field_dict["agreementId"] = agreement_id
        if signer_name is not UNSET:
            field_dict["signerName"] = signer_name
        if signer_signature is not UNSET:
            field_dict["signerSignature"] = signer_signature
        if source is not UNSET:
            field_dict["source"] = source
        if origin_device_serial is not UNSET:
            field_dict["originDeviceSerial"] = origin_device_serial
        if device_serial_number is not UNSET:
            field_dict["deviceSerialNumber"] = device_serial_number
        if template_parameters is not UNSET:
            field_dict["templateParameters"] = template_parameters
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if deleted_time is not UNSET:
            field_dict["deletedTime"] = deleted_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acceptance_metadata import AcceptanceMetadata
        from ..models.acceptance_template_parameters import AcceptanceTemplateParameters

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if _id and not isinstance(_id, Unset):
            id = UUID(_id)

        else:
            id = UNSET

        merchant_id = d.pop("merchantId", UNSET)

        account_id = d.pop("accountId", UNSET)

        agreement_type = d.pop("agreementType", UNSET)

        current = d.pop("current", UNSET)

        version = d.pop("version", UNSET)

        _agreement_id = d.pop("agreementId", UNSET)
        agreement_id: Union[Unset, UUID]
        if _agreement_id and not isinstance(_agreement_id, Unset):
            agreement_id = UUID(_agreement_id)

        else:
            agreement_id = UNSET

        signer_name = d.pop("signerName", UNSET)

        signer_signature = d.pop("signerSignature", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, AcceptanceSource]
        if _source and not isinstance(_source, Unset):
            source = AcceptanceSource(_source)

        else:
            source = UNSET

        origin_device_serial = d.pop("originDeviceSerial", UNSET)

        device_serial_number = d.pop("deviceSerialNumber", UNSET)

        _template_parameters = d.pop("templateParameters", UNSET)
        template_parameters: Union[Unset, AcceptanceTemplateParameters]
        if _template_parameters and not isinstance(_template_parameters, Unset):
            template_parameters = AcceptanceTemplateParameters.from_dict(_template_parameters)

        else:
            template_parameters = UNSET

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AcceptanceMetadata]
        if _metadata and not isinstance(_metadata, Unset):
            metadata = AcceptanceMetadata.from_dict(_metadata)

        else:
            metadata = UNSET

        _created_time = d.pop("createdTime", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if _created_time and not isinstance(_created_time, Unset):
            created_time = isoparse(_created_time)

        else:
            created_time = UNSET

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if _expiration_date and not isinstance(_expiration_date, Unset):
            expiration_date = isoparse(_expiration_date)

        else:
            expiration_date = UNSET

        _deleted_time = d.pop("deletedTime", UNSET)
        deleted_time: Union[Unset, datetime.datetime]
        if _deleted_time and not isinstance(_deleted_time, Unset):
            deleted_time = isoparse(_deleted_time)

        else:
            deleted_time = UNSET

        _modified_time = d.pop("modifiedTime", UNSET)
        modified_time: Union[Unset, datetime.datetime]
        if _modified_time and not isinstance(_modified_time, Unset):
            modified_time = isoparse(_modified_time)

        else:
            modified_time = UNSET

        _action = d.pop("action", UNSET)
        action: Union[Unset, AcceptanceAction]
        if _action and not isinstance(_action, Unset):
            action = AcceptanceAction(_action)

        else:
            action = UNSET

        acceptance = cls(
            id=id,
            merchant_id=merchant_id,
            account_id=account_id,
            agreement_type=agreement_type,
            current=current,
            version=version,
            agreement_id=agreement_id,
            signer_name=signer_name,
            signer_signature=signer_signature,
            source=source,
            origin_device_serial=origin_device_serial,
            device_serial_number=device_serial_number,
            template_parameters=template_parameters,
            metadata=metadata,
            created_time=created_time,
            expiration_date=expiration_date,
            deleted_time=deleted_time,
            modified_time=modified_time,
            action=action,
        )

        acceptance.additional_properties = d
        return acceptance

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
