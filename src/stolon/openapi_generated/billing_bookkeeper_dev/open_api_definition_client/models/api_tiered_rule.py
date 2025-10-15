import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_tiered_rule_rule_status import ApiTieredRuleRuleStatus
from ..models.api_tiered_rule_target_entity_type import ApiTieredRuleTargetEntityType
from ..models.api_tiered_rule_tiered_basis import ApiTieredRuleTieredBasis
from ..models.api_tiered_rule_tiered_model import ApiTieredRuleTieredModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTieredRule")


@_attrs_define
class ApiTieredRule:
    """
    Attributes:
        id (Union[Unset, int]): ID of the tiered rule
        uuid (Union[Unset, str]): 26-character UUID of the tiered rule
        rule_alias (Union[Unset, str]): the alias for this tiered rule
        rule_status (Union[Unset, ApiTieredRuleRuleStatus]):
        tiered_basis (Union[Unset, ApiTieredRuleTieredBasis]):
        tiered_model (Union[Unset, ApiTieredRuleTieredModel]):
        target_entity_type (Union[Unset, ApiTieredRuleTargetEntityType]):
        short_desc (Union[Unset, str]): short description of the tiered rule
        full_desc (Union[Unset, str]): full description of the tiered rule
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the tiered rule was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the tiered rule was last modified
            Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this tiered rule
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    rule_alias: Union[Unset, str] = UNSET
    rule_status: Union[Unset, ApiTieredRuleRuleStatus] = UNSET
    tiered_basis: Union[Unset, ApiTieredRuleTieredBasis] = UNSET
    tiered_model: Union[Unset, ApiTieredRuleTieredModel] = UNSET
    target_entity_type: Union[Unset, ApiTieredRuleTargetEntityType] = UNSET
    short_desc: Union[Unset, str] = UNSET
    full_desc: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        rule_alias = self.rule_alias

        rule_status: Union[Unset, str] = UNSET
        if not isinstance(self.rule_status, Unset):
            rule_status = self.rule_status.value

        tiered_basis: Union[Unset, str] = UNSET
        if not isinstance(self.tiered_basis, Unset):
            tiered_basis = self.tiered_basis.value

        tiered_model: Union[Unset, str] = UNSET
        if not isinstance(self.tiered_model, Unset):
            tiered_model = self.tiered_model.value

        target_entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_entity_type, Unset):
            target_entity_type = self.target_entity_type.value

        short_desc = self.short_desc

        full_desc = self.full_desc

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if rule_alias is not UNSET:
            field_dict["ruleAlias"] = rule_alias
        if rule_status is not UNSET:
            field_dict["ruleStatus"] = rule_status
        if tiered_basis is not UNSET:
            field_dict["tieredBasis"] = tiered_basis
        if tiered_model is not UNSET:
            field_dict["tieredModel"] = tiered_model
        if target_entity_type is not UNSET:
            field_dict["targetEntityType"] = target_entity_type
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if full_desc is not UNSET:
            field_dict["fullDesc"] = full_desc
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        rule_alias = d.pop("ruleAlias", UNSET)

        _rule_status = d.pop("ruleStatus", UNSET)
        rule_status: Union[Unset, ApiTieredRuleRuleStatus]
        if _rule_status and not isinstance(_rule_status, Unset):
            rule_status = ApiTieredRuleRuleStatus(_rule_status)

        else:
            rule_status = UNSET

        _tiered_basis = d.pop("tieredBasis", UNSET)
        tiered_basis: Union[Unset, ApiTieredRuleTieredBasis]
        if _tiered_basis and not isinstance(_tiered_basis, Unset):
            tiered_basis = ApiTieredRuleTieredBasis(_tiered_basis)

        else:
            tiered_basis = UNSET

        _tiered_model = d.pop("tieredModel", UNSET)
        tiered_model: Union[Unset, ApiTieredRuleTieredModel]
        if _tiered_model and not isinstance(_tiered_model, Unset):
            tiered_model = ApiTieredRuleTieredModel(_tiered_model)

        else:
            tiered_model = UNSET

        _target_entity_type = d.pop("targetEntityType", UNSET)
        target_entity_type: Union[Unset, ApiTieredRuleTargetEntityType]
        if _target_entity_type and not isinstance(_target_entity_type, Unset):
            target_entity_type = ApiTieredRuleTargetEntityType(_target_entity_type)

        else:
            target_entity_type = UNSET

        short_desc = d.pop("shortDesc", UNSET)

        full_desc = d.pop("fullDesc", UNSET)

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

        audit_id = d.pop("auditId", UNSET)

        api_tiered_rule = cls(
            id=id,
            uuid=uuid,
            rule_alias=rule_alias,
            rule_status=rule_status,
            tiered_basis=tiered_basis,
            tiered_model=tiered_model,
            target_entity_type=target_entity_type,
            short_desc=short_desc,
            full_desc=full_desc,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_tiered_rule.additional_properties = d
        return api_tiered_rule

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
