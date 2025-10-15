from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.merchant_passes_response_200 import MerchantPassesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/managed_item/merchant/{uuid}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MerchantPassesResponse200]:
    if response.status_code == 200:
        response_200 = MerchantPassesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MerchantPassesResponse200]:
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
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[MerchantPassesResponse200]:
    """Check if merchant meets criteria

    Args:
        uuid (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MerchantPassesResponse200]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[MerchantPassesResponse200]:
    """Check if merchant meets criteria

    Args:
        uuid (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MerchantPassesResponse200
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[MerchantPassesResponse200]:
    """Check if merchant meets criteria

    Args:
        uuid (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MerchantPassesResponse200]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[MerchantPassesResponse200]:
    """Check if merchant meets criteria

    Args:
        uuid (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MerchantPassesResponse200
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
