import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mlc_captured_events_response_200 import GetMlcCapturedEventsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["merchantUuid"] = merchant_uuid

    params["resellerUuid"] = reseller_uuid

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/mlc_captured_event",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMlcCapturedEventsResponse200]:
    if response.status_code == 200:
        response_200 = GetMlcCapturedEventsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMlcCapturedEventsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[GetMlcCapturedEventsResponse200]:
    """Get captured MLC events

    Args:
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMlcCapturedEventsResponse200]
    """

    kwargs = _get_kwargs(
        merchant_uuid=merchant_uuid,
        reseller_uuid=reseller_uuid,
        start_date=start_date,
        end_date=end_date,
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
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[GetMlcCapturedEventsResponse200]:
    """Get captured MLC events

    Args:
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMlcCapturedEventsResponse200
    """

    return sync_detailed(
        client=client,
        merchant_uuid=merchant_uuid,
        reseller_uuid=reseller_uuid,
        start_date=start_date,
        end_date=end_date,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[GetMlcCapturedEventsResponse200]:
    """Get captured MLC events

    Args:
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMlcCapturedEventsResponse200]
    """

    kwargs = _get_kwargs(
        merchant_uuid=merchant_uuid,
        reseller_uuid=reseller_uuid,
        start_date=start_date,
        end_date=end_date,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[GetMlcCapturedEventsResponse200]:
    """Get captured MLC events

    Args:
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMlcCapturedEventsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            merchant_uuid=merchant_uuid,
            reseller_uuid=reseller_uuid,
            start_date=start_date,
            end_date=end_date,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
