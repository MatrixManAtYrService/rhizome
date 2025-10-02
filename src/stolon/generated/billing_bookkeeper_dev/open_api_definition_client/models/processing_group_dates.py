import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessingGroupDates")


@_attrs_define
class ProcessingGroupDates:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        billing_entity_name (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        hierarchy_type (Union[Unset, str]):
        cycle_date (Union[Unset, datetime.date]):
        last_cycle_date (Union[Unset, datetime.date]):
        posting_date (Union[Unset, datetime.date]):
        last_posting_date (Union[Unset, datetime.date]):
        billing_date (Union[Unset, datetime.date]):
        last_billing_date (Union[Unset, datetime.date]):
        settlement_date (Union[Unset, datetime.date]):
        last_settlement_date (Union[Unset, datetime.date]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
    """

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
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        _cycle_date = d.pop("cycleDate", UNSET)
        cycle_date: Union[Unset, datetime.date]
        if isinstance(_cycle_date, Unset):
            cycle_date = UNSET
        else:
            cycle_date = isoparse(_cycle_date).date()

        _last_cycle_date = d.pop("lastCycleDate", UNSET)
        last_cycle_date: Union[Unset, datetime.date]
        if isinstance(_last_cycle_date, Unset):
            last_cycle_date = UNSET
        else:
            last_cycle_date = isoparse(_last_cycle_date).date()

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if isinstance(_posting_date, Unset):
            posting_date = UNSET
        else:
            posting_date = isoparse(_posting_date).date()

        _last_posting_date = d.pop("lastPostingDate", UNSET)
        last_posting_date: Union[Unset, datetime.date]
        if isinstance(_last_posting_date, Unset):
            last_posting_date = UNSET
        else:
            last_posting_date = isoparse(_last_posting_date).date()

        _billing_date = d.pop("billingDate", UNSET)
        billing_date: Union[Unset, datetime.date]
        if isinstance(_billing_date, Unset):
            billing_date = UNSET
        else:
            billing_date = isoparse(_billing_date).date()

        _last_billing_date = d.pop("lastBillingDate", UNSET)
        last_billing_date: Union[Unset, datetime.date]
        if isinstance(_last_billing_date, Unset):
            last_billing_date = UNSET
        else:
            last_billing_date = isoparse(_last_billing_date).date()

        _settlement_date = d.pop("settlementDate", UNSET)
        settlement_date: Union[Unset, datetime.date]
        if isinstance(_settlement_date, Unset):
            settlement_date = UNSET
        else:
            settlement_date = isoparse(_settlement_date).date()

        _last_settlement_date = d.pop("lastSettlementDate", UNSET)
        last_settlement_date: Union[Unset, datetime.date]
        if isinstance(_last_settlement_date, Unset):
            last_settlement_date = UNSET
        else:
            last_settlement_date = isoparse(_last_settlement_date).date()

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_modified_timestamp, Unset):
            modified_timestamp = UNSET
        else:
            modified_timestamp = isoparse(_modified_timestamp)

        processing_group_dates = cls(
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

        processing_group_dates.additional_properties = d
        return processing_group_dates

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
