from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.merchant_plan_mcc_match import MerchantPlanMccMatch
from ..models.merchant_plan_pricing_model import MerchantPlanPricingModel
from ..models.merchant_plan_type import MerchantPlanType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_bundle import AppBundle
    from ..models.merchant_plan_group import MerchantPlanGroup
    from ..models.modules import Modules


T = TypeVar("T", bound="MerchantPlan")


@_attrs_define
class MerchantPlan:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        merchant_plan_group (Union[Unset, MerchantPlanGroup]):
        merchant_plan_groups (Union[Unset, list['MerchantPlanGroup']]):
        app_bundle (Union[Unset, AppBundle]):
        mccs (Union[Unset, list[str]]):
        mcc_match (Union[Unset, MerchantPlanMccMatch]):
        type_ (Union[Unset, MerchantPlanType]):
        pricing_model (Union[Unset, MerchantPlanPricingModel]):
        plan_code (Union[Unset, str]):
        modules (Union[Unset, Modules]):
        hidden (Union[Unset, bool]):
        bogo (Union[Unset, bool]):
        recommended (Union[Unset, bool]):
        enforced (Union[Unset, bool]):
        weight (Union[Unset, int]):
        trial_days (Union[Unset, int]):
        trial_remaining_days (Union[Unset, int]):
        trial_expiration_time (Union[Unset, int]):
        activation_time (Union[Unset, int]):
        deactivation_time (Union[Unset, int]):
        created_time (Union[Unset, int]):
        modified_time (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    merchant_plan_group: Union[Unset, "MerchantPlanGroup"] = UNSET
    merchant_plan_groups: Union[Unset, list["MerchantPlanGroup"]] = UNSET
    app_bundle: Union[Unset, "AppBundle"] = UNSET
    mccs: Union[Unset, list[str]] = UNSET
    mcc_match: Union[Unset, MerchantPlanMccMatch] = UNSET
    type_: Union[Unset, MerchantPlanType] = UNSET
    pricing_model: Union[Unset, MerchantPlanPricingModel] = UNSET
    plan_code: Union[Unset, str] = UNSET
    modules: Union[Unset, "Modules"] = UNSET
    hidden: Union[Unset, bool] = UNSET
    bogo: Union[Unset, bool] = UNSET
    recommended: Union[Unset, bool] = UNSET
    enforced: Union[Unset, bool] = UNSET
    weight: Union[Unset, int] = UNSET
    trial_days: Union[Unset, int] = UNSET
    trial_remaining_days: Union[Unset, int] = UNSET
    trial_expiration_time: Union[Unset, int] = UNSET
    activation_time: Union[Unset, int] = UNSET
    deactivation_time: Union[Unset, int] = UNSET
    created_time: Union[Unset, int] = UNSET
    modified_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        merchant_plan_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_plan_group, Unset):
            merchant_plan_group = self.merchant_plan_group.to_dict()

        merchant_plan_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.merchant_plan_groups, Unset):
            merchant_plan_groups = []
            for merchant_plan_groups_item_data in self.merchant_plan_groups:
                merchant_plan_groups_item = merchant_plan_groups_item_data.to_dict()
                merchant_plan_groups.append(merchant_plan_groups_item)

        app_bundle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_bundle, Unset):
            app_bundle = self.app_bundle.to_dict()

        mccs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mccs, Unset):
            mccs = self.mccs

        mcc_match: Union[Unset, str] = UNSET
        if not isinstance(self.mcc_match, Unset):
            mcc_match = self.mcc_match.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        pricing_model: Union[Unset, str] = UNSET
        if not isinstance(self.pricing_model, Unset):
            pricing_model = self.pricing_model.value

        plan_code = self.plan_code

        modules: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.modules, Unset):
            modules = self.modules.to_dict()

        hidden = self.hidden

        bogo = self.bogo

        recommended = self.recommended

        enforced = self.enforced

        weight = self.weight

        trial_days = self.trial_days

        trial_remaining_days = self.trial_remaining_days

        trial_expiration_time = self.trial_expiration_time

        activation_time = self.activation_time

        deactivation_time = self.deactivation_time

        created_time = self.created_time

        modified_time = self.modified_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if merchant_plan_group is not UNSET:
            field_dict["merchantPlanGroup"] = merchant_plan_group
        if merchant_plan_groups is not UNSET:
            field_dict["merchantPlanGroups"] = merchant_plan_groups
        if app_bundle is not UNSET:
            field_dict["appBundle"] = app_bundle
        if mccs is not UNSET:
            field_dict["mccs"] = mccs
        if mcc_match is not UNSET:
            field_dict["mccMatch"] = mcc_match
        if type_ is not UNSET:
            field_dict["type"] = type_
        if pricing_model is not UNSET:
            field_dict["pricingModel"] = pricing_model
        if plan_code is not UNSET:
            field_dict["planCode"] = plan_code
        if modules is not UNSET:
            field_dict["modules"] = modules
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if bogo is not UNSET:
            field_dict["bogo"] = bogo
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if enforced is not UNSET:
            field_dict["enforced"] = enforced
        if weight is not UNSET:
            field_dict["weight"] = weight
        if trial_days is not UNSET:
            field_dict["trialDays"] = trial_days
        if trial_remaining_days is not UNSET:
            field_dict["trialRemainingDays"] = trial_remaining_days
        if trial_expiration_time is not UNSET:
            field_dict["trialExpirationTime"] = trial_expiration_time
        if activation_time is not UNSET:
            field_dict["activationTime"] = activation_time
        if deactivation_time is not UNSET:
            field_dict["deactivationTime"] = deactivation_time
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_bundle import AppBundle
        from ..models.merchant_plan_group import MerchantPlanGroup
        from ..models.modules import Modules

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _merchant_plan_group = d.pop("merchantPlanGroup", UNSET)
        merchant_plan_group: Union[Unset, MerchantPlanGroup]
        if _merchant_plan_group and not isinstance(_merchant_plan_group, Unset):
            merchant_plan_group = MerchantPlanGroup.from_dict(_merchant_plan_group)

        else:
            merchant_plan_group = UNSET

        merchant_plan_groups = []
        _merchant_plan_groups = d.pop("merchantPlanGroups", UNSET)
        for merchant_plan_groups_item_data in _merchant_plan_groups or []:
            merchant_plan_groups_item = MerchantPlanGroup.from_dict(merchant_plan_groups_item_data)

            merchant_plan_groups.append(merchant_plan_groups_item)

        _app_bundle = d.pop("appBundle", UNSET)
        app_bundle: Union[Unset, AppBundle]
        if _app_bundle and not isinstance(_app_bundle, Unset):
            app_bundle = AppBundle.from_dict(_app_bundle)

        else:
            app_bundle = UNSET

        mccs = cast(list[str], d.pop("mccs", UNSET))

        _mcc_match = d.pop("mccMatch", UNSET)
        mcc_match: Union[Unset, MerchantPlanMccMatch]
        if _mcc_match and not isinstance(_mcc_match, Unset):
            mcc_match = MerchantPlanMccMatch(_mcc_match)

        else:
            mcc_match = UNSET

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, MerchantPlanType]
        if _type_ and not isinstance(_type_, Unset):
            type_ = MerchantPlanType(_type_)

        else:
            type_ = UNSET

        _pricing_model = d.pop("pricingModel", UNSET)
        pricing_model: Union[Unset, MerchantPlanPricingModel]
        if _pricing_model and not isinstance(_pricing_model, Unset):
            pricing_model = MerchantPlanPricingModel(_pricing_model)

        else:
            pricing_model = UNSET

        plan_code = d.pop("planCode", UNSET)

        _modules = d.pop("modules", UNSET)
        modules: Union[Unset, Modules]
        if _modules and not isinstance(_modules, Unset):
            modules = Modules.from_dict(_modules)

        else:
            modules = UNSET

        hidden = d.pop("hidden", UNSET)

        bogo = d.pop("bogo", UNSET)

        recommended = d.pop("recommended", UNSET)

        enforced = d.pop("enforced", UNSET)

        weight = d.pop("weight", UNSET)

        trial_days = d.pop("trialDays", UNSET)

        trial_remaining_days = d.pop("trialRemainingDays", UNSET)

        trial_expiration_time = d.pop("trialExpirationTime", UNSET)

        activation_time = d.pop("activationTime", UNSET)

        deactivation_time = d.pop("deactivationTime", UNSET)

        created_time = d.pop("createdTime", UNSET)

        modified_time = d.pop("modifiedTime", UNSET)

        merchant_plan = cls(
            id=id,
            name=name,
            description=description,
            merchant_plan_group=merchant_plan_group,
            merchant_plan_groups=merchant_plan_groups,
            app_bundle=app_bundle,
            mccs=mccs,
            mcc_match=mcc_match,
            type_=type_,
            pricing_model=pricing_model,
            plan_code=plan_code,
            modules=modules,
            hidden=hidden,
            bogo=bogo,
            recommended=recommended,
            enforced=enforced,
            weight=weight,
            trial_days=trial_days,
            trial_remaining_days=trial_remaining_days,
            trial_expiration_time=trial_expiration_time,
            activation_time=activation_time,
            deactivation_time=deactivation_time,
            created_time=created_time,
            modified_time=modified_time,
        )

        merchant_plan.additional_properties = d
        return merchant_plan

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
