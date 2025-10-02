import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_invoice_info_extended import ApiInvoiceInfoExtended
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    merchant_uuids: list[str],
    date: Union[Unset, datetime.date] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_merchant_uuids = merchant_uuids

    params["merchantUuids"] = json_merchant_uuids

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/invoiceinfo/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiInvoiceInfoExtended, list["ApiInvoiceInfoExtended"]]]:
    if response.status_code == 200:
        response_200 = ApiInvoiceInfoExtended.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiInvoiceInfoExtended.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 500:
        response_500 = []
        _response_500 = response.json()
        for response_500_item_data in _response_500:
            response_500_item = ApiInvoiceInfoExtended.from_dict(response_500_item_data)

            response_500.append(response_500_item)

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiInvoiceInfoExtended, list["ApiInvoiceInfoExtended"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuids: list[str],
    date: Union[Unset, datetime.date] = UNSET,
) -> Response[Union[ApiInvoiceInfoExtended, list["ApiInvoiceInfoExtended"]]]:
    """Return Extended Invoice Information per Location

     Returns a list of Invoice_info objects with Invoice_info_extended filtered by a list of merchant
    UUIDs and invoice date. This endpoint is intended to provide a summary view per location.

    Args:
        merchant_uuids (list[str]):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiInvoiceInfoExtended, list['ApiInvoiceInfoExtended']]]
    """

    kwargs = _get_kwargs(
        merchant_uuids=merchant_uuids,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuids: list[str],
    date: Union[Unset, datetime.date] = UNSET,
) -> Optional[Union[ApiInvoiceInfoExtended, list["ApiInvoiceInfoExtended"]]]:
    """Return Extended Invoice Information per Location

     Returns a list of Invoice_info objects with Invoice_info_extended filtered by a list of merchant
    UUIDs and invoice date. This endpoint is intended to provide a summary view per location.

    Args:
        merchant_uuids (list[str]):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiInvoiceInfoExtended, list['ApiInvoiceInfoExtended']]
    """

    return sync_detailed(
        client=client,
        merchant_uuids=merchant_uuids,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuids: list[str],
    date: Union[Unset, datetime.date] = UNSET,
) -> Response[Union[ApiInvoiceInfoExtended, list["ApiInvoiceInfoExtended"]]]:
    """Return Extended Invoice Information per Location

     Returns a list of Invoice_info objects with Invoice_info_extended filtered by a list of merchant
    UUIDs and invoice date. This endpoint is intended to provide a summary view per location.

    Args:
        merchant_uuids (list[str]):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiInvoiceInfoExtended, list['ApiInvoiceInfoExtended']]]
    """

    kwargs = _get_kwargs(
        merchant_uuids=merchant_uuids,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuids: list[str],
    date: Union[Unset, datetime.date] = UNSET,
) -> Optional[Union[ApiInvoiceInfoExtended, list["ApiInvoiceInfoExtended"]]]:
    """Return Extended Invoice Information per Location

     Returns a list of Invoice_info objects with Invoice_info_extended filtered by a list of merchant
    UUIDs and invoice date. This endpoint is intended to provide a summary view per location.

    Args:
        merchant_uuids (list[str]):
        date (Union[Unset, datetime.date]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiInvoiceInfoExtended, list['ApiInvoiceInfoExtended']]
    """

    return (
        await asyncio_detailed(
            client=client,
            merchant_uuids=merchant_uuids,
            date=date,
        )
    ).parsed
