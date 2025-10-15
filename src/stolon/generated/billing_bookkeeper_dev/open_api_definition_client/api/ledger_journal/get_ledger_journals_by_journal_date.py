import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_ledger_journal_projection import ApiLedgerJournalProjection
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    min_date: Union[Unset, datetime.date] = UNSET,
    max_date: Union[Unset, datetime.date] = UNSET,
    ledger_account_uuid: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_min_date: Union[Unset, str] = UNSET
    if not isinstance(min_date, Unset):
        json_min_date = min_date.isoformat()
    params["minDate"] = json_min_date

    json_max_date: Union[Unset, str] = UNSET
    if not isinstance(max_date, Unset):
        json_max_date = max_date.isoformat()
    params["maxDate"] = json_max_date

    params["ledgerAccountUuid"] = ledger_account_uuid

    params["currency"] = currency

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ledgerjournal/date",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ResponseError, list["ApiLedgerJournalProjection"]]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiLedgerJournalProjection.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ResponseError, list["ApiLedgerJournalProjection"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    min_date: Union[Unset, datetime.date] = UNSET,
    max_date: Union[Unset, datetime.date] = UNSET,
    ledger_account_uuid: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ResponseError, list["ApiLedgerJournalProjection"]]]:
    """Get ledger journal entries for the specified journal date range

    Args:
        min_date (Union[Unset, datetime.date]):
        max_date (Union[Unset, datetime.date]):
        ledger_account_uuid (Union[Unset, str]):
        currency (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseError, list['ApiLedgerJournalProjection']]]
    """

    kwargs = _get_kwargs(
        min_date=min_date,
        max_date=max_date,
        ledger_account_uuid=ledger_account_uuid,
        currency=currency,
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
    min_date: Union[Unset, datetime.date] = UNSET,
    max_date: Union[Unset, datetime.date] = UNSET,
    ledger_account_uuid: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ResponseError, list["ApiLedgerJournalProjection"]]]:
    """Get ledger journal entries for the specified journal date range

    Args:
        min_date (Union[Unset, datetime.date]):
        max_date (Union[Unset, datetime.date]):
        ledger_account_uuid (Union[Unset, str]):
        currency (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseError, list['ApiLedgerJournalProjection']]
    """

    return sync_detailed(
        client=client,
        min_date=min_date,
        max_date=max_date,
        ledger_account_uuid=ledger_account_uuid,
        currency=currency,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    min_date: Union[Unset, datetime.date] = UNSET,
    max_date: Union[Unset, datetime.date] = UNSET,
    ledger_account_uuid: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ResponseError, list["ApiLedgerJournalProjection"]]]:
    """Get ledger journal entries for the specified journal date range

    Args:
        min_date (Union[Unset, datetime.date]):
        max_date (Union[Unset, datetime.date]):
        ledger_account_uuid (Union[Unset, str]):
        currency (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseError, list['ApiLedgerJournalProjection']]]
    """

    kwargs = _get_kwargs(
        min_date=min_date,
        max_date=max_date,
        ledger_account_uuid=ledger_account_uuid,
        currency=currency,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    min_date: Union[Unset, datetime.date] = UNSET,
    max_date: Union[Unset, datetime.date] = UNSET,
    ledger_account_uuid: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ResponseError, list["ApiLedgerJournalProjection"]]]:
    """Get ledger journal entries for the specified journal date range

    Args:
        min_date (Union[Unset, datetime.date]):
        max_date (Union[Unset, datetime.date]):
        ledger_account_uuid (Union[Unset, str]):
        currency (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseError, list['ApiLedgerJournalProjection']]
    """

    return (
        await asyncio_detailed(
            client=client,
            min_date=min_date,
            max_date=max_date,
            ledger_account_uuid=ledger_account_uuid,
            currency=currency,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
