import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_errors import ActionErrors
    from ..models.actions import Actions
    from ..models.api_billing_hierarchy_level_node import ApiBillingHierarchyLevelNode
    from ..models.billing_entity import BillingEntity
    from ..models.billing_entity_config import BillingEntityConfig
    from ..models.billing_hierarchy import BillingHierarchy
    from ..models.billing_hierarchy_cycle import BillingHierarchyCycle
    from ..models.billing_schedule import BillingSchedule
    from ..models.effective import Effective
    from ..models.fees import Fees
    from ..models.ledgers import Ledgers
    from ..models.monetary import Monetary
    from ..models.processing_group_dates import ProcessingGroupDates


T = TypeVar("T", bound="BillingEntityMinutiae")


@_attrs_define
class BillingEntityMinutiae:
    """
    Attributes:
        as_of_date (Union[Unset, datetime.date]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        limit_exceeded (Union[Unset, bool]):
        billing_entity (Union[Unset, BillingEntity]):
        effective (Union[Unset, Effective]):
        billing_schedules (Union[Unset, list['BillingSchedule']]):
        billing_hierarchies (Union[Unset, list['BillingHierarchy']]):
        billing_hierarchy_cycles (Union[Unset, list['BillingHierarchyCycle']]):
        parents (Union[Unset, list['ApiBillingHierarchyLevelNode']]):
        billing_entity_configs (Union[Unset, list['BillingEntityConfig']]):
        fees (Union[Unset, Fees]):
        actions (Union[Unset, Actions]):
        action_errors (Union[Unset, ActionErrors]):
        ledgers (Union[Unset, Ledgers]):
        monetary (Union[Unset, Monetary]):
        processing_group_dates (Union[Unset, ProcessingGroupDates]):
        effective_billing_schedule (Union[Unset, BillingSchedule]):
        effective_billing_hierarchy_cycle (Union[Unset, BillingHierarchyCycle]):
    """

    as_of_date: Union[Unset, datetime.date] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    limit: Union[Unset, int] = UNSET
    limit_exceeded: Union[Unset, bool] = UNSET
    billing_entity: Union[Unset, "BillingEntity"] = UNSET
    effective: Union[Unset, "Effective"] = UNSET
    billing_schedules: Union[Unset, list["BillingSchedule"]] = UNSET
    billing_hierarchies: Union[Unset, list["BillingHierarchy"]] = UNSET
    billing_hierarchy_cycles: Union[Unset, list["BillingHierarchyCycle"]] = UNSET
    parents: Union[Unset, list["ApiBillingHierarchyLevelNode"]] = UNSET
    billing_entity_configs: Union[Unset, list["BillingEntityConfig"]] = UNSET
    fees: Union[Unset, "Fees"] = UNSET
    actions: Union[Unset, "Actions"] = UNSET
    action_errors: Union[Unset, "ActionErrors"] = UNSET
    ledgers: Union[Unset, "Ledgers"] = UNSET
    monetary: Union[Unset, "Monetary"] = UNSET
    processing_group_dates: Union[Unset, "ProcessingGroupDates"] = UNSET
    effective_billing_schedule: Union[Unset, "BillingSchedule"] = UNSET
    effective_billing_hierarchy_cycle: Union[Unset, "BillingHierarchyCycle"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of_date: Union[Unset, str] = UNSET
        if not isinstance(self.as_of_date, Unset):
            as_of_date = self.as_of_date.isoformat()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        limit = self.limit

        limit_exceeded = self.limit_exceeded

        billing_entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_entity, Unset):
            billing_entity = self.billing_entity.to_dict()

        effective: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.effective, Unset):
            effective = self.effective.to_dict()

        billing_schedules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_schedules, Unset):
            billing_schedules = []
            for billing_schedules_item_data in self.billing_schedules:
                billing_schedules_item = billing_schedules_item_data.to_dict()
                billing_schedules.append(billing_schedules_item)

        billing_hierarchies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_hierarchies, Unset):
            billing_hierarchies = []
            for billing_hierarchies_item_data in self.billing_hierarchies:
                billing_hierarchies_item = billing_hierarchies_item_data.to_dict()
                billing_hierarchies.append(billing_hierarchies_item)

        billing_hierarchy_cycles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_hierarchy_cycles, Unset):
            billing_hierarchy_cycles = []
            for billing_hierarchy_cycles_item_data in self.billing_hierarchy_cycles:
                billing_hierarchy_cycles_item = billing_hierarchy_cycles_item_data.to_dict()
                billing_hierarchy_cycles.append(billing_hierarchy_cycles_item)

        parents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = parents_item_data.to_dict()
                parents.append(parents_item)

        billing_entity_configs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_entity_configs, Unset):
            billing_entity_configs = []
            for billing_entity_configs_item_data in self.billing_entity_configs:
                billing_entity_configs_item = billing_entity_configs_item_data.to_dict()
                billing_entity_configs.append(billing_entity_configs_item)

        fees: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = self.fees.to_dict()

        actions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        action_errors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.action_errors, Unset):
            action_errors = self.action_errors.to_dict()

        ledgers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ledgers, Unset):
            ledgers = self.ledgers.to_dict()

        monetary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monetary, Unset):
            monetary = self.monetary.to_dict()

        processing_group_dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.processing_group_dates, Unset):
            processing_group_dates = self.processing_group_dates.to_dict()

        effective_billing_schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.effective_billing_schedule, Unset):
            effective_billing_schedule = self.effective_billing_schedule.to_dict()

        effective_billing_hierarchy_cycle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.effective_billing_hierarchy_cycle, Unset):
            effective_billing_hierarchy_cycle = self.effective_billing_hierarchy_cycle.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_of_date is not UNSET:
            field_dict["asOfDate"] = as_of_date
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if limit is not UNSET:
            field_dict["limit"] = limit
        if limit_exceeded is not UNSET:
            field_dict["limitExceeded"] = limit_exceeded
        if billing_entity is not UNSET:
            field_dict["billingEntity"] = billing_entity
        if effective is not UNSET:
            field_dict["effective"] = effective
        if billing_schedules is not UNSET:
            field_dict["billingSchedules"] = billing_schedules
        if billing_hierarchies is not UNSET:
            field_dict["billingHierarchies"] = billing_hierarchies
        if billing_hierarchy_cycles is not UNSET:
            field_dict["billingHierarchyCycles"] = billing_hierarchy_cycles
        if parents is not UNSET:
            field_dict["parents"] = parents
        if billing_entity_configs is not UNSET:
            field_dict["billingEntityConfigs"] = billing_entity_configs
        if fees is not UNSET:
            field_dict["fees"] = fees
        if actions is not UNSET:
            field_dict["actions"] = actions
        if action_errors is not UNSET:
            field_dict["actionErrors"] = action_errors
        if ledgers is not UNSET:
            field_dict["ledgers"] = ledgers
        if monetary is not UNSET:
            field_dict["monetary"] = monetary
        if processing_group_dates is not UNSET:
            field_dict["processingGroupDates"] = processing_group_dates
        if effective_billing_schedule is not UNSET:
            field_dict["effectiveBillingSchedule"] = effective_billing_schedule
        if effective_billing_hierarchy_cycle is not UNSET:
            field_dict["effectiveBillingHierarchyCycle"] = effective_billing_hierarchy_cycle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_errors import ActionErrors
        from ..models.actions import Actions
        from ..models.api_billing_hierarchy_level_node import ApiBillingHierarchyLevelNode
        from ..models.billing_entity import BillingEntity
        from ..models.billing_entity_config import BillingEntityConfig
        from ..models.billing_hierarchy import BillingHierarchy
        from ..models.billing_hierarchy_cycle import BillingHierarchyCycle
        from ..models.billing_schedule import BillingSchedule
        from ..models.effective import Effective
        from ..models.fees import Fees
        from ..models.ledgers import Ledgers
        from ..models.monetary import Monetary
        from ..models.processing_group_dates import ProcessingGroupDates

        d = dict(src_dict)
        _as_of_date = d.pop("asOfDate", UNSET)
        as_of_date: Union[Unset, datetime.date]
        if _as_of_date and not isinstance(_as_of_date, Unset):
            as_of_date = isoparse(_as_of_date).date()

        else:
            as_of_date = UNSET

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if _start_date and not isinstance(_start_date, Unset):
            start_date = isoparse(_start_date).date()

        else:
            start_date = UNSET

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if _end_date and not isinstance(_end_date, Unset):
            end_date = isoparse(_end_date).date()

        else:
            end_date = UNSET

        limit = d.pop("limit", UNSET)

        limit_exceeded = d.pop("limitExceeded", UNSET)

        _billing_entity = d.pop("billingEntity", UNSET)
        billing_entity: Union[Unset, BillingEntity]
        if _billing_entity and not isinstance(_billing_entity, Unset):
            billing_entity = BillingEntity.from_dict(_billing_entity)

        else:
            billing_entity = UNSET

        _effective = d.pop("effective", UNSET)
        effective: Union[Unset, Effective]
        if _effective and not isinstance(_effective, Unset):
            effective = Effective.from_dict(_effective)

        else:
            effective = UNSET

        billing_schedules = []
        _billing_schedules = d.pop("billingSchedules", UNSET)
        for billing_schedules_item_data in _billing_schedules or []:
            billing_schedules_item = BillingSchedule.from_dict(billing_schedules_item_data)

            billing_schedules.append(billing_schedules_item)

        billing_hierarchies = []
        _billing_hierarchies = d.pop("billingHierarchies", UNSET)
        for billing_hierarchies_item_data in _billing_hierarchies or []:
            billing_hierarchies_item = BillingHierarchy.from_dict(billing_hierarchies_item_data)

            billing_hierarchies.append(billing_hierarchies_item)

        billing_hierarchy_cycles = []
        _billing_hierarchy_cycles = d.pop("billingHierarchyCycles", UNSET)
        for billing_hierarchy_cycles_item_data in _billing_hierarchy_cycles or []:
            billing_hierarchy_cycles_item = BillingHierarchyCycle.from_dict(billing_hierarchy_cycles_item_data)

            billing_hierarchy_cycles.append(billing_hierarchy_cycles_item)

        parents = []
        _parents = d.pop("parents", UNSET)
        for parents_item_data in _parents or []:
            parents_item = ApiBillingHierarchyLevelNode.from_dict(parents_item_data)

            parents.append(parents_item)

        billing_entity_configs = []
        _billing_entity_configs = d.pop("billingEntityConfigs", UNSET)
        for billing_entity_configs_item_data in _billing_entity_configs or []:
            billing_entity_configs_item = BillingEntityConfig.from_dict(billing_entity_configs_item_data)

            billing_entity_configs.append(billing_entity_configs_item)

        _fees = d.pop("fees", UNSET)
        fees: Union[Unset, Fees]
        if _fees and not isinstance(_fees, Unset):
            fees = Fees.from_dict(_fees)

        else:
            fees = UNSET

        _actions = d.pop("actions", UNSET)
        actions: Union[Unset, Actions]
        if _actions and not isinstance(_actions, Unset):
            actions = Actions.from_dict(_actions)

        else:
            actions = UNSET

        _action_errors = d.pop("actionErrors", UNSET)
        action_errors: Union[Unset, ActionErrors]
        if _action_errors and not isinstance(_action_errors, Unset):
            action_errors = ActionErrors.from_dict(_action_errors)

        else:
            action_errors = UNSET

        _ledgers = d.pop("ledgers", UNSET)
        ledgers: Union[Unset, Ledgers]
        if _ledgers and not isinstance(_ledgers, Unset):
            ledgers = Ledgers.from_dict(_ledgers)

        else:
            ledgers = UNSET

        _monetary = d.pop("monetary", UNSET)
        monetary: Union[Unset, Monetary]
        if _monetary and not isinstance(_monetary, Unset):
            monetary = Monetary.from_dict(_monetary)

        else:
            monetary = UNSET

        _processing_group_dates = d.pop("processingGroupDates", UNSET)
        processing_group_dates: Union[Unset, ProcessingGroupDates]
        if _processing_group_dates and not isinstance(_processing_group_dates, Unset):
            processing_group_dates = ProcessingGroupDates.from_dict(_processing_group_dates)

        else:
            processing_group_dates = UNSET

        _effective_billing_schedule = d.pop("effectiveBillingSchedule", UNSET)
        effective_billing_schedule: Union[Unset, BillingSchedule]
        if _effective_billing_schedule and not isinstance(_effective_billing_schedule, Unset):
            effective_billing_schedule = BillingSchedule.from_dict(_effective_billing_schedule)

        else:
            effective_billing_schedule = UNSET

        _effective_billing_hierarchy_cycle = d.pop("effectiveBillingHierarchyCycle", UNSET)
        effective_billing_hierarchy_cycle: Union[Unset, BillingHierarchyCycle]
        if _effective_billing_hierarchy_cycle and not isinstance(_effective_billing_hierarchy_cycle, Unset):
            effective_billing_hierarchy_cycle = BillingHierarchyCycle.from_dict(_effective_billing_hierarchy_cycle)

        else:
            effective_billing_hierarchy_cycle = UNSET

        billing_entity_minutiae = cls(
            as_of_date=as_of_date,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            limit_exceeded=limit_exceeded,
            billing_entity=billing_entity,
            effective=effective,
            billing_schedules=billing_schedules,
            billing_hierarchies=billing_hierarchies,
            billing_hierarchy_cycles=billing_hierarchy_cycles,
            parents=parents,
            billing_entity_configs=billing_entity_configs,
            fees=fees,
            actions=actions,
            action_errors=action_errors,
            ledgers=ledgers,
            monetary=monetary,
            processing_group_dates=processing_group_dates,
            effective_billing_schedule=effective_billing_schedule,
            effective_billing_hierarchy_cycle=effective_billing_hierarchy_cycle,
        )

        billing_entity_minutiae.additional_properties = d
        return billing_entity_minutiae

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
