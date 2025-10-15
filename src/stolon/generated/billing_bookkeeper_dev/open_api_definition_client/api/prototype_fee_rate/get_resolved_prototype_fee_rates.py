from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hierarchy_type: str,
    prototype_fee_set_uuid: str,
    billing_entity_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_rates_be_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["hierarchyType"] = hierarchy_type

    params["prototypeFeeSetUuid"] = prototype_fee_set_uuid

    params["billingEntityUuid"] = billing_entity_uuid

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    params["currency"] = currency

    params["excludeRatesBeUuid"] = exclude_rates_be_uuid

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/prototypefeerate",
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
    hierarchy_type: str,
    prototype_fee_set_uuid: str,
    billing_entity_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_rates_be_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Get resolved prototype fee rates by prototype fee set, hierarchy type, billing entity, date, fee
    category, fee code, and/or currency

    Args:
        hierarchy_type (str):
        prototype_fee_set_uuid (str):
        billing_entity_uuid (str):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_rates_be_uuid (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        hierarchy_type=hierarchy_type,
        prototype_fee_set_uuid=prototype_fee_set_uuid,
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_rates_be_uuid=exclude_rates_be_uuid,
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
    hierarchy_type: str,
    prototype_fee_set_uuid: str,
    billing_entity_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_rates_be_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Get resolved prototype fee rates by prototype fee set, hierarchy type, billing entity, date, fee
    category, fee code, and/or currency

    Args:
        hierarchy_type (str):
        prototype_fee_set_uuid (str):
        billing_entity_uuid (str):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_rates_be_uuid (Union[Unset, str]):
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
        hierarchy_type=hierarchy_type,
        prototype_fee_set_uuid=prototype_fee_set_uuid,
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_rates_be_uuid=exclude_rates_be_uuid,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    prototype_fee_set_uuid: str,
    billing_entity_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_rates_be_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Get resolved prototype fee rates by prototype fee set, hierarchy type, billing entity, date, fee
    category, fee code, and/or currency

    Args:
        hierarchy_type (str):
        prototype_fee_set_uuid (str):
        billing_entity_uuid (str):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_rates_be_uuid (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        hierarchy_type=hierarchy_type,
        prototype_fee_set_uuid=prototype_fee_set_uuid,
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        currency=currency,
        exclude_rates_be_uuid=exclude_rates_be_uuid,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    prototype_fee_set_uuid: str,
    billing_entity_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    exclude_rates_be_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Get resolved prototype fee rates by prototype fee set, hierarchy type, billing entity, date, fee
    category, fee code, and/or currency

    Args:
        hierarchy_type (str):
        prototype_fee_set_uuid (str):
        billing_entity_uuid (str):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        exclude_rates_be_uuid (Union[Unset, str]):
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
            hierarchy_type=hierarchy_type,
            prototype_fee_set_uuid=prototype_fee_set_uuid,
            billing_entity_uuid=billing_entity_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            exclude_rates_be_uuid=exclude_rates_be_uuid,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
