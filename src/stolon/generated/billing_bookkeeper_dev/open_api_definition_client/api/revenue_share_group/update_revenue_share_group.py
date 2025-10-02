from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_revenue_share_group import ApiRevenueShareGroup
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    body: ApiRevenueShareGroup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/revsharegroup/{uuid}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiRevenueShareGroup,
) -> Response[ApiRevenueShareGroup]:
    """Update revenue share group

    Args:
        uuid (str):
        body (ApiRevenueShareGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRevenueShareGroup]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiRevenueShareGroup,
) -> Optional[ApiRevenueShareGroup]:
    """Update revenue share group

    Args:
        uuid (str):
        body (ApiRevenueShareGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRevenueShareGroup
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiRevenueShareGroup,
) -> Response[ApiRevenueShareGroup]:
    """Update revenue share group

    Args:
        uuid (str):
        body (ApiRevenueShareGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRevenueShareGroup]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiRevenueShareGroup,
) -> Optional[ApiRevenueShareGroup]:
    """Update revenue share group

    Args:
        uuid (str):
        body (ApiRevenueShareGroup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRevenueShareGroup
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
