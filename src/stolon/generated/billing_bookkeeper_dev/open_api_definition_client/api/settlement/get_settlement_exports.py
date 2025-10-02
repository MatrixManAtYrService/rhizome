import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_settlement_export import ApiSettlementExport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date,
    billing_entity_uuids: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    params["billingEntityUuids"] = billing_entity_uuids

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/settlement/export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiSettlementExport, list["ApiSettlementExport"]]]:
    if response.status_code == 200:
        response_200 = ApiSettlementExport.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiSettlementExport.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiSettlementExport, list["ApiSettlementExport"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    billing_entity_uuids: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ApiSettlementExport, list["ApiSettlementExport"]]]:
    """Get export data for settlement requests

    Args:
        date (datetime.date):
        billing_entity_uuids (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSettlementExport, list['ApiSettlementExport']]]
    """

    kwargs = _get_kwargs(
        date=date,
        billing_entity_uuids=billing_entity_uuids,
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
    date: datetime.date,
    billing_entity_uuids: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiSettlementExport, list["ApiSettlementExport"]]]:
    """Get export data for settlement requests

    Args:
        date (datetime.date):
        billing_entity_uuids (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSettlementExport, list['ApiSettlementExport']]
    """

    return sync_detailed(
        client=client,
        date=date,
        billing_entity_uuids=billing_entity_uuids,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    billing_entity_uuids: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ApiSettlementExport, list["ApiSettlementExport"]]]:
    """Get export data for settlement requests

    Args:
        date (datetime.date):
        billing_entity_uuids (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSettlementExport, list['ApiSettlementExport']]]
    """

    kwargs = _get_kwargs(
        date=date,
        billing_entity_uuids=billing_entity_uuids,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    billing_entity_uuids: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiSettlementExport, list["ApiSettlementExport"]]]:
    """Get export data for settlement requests

    Args:
        date (datetime.date):
        billing_entity_uuids (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSettlementExport, list['ApiSettlementExport']]
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            billing_entity_uuids=billing_entity_uuids,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
