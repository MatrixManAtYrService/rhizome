from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_invoice_alliance_code import ApiInvoiceAllianceCode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    alliance_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billingEntityUuid"] = billing_entity_uuid

    params["allianceCode"] = alliance_code

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alliancecode",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiInvoiceAllianceCode]:
    if response.status_code == 200:
        response_200 = ApiInvoiceAllianceCode.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiInvoiceAllianceCode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: Union[Unset, str] = UNSET,
    alliance_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiInvoiceAllianceCode]:
    """Get invoice alliance codes

    Args:
        billing_entity_uuid (Union[Unset, str]):
        alliance_code (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiInvoiceAllianceCode]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        alliance_code=alliance_code,
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
    billing_entity_uuid: Union[Unset, str] = UNSET,
    alliance_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiInvoiceAllianceCode]:
    """Get invoice alliance codes

    Args:
        billing_entity_uuid (Union[Unset, str]):
        alliance_code (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiInvoiceAllianceCode
    """

    return sync_detailed(
        client=client,
        billing_entity_uuid=billing_entity_uuid,
        alliance_code=alliance_code,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: Union[Unset, str] = UNSET,
    alliance_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiInvoiceAllianceCode]:
    """Get invoice alliance codes

    Args:
        billing_entity_uuid (Union[Unset, str]):
        alliance_code (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiInvoiceAllianceCode]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        alliance_code=alliance_code,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: Union[Unset, str] = UNSET,
    alliance_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiInvoiceAllianceCode]:
    """Get invoice alliance codes

    Args:
        billing_entity_uuid (Union[Unset, str]):
        alliance_code (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiInvoiceAllianceCode
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_entity_uuid=billing_entity_uuid,
            alliance_code=alliance_code,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
