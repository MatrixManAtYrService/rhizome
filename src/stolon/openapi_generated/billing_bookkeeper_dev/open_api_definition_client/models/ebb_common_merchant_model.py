from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ebb_device_provision import EbbDeviceProvision
    from ..models.ebb_gateway import EbbGateway
    from ..models.ebb_merchant import EbbMerchant
    from ..models.ebb_merchant_boarding import EbbMerchantBoarding
    from ..models.ebb_merchant_plan import EbbMerchantPlan
    from ..models.ebb_merchant_plan_history import EbbMerchantPlanHistory


T = TypeVar("T", bound="EbbCommonMerchantModel")


@_attrs_define
class EbbCommonMerchantModel:
    """
    Attributes:
        environment (Union[Unset, str]):
        merchant (Union[Unset, EbbMerchant]):
        merchant_plan (Union[Unset, EbbMerchantPlan]):
        merchant_plan_histories (Union[Unset, list['EbbMerchantPlanHistory']]):
        device_provisions (Union[Unset, list['EbbDeviceProvision']]):
        merchant_boarding (Union[Unset, EbbMerchantBoarding]):
        gateway (Union[Unset, EbbGateway]):
    """

    environment: Union[Unset, str] = UNSET
    merchant: Union[Unset, "EbbMerchant"] = UNSET
    merchant_plan: Union[Unset, "EbbMerchantPlan"] = UNSET
    merchant_plan_histories: Union[Unset, list["EbbMerchantPlanHistory"]] = UNSET
    device_provisions: Union[Unset, list["EbbDeviceProvision"]] = UNSET
    merchant_boarding: Union[Unset, "EbbMerchantBoarding"] = UNSET
    gateway: Union[Unset, "EbbGateway"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment = self.environment

        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        merchant_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_plan, Unset):
            merchant_plan = self.merchant_plan.to_dict()

        merchant_plan_histories: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.merchant_plan_histories, Unset):
            merchant_plan_histories = []
            for merchant_plan_histories_item_data in self.merchant_plan_histories:
                merchant_plan_histories_item = merchant_plan_histories_item_data.to_dict()
                merchant_plan_histories.append(merchant_plan_histories_item)

        device_provisions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_provisions, Unset):
            device_provisions = []
            for device_provisions_item_data in self.device_provisions:
                device_provisions_item = device_provisions_item_data.to_dict()
                device_provisions.append(device_provisions_item)

        merchant_boarding: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant_boarding, Unset):
            merchant_boarding = self.merchant_boarding.to_dict()

        gateway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if environment is not UNSET:
            field_dict["environment"] = environment
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if merchant_plan is not UNSET:
            field_dict["merchantPlan"] = merchant_plan
        if merchant_plan_histories is not UNSET:
            field_dict["merchantPlanHistories"] = merchant_plan_histories
        if device_provisions is not UNSET:
            field_dict["deviceProvisions"] = device_provisions
        if merchant_boarding is not UNSET:
            field_dict["merchantBoarding"] = merchant_boarding
        if gateway is not UNSET:
            field_dict["gateway"] = gateway

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ebb_device_provision import EbbDeviceProvision
        from ..models.ebb_gateway import EbbGateway
        from ..models.ebb_merchant import EbbMerchant
        from ..models.ebb_merchant_boarding import EbbMerchantBoarding
        from ..models.ebb_merchant_plan import EbbMerchantPlan
        from ..models.ebb_merchant_plan_history import EbbMerchantPlanHistory

        d = dict(src_dict)
        environment = d.pop("environment", UNSET)

        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, EbbMerchant]
        if _merchant and not isinstance(_merchant, Unset):
            merchant = EbbMerchant.from_dict(_merchant)

        else:
            merchant = UNSET

        _merchant_plan = d.pop("merchantPlan", UNSET)
        merchant_plan: Union[Unset, EbbMerchantPlan]
        if _merchant_plan and not isinstance(_merchant_plan, Unset):
            merchant_plan = EbbMerchantPlan.from_dict(_merchant_plan)

        else:
            merchant_plan = UNSET

        merchant_plan_histories = []
        _merchant_plan_histories = d.pop("merchantPlanHistories", UNSET)
        for merchant_plan_histories_item_data in _merchant_plan_histories or []:
            merchant_plan_histories_item = EbbMerchantPlanHistory.from_dict(merchant_plan_histories_item_data)

            merchant_plan_histories.append(merchant_plan_histories_item)

        device_provisions = []
        _device_provisions = d.pop("deviceProvisions", UNSET)
        for device_provisions_item_data in _device_provisions or []:
            device_provisions_item = EbbDeviceProvision.from_dict(device_provisions_item_data)

            device_provisions.append(device_provisions_item)

        _merchant_boarding = d.pop("merchantBoarding", UNSET)
        merchant_boarding: Union[Unset, EbbMerchantBoarding]
        if _merchant_boarding and not isinstance(_merchant_boarding, Unset):
            merchant_boarding = EbbMerchantBoarding.from_dict(_merchant_boarding)

        else:
            merchant_boarding = UNSET

        _gateway = d.pop("gateway", UNSET)
        gateway: Union[Unset, EbbGateway]
        if _gateway and not isinstance(_gateway, Unset):
            gateway = EbbGateway.from_dict(_gateway)

        else:
            gateway = UNSET

        ebb_common_merchant_model = cls(
            environment=environment,
            merchant=merchant,
            merchant_plan=merchant_plan,
            merchant_plan_histories=merchant_plan_histories,
            device_provisions=device_provisions,
            merchant_boarding=merchant_boarding,
            gateway=gateway,
        )

        ebb_common_merchant_model.additional_properties = d
        return ebb_common_merchant_model

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
