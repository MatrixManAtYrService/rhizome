from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_fee_ctd_extended import ApiFeeCtdExtended
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billing_entity_uuid: str,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billingEntityUuid"] = billing_entity_uuid

    json_fee_category: Union[Unset, list[str]] = UNSET
    if not isinstance(fee_category, Unset):
        json_fee_category = fee_category

    params["feeCategory"] = json_fee_category

    params["feeCode"] = fee_code

    params["currency"] = currency

    params["excludeZeroAmounts"] = exclude_zero_amounts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ctd",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiFeeCtdExtended]:
    if response.status_code == 200:
        response_200 = ApiFeeCtdExtended.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiFeeCtdExtended]:
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
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
) -> Response[ApiFeeCtdExtended]:
    """Get current-to-date fee(s) for a billing entity

    Args:
        billing_entity_uuid (str):
        fee_category (Union[Unset, list[str]]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_zero_amounts (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeCtdExtended]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_zero_amounts=exclude_zero_amounts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
) -> Optional[ApiFeeCtdExtended]:
    """Get current-to-date fee(s) for a billing entity

    Args:
        billing_entity_uuid (str):
        fee_category (Union[Unset, list[str]]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_zero_amounts (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeCtdExtended
    """

    return sync_detailed(
        client=client,
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_zero_amounts=exclude_zero_amounts,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
) -> Response[ApiFeeCtdExtended]:
    """Get current-to-date fee(s) for a billing entity

    Args:
        billing_entity_uuid (str):
        fee_category (Union[Unset, list[str]]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_zero_amounts (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeCtdExtended]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_zero_amounts=exclude_zero_amounts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    fee_category: Union[Unset, list[str]] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_zero_amounts: Union[Unset, bool] = UNSET,
) -> Optional[ApiFeeCtdExtended]:
    """Get current-to-date fee(s) for a billing entity

    Args:
        billing_entity_uuid (str):
        fee_category (Union[Unset, list[str]]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_zero_amounts (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeCtdExtended
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_entity_uuid=billing_entity_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            exclude_zero_amounts=exclude_zero_amounts,
        )
    ).parsed
