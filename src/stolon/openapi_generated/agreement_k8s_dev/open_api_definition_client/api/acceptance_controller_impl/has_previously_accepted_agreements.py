from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    type_: str,
    *,
    x_clover_merchant_id: str,
    x_clover_account_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Clover-Merchant-Id"] = x_clover_merchant_id

    headers["X-Clover-Account-Id"] = x_clover_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/acceptances/{type_}/hasPreviousAcceptances",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[bool]:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[bool]:
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
    x_clover_merchant_id: str,
    x_clover_account_id: str,
) -> Response[bool]:
    """
    Args:
        type_ (str):
        x_clover_merchant_id (str):
        x_clover_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        type_=type_,
        x_clover_merchant_id=x_clover_merchant_id,
        x_clover_account_id=x_clover_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_merchant_id: str,
    x_clover_account_id: str,
) -> Optional[bool]:
    """
    Args:
        type_ (str):
        x_clover_merchant_id (str):
        x_clover_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        bool
    """

    return sync_detailed(
        type_=type_,
        client=client,
        x_clover_merchant_id=x_clover_merchant_id,
        x_clover_account_id=x_clover_account_id,
    ).parsed


async def asyncio_detailed(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_merchant_id: str,
    x_clover_account_id: str,
) -> Response[bool]:
    """
    Args:
        type_ (str):
        x_clover_merchant_id (str):
        x_clover_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        type_=type_,
        x_clover_merchant_id=x_clover_merchant_id,
        x_clover_account_id=x_clover_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_merchant_id: str,
    x_clover_account_id: str,
) -> Optional[bool]:
    """
    Args:
        type_ (str):
        x_clover_merchant_id (str):
        x_clover_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        bool
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            x_clover_merchant_id=x_clover_merchant_id,
            x_clover_account_id=x_clover_account_id,
        )
    ).parsed
