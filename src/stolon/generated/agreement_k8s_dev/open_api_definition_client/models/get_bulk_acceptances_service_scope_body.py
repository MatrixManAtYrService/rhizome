from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acceptance_query import AcceptanceQuery
    from ..models.acceptance_sort import AcceptanceSort
    from ..models.get_bulk_acceptances_service_scope_body_request_body import (
        GetBulkAcceptancesServiceScopeBodyRequestBody,
    )
    from ..models.pagination import Pagination


T = TypeVar("T", bound="GetBulkAcceptancesServiceScopeBody")


@_attrs_define
class GetBulkAcceptancesServiceScopeBody:
    """
    Attributes:
        acceptance_query (Union[Unset, AcceptanceQuery]):
        sort (Union[Unset, AcceptanceSort]):
        pagination (Union[Unset, Pagination]):
        request_body (Union[Unset, GetBulkAcceptancesServiceScopeBodyRequestBody]):
    """

    acceptance_query: Union[Unset, "AcceptanceQuery"] = UNSET
    sort: Union[Unset, "AcceptanceSort"] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    request_body: Union[Unset, "GetBulkAcceptancesServiceScopeBodyRequestBody"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acceptance_query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.acceptance_query, Unset):
            acceptance_query = self.acceptance_query.to_dict()

        sort: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        request_body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request_body, Unset):
            request_body = self.request_body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acceptance_query is not UNSET:
            field_dict["acceptanceQuery"] = acceptance_query
        if sort is not UNSET:
            field_dict["sort"] = sort
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if request_body is not UNSET:
            field_dict["requestBody"] = request_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acceptance_query import AcceptanceQuery
        from ..models.acceptance_sort import AcceptanceSort
        from ..models.get_bulk_acceptances_service_scope_body_request_body import (
            GetBulkAcceptancesServiceScopeBodyRequestBody,
        )
        from ..models.pagination import Pagination

        d = dict(src_dict)
        _acceptance_query = d.pop("acceptanceQuery", UNSET)
        acceptance_query: Union[Unset, AcceptanceQuery]
        if _acceptance_query and not isinstance(_acceptance_query, Unset):
            acceptance_query = AcceptanceQuery.from_dict(_acceptance_query)

        else:
            acceptance_query = UNSET

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, AcceptanceSort]
        if _sort and not isinstance(_sort, Unset):
            sort = AcceptanceSort.from_dict(_sort)

        else:
            sort = UNSET

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if _pagination and not isinstance(_pagination, Unset):
            pagination = Pagination.from_dict(_pagination)

        else:
            pagination = UNSET

        _request_body = d.pop("requestBody", UNSET)
        request_body: Union[Unset, GetBulkAcceptancesServiceScopeBodyRequestBody]
        if _request_body and not isinstance(_request_body, Unset):
            request_body = GetBulkAcceptancesServiceScopeBodyRequestBody.from_dict(_request_body)

        else:
            request_body = UNSET

        get_bulk_acceptances_service_scope_body = cls(
            acceptance_query=acceptance_query,
            sort=sort,
            pagination=pagination,
            request_body=request_body,
        )

        get_bulk_acceptances_service_scope_body.additional_properties = d
        return get_bulk_acceptances_service_scope_body

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
