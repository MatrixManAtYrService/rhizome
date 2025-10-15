import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_fee_code_ledger_account import ApiFeeCodeLedgerAccount
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fee_category: str,
    fee_code: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/feecodeledgeracct",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiFeeCodeLedgerAccount, ResponseError]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiFeeCodeLedgerAccount.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiFeeCodeLedgerAccount.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiFeeCodeLedgerAccount, ResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: str,
    fee_code: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
) -> Response[Union[ApiFeeCodeLedgerAccount, ResponseError]]:
    """Get a fee-code-to-ledger-account mapping using the fee category, fee code, and as-of date

    Args:
        fee_category (str):
        fee_code (Union[Unset, str]):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiFeeCodeLedgerAccount, ResponseError]]
    """

    kwargs = _get_kwargs(
        fee_category=fee_category,
        fee_code=fee_code,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: str,
    fee_code: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
) -> Optional[Union[ApiFeeCodeLedgerAccount, ResponseError]]:
    """Get a fee-code-to-ledger-account mapping using the fee category, fee code, and as-of date

    Args:
        fee_category (str):
        fee_code (Union[Unset, str]):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiFeeCodeLedgerAccount, ResponseError]
    """

    return sync_detailed(
        client=client,
        fee_category=fee_category,
        fee_code=fee_code,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: str,
    fee_code: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
) -> Response[Union[ApiFeeCodeLedgerAccount, ResponseError]]:
    """Get a fee-code-to-ledger-account mapping using the fee category, fee code, and as-of date

    Args:
        fee_category (str):
        fee_code (Union[Unset, str]):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiFeeCodeLedgerAccount, ResponseError]]
    """

    kwargs = _get_kwargs(
        fee_category=fee_category,
        fee_code=fee_code,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: str,
    fee_code: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
) -> Optional[Union[ApiFeeCodeLedgerAccount, ResponseError]]:
    """Get a fee-code-to-ledger-account mapping using the fee category, fee code, and as-of date

    Args:
        fee_category (str):
        fee_code (Union[Unset, str]):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiFeeCodeLedgerAccount, ResponseError]
    """

    return (
        await asyncio_detailed(
            client=client,
            fee_category=fee_category,
            fee_code=fee_code,
            date=date,
        )
    ).parsed
