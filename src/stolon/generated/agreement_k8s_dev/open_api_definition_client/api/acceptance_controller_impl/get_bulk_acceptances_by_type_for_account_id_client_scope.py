from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acceptance import Acceptance
from ...models.acceptance_query import AcceptanceQuery
from ...models.acceptance_sort import AcceptanceSort
from ...models.pagination import Pagination
from ...types import UNSET, Response


def _get_kwargs(
    type_: str,
    *,
    account_id: str,
    acceptance_query: "AcceptanceQuery",
    sort: "AcceptanceSort",
    pagination: "Pagination",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accountId"] = account_id

    json_acceptance_query = acceptance_query.to_dict()
    params.update(json_acceptance_query)

    json_sort = sort.to_dict()
    params.update(json_sort)

    json_pagination = pagination.to_dict()
    params.update(json_pagination)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/acceptances/bulk/{type_}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Acceptance"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Acceptance.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Acceptance"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: str,
    acceptance_query: "AcceptanceQuery",
    sort: "AcceptanceSort",
    pagination: "Pagination",
) -> Response[list["Acceptance"]]:
    """
    Args:
        type_ (str):
        account_id (str):
        acceptance_query (AcceptanceQuery):
        sort (AcceptanceSort):
        pagination (Pagination):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Acceptance']]
    """

    kwargs = _get_kwargs(
        type_=type_,
        account_id=account_id,
        acceptance_query=acceptance_query,
        sort=sort,
        pagination=pagination,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: str,
    acceptance_query: "AcceptanceQuery",
    sort: "AcceptanceSort",
    pagination: "Pagination",
) -> Optional[list["Acceptance"]]:
    """
    Args:
        type_ (str):
        account_id (str):
        acceptance_query (AcceptanceQuery):
        sort (AcceptanceSort):
        pagination (Pagination):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Acceptance']
    """

    return sync_detailed(
        type_=type_,
        client=client,
        account_id=account_id,
        acceptance_query=acceptance_query,
        sort=sort,
        pagination=pagination,
    ).parsed


async def asyncio_detailed(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: str,
    acceptance_query: "AcceptanceQuery",
    sort: "AcceptanceSort",
    pagination: "Pagination",
) -> Response[list["Acceptance"]]:
    """
    Args:
        type_ (str):
        account_id (str):
        acceptance_query (AcceptanceQuery):
        sort (AcceptanceSort):
        pagination (Pagination):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Acceptance']]
    """

    kwargs = _get_kwargs(
        type_=type_,
        account_id=account_id,
        acceptance_query=acceptance_query,
        sort=sort,
        pagination=pagination,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: str,
    acceptance_query: "AcceptanceQuery",
    sort: "AcceptanceSort",
    pagination: "Pagination",
) -> Optional[list["Acceptance"]]:
    """
    Args:
        type_ (str):
        account_id (str):
        acceptance_query (AcceptanceQuery):
        sort (AcceptanceSort):
        pagination (Pagination):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Acceptance']
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            account_id=account_id,
            acceptance_query=acceptance_query,
            sort=sort,
            pagination=pagination,
        )
    ).parsed
