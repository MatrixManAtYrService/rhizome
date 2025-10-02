from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_ledger_account_key import ApiLedgerAccountKey
from ...models.response_error import ResponseError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    ledger_account_key: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ledgerAccountKey"] = ledger_account_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ledgeracctkey",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiLedgerAccountKey, ResponseError]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiLedgerAccountKey.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiLedgerAccountKey.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiLedgerAccountKey, ResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_account_key: str,
) -> Response[Union[ApiLedgerAccountKey, ResponseError]]:
    """Get ledger account key using the key value

    Args:
        ledger_account_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLedgerAccountKey, ResponseError]]
    """

    kwargs = _get_kwargs(
        ledger_account_key=ledger_account_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_account_key: str,
) -> Optional[Union[ApiLedgerAccountKey, ResponseError]]:
    """Get ledger account key using the key value

    Args:
        ledger_account_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLedgerAccountKey, ResponseError]
    """

    return sync_detailed(
        client=client,
        ledger_account_key=ledger_account_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_account_key: str,
) -> Response[Union[ApiLedgerAccountKey, ResponseError]]:
    """Get ledger account key using the key value

    Args:
        ledger_account_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLedgerAccountKey, ResponseError]]
    """

    kwargs = _get_kwargs(
        ledger_account_key=ledger_account_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_account_key: str,
) -> Optional[Union[ApiLedgerAccountKey, ResponseError]]:
    """Get ledger account key using the key value

    Args:
        ledger_account_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLedgerAccountKey, ResponseError]
    """

    return (
        await asyncio_detailed(
            client=client,
            ledger_account_key=ledger_account_key,
        )
    ).parsed
