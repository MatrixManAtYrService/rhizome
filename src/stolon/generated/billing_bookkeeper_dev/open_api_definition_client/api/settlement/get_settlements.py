import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_settlement import ApiSettlement
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: Union[Unset, datetime.date] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    entity_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["billingEntityUuid"] = billing_entity_uuid

    params["entityUuid"] = entity_uuid

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/settlement",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ResponseError, list["ApiSettlement"]]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiSettlement.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ResponseError, list["ApiSettlement"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    entity_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ResponseError, list["ApiSettlement"]]]:
    """Get settlement requests

    Args:
        date (Union[Unset, datetime.date]):
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseError, list['ApiSettlement']]]
    """

    kwargs = _get_kwargs(
        date=date,
        billing_entity_uuid=billing_entity_uuid,
        entity_uuid=entity_uuid,
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
    date: Union[Unset, datetime.date] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    entity_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ResponseError, list["ApiSettlement"]]]:
    """Get settlement requests

    Args:
        date (Union[Unset, datetime.date]):
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseError, list['ApiSettlement']]
    """

    return sync_detailed(
        client=client,
        date=date,
        billing_entity_uuid=billing_entity_uuid,
        entity_uuid=entity_uuid,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    entity_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ResponseError, list["ApiSettlement"]]]:
    """Get settlement requests

    Args:
        date (Union[Unset, datetime.date]):
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseError, list['ApiSettlement']]]
    """

    kwargs = _get_kwargs(
        date=date,
        billing_entity_uuid=billing_entity_uuid,
        entity_uuid=entity_uuid,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.date] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    entity_uuid: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ResponseError, list["ApiSettlement"]]]:
    """Get settlement requests

    Args:
        date (Union[Unset, datetime.date]):
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseError, list['ApiSettlement']]
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            billing_entity_uuid=billing_entity_uuid,
            entity_uuid=entity_uuid,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
