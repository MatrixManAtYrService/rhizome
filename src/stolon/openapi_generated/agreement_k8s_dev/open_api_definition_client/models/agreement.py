import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.agreement_acceptance_sign_context import AgreementAcceptanceSignContext
from ..models.agreement_template_engine import AgreementTemplateEngine
from ..types import UNSET, Unset

T = TypeVar("T", bound="Agreement")


@_attrs_define
class Agreement:
    """
    Attributes:
        full_text (str):
        mime_type (str):
        agreement_type (str):
        acceptance_sign_context (AgreementAcceptanceSignContext):
        locale (str):
        template_engine (AgreementTemplateEngine):
        id (Union[Unset, UUID]):
        version (Union[Unset, str]):
        major_revision (Union[Unset, bool]):
        effective_time (Union[Unset, datetime.datetime]):
    """

    full_text: str
    mime_type: str
    agreement_type: str
    acceptance_sign_context: AgreementAcceptanceSignContext
    locale: str
    template_engine: AgreementTemplateEngine
    id: Union[Unset, UUID] = UNSET
    version: Union[Unset, str] = UNSET
    major_revision: Union[Unset, bool] = UNSET
    effective_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_text = self.full_text

        mime_type = self.mime_type

        agreement_type = self.agreement_type

        acceptance_sign_context = self.acceptance_sign_context.value

        locale = self.locale

        template_engine = self.template_engine.value

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        version = self.version

        major_revision = self.major_revision

        effective_time: Union[Unset, str] = UNSET
        if not isinstance(self.effective_time, Unset):
            effective_time = self.effective_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fullText": full_text,
                "mimeType": mime_type,
                "agreementType": agreement_type,
                "acceptanceSignContext": acceptance_sign_context,
                "locale": locale,
                "templateEngine": template_engine,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if major_revision is not UNSET:
            field_dict["majorRevision"] = major_revision
        if effective_time is not UNSET:
            field_dict["effectiveTime"] = effective_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_text = d.pop("fullText")

        mime_type = d.pop("mimeType")

        agreement_type = d.pop("agreementType")

        acceptance_sign_context = AgreementAcceptanceSignContext(d.pop("acceptanceSignContext"))

        locale = d.pop("locale")

        template_engine = AgreementTemplateEngine(d.pop("templateEngine"))

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if _id and not isinstance(_id, Unset):
            id = UUID(_id)

        else:
            id = UNSET

        version = d.pop("version", UNSET)

        major_revision = d.pop("majorRevision", UNSET)

        _effective_time = d.pop("effectiveTime", UNSET)
        effective_time: Union[Unset, datetime.datetime]
        if _effective_time and not isinstance(_effective_time, Unset):
            effective_time = isoparse(_effective_time)

        else:
            effective_time = UNSET

        agreement = cls(
            full_text=full_text,
            mime_type=mime_type,
            agreement_type=agreement_type,
            acceptance_sign_context=acceptance_sign_context,
            locale=locale,
            template_engine=template_engine,
            id=id,
            version=version,
            major_revision=major_revision,
            effective_time=effective_time,
        )

        agreement.additional_properties = d
        return agreement

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
