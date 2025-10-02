from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_billing_entity import ApiBillingEntity
    from ..models.api_billing_hierarchy import ApiBillingHierarchy
    from ..models.api_fee_rate import ApiFeeRate
    from ..models.api_revenue_action_fee_code import ApiRevenueActionFeeCode


T = TypeVar("T", bound="ApiRevShareAbstractionDetails")


@_attrs_define
class ApiRevShareAbstractionDetails:
    """
    Attributes:
        revenue_action_fee_codes (Union[Unset, list['ApiRevenueActionFeeCode']]): All revenue action fee code records
            used by this revenue share abstraction.
        reseller_fee_rate_entity (Union[Unset, ApiBillingEntity]):
        reseller_fee_rate_hierarchy (Union[Unset, ApiBillingHierarchy]):
        reseller_fee_rate (Union[Unset, ApiFeeRate]): All fee rates for the owningBillingEntity that are used to build
            this abstraction
        developer_fee_rate_entity (Union[Unset, ApiBillingEntity]):
        developer_fee_rate_hierarchy (Union[Unset, ApiBillingHierarchy]):
        developer_fee_rate (Union[Unset, ApiFeeRate]): All fee rates for the owningBillingEntity that are used to build
            this abstraction
        validation_errors (Union[Unset, list[str]]): Validation errors.  Errors must be corrected manually in the
            database before the abstraction can be updated.
        validation_warnings (Union[Unset, list[str]]): Validation warnings.  Warnings should automatically be corrected
            when the abstraction is next updated.
    """

    revenue_action_fee_codes: Union[Unset, list["ApiRevenueActionFeeCode"]] = UNSET
    reseller_fee_rate_entity: Union[Unset, "ApiBillingEntity"] = UNSET
    reseller_fee_rate_hierarchy: Union[Unset, "ApiBillingHierarchy"] = UNSET
    reseller_fee_rate: Union[Unset, "ApiFeeRate"] = UNSET
    developer_fee_rate_entity: Union[Unset, "ApiBillingEntity"] = UNSET
    developer_fee_rate_hierarchy: Union[Unset, "ApiBillingHierarchy"] = UNSET
    developer_fee_rate: Union[Unset, "ApiFeeRate"] = UNSET
    validation_errors: Union[Unset, list[str]] = UNSET
    validation_warnings: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revenue_action_fee_codes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revenue_action_fee_codes, Unset):
            revenue_action_fee_codes = []
            for revenue_action_fee_codes_item_data in self.revenue_action_fee_codes:
                revenue_action_fee_codes_item = revenue_action_fee_codes_item_data.to_dict()
                revenue_action_fee_codes.append(revenue_action_fee_codes_item)

        reseller_fee_rate_entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reseller_fee_rate_entity, Unset):
            reseller_fee_rate_entity = self.reseller_fee_rate_entity.to_dict()

        reseller_fee_rate_hierarchy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reseller_fee_rate_hierarchy, Unset):
            reseller_fee_rate_hierarchy = self.reseller_fee_rate_hierarchy.to_dict()

        reseller_fee_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reseller_fee_rate, Unset):
            reseller_fee_rate = self.reseller_fee_rate.to_dict()

        developer_fee_rate_entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.developer_fee_rate_entity, Unset):
            developer_fee_rate_entity = self.developer_fee_rate_entity.to_dict()

        developer_fee_rate_hierarchy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.developer_fee_rate_hierarchy, Unset):
            developer_fee_rate_hierarchy = self.developer_fee_rate_hierarchy.to_dict()

        developer_fee_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.developer_fee_rate, Unset):
            developer_fee_rate = self.developer_fee_rate.to_dict()

        validation_errors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.validation_errors, Unset):
            validation_errors = self.validation_errors

        validation_warnings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.validation_warnings, Unset):
            validation_warnings = self.validation_warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revenue_action_fee_codes is not UNSET:
            field_dict["revenueActionFeeCodes"] = revenue_action_fee_codes
        if reseller_fee_rate_entity is not UNSET:
            field_dict["resellerFeeRateEntity"] = reseller_fee_rate_entity
        if reseller_fee_rate_hierarchy is not UNSET:
            field_dict["resellerFeeRateHierarchy"] = reseller_fee_rate_hierarchy
        if reseller_fee_rate is not UNSET:
            field_dict["resellerFeeRate"] = reseller_fee_rate
        if developer_fee_rate_entity is not UNSET:
            field_dict["developerFeeRateEntity"] = developer_fee_rate_entity
        if developer_fee_rate_hierarchy is not UNSET:
            field_dict["developerFeeRateHierarchy"] = developer_fee_rate_hierarchy
        if developer_fee_rate is not UNSET:
            field_dict["developerFeeRate"] = developer_fee_rate
        if validation_errors is not UNSET:
            field_dict["validationErrors"] = validation_errors
        if validation_warnings is not UNSET:
            field_dict["validationWarnings"] = validation_warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_billing_entity import ApiBillingEntity
        from ..models.api_billing_hierarchy import ApiBillingHierarchy
        from ..models.api_fee_rate import ApiFeeRate
        from ..models.api_revenue_action_fee_code import ApiRevenueActionFeeCode

        d = dict(src_dict)
        revenue_action_fee_codes = []
        _revenue_action_fee_codes = d.pop("revenueActionFeeCodes", UNSET)
        for revenue_action_fee_codes_item_data in _revenue_action_fee_codes or []:
            revenue_action_fee_codes_item = ApiRevenueActionFeeCode.from_dict(revenue_action_fee_codes_item_data)

            revenue_action_fee_codes.append(revenue_action_fee_codes_item)

        _reseller_fee_rate_entity = d.pop("resellerFeeRateEntity", UNSET)
        reseller_fee_rate_entity: Union[Unset, ApiBillingEntity]
        if isinstance(_reseller_fee_rate_entity, Unset):
            reseller_fee_rate_entity = UNSET
        else:
            reseller_fee_rate_entity = ApiBillingEntity.from_dict(_reseller_fee_rate_entity)

        _reseller_fee_rate_hierarchy = d.pop("resellerFeeRateHierarchy", UNSET)
        reseller_fee_rate_hierarchy: Union[Unset, ApiBillingHierarchy]
        if isinstance(_reseller_fee_rate_hierarchy, Unset):
            reseller_fee_rate_hierarchy = UNSET
        else:
            reseller_fee_rate_hierarchy = ApiBillingHierarchy.from_dict(_reseller_fee_rate_hierarchy)

        _reseller_fee_rate = d.pop("resellerFeeRate", UNSET)
        reseller_fee_rate: Union[Unset, ApiFeeRate]
        if isinstance(_reseller_fee_rate, Unset):
            reseller_fee_rate = UNSET
        else:
            reseller_fee_rate = ApiFeeRate.from_dict(_reseller_fee_rate)

        _developer_fee_rate_entity = d.pop("developerFeeRateEntity", UNSET)
        developer_fee_rate_entity: Union[Unset, ApiBillingEntity]
        if isinstance(_developer_fee_rate_entity, Unset):
            developer_fee_rate_entity = UNSET
        else:
            developer_fee_rate_entity = ApiBillingEntity.from_dict(_developer_fee_rate_entity)

        _developer_fee_rate_hierarchy = d.pop("developerFeeRateHierarchy", UNSET)
        developer_fee_rate_hierarchy: Union[Unset, ApiBillingHierarchy]
        if isinstance(_developer_fee_rate_hierarchy, Unset):
            developer_fee_rate_hierarchy = UNSET
        else:
            developer_fee_rate_hierarchy = ApiBillingHierarchy.from_dict(_developer_fee_rate_hierarchy)

        _developer_fee_rate = d.pop("developerFeeRate", UNSET)
        developer_fee_rate: Union[Unset, ApiFeeRate]
        if isinstance(_developer_fee_rate, Unset):
            developer_fee_rate = UNSET
        else:
            developer_fee_rate = ApiFeeRate.from_dict(_developer_fee_rate)

        validation_errors = cast(list[str], d.pop("validationErrors", UNSET))

        validation_warnings = cast(list[str], d.pop("validationWarnings", UNSET))

        api_rev_share_abstraction_details = cls(
            revenue_action_fee_codes=revenue_action_fee_codes,
            reseller_fee_rate_entity=reseller_fee_rate_entity,
            reseller_fee_rate_hierarchy=reseller_fee_rate_hierarchy,
            reseller_fee_rate=reseller_fee_rate,
            developer_fee_rate_entity=developer_fee_rate_entity,
            developer_fee_rate_hierarchy=developer_fee_rate_hierarchy,
            developer_fee_rate=developer_fee_rate,
            validation_errors=validation_errors,
            validation_warnings=validation_warnings,
        )

        api_rev_share_abstraction_details.additional_properties = d
        return api_rev_share_abstraction_details

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
