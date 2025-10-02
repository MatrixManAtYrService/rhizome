from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bulk_acceptances_sort import GetBulkAcceptancesSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agreement_type: Union[Unset, str] = "BILLING",
    include_deleted: Union[Unset, bool] = False,
    include_template: Union[Unset, bool] = False,
    sort: Union[Unset, GetBulkAcceptancesSort] = GetBulkAcceptancesSort.CREATEDTIME,
    page_size: Union[Unset, int] = 100,
    page_number: Union[Unset, int] = 0,
    merchant_uuids: list[str],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    params: dict[str, Any] = {}

    params["agreementType"] = agreement_type

    params["includeDeleted"] = include_deleted

    params["includeTemplate"] = include_template

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    json_merchant_uuids = merchant_uuids

    params["merchantUuids"] = json_merchant_uuids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/external/bulkAcceptances",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    agreement_type: Union[Unset, str] = "BILLING",
    include_deleted: Union[Unset, bool] = False,
    include_template: Union[Unset, bool] = False,
    sort: Union[Unset, GetBulkAcceptancesSort] = GetBulkAcceptancesSort.CREATEDTIME,
    page_size: Union[Unset, int] = 100,
    page_number: Union[Unset, int] = 0,
    merchant_uuids: list[str],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        agreement_type (Union[Unset, str]):  Default: 'BILLING'.
        include_deleted (Union[Unset, bool]):  Default: False.
        include_template (Union[Unset, bool]):  Default: False.
        sort (Union[Unset, GetBulkAcceptancesSort]):  Default: GetBulkAcceptancesSort.CREATEDTIME.
        page_size (Union[Unset, int]):  Default: 100.
        page_number (Union[Unset, int]):  Default: 0.
        merchant_uuids (list[str]):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agreement_type=agreement_type,
        include_deleted=include_deleted,
        include_template=include_template,
        sort=sort,
        page_size=page_size,
        page_number=page_number,
        merchant_uuids=merchant_uuids,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    agreement_type: Union[Unset, str] = "BILLING",
    include_deleted: Union[Unset, bool] = False,
    include_template: Union[Unset, bool] = False,
    sort: Union[Unset, GetBulkAcceptancesSort] = GetBulkAcceptancesSort.CREATEDTIME,
    page_size: Union[Unset, int] = 100,
    page_number: Union[Unset, int] = 0,
    merchant_uuids: list[str],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        agreement_type (Union[Unset, str]):  Default: 'BILLING'.
        include_deleted (Union[Unset, bool]):  Default: False.
        include_template (Union[Unset, bool]):  Default: False.
        sort (Union[Unset, GetBulkAcceptancesSort]):  Default: GetBulkAcceptancesSort.CREATEDTIME.
        page_size (Union[Unset, int]):  Default: 100.
        page_number (Union[Unset, int]):  Default: 0.
        merchant_uuids (list[str]):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agreement_type=agreement_type,
        include_deleted=include_deleted,
        include_template=include_template,
        sort=sort,
        page_size=page_size,
        page_number=page_number,
        merchant_uuids=merchant_uuids,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
