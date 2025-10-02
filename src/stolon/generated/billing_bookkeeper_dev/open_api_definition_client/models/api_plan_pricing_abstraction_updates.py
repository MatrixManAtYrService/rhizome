from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_fee_code import ApiFeeCode
    from ..models.api_fee_rate import ApiFeeRate
    from ..models.api_plan_action_fee_code import ApiPlanActionFeeCode


T = TypeVar("T", bound="ApiPlanPricingAbstractionUpdates")


@_attrs_define
class ApiPlanPricingAbstractionUpdates:
    """
    Attributes:
        fee_code_inserts (Union[Unset, list['ApiFeeCode']]): All fee code records that will be added
        plan_action_fee_code_inserts (Union[Unset, list['ApiPlanActionFeeCode']]): All plan action fee code records that
            will be added
        plan_action_fee_code_updates (Union[Unset, list['ApiPlanActionFeeCode']]): All plan action fee code records that
            will be updated.  This would be used for a soft-delete.
        plan_action_fee_code_deletes (Union[Unset, list['ApiPlanActionFeeCode']]): All plan action fee code records that
            will be deleted.  These are records that never were effective and no longer needed.
        fee_rate_inserts (Union[Unset, list['ApiFeeRate']]): All fee rate records that will be added
        fee_rate_updates (Union[Unset, list['ApiFeeRate']]): All fee rate records that will be updated.  These are
            records that changed but were never effective.
        fee_rate_deletes (Union[Unset, list['ApiFeeRate']]): All fee rate records that will be deleted.
    """

    fee_code_inserts: Union[Unset, list["ApiFeeCode"]] = UNSET
    plan_action_fee_code_inserts: Union[Unset, list["ApiPlanActionFeeCode"]] = UNSET
    plan_action_fee_code_updates: Union[Unset, list["ApiPlanActionFeeCode"]] = UNSET
    plan_action_fee_code_deletes: Union[Unset, list["ApiPlanActionFeeCode"]] = UNSET
    fee_rate_inserts: Union[Unset, list["ApiFeeRate"]] = UNSET
    fee_rate_updates: Union[Unset, list["ApiFeeRate"]] = UNSET
    fee_rate_deletes: Union[Unset, list["ApiFeeRate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_code_inserts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_code_inserts, Unset):
            fee_code_inserts = []
            for fee_code_inserts_item_data in self.fee_code_inserts:
                fee_code_inserts_item = fee_code_inserts_item_data.to_dict()
                fee_code_inserts.append(fee_code_inserts_item)

        plan_action_fee_code_inserts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_action_fee_code_inserts, Unset):
            plan_action_fee_code_inserts = []
            for plan_action_fee_code_inserts_item_data in self.plan_action_fee_code_inserts:
                plan_action_fee_code_inserts_item = plan_action_fee_code_inserts_item_data.to_dict()
                plan_action_fee_code_inserts.append(plan_action_fee_code_inserts_item)

        plan_action_fee_code_updates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_action_fee_code_updates, Unset):
            plan_action_fee_code_updates = []
            for plan_action_fee_code_updates_item_data in self.plan_action_fee_code_updates:
                plan_action_fee_code_updates_item = plan_action_fee_code_updates_item_data.to_dict()
                plan_action_fee_code_updates.append(plan_action_fee_code_updates_item)

        plan_action_fee_code_deletes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_action_fee_code_deletes, Unset):
            plan_action_fee_code_deletes = []
            for plan_action_fee_code_deletes_item_data in self.plan_action_fee_code_deletes:
                plan_action_fee_code_deletes_item = plan_action_fee_code_deletes_item_data.to_dict()
                plan_action_fee_code_deletes.append(plan_action_fee_code_deletes_item)

        fee_rate_inserts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_rate_inserts, Unset):
            fee_rate_inserts = []
            for fee_rate_inserts_item_data in self.fee_rate_inserts:
                fee_rate_inserts_item = fee_rate_inserts_item_data.to_dict()
                fee_rate_inserts.append(fee_rate_inserts_item)

        fee_rate_updates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_rate_updates, Unset):
            fee_rate_updates = []
            for fee_rate_updates_item_data in self.fee_rate_updates:
                fee_rate_updates_item = fee_rate_updates_item_data.to_dict()
                fee_rate_updates.append(fee_rate_updates_item)

        fee_rate_deletes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_rate_deletes, Unset):
            fee_rate_deletes = []
            for fee_rate_deletes_item_data in self.fee_rate_deletes:
                fee_rate_deletes_item = fee_rate_deletes_item_data.to_dict()
                fee_rate_deletes.append(fee_rate_deletes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_code_inserts is not UNSET:
            field_dict["feeCodeInserts"] = fee_code_inserts
        if plan_action_fee_code_inserts is not UNSET:
            field_dict["planActionFeeCodeInserts"] = plan_action_fee_code_inserts
        if plan_action_fee_code_updates is not UNSET:
            field_dict["planActionFeeCodeUpdates"] = plan_action_fee_code_updates
        if plan_action_fee_code_deletes is not UNSET:
            field_dict["planActionFeeCodeDeletes"] = plan_action_fee_code_deletes
        if fee_rate_inserts is not UNSET:
            field_dict["feeRateInserts"] = fee_rate_inserts
        if fee_rate_updates is not UNSET:
            field_dict["feeRateUpdates"] = fee_rate_updates
        if fee_rate_deletes is not UNSET:
            field_dict["feeRateDeletes"] = fee_rate_deletes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_fee_code import ApiFeeCode
        from ..models.api_fee_rate import ApiFeeRate
        from ..models.api_plan_action_fee_code import ApiPlanActionFeeCode

        d = dict(src_dict)
        fee_code_inserts = []
        _fee_code_inserts = d.pop("feeCodeInserts", UNSET)
        for fee_code_inserts_item_data in _fee_code_inserts or []:
            fee_code_inserts_item = ApiFeeCode.from_dict(fee_code_inserts_item_data)

            fee_code_inserts.append(fee_code_inserts_item)

        plan_action_fee_code_inserts = []
        _plan_action_fee_code_inserts = d.pop("planActionFeeCodeInserts", UNSET)
        for plan_action_fee_code_inserts_item_data in _plan_action_fee_code_inserts or []:
            plan_action_fee_code_inserts_item = ApiPlanActionFeeCode.from_dict(plan_action_fee_code_inserts_item_data)

            plan_action_fee_code_inserts.append(plan_action_fee_code_inserts_item)

        plan_action_fee_code_updates = []
        _plan_action_fee_code_updates = d.pop("planActionFeeCodeUpdates", UNSET)
        for plan_action_fee_code_updates_item_data in _plan_action_fee_code_updates or []:
            plan_action_fee_code_updates_item = ApiPlanActionFeeCode.from_dict(plan_action_fee_code_updates_item_data)

            plan_action_fee_code_updates.append(plan_action_fee_code_updates_item)

        plan_action_fee_code_deletes = []
        _plan_action_fee_code_deletes = d.pop("planActionFeeCodeDeletes", UNSET)
        for plan_action_fee_code_deletes_item_data in _plan_action_fee_code_deletes or []:
            plan_action_fee_code_deletes_item = ApiPlanActionFeeCode.from_dict(plan_action_fee_code_deletes_item_data)

            plan_action_fee_code_deletes.append(plan_action_fee_code_deletes_item)

        fee_rate_inserts = []
        _fee_rate_inserts = d.pop("feeRateInserts", UNSET)
        for fee_rate_inserts_item_data in _fee_rate_inserts or []:
            fee_rate_inserts_item = ApiFeeRate.from_dict(fee_rate_inserts_item_data)

            fee_rate_inserts.append(fee_rate_inserts_item)

        fee_rate_updates = []
        _fee_rate_updates = d.pop("feeRateUpdates", UNSET)
        for fee_rate_updates_item_data in _fee_rate_updates or []:
            fee_rate_updates_item = ApiFeeRate.from_dict(fee_rate_updates_item_data)

            fee_rate_updates.append(fee_rate_updates_item)

        fee_rate_deletes = []
        _fee_rate_deletes = d.pop("feeRateDeletes", UNSET)
        for fee_rate_deletes_item_data in _fee_rate_deletes or []:
            fee_rate_deletes_item = ApiFeeRate.from_dict(fee_rate_deletes_item_data)

            fee_rate_deletes.append(fee_rate_deletes_item)

        api_plan_pricing_abstraction_updates = cls(
            fee_code_inserts=fee_code_inserts,
            plan_action_fee_code_inserts=plan_action_fee_code_inserts,
            plan_action_fee_code_updates=plan_action_fee_code_updates,
            plan_action_fee_code_deletes=plan_action_fee_code_deletes,
            fee_rate_inserts=fee_rate_inserts,
            fee_rate_updates=fee_rate_updates,
            fee_rate_deletes=fee_rate_deletes,
        )

        api_plan_pricing_abstraction_updates.additional_properties = d
        return api_plan_pricing_abstraction_updates

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
