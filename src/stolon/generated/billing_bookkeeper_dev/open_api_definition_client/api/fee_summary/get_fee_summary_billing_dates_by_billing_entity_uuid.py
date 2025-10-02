import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx
from dateutil.parser import isoparse

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    billing_entity_uuid: str,
    *,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/summary/billingdates/{billing_entity_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[datetime.date, list[datetime.date]]]:
    if response.status_code == 200:
        response_200 = isoparse(response.json()).date()

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = isoparse(response_400_item_data).date()

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = isoparse(response_404_item_data).date()

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[datetime.date, list[datetime.date]]]:
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
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[datetime.date, list[datetime.date]]]:
    """Get billing dates for the summarized fees for a billing entity UUID

    Args:
        billing_entity_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[datetime.date, list[datetime.date]]]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        page_size=page_size,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[datetime.date, list[datetime.date]]]:
    """Get billing dates for the summarized fees for a billing entity UUID

    Args:
        billing_entity_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[datetime.date, list[datetime.date]]
    """

    return sync_detailed(
        billing_entity_uuid=billing_entity_uuid,
        client=client,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[datetime.date, list[datetime.date]]]:
    """Get billing dates for the summarized fees for a billing entity UUID

    Args:
        billing_entity_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[datetime.date, list[datetime.date]]]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[datetime.date, list[datetime.date]]]:
    """Get billing dates for the summarized fees for a billing entity UUID

    Args:
        billing_entity_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[datetime.date, list[datetime.date]]
    """

    return (
        await asyncio_detailed(
            billing_entity_uuid=billing_entity_uuid,
            client=client,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
