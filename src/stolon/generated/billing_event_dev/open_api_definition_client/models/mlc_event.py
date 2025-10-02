import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.mlc_event_event_type import MlcEventEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_data import DeviceData
    from ..models.device_shipping_data import DeviceShippingData
    from ..models.merchant_accoun_status_change_data import MerchantAccounStatusChangeData
    from ..models.merchant_account_activated_data import MerchantAccountActivatedData
    from ..models.merchant_bank_account_change_data import MerchantBankAccountChangeData
    from ..models.merchant_created_data import MerchantCreatedData
    from ..models.merchant_modified_data import MerchantModifiedData
    from ..models.merchant_owner_email_change_data import MerchantOwnerEmailChangeData
    from ..models.merchant_plan_change_data import MerchantPlanChangeData
    from ..models.merchant_shell_created_data import MerchantShellCreatedData
    from ..models.program_express_code_data import ProgramExpressCodeData
    from ..models.reseller_device_assignment_data import ResellerDeviceAssignmentData
    from ..models.schema import Schema
    from ..models.specific_data import SpecificData


T = TypeVar("T", bound="MlcEvent")


@_attrs_define
class MlcEvent:
    """
    Attributes:
        event_type (Union[Unset, MlcEventEventType]):
        source_url (Union[Unset, str]):
        event_date (Union[Unset, datetime.datetime]):
        merchant_bank_account_change (Union[Unset, MerchantBankAccountChangeData]):
        merchant_owner_email_change (Union[Unset, MerchantOwnerEmailChangeData]):
        merchant_account_status_change (Union[Unset, MerchantAccounStatusChangeData]):
        device (Union[Unset, DeviceData]):
        shipped_device (Union[Unset, DeviceShippingData]):
        program_express_code (Union[Unset, ProgramExpressCodeData]):
        merchant_modified (Union[Unset, MerchantModifiedData]):
        merchant_plan_change (Union[Unset, MerchantPlanChangeData]):
        merchant_created (Union[Unset, MerchantCreatedData]):
        reseller_device_assignment (Union[Unset, ResellerDeviceAssignmentData]):
        merchant_account_activated (Union[Unset, MerchantAccountActivatedData]):
        event_uuid (Union[Unset, str]):
        merchant_shell_created (Union[Unset, MerchantShellCreatedData]):
        version (Union[Unset, int]):
        specific_data (Union[Unset, SpecificData]):
        schema (Union[Unset, Schema]):
    """

    event_type: Union[Unset, MlcEventEventType] = UNSET
    source_url: Union[Unset, str] = UNSET
    event_date: Union[Unset, datetime.datetime] = UNSET
    merchant_bank_account_change: Union[Unset, "MerchantBankAccountChangeData"] = UNSET
    merchant_owner_email_change: Union[Unset, "MerchantOwnerEmailChangeData"] = UNSET
    merchant_account_status_change: Union[Unset, "MerchantAccounStatusChangeData"] = UNSET
    device: Union[Unset, "DeviceData"] = UNSET
    shipped_device: Union[Unset, "DeviceShippingData"] = UNSET
    program_express_code: Union[Unset, "ProgramExpressCodeData"] = UNSET
    merchant_modified: Union[Unset, "MerchantModifiedData"] = UNSET
    merchant_plan_change: Union[Unset, "MerchantPlanChangeData"] = UNSET
    merchant_created: Union[Unset, "MerchantCreatedData"] = UNSET
    reseller_device_assignment: Union[Unset, "ResellerDeviceAssignmentData"] = UNSET
    merchant_account_activated: Union[Unset, "MerchantAccountActivatedData"] = UNSET
    event_uuid: Union[Unset, str] = UNSET
    merchant_shell_created: Union[Unset, "MerchantShellCreatedData"] = UNSET
    version: Union[Unset, int] = UNSET
    specific_data: Union[Unset, "SpecificData"] = UNSET
    schema: Union[Unset, "Schema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        source_url = self.source_url

        event_date: Union[Unset, str] = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.isoformat()

        merchant_bank_account_change: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_bank_account_change, Unset):
            merchant_bank_account_change = self.merchant_bank_account_change.to_dict()

        merchant_owner_email_change: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_owner_email_change, Unset):
            merchant_owner_email_change = self.merchant_owner_email_change.to_dict()

        merchant_account_status_change: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_account_status_change, Unset):
            merchant_account_status_change = self.merchant_account_status_change.to_dict()

        device: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device, Unset):
            device = self.device.to_dict()

        shipped_device: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipped_device, Unset):
            shipped_device = self.shipped_device.to_dict()

        program_express_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_express_code, Unset):
            program_express_code = self.program_express_code.to_dict()

        merchant_modified: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_modified, Unset):
            merchant_modified = self.merchant_modified.to_dict()

        merchant_plan_change: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_plan_change, Unset):
            merchant_plan_change = self.merchant_plan_change.to_dict()

        merchant_created: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_created, Unset):
            merchant_created = self.merchant_created.to_dict()

        reseller_device_assignment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reseller_device_assignment, Unset):
            reseller_device_assignment = self.reseller_device_assignment.to_dict()

        merchant_account_activated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_account_activated, Unset):
            merchant_account_activated = self.merchant_account_activated.to_dict()

        event_uuid = self.event_uuid

        merchant_shell_created: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_shell_created, Unset):
            merchant_shell_created = self.merchant_shell_created.to_dict()

        version = self.version

        specific_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.specific_data, Unset):
            specific_data = self.specific_data.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if merchant_bank_account_change is not UNSET:
            field_dict["merchantBankAccountChange"] = merchant_bank_account_change
        if merchant_owner_email_change is not UNSET:
            field_dict["merchantOwnerEmailChange"] = merchant_owner_email_change
        if merchant_account_status_change is not UNSET:
            field_dict["merchantAccountStatusChange"] = merchant_account_status_change
        if device is not UNSET:
            field_dict["device"] = device
        if shipped_device is not UNSET:
            field_dict["shippedDevice"] = shipped_device
        if program_express_code is not UNSET:
            field_dict["programExpressCode"] = program_express_code
        if merchant_modified is not UNSET:
            field_dict["merchantModified"] = merchant_modified
        if merchant_plan_change is not UNSET:
            field_dict["merchantPlanChange"] = merchant_plan_change
        if merchant_created is not UNSET:
            field_dict["merchantCreated"] = merchant_created
        if reseller_device_assignment is not UNSET:
            field_dict["resellerDeviceAssignment"] = reseller_device_assignment
        if merchant_account_activated is not UNSET:
            field_dict["merchantAccountActivated"] = merchant_account_activated
        if event_uuid is not UNSET:
            field_dict["eventUuid"] = event_uuid
        if merchant_shell_created is not UNSET:
            field_dict["merchantShellCreated"] = merchant_shell_created
        if version is not UNSET:
            field_dict["version"] = version
        if specific_data is not UNSET:
            field_dict["specificData"] = specific_data
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_data import DeviceData
        from ..models.device_shipping_data import DeviceShippingData
        from ..models.merchant_accoun_status_change_data import MerchantAccounStatusChangeData
        from ..models.merchant_account_activated_data import MerchantAccountActivatedData
        from ..models.merchant_bank_account_change_data import MerchantBankAccountChangeData
        from ..models.merchant_created_data import MerchantCreatedData
        from ..models.merchant_modified_data import MerchantModifiedData
        from ..models.merchant_owner_email_change_data import MerchantOwnerEmailChangeData
        from ..models.merchant_plan_change_data import MerchantPlanChangeData
        from ..models.merchant_shell_created_data import MerchantShellCreatedData
        from ..models.program_express_code_data import ProgramExpressCodeData
        from ..models.reseller_device_assignment_data import ResellerDeviceAssignmentData
        from ..models.schema import Schema
        from ..models.specific_data import SpecificData

        d = dict(src_dict)
        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, MlcEventEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = MlcEventEventType(_event_type)

        source_url = d.pop("sourceUrl", UNSET)

        _event_date = d.pop("eventDate", UNSET)
        event_date: Union[Unset, datetime.datetime]
        if isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = isoparse(_event_date)

        _merchant_bank_account_change = d.pop("merchantBankAccountChange", UNSET)
        merchant_bank_account_change: Union[Unset, MerchantBankAccountChangeData]
        if isinstance(_merchant_bank_account_change, Unset):
            merchant_bank_account_change = UNSET
        else:
            merchant_bank_account_change = MerchantBankAccountChangeData.from_dict(_merchant_bank_account_change)

        _merchant_owner_email_change = d.pop("merchantOwnerEmailChange", UNSET)
        merchant_owner_email_change: Union[Unset, MerchantOwnerEmailChangeData]
        if isinstance(_merchant_owner_email_change, Unset):
            merchant_owner_email_change = UNSET
        else:
            merchant_owner_email_change = MerchantOwnerEmailChangeData.from_dict(_merchant_owner_email_change)

        _merchant_account_status_change = d.pop("merchantAccountStatusChange", UNSET)
        merchant_account_status_change: Union[Unset, MerchantAccounStatusChangeData]
        if isinstance(_merchant_account_status_change, Unset):
            merchant_account_status_change = UNSET
        else:
            merchant_account_status_change = MerchantAccounStatusChangeData.from_dict(_merchant_account_status_change)

        _device = d.pop("device", UNSET)
        device: Union[Unset, DeviceData]
        if isinstance(_device, Unset):
            device = UNSET
        else:
            device = DeviceData.from_dict(_device)

        _shipped_device = d.pop("shippedDevice", UNSET)
        shipped_device: Union[Unset, DeviceShippingData]
        if isinstance(_shipped_device, Unset):
            shipped_device = UNSET
        else:
            shipped_device = DeviceShippingData.from_dict(_shipped_device)

        _program_express_code = d.pop("programExpressCode", UNSET)
        program_express_code: Union[Unset, ProgramExpressCodeData]
        if isinstance(_program_express_code, Unset):
            program_express_code = UNSET
        else:
            program_express_code = ProgramExpressCodeData.from_dict(_program_express_code)

        _merchant_modified = d.pop("merchantModified", UNSET)
        merchant_modified: Union[Unset, MerchantModifiedData]
        if isinstance(_merchant_modified, Unset):
            merchant_modified = UNSET
        else:
            merchant_modified = MerchantModifiedData.from_dict(_merchant_modified)

        _merchant_plan_change = d.pop("merchantPlanChange", UNSET)
        merchant_plan_change: Union[Unset, MerchantPlanChangeData]
        if isinstance(_merchant_plan_change, Unset):
            merchant_plan_change = UNSET
        else:
            merchant_plan_change = MerchantPlanChangeData.from_dict(_merchant_plan_change)

        _merchant_created = d.pop("merchantCreated", UNSET)
        merchant_created: Union[Unset, MerchantCreatedData]
        if isinstance(_merchant_created, Unset):
            merchant_created = UNSET
        else:
            merchant_created = MerchantCreatedData.from_dict(_merchant_created)

        _reseller_device_assignment = d.pop("resellerDeviceAssignment", UNSET)
        reseller_device_assignment: Union[Unset, ResellerDeviceAssignmentData]
        if isinstance(_reseller_device_assignment, Unset):
            reseller_device_assignment = UNSET
        else:
            reseller_device_assignment = ResellerDeviceAssignmentData.from_dict(_reseller_device_assignment)

        _merchant_account_activated = d.pop("merchantAccountActivated", UNSET)
        merchant_account_activated: Union[Unset, MerchantAccountActivatedData]
        if isinstance(_merchant_account_activated, Unset):
            merchant_account_activated = UNSET
        else:
            merchant_account_activated = MerchantAccountActivatedData.from_dict(_merchant_account_activated)

        event_uuid = d.pop("eventUuid", UNSET)

        _merchant_shell_created = d.pop("merchantShellCreated", UNSET)
        merchant_shell_created: Union[Unset, MerchantShellCreatedData]
        if isinstance(_merchant_shell_created, Unset):
            merchant_shell_created = UNSET
        else:
            merchant_shell_created = MerchantShellCreatedData.from_dict(_merchant_shell_created)

        version = d.pop("version", UNSET)

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

        mlc_event = cls(
            event_type=event_type,
            source_url=source_url,
            event_date=event_date,
            merchant_bank_account_change=merchant_bank_account_change,
            merchant_owner_email_change=merchant_owner_email_change,
            merchant_account_status_change=merchant_account_status_change,
            device=device,
            shipped_device=shipped_device,
            program_express_code=program_express_code,
            merchant_modified=merchant_modified,
            merchant_plan_change=merchant_plan_change,
            merchant_created=merchant_created,
            reseller_device_assignment=reseller_device_assignment,
            merchant_account_activated=merchant_account_activated,
            event_uuid=event_uuid,
            merchant_shell_created=merchant_shell_created,
            version=version,
            specific_data=specific_data,
            schema=schema,
        )

        mlc_event.additional_properties = d
        return mlc_event

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
