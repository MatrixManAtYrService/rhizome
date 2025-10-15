from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acceptance import Acceptance
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_: str,
    *,
    x_clover_merchant_id: Union[Unset, str] = UNSET,
    x_clover_account_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_merchant_id, Unset):
        headers["X-Clover-Merchant-Id"] = x_clover_merchant_id

    if not isinstance(x_clover_account_id, Unset):
        headers["X-Clover-Account-Id"] = x_clover_account_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/acceptances/type/{type_}/latest",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Acceptance]:
    if response.status_code == 200:
        response_200 = Acceptance.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Acceptance]:
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
    x_clover_merchant_id: Union[Unset, str] = UNSET,
    x_clover_account_id: Union[Unset, str] = UNSET,
) -> Response[Acceptance]:
    """
    Args:
        type_ (str):
        x_clover_merchant_id (Union[Unset, str]):
        x_clover_account_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acceptance]
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
    x_clover_merchant_id: Union[Unset, str] = UNSET,
    x_clover_account_id: Union[Unset, str] = UNSET,
) -> Optional[Acceptance]:
    """
    Args:
        type_ (str):
        x_clover_merchant_id (Union[Unset, str]):
        x_clover_account_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acceptance
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
    x_clover_merchant_id: Union[Unset, str] = UNSET,
    x_clover_account_id: Union[Unset, str] = UNSET,
) -> Response[Acceptance]:
    """
    Args:
        type_ (str):
        x_clover_merchant_id (Union[Unset, str]):
        x_clover_account_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acceptance]
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
    x_clover_merchant_id: Union[Unset, str] = UNSET,
    x_clover_account_id: Union[Unset, str] = UNSET,
) -> Optional[Acceptance]:
    """
    Args:
        type_ (str):
        x_clover_merchant_id (Union[Unset, str]):
        x_clover_account_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acceptance
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            x_clover_merchant_id=x_clover_merchant_id,
            x_clover_account_id=x_clover_account_id,
        )
    ).parsed
