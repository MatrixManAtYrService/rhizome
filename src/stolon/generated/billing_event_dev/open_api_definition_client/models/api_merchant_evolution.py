import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_merchant_evolution_billable_merchant_type import ApiMerchantEvolutionBillableMerchantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMerchantEvolution")


@_attrs_define
class ApiMerchantEvolution:
    """
    Attributes:
        id (Union[Unset, int]): ID of the merchant evolution
        merchant_uuid (Union[Unset, str]): 13-character COS UUID for the merchant
        reseller_uuid (Union[Unset, str]): 13-character COS UUID for the reseller that the merchant belongs to
        merchant_name (Union[Unset, str]): the name of the merchant
        seasonal (Union[Unset, bool]): true indicates the merchant is seasonal and only does business for a portion of
            the year; false indicates the merchant does business all year
        tax_exempt (Union[Unset, bool]): indicates whether the merchant is exempt from paying taxes
        billable_merchant_type (Union[Unset, ApiMerchantEvolutionBillableMerchantType]):
        created_in_bookkeeper_datetime (Union[Unset, datetime.datetime]): date and time when the merchant was created in
            bookkeeper Example: 2020-12-31T23:59:59.123456Z.
        mlc_merchant_created_event_datetime (Union[Unset, datetime.datetime]): date and time of the MLC merchant-created
            event Example: 2020-12-31T23:59:59.123456Z.
        mlc_merchant_created_event_uuid (Union[Unset, str]): 26-character UUID for the MLC merchant-created event
        terms_accepted_datetime (Union[Unset, datetime.datetime]): date and time when billing terms were accepted by the
            merchant Example: 2020-12-31T23:59:59.123456Z.
        agreement_event_uuid (Union[Unset, str]): 26-character UUID for the Agreement event for the billing terms
            acceptance
        close_date (Union[Unset, datetime.date]): the date when the merchant closed
        effective_close_date (Union[Unset, datetime.date]): the date when the close became effective
        mlc_close_event_uuid (Union[Unset, str]): 26-character UUID for the MLC merchant-status-changed event which
            closed the merchant
        created_timestamp (Union[Unset, datetime.datetime]): timestamp for when the merchant evolution data was first
            created Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): timestamp for when the merchant evolution data was most
            recently modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    reseller_uuid: Union[Unset, str] = UNSET
    merchant_name: Union[Unset, str] = UNSET
    seasonal: Union[Unset, bool] = UNSET
    tax_exempt: Union[Unset, bool] = UNSET
    billable_merchant_type: Union[Unset, ApiMerchantEvolutionBillableMerchantType] = UNSET
    created_in_bookkeeper_datetime: Union[Unset, datetime.datetime] = UNSET
    mlc_merchant_created_event_datetime: Union[Unset, datetime.datetime] = UNSET
    mlc_merchant_created_event_uuid: Union[Unset, str] = UNSET
    terms_accepted_datetime: Union[Unset, datetime.datetime] = UNSET
    agreement_event_uuid: Union[Unset, str] = UNSET
    close_date: Union[Unset, datetime.date] = UNSET
    effective_close_date: Union[Unset, datetime.date] = UNSET
    mlc_close_event_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        merchant_uuid = self.merchant_uuid

        reseller_uuid = self.reseller_uuid

        merchant_name = self.merchant_name

        seasonal = self.seasonal

        tax_exempt = self.tax_exempt

        billable_merchant_type: Union[Unset, str] = UNSET
        if not isinstance(self.billable_merchant_type, Unset):
            billable_merchant_type = self.billable_merchant_type.value

        created_in_bookkeeper_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.created_in_bookkeeper_datetime, Unset):
            created_in_bookkeeper_datetime = self.created_in_bookkeeper_datetime.isoformat()

        mlc_merchant_created_event_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.mlc_merchant_created_event_datetime, Unset):
            mlc_merchant_created_event_datetime = self.mlc_merchant_created_event_datetime.isoformat()

        mlc_merchant_created_event_uuid = self.mlc_merchant_created_event_uuid

        terms_accepted_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.terms_accepted_datetime, Unset):
            terms_accepted_datetime = self.terms_accepted_datetime.isoformat()

        agreement_event_uuid = self.agreement_event_uuid

        close_date: Union[Unset, str] = UNSET
        if not isinstance(self.close_date, Unset):
            close_date = self.close_date.isoformat()

        effective_close_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_close_date, Unset):
            effective_close_date = self.effective_close_date.isoformat()

        mlc_close_event_uuid = self.mlc_close_event_uuid

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
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if reseller_uuid is not UNSET:
            field_dict["resellerUuid"] = reseller_uuid
        if merchant_name is not UNSET:
            field_dict["merchantName"] = merchant_name
        if seasonal is not UNSET:
            field_dict["seasonal"] = seasonal
        if tax_exempt is not UNSET:
            field_dict["taxExempt"] = tax_exempt
        if billable_merchant_type is not UNSET:
            field_dict["billableMerchantType"] = billable_merchant_type
        if created_in_bookkeeper_datetime is not UNSET:
            field_dict["createdInBookkeeperDatetime"] = created_in_bookkeeper_datetime
        if mlc_merchant_created_event_datetime is not UNSET:
            field_dict["mlcMerchantCreatedEventDatetime"] = mlc_merchant_created_event_datetime
        if mlc_merchant_created_event_uuid is not UNSET:
            field_dict["mlcMerchantCreatedEventUuid"] = mlc_merchant_created_event_uuid
        if terms_accepted_datetime is not UNSET:
            field_dict["termsAcceptedDatetime"] = terms_accepted_datetime
        if agreement_event_uuid is not UNSET:
            field_dict["agreementEventUuid"] = agreement_event_uuid
        if close_date is not UNSET:
            field_dict["closeDate"] = close_date
        if effective_close_date is not UNSET:
            field_dict["effectiveCloseDate"] = effective_close_date
        if mlc_close_event_uuid is not UNSET:
            field_dict["mlcCloseEventUuid"] = mlc_close_event_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        reseller_uuid = d.pop("resellerUuid", UNSET)

        merchant_name = d.pop("merchantName", UNSET)

        seasonal = d.pop("seasonal", UNSET)

        tax_exempt = d.pop("taxExempt", UNSET)

        _billable_merchant_type = d.pop("billableMerchantType", UNSET)
        billable_merchant_type: Union[Unset, ApiMerchantEvolutionBillableMerchantType]
        if _billable_merchant_type and not isinstance(_billable_merchant_type, Unset):
            billable_merchant_type = ApiMerchantEvolutionBillableMerchantType(_billable_merchant_type)

        else:
            billable_merchant_type = UNSET

        _created_in_bookkeeper_datetime = d.pop("createdInBookkeeperDatetime", UNSET)
        created_in_bookkeeper_datetime: Union[Unset, datetime.datetime]
        if _created_in_bookkeeper_datetime and not isinstance(_created_in_bookkeeper_datetime, Unset):
            created_in_bookkeeper_datetime = isoparse(_created_in_bookkeeper_datetime)

        else:
            created_in_bookkeeper_datetime = UNSET

        _mlc_merchant_created_event_datetime = d.pop("mlcMerchantCreatedEventDatetime", UNSET)
        mlc_merchant_created_event_datetime: Union[Unset, datetime.datetime]
        if _mlc_merchant_created_event_datetime and not isinstance(_mlc_merchant_created_event_datetime, Unset):
            mlc_merchant_created_event_datetime = isoparse(_mlc_merchant_created_event_datetime)

        else:
            mlc_merchant_created_event_datetime = UNSET

        mlc_merchant_created_event_uuid = d.pop("mlcMerchantCreatedEventUuid", UNSET)

        _terms_accepted_datetime = d.pop("termsAcceptedDatetime", UNSET)
        terms_accepted_datetime: Union[Unset, datetime.datetime]
        if _terms_accepted_datetime and not isinstance(_terms_accepted_datetime, Unset):
            terms_accepted_datetime = isoparse(_terms_accepted_datetime)

        else:
            terms_accepted_datetime = UNSET

        agreement_event_uuid = d.pop("agreementEventUuid", UNSET)

        _close_date = d.pop("closeDate", UNSET)
        close_date: Union[Unset, datetime.date]
        if _close_date and not isinstance(_close_date, Unset):
            close_date = isoparse(_close_date).date()

        else:
            close_date = UNSET

        _effective_close_date = d.pop("effectiveCloseDate", UNSET)
        effective_close_date: Union[Unset, datetime.date]
        if _effective_close_date and not isinstance(_effective_close_date, Unset):
            effective_close_date = isoparse(_effective_close_date).date()

        else:
            effective_close_date = UNSET

        mlc_close_event_uuid = d.pop("mlcCloseEventUuid", UNSET)

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

        api_merchant_evolution = cls(
            id=id,
            merchant_uuid=merchant_uuid,
            reseller_uuid=reseller_uuid,
            merchant_name=merchant_name,
            seasonal=seasonal,
            tax_exempt=tax_exempt,
            billable_merchant_type=billable_merchant_type,
            created_in_bookkeeper_datetime=created_in_bookkeeper_datetime,
            mlc_merchant_created_event_datetime=mlc_merchant_created_event_datetime,
            mlc_merchant_created_event_uuid=mlc_merchant_created_event_uuid,
            terms_accepted_datetime=terms_accepted_datetime,
            agreement_event_uuid=agreement_event_uuid,
            close_date=close_date,
            effective_close_date=effective_close_date,
            mlc_close_event_uuid=mlc_close_event_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_merchant_evolution.additional_properties = d
        return api_merchant_evolution

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
