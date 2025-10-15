from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agreement import Agreement
from ...types import Response


def _get_kwargs(
    agreement_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/agreements/{agreement_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Agreement]:
    if response.status_code == 200:
        response_200 = Agreement.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Agreement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agreement_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Agreement]:
    """
    Args:
        agreement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Agreement]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agreement_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Agreement]:
    """
    Args:
        agreement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Agreement
    """

    return sync_detailed(
        agreement_id=agreement_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    agreement_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Agreement]:
    """
    Args:
        agreement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Agreement]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agreement_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Agreement]:
    """
    Args:
        agreement_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Agreement
    """

    return (
        await asyncio_detailed(
            agreement_id=agreement_id,
            client=client,
        )
    ).parsed
