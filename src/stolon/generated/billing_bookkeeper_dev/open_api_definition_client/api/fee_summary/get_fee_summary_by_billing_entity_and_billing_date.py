import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billing_entity_uuid: str,
    date: Union[Unset, datetime.date] = UNSET,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billingEntityUuid"] = billing_entity_uuid

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_fee_category: Union[Unset, list[str]] = UNSET
    if not isinstance(fee_category, Unset):
        json_fee_category = fee_category

    params["feeCategory"] = json_fee_category

    params["feeCode"] = fee_code

    params["currency"] = currency

    params["excludeZeroAmounts"] = exclude_zero_amounts

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ResponseError]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ResponseError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    date: Union[Unset, datetime.date] = UNSET,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Get fee summary(ies) for a billing entity

    Args:
        billing_entity_uuid (str):
        date (Union[Unset, datetime.date]):
        fee_category (Union[Unset, list[str]]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_zero_amounts (Union[Unset, bool]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        date=date,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_zero_amounts=exclude_zero_amounts,
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
    billing_entity_uuid: str,
    date: Union[Unset, datetime.date] = UNSET,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Get fee summary(ies) for a billing entity

    Args:
        billing_entity_uuid (str):
        date (Union[Unset, datetime.date]):
        fee_category (Union[Unset, list[str]]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_zero_amounts (Union[Unset, bool]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        client=client,
        billing_entity_uuid=billing_entity_uuid,
        date=date,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_zero_amounts=exclude_zero_amounts,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    date: Union[Unset, datetime.date] = UNSET,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Get fee summary(ies) for a billing entity

    Args:
        billing_entity_uuid (str):
        date (Union[Unset, datetime.date]):
        fee_category (Union[Unset, list[str]]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_zero_amounts (Union[Unset, bool]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        date=date,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_zero_amounts=exclude_zero_amounts,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    date: Union[Unset, datetime.date] = UNSET,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Get fee summary(ies) for a billing entity

    Args:
        billing_entity_uuid (str):
        date (Union[Unset, datetime.date]):
        fee_category (Union[Unset, list[str]]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_zero_amounts (Union[Unset, bool]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_entity_uuid=billing_entity_uuid,
            date=date,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            exclude_zero_amounts=exclude_zero_amounts,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
