import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_revenue_modifier import ApiRevenueModifier


T = TypeVar("T", bound="ApiRevenueEvent")


@_attrs_define
class ApiRevenueEvent:
    """revenue events

    Attributes:
        tlement_action_uuid (Union[Unset, ApiRevenueEvent]): revenue events
        code (Union[Unset, str]): revenue event code
        effective_date_time (Union[Unset, datetime.datetime]): date and time that the event is effective Example:
            2020-12-31T23:59:59.123456Z.
        merch_uuid (Union[Unset, str]): 13-character UUID assigned to the merchant
        settlement_action_uuid (Union[Unset, str]): 26-character UUID of the settlement action that was the source of
            this revenue
        fee_category_group (Union[Unset, str]): the fee category grouping that was used for settled revenue
        revenue_group (Union[Unset, str]): the revenue group that was used to sub-categorize settled revenue
        merch_plan_uuid (Union[Unset, str]): 13-character UUID of the merchant plan that was the source of the revenue
        developer_uuid (Union[Unset, str]): 13-character UUID of the developer that was the source of the revenue
        dev_app_uuid (Union[Unset, str]): 13-character UUID of the developer app that was the source of the revenue
        app_sub_uuid (Union[Unset, str]): 13-character UUID of the app subscription level that was the source of the
            revenue
        app_metered_uuid (Union[Unset, str]): 13-character UUID of the app metered activity that was the source of the
            revenue
        ref (Union[Unset, str]): reference
        num_units (Union[Unset, int]): the number of billable units
        basis_units (Union[Unset, int]): the number of basis units
        basis_amt (Union[Unset, float]): the basis amount
        basis_currency (Union[Unset, str]): 3-letter currency code Example: USD.
        revenue_mods (Union[Unset, list['ApiRevenueModifier']]): revenue event modifiers
    """

    tlement_action_uuid: Union[Unset, "ApiRevenueEvent"] = UNSET
    code: Union[Unset, str] = UNSET
    effective_date_time: Union[Unset, datetime.datetime] = UNSET
    merch_uuid: Union[Unset, str] = UNSET
    settlement_action_uuid: Union[Unset, str] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    revenue_group: Union[Unset, str] = UNSET
    merch_plan_uuid: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    dev_app_uuid: Union[Unset, str] = UNSET
    app_sub_uuid: Union[Unset, str] = UNSET
    app_metered_uuid: Union[Unset, str] = UNSET
    ref: Union[Unset, str] = UNSET
    num_units: Union[Unset, int] = UNSET
    basis_units: Union[Unset, int] = UNSET
    basis_amt: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    revenue_mods: Union[Unset, list["ApiRevenueModifier"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlement_action_uuid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_action_uuid, Unset):
            tlement_action_uuid = self.tlement_action_uuid.to_dict()

        code = self.code

        effective_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date_time, Unset):
            effective_date_time = self.effective_date_time.isoformat()

        merch_uuid = self.merch_uuid

        settlement_action_uuid = self.settlement_action_uuid

        fee_category_group = self.fee_category_group

        revenue_group = self.revenue_group

        merch_plan_uuid = self.merch_plan_uuid

        developer_uuid = self.developer_uuid

        dev_app_uuid = self.dev_app_uuid

        app_sub_uuid = self.app_sub_uuid

        app_metered_uuid = self.app_metered_uuid

        ref = self.ref

        num_units = self.num_units

        basis_units = self.basis_units

        basis_amt = self.basis_amt

        basis_currency = self.basis_currency

        revenue_mods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revenue_mods, Unset):
            revenue_mods = []
            for revenue_mods_item_data in self.revenue_mods:
                revenue_mods_item = revenue_mods_item_data.to_dict()
                revenue_mods.append(revenue_mods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tlement_action_uuid is not UNSET:
            field_dict["tlementActionUuid"] = tlement_action_uuid
        if code is not UNSET:
            field_dict["code"] = code
        if effective_date_time is not UNSET:
            field_dict["effectiveDateTime"] = effective_date_time
        if merch_uuid is not UNSET:
            field_dict["merchUuid"] = merch_uuid
        if settlement_action_uuid is not UNSET:
            field_dict["settlementActionUuid"] = settlement_action_uuid
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if revenue_group is not UNSET:
            field_dict["revenueGroup"] = revenue_group
        if merch_plan_uuid is not UNSET:
            field_dict["merchPlanUuid"] = merch_plan_uuid
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if dev_app_uuid is not UNSET:
            field_dict["devAppUuid"] = dev_app_uuid
        if app_sub_uuid is not UNSET:
            field_dict["appSubUuid"] = app_sub_uuid
        if app_metered_uuid is not UNSET:
            field_dict["appMeteredUuid"] = app_metered_uuid
        if ref is not UNSET:
            field_dict["ref"] = ref
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units
        if basis_units is not UNSET:
            field_dict["basisUnits"] = basis_units
        if basis_amt is not UNSET:
            field_dict["basisAmt"] = basis_amt
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency
        if revenue_mods is not UNSET:
            field_dict["revenueMods"] = revenue_mods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_revenue_modifier import ApiRevenueModifier

        d = dict(src_dict)
        _tlement_action_uuid = d.pop("tlementActionUuid", UNSET)
        tlement_action_uuid: Union[Unset, ApiRevenueEvent]
        if _tlement_action_uuid and not isinstance(_tlement_action_uuid, Unset):
            tlement_action_uuid = ApiRevenueEvent.from_dict(_tlement_action_uuid)

        else:
            tlement_action_uuid = UNSET

        code = d.pop("code", UNSET)

        _effective_date_time = d.pop("effectiveDateTime", UNSET)
        effective_date_time: Union[Unset, datetime.datetime]
        if _effective_date_time and not isinstance(_effective_date_time, Unset):
            effective_date_time = isoparse(_effective_date_time)

        else:
            effective_date_time = UNSET

        merch_uuid = d.pop("merchUuid", UNSET)

        settlement_action_uuid = d.pop("settlementActionUuid", UNSET)

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        revenue_group = d.pop("revenueGroup", UNSET)

        merch_plan_uuid = d.pop("merchPlanUuid", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        dev_app_uuid = d.pop("devAppUuid", UNSET)

        app_sub_uuid = d.pop("appSubUuid", UNSET)

        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

        ref = d.pop("ref", UNSET)

        num_units = d.pop("numUnits", UNSET)

        basis_units = d.pop("basisUnits", UNSET)

        basis_amt = d.pop("basisAmt", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        revenue_mods = []
        _revenue_mods = d.pop("revenueMods", UNSET)
        for revenue_mods_item_data in _revenue_mods or []:
            revenue_mods_item = ApiRevenueModifier.from_dict(revenue_mods_item_data)

            revenue_mods.append(revenue_mods_item)

        api_revenue_event = cls(
            tlement_action_uuid=tlement_action_uuid,
            code=code,
            effective_date_time=effective_date_time,
            merch_uuid=merch_uuid,
            settlement_action_uuid=settlement_action_uuid,
            fee_category_group=fee_category_group,
            revenue_group=revenue_group,
            merch_plan_uuid=merch_plan_uuid,
            developer_uuid=developer_uuid,
            dev_app_uuid=dev_app_uuid,
            app_sub_uuid=app_sub_uuid,
            app_metered_uuid=app_metered_uuid,
            ref=ref,
            num_units=num_units,
            basis_units=basis_units,
            basis_amt=basis_amt,
            basis_currency=basis_currency,
            revenue_mods=revenue_mods,
        )

        api_revenue_event.additional_properties = d
        return api_revenue_event

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
