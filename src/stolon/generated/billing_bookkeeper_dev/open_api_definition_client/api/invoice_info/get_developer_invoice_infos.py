import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_invoice_info import ApiInvoiceInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    developer_uuid: str,
    *,
    date: Union[Unset, datetime.date] = UNSET,
    invoice_num: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Clover-Appenv"] = x_clover_appenv

    params: dict[str, Any] = {}

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["invoiceNum"] = invoice_num

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/developers/{developer_uuid}/invoiceinfo",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiInvoiceInfo, list["ApiInvoiceInfo"]]]:
    if response.status_code == 200:
        response_200 = ApiInvoiceInfo.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiInvoiceInfo.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiInvoiceInfo, list["ApiInvoiceInfo"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    developer_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    invoice_num: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> Response[Union[ApiInvoiceInfo, list["ApiInvoiceInfo"]]]:
    """Get invoice information for developer

    Args:
        developer_uuid (str):
        date (Union[Unset, datetime.date]):
        invoice_num (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiInvoiceInfo, list['ApiInvoiceInfo']]]
    """

    kwargs = _get_kwargs(
        developer_uuid=developer_uuid,
        date=date,
        invoice_num=invoice_num,
        page_size=page_size,
        page_number=page_number,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    developer_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    invoice_num: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> Optional[Union[ApiInvoiceInfo, list["ApiInvoiceInfo"]]]:
    """Get invoice information for developer

    Args:
        developer_uuid (str):
        date (Union[Unset, datetime.date]):
        invoice_num (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiInvoiceInfo, list['ApiInvoiceInfo']]
    """

    return sync_detailed(
        developer_uuid=developer_uuid,
        client=client,
        date=date,
        invoice_num=invoice_num,
        page_size=page_size,
        page_number=page_number,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    developer_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    invoice_num: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> Response[Union[ApiInvoiceInfo, list["ApiInvoiceInfo"]]]:
    """Get invoice information for developer

    Args:
        developer_uuid (str):
        date (Union[Unset, datetime.date]):
        invoice_num (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiInvoiceInfo, list['ApiInvoiceInfo']]]
    """

    kwargs = _get_kwargs(
        developer_uuid=developer_uuid,
        date=date,
        invoice_num=invoice_num,
        page_size=page_size,
        page_number=page_number,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    developer_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    invoice_num: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> Optional[Union[ApiInvoiceInfo, list["ApiInvoiceInfo"]]]:
    """Get invoice information for developer

    Args:
        developer_uuid (str):
        date (Union[Unset, datetime.date]):
        invoice_num (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiInvoiceInfo, list['ApiInvoiceInfo']]
    """

    return (
        await asyncio_detailed(
            developer_uuid=developer_uuid,
            client=client,
            date=date,
            invoice_num=invoice_num,
            page_size=page_size,
            page_number=page_number,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
