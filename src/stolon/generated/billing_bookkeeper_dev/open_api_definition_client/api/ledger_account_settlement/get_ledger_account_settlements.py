import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_ledger_account_settlement import ApiLedgerAccountSettlement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: Union[Unset, datetime.date] = UNSET,
    ledger_account_key: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["ledgerAccountKey"] = ledger_account_key

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ledgeracctsettlement",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiLedgerAccountSettlement, list["ApiLedgerAccountSettlement"]]]:
    if response.status_code == 200:
        response_200 = ApiLedgerAccountSettlement.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiLedgerAccountSettlement.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ApiLedgerAccountSettlement.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiLedgerAccountSettlement, list["ApiLedgerAccountSettlement"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    ledger_account_key: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ApiLedgerAccountSettlement, list["ApiLedgerAccountSettlement"]]]:
    """Get ledger account settlement configurations using the ledger account key

    Args:
        date (Union[Unset, datetime.date]):
        ledger_account_key (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLedgerAccountSettlement, list['ApiLedgerAccountSettlement']]]
    """

    kwargs = _get_kwargs(
        date=date,
        ledger_account_key=ledger_account_key,
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
    date: Union[Unset, datetime.date] = UNSET,
    ledger_account_key: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiLedgerAccountSettlement, list["ApiLedgerAccountSettlement"]]]:
    """Get ledger account settlement configurations using the ledger account key

    Args:
        date (Union[Unset, datetime.date]):
        ledger_account_key (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLedgerAccountSettlement, list['ApiLedgerAccountSettlement']]
    """

    return sync_detailed(
        client=client,
        date=date,
        ledger_account_key=ledger_account_key,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    ledger_account_key: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ApiLedgerAccountSettlement, list["ApiLedgerAccountSettlement"]]]:
    """Get ledger account settlement configurations using the ledger account key

    Args:
        date (Union[Unset, datetime.date]):
        ledger_account_key (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLedgerAccountSettlement, list['ApiLedgerAccountSettlement']]]
    """

    kwargs = _get_kwargs(
        date=date,
        ledger_account_key=ledger_account_key,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    ledger_account_key: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiLedgerAccountSettlement, list["ApiLedgerAccountSettlement"]]]:
    """Get ledger account settlement configurations using the ledger account key

    Args:
        date (Union[Unset, datetime.date]):
        ledger_account_key (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLedgerAccountSettlement, list['ApiLedgerAccountSettlement']]
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            ledger_account_key=ledger_account_key,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
