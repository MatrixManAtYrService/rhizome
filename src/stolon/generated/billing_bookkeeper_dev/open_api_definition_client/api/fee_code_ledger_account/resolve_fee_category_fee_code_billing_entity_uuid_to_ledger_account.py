import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_ledger_account import ApiLedgerAccount
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    billing_entity_uuid: str,
    *,
    fee_category: str,
    fee_code: str,
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
        "url": f"/v1/feecodeledgeracct/resolve/{billing_entity_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiLedgerAccount, ResponseError]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiLedgerAccount.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiLedgerAccount, ResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: str,
    fee_code: str,
    date: Union[Unset, datetime.date] = UNSET,
) -> Response[Union[ApiLedgerAccount, ResponseError]]:
    """Resolves a fee category and fee code pair to the fee-code-to-ledger-account mapping for a billing
    entity

    Args:
        billing_entity_uuid (str):
        fee_category (str):
        fee_code (str):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLedgerAccount, ResponseError]]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: str,
    fee_code: str,
    date: Union[Unset, datetime.date] = UNSET,
) -> Optional[Union[ApiLedgerAccount, ResponseError]]:
    """Resolves a fee category and fee code pair to the fee-code-to-ledger-account mapping for a billing
    entity

    Args:
        billing_entity_uuid (str):
        fee_category (str):
        fee_code (str):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLedgerAccount, ResponseError]
    """

    return sync_detailed(
        billing_entity_uuid=billing_entity_uuid,
        client=client,
        fee_category=fee_category,
        fee_code=fee_code,
        date=date,
    ).parsed


async def asyncio_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: str,
    fee_code: str,
    date: Union[Unset, datetime.date] = UNSET,
) -> Response[Union[ApiLedgerAccount, ResponseError]]:
    """Resolves a fee category and fee code pair to the fee-code-to-ledger-account mapping for a billing
    entity

    Args:
        billing_entity_uuid (str):
        fee_category (str):
        fee_code (str):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiLedgerAccount, ResponseError]]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: str,
    fee_code: str,
    date: Union[Unset, datetime.date] = UNSET,
) -> Optional[Union[ApiLedgerAccount, ResponseError]]:
    """Resolves a fee category and fee code pair to the fee-code-to-ledger-account mapping for a billing
    entity

    Args:
        billing_entity_uuid (str):
        fee_category (str):
        fee_code (str):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiLedgerAccount, ResponseError]
    """

    return (
        await asyncio_detailed(
            billing_entity_uuid=billing_entity_uuid,
            client=client,
            fee_category=fee_category,
            fee_code=fee_code,
            date=date,
        )
    ).parsed
