from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_fee_ytd_extended import ApiFeeYtdExtended
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billing_entity_uuid: str,
    year: int,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billingEntityUuid"] = billing_entity_uuid

    params["year"] = year

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ytd",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiFeeYtdExtended]:
    if response.status_code == 200:
        response_200 = ApiFeeYtdExtended.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiFeeYtdExtended]:
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
    year: int,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
) -> Response[ApiFeeYtdExtended]:
    """Get year-to-date fee(s) for a billing entity

    Args:
        billing_entity_uuid (str):
        year (int):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeYtdExtended]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        year=year,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    year: int,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
) -> Optional[ApiFeeYtdExtended]:
    """Get year-to-date fee(s) for a billing entity

    Args:
        billing_entity_uuid (str):
        year (int):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeYtdExtended
    """

    return sync_detailed(
        client=client,
        billing_entity_uuid=billing_entity_uuid,
        year=year,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    year: int,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
) -> Response[ApiFeeYtdExtended]:
    """Get year-to-date fee(s) for a billing entity

    Args:
        billing_entity_uuid (str):
        year (int):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeYtdExtended]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        year=year,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    year: int,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
) -> Optional[ApiFeeYtdExtended]:
    """Get year-to-date fee(s) for a billing entity

    Args:
        billing_entity_uuid (str):
        year (int):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeYtdExtended
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_entity_uuid=billing_entity_uuid,
            year=year,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
        )
    ).parsed
