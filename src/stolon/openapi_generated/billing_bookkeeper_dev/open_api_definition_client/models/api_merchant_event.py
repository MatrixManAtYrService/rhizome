import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_merchant_event_status_change import ApiMerchantEventStatusChange
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_attribute import ApiAttribute


T = TypeVar("T", bound="ApiMerchantEvent")


@_attrs_define
class ApiMerchantEvent:
    """merchant events

    Attributes:
        code (Union[Unset, str]): merchant event code
        effective_date_time (Union[Unset, datetime.datetime]): date and time that the event is effective Example:
            2020-12-31T23:59:59.123456Z.
        merch_uuid (Union[Unset, str]): 13-character UUID assigned to the merchant
        merch_name (Union[Unset, str]): The name of the merchant
        reseller_uuid (Union[Unset, str]): 13-character UUID assigned to the reseller
        is_test_merchant (Union[Unset, bool]): used to indicate that the merchant is a demo/test merchant
        status_change (Union[Unset, ApiMerchantEventStatusChange]):
        merch_attributes (Union[Unset, list['ApiAttribute']]): merchant attributes
    """

    code: Union[Unset, str] = UNSET
    effective_date_time: Union[Unset, datetime.datetime] = UNSET
    merch_uuid: Union[Unset, str] = UNSET
    merch_name: Union[Unset, str] = UNSET
    reseller_uuid: Union[Unset, str] = UNSET
    is_test_merchant: Union[Unset, bool] = UNSET
    status_change: Union[Unset, ApiMerchantEventStatusChange] = UNSET
    merch_attributes: Union[Unset, list["ApiAttribute"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        effective_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date_time, Unset):
            effective_date_time = self.effective_date_time.isoformat()

        merch_uuid = self.merch_uuid

        merch_name = self.merch_name

        reseller_uuid = self.reseller_uuid

        is_test_merchant = self.is_test_merchant

        status_change: Union[Unset, str] = UNSET
        if not isinstance(self.status_change, Unset):
            status_change = self.status_change.value

        merch_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.merch_attributes, Unset):
            merch_attributes = []
            for merch_attributes_item_data in self.merch_attributes:
                merch_attributes_item = merch_attributes_item_data.to_dict()
                merch_attributes.append(merch_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if effective_date_time is not UNSET:
            field_dict["effectiveDateTime"] = effective_date_time
        if merch_uuid is not UNSET:
            field_dict["merchUuid"] = merch_uuid
        if merch_name is not UNSET:
            field_dict["merchName"] = merch_name
        if reseller_uuid is not UNSET:
            field_dict["resellerUuid"] = reseller_uuid
        if is_test_merchant is not UNSET:
            field_dict["isTestMerchant"] = is_test_merchant
        if status_change is not UNSET:
            field_dict["statusChange"] = status_change
        if merch_attributes is not UNSET:
            field_dict["merchAttributes"] = merch_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_attribute import ApiAttribute

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _effective_date_time = d.pop("effectiveDateTime", UNSET)
        effective_date_time: Union[Unset, datetime.datetime]
        if _effective_date_time and not isinstance(_effective_date_time, Unset):
            effective_date_time = isoparse(_effective_date_time)

        else:
            effective_date_time = UNSET

        merch_uuid = d.pop("merchUuid", UNSET)

        merch_name = d.pop("merchName", UNSET)

        reseller_uuid = d.pop("resellerUuid", UNSET)

        is_test_merchant = d.pop("isTestMerchant", UNSET)

        _status_change = d.pop("statusChange", UNSET)
        status_change: Union[Unset, ApiMerchantEventStatusChange]
        if _status_change and not isinstance(_status_change, Unset):
            status_change = ApiMerchantEventStatusChange(_status_change)

        else:
            status_change = UNSET

        merch_attributes = []
        _merch_attributes = d.pop("merchAttributes", UNSET)
        for merch_attributes_item_data in _merch_attributes or []:
            merch_attributes_item = ApiAttribute.from_dict(merch_attributes_item_data)

            merch_attributes.append(merch_attributes_item)

        api_merchant_event = cls(
            code=code,
            effective_date_time=effective_date_time,
            merch_uuid=merch_uuid,
            merch_name=merch_name,
            reseller_uuid=reseller_uuid,
            is_test_merchant=is_test_merchant,
            status_change=status_change,
            merch_attributes=merch_attributes,
        )

        api_merchant_event.additional_properties = d
        return api_merchant_event

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
