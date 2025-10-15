import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_ledger_journal import ApiLedgerJournal
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ledger_acct_uuid: str,
    journal_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ledgerAcctUuid"] = ledger_acct_uuid

    json_journal_date: Union[Unset, str] = UNSET
    if not isinstance(journal_date, Unset):
        json_journal_date = journal_date.isoformat()
    params["journalDate"] = json_journal_date

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ledgerjournal",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ResponseError, list["ApiLedgerJournal"]]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiLedgerJournal.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ApiLedgerJournal.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ResponseError, list["ApiLedgerJournal"]]]:
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
    journal_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ResponseError, list["ApiLedgerJournal"]]]:
    """Get ledger journal entries using the UUID of the ledger account that the journal entries are for and
    optionally the journal date

    Args:
        ledger_acct_uuid (str):
        journal_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseError, list['ApiLedgerJournal']]]
    """

    kwargs = _get_kwargs(
        ledger_acct_uuid=ledger_acct_uuid,
        journal_date=journal_date,
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
    ledger_acct_uuid: str,
    journal_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ResponseError, list["ApiLedgerJournal"]]]:
    """Get ledger journal entries using the UUID of the ledger account that the journal entries are for and
    optionally the journal date

    Args:
        ledger_acct_uuid (str):
        journal_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseError, list['ApiLedgerJournal']]
    """

    return sync_detailed(
        client=client,
        ledger_acct_uuid=ledger_acct_uuid,
        journal_date=journal_date,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_acct_uuid: str,
    journal_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ResponseError, list["ApiLedgerJournal"]]]:
    """Get ledger journal entries using the UUID of the ledger account that the journal entries are for and
    optionally the journal date

    Args:
        ledger_acct_uuid (str):
        journal_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseError, list['ApiLedgerJournal']]]
    """

    kwargs = _get_kwargs(
        ledger_acct_uuid=ledger_acct_uuid,
        journal_date=journal_date,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ledger_acct_uuid: str,
    journal_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ResponseError, list["ApiLedgerJournal"]]]:
    """Get ledger journal entries using the UUID of the ledger account that the journal entries are for and
    optionally the journal date

    Args:
        ledger_acct_uuid (str):
        journal_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseError, list['ApiLedgerJournal']]
    """

    return (
        await asyncio_detailed(
            client=client,
            ledger_acct_uuid=ledger_acct_uuid,
            journal_date=journal_date,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
