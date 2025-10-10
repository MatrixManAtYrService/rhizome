import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProcessingGroupDates")


@_attrs_define
class ApiProcessingGroupDates:
    """
    Attributes:
        tlement_date (Union[Unset, ApiProcessingGroupDates]):
        id (Union[Unset, int]): Id of the processing group dates
        uuid (Union[Unset, str]): 26-character UUID of the processing group dates
        billing_entity_name (Union[Unset, str]): name of the processing group billing entity
        billing_entity_uuid (Union[Unset, str]): UUID of the processing group billing entity associated with the dates
        hierarchy_type (Union[Unset, str]): billing hierarchy type value
        cycle_date (Union[Unset, datetime.date]): current cycle date for the processing group
        last_cycle_date (Union[Unset, datetime.date]): last, or previous, cycle date for the processing group
        posting_date (Union[Unset, datetime.date]): current posting date for the processing group
        last_posting_date (Union[Unset, datetime.date]): last, or previous, posting date for the processing group
        billing_date (Union[Unset, datetime.date]): current billing date for the processing group
        last_billing_date (Union[Unset, datetime.date]): last, or previous, billing date for the processing group
        settlement_date (Union[Unset, datetime.date]): current settlement date for the processing group
        last_settlement_date (Union[Unset, datetime.date]): last, or previous, settlement date for the processing group
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the processing group dates record was
            created Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the processing group dates record was
            last modified Example: 2020-12-31T23:59:59.123456Z.
    """

    tlement_date: Union[Unset, "ApiProcessingGroupDates"] = UNSET
    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    cycle_date: Union[Unset, datetime.date] = UNSET
    last_cycle_date: Union[Unset, datetime.date] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    last_posting_date: Union[Unset, datetime.date] = UNSET
    billing_date: Union[Unset, datetime.date] = UNSET
    last_billing_date: Union[Unset, datetime.date] = UNSET
    settlement_date: Union[Unset, datetime.date] = UNSET
    last_settlement_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlement_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_date, Unset):
            tlement_date = self.tlement_date.to_dict()

        id = self.id

        uuid = self.uuid

        billing_entity_name = self.billing_entity_name

        billing_entity_uuid = self.billing_entity_uuid

        hierarchy_type = self.hierarchy_type

        cycle_date: Union[Unset, str] = UNSET
        if not isinstance(self.cycle_date, Unset):
            cycle_date = self.cycle_date.isoformat()

        last_cycle_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_cycle_date, Unset):
            last_cycle_date = self.last_cycle_date.isoformat()

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        last_posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_posting_date, Unset):
            last_posting_date = self.last_posting_date.isoformat()

        billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.billing_date, Unset):
            billing_date = self.billing_date.isoformat()

        last_billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_billing_date, Unset):
            last_billing_date = self.last_billing_date.isoformat()

        settlement_date: Union[Unset, str] = UNSET
        if not isinstance(self.settlement_date, Unset):
            settlement_date = self.settlement_date.isoformat()

        last_settlement_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_settlement_date, Unset):
            last_settlement_date = self.last_settlement_date.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tlement_date is not UNSET:
            field_dict["tlementDate"] = tlement_date
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_name is not UNSET:
            field_dict["billingEntityName"] = billing_entity_name
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if cycle_date is not UNSET:
            field_dict["cycleDate"] = cycle_date
        if last_cycle_date is not UNSET:
            field_dict["lastCycleDate"] = last_cycle_date
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date
        if last_posting_date is not UNSET:
            field_dict["lastPostingDate"] = last_posting_date
        if billing_date is not UNSET:
            field_dict["billingDate"] = billing_date
        if last_billing_date is not UNSET:
            field_dict["lastBillingDate"] = last_billing_date
        if settlement_date is not UNSET:
            field_dict["settlementDate"] = settlement_date
        if last_settlement_date is not UNSET:
            field_dict["lastSettlementDate"] = last_settlement_date
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tlement_date = d.pop("tlementDate", UNSET)
        tlement_date: Union[Unset, ApiProcessingGroupDates]
        if _tlement_date and not isinstance(_tlement_date, Unset):
            tlement_date = ApiProcessingGroupDates.from_dict(_tlement_date)

        else:
            tlement_date = UNSET

        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        _cycle_date = d.pop("cycleDate", UNSET)
        cycle_date: Union[Unset, datetime.date]
        if _cycle_date and not isinstance(_cycle_date, Unset):
            cycle_date = isoparse(_cycle_date).date()

        else:
            cycle_date = UNSET

        _last_cycle_date = d.pop("lastCycleDate", UNSET)
        last_cycle_date: Union[Unset, datetime.date]
        if _last_cycle_date and not isinstance(_last_cycle_date, Unset):
            last_cycle_date = isoparse(_last_cycle_date).date()

        else:
            last_cycle_date = UNSET

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if _posting_date and not isinstance(_posting_date, Unset):
            posting_date = isoparse(_posting_date).date()

        else:
            posting_date = UNSET

        _last_posting_date = d.pop("lastPostingDate", UNSET)
        last_posting_date: Union[Unset, datetime.date]
        if _last_posting_date and not isinstance(_last_posting_date, Unset):
            last_posting_date = isoparse(_last_posting_date).date()

        else:
            last_posting_date = UNSET

        _billing_date = d.pop("billingDate", UNSET)
        billing_date: Union[Unset, datetime.date]
        if _billing_date and not isinstance(_billing_date, Unset):
            billing_date = isoparse(_billing_date).date()

        else:
            billing_date = UNSET

        _last_billing_date = d.pop("lastBillingDate", UNSET)
        last_billing_date: Union[Unset, datetime.date]
        if _last_billing_date and not isinstance(_last_billing_date, Unset):
            last_billing_date = isoparse(_last_billing_date).date()

        else:
            last_billing_date = UNSET

        _settlement_date = d.pop("settlementDate", UNSET)
        settlement_date: Union[Unset, datetime.date]
        if _settlement_date and not isinstance(_settlement_date, Unset):
            settlement_date = isoparse(_settlement_date).date()

        else:
            settlement_date = UNSET

        _last_settlement_date = d.pop("lastSettlementDate", UNSET)
        last_settlement_date: Union[Unset, datetime.date]
        if _last_settlement_date and not isinstance(_last_settlement_date, Unset):
            last_settlement_date = isoparse(_last_settlement_date).date()

        else:
            last_settlement_date = UNSET

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

        api_processing_group_dates = cls(
            tlement_date=tlement_date,
            id=id,
            uuid=uuid,
            billing_entity_name=billing_entity_name,
            billing_entity_uuid=billing_entity_uuid,
            hierarchy_type=hierarchy_type,
            cycle_date=cycle_date,
            last_cycle_date=last_cycle_date,
            posting_date=posting_date,
            last_posting_date=last_posting_date,
            billing_date=billing_date,
            last_billing_date=last_billing_date,
            settlement_date=settlement_date,
            last_settlement_date=last_settlement_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_processing_group_dates.additional_properties = d
        return api_processing_group_dates

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
