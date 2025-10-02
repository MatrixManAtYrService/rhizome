from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_ledger_account_balance import ApiLedgerAccountBalance
from ...types import UNSET, Response


def _get_kwargs(
    *,
    ledger_acct_uuid: str,
    currency: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ledgerAcctUuid"] = ledger_acct_uuid

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ledgeracctbalance",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiLedgerAccountBalance]:
    if response.status_code == 200:
        response_200 = ApiLedgerAccountBalance.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiLedgerAccountBalance.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiLedgerAccountBalance.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiLedgerAccountBalance]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_acct_uuid: str,
    currency: str,
) -> Response[ApiLedgerAccountBalance]:
    """Get ledger account balance using the UUID of the ledger account the balance is for along with the
    currency

    Args:
        ledger_acct_uuid (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiLedgerAccountBalance]
    """

    kwargs = _get_kwargs(
        ledger_acct_uuid=ledger_acct_uuid,
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_acct_uuid: str,
    currency: str,
) -> Optional[ApiLedgerAccountBalance]:
    """Get ledger account balance using the UUID of the ledger account the balance is for along with the
    currency

    Args:
        ledger_acct_uuid (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiLedgerAccountBalance
    """

    return sync_detailed(
        client=client,
        ledger_acct_uuid=ledger_acct_uuid,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_acct_uuid: str,
    currency: str,
) -> Response[ApiLedgerAccountBalance]:
    """Get ledger account balance using the UUID of the ledger account the balance is for along with the
    currency

    Args:
        ledger_acct_uuid (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiLedgerAccountBalance]
    """

    kwargs = _get_kwargs(
        ledger_acct_uuid=ledger_acct_uuid,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_acct_uuid: str,
    currency: str,
) -> Optional[ApiLedgerAccountBalance]:
    """Get ledger account balance using the UUID of the ledger account the balance is for along with the
    currency

    Args:
        ledger_acct_uuid (str):
        currency (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiLedgerAccountBalance
    """

    return (
        await asyncio_detailed(
            client=client,
            ledger_acct_uuid=ledger_acct_uuid,
            currency=currency,
        )
    ).parsed
