from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_revenue_share_group import ApiRevenueShareGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    revenue_share_group: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["revenueShareGroup"] = revenue_share_group

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/revsharegroup",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiRevenueShareGroup]:
    if response.status_code == 200:
        response_200 = ApiRevenueShareGroup.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiRevenueShareGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    revenue_share_group: Union[Unset, str] = UNSET,
) -> Response[ApiRevenueShareGroup]:
    """Get revenue share groups, optionally filtering by revenue share group value

    Args:
        revenue_share_group (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRevenueShareGroup]
    """

    kwargs = _get_kwargs(
        revenue_share_group=revenue_share_group,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    revenue_share_group: Union[Unset, str] = UNSET,
) -> Optional[ApiRevenueShareGroup]:
    """Get revenue share groups, optionally filtering by revenue share group value

    Args:
        revenue_share_group (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRevenueShareGroup
    """

    return sync_detailed(
        client=client,
        revenue_share_group=revenue_share_group,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    revenue_share_group: Union[Unset, str] = UNSET,
) -> Response[ApiRevenueShareGroup]:
    """Get revenue share groups, optionally filtering by revenue share group value

    Args:
        revenue_share_group (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRevenueShareGroup]
    """

    kwargs = _get_kwargs(
        revenue_share_group=revenue_share_group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    revenue_share_group: Union[Unset, str] = UNSET,
) -> Optional[ApiRevenueShareGroup]:
    """Get revenue share groups, optionally filtering by revenue share group value

    Args:
        revenue_share_group (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRevenueShareGroup
    """

    return (
        await asyncio_detailed(
            client=client,
            revenue_share_group=revenue_share_group,
        )
    ).parsed
