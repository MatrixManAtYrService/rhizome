from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_4_response_200 import Delete4Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    acceptance_id: str,
    *,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/backfill_acceptance/{acceptance_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Delete4Response200]:
    if response.status_code == 200:
        response_200 = Delete4Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Delete4Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    acceptance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[Delete4Response200]:
    """Delete backfilled acceptance by acceptance UUID

    Args:
        acceptance_id (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Delete4Response200]
    """

    kwargs = _get_kwargs(
        acceptance_id=acceptance_id,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    acceptance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[Delete4Response200]:
    """Delete backfilled acceptance by acceptance UUID

    Args:
        acceptance_id (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Delete4Response200
    """

    return sync_detailed(
        acceptance_id=acceptance_id,
        client=client,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    acceptance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[Delete4Response200]:
    """Delete backfilled acceptance by acceptance UUID

    Args:
        acceptance_id (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Delete4Response200]
    """

    kwargs = _get_kwargs(
        acceptance_id=acceptance_id,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    acceptance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[Delete4Response200]:
    """Delete backfilled acceptance by acceptance UUID

    Args:
        acceptance_id (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Delete4Response200
    """

    return (
        await asyncio_detailed(
            acceptance_id=acceptance_id,
            client=client,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
