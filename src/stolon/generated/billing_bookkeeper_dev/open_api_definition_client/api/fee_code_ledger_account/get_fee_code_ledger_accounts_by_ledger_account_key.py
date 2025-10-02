import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_fee_code_ledger_account import ApiFeeCodeLedgerAccount
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ledger_account_key: str,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ledgerAccountKey"] = ledger_account_key

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/feecodeledgeracct/key",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiFeeCodeLedgerAccount, list["ApiFeeCodeLedgerAccount"]]]:
    if response.status_code == 200:
        response_200 = ApiFeeCodeLedgerAccount.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiFeeCodeLedgerAccount.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiFeeCodeLedgerAccount, list["ApiFeeCodeLedgerAccount"]]]:
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
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ApiFeeCodeLedgerAccount, list["ApiFeeCodeLedgerAccount"]]]:
    """Get fee-code-to-ledger-account mappings that map to a ledger account key value

    Args:
        ledger_account_key (str):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiFeeCodeLedgerAccount, list['ApiFeeCodeLedgerAccount']]]
    """

    kwargs = _get_kwargs(
        ledger_account_key=ledger_account_key,
        date=date,
        page_size=page_size,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_account_key: str,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiFeeCodeLedgerAccount, list["ApiFeeCodeLedgerAccount"]]]:
    """Get fee-code-to-ledger-account mappings that map to a ledger account key value

    Args:
        ledger_account_key (str):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiFeeCodeLedgerAccount, list['ApiFeeCodeLedgerAccount']]
    """

    return sync_detailed(
        client=client,
        ledger_account_key=ledger_account_key,
        date=date,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_account_key: str,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ApiFeeCodeLedgerAccount, list["ApiFeeCodeLedgerAccount"]]]:
    """Get fee-code-to-ledger-account mappings that map to a ledger account key value

    Args:
        ledger_account_key (str):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiFeeCodeLedgerAccount, list['ApiFeeCodeLedgerAccount']]]
    """

    kwargs = _get_kwargs(
        ledger_account_key=ledger_account_key,
        date=date,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_account_key: str,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiFeeCodeLedgerAccount, list["ApiFeeCodeLedgerAccount"]]]:
    """Get fee-code-to-ledger-account mappings that map to a ledger account key value

    Args:
        ledger_account_key (str):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiFeeCodeLedgerAccount, list['ApiFeeCodeLedgerAccount']]
    """

    return (
        await asyncio_detailed(
            client=client,
            ledger_account_key=ledger_account_key,
            date=date,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
