import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    processing_group_uuid: str,
    *,
    hierarchy_type: str,
    date: datetime.date,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["hierarchyType"] = hierarchy_type

    json_date = date.isoformat()
    params["date"] = json_date

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/hierarchycycle/{processing_group_uuid}/purge",
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
    processing_group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    date: datetime.date,
    page_size: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Purge billing hierarchy cycle entries for the processing group and hierarchy type where the cycle
    date is before the specified date

    Args:
        processing_group_uuid (str):
        hierarchy_type (str):
        date (datetime.date):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        processing_group_uuid=processing_group_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    processing_group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    date: datetime.date,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Purge billing hierarchy cycle entries for the processing group and hierarchy type where the cycle
    date is before the specified date

    Args:
        processing_group_uuid (str):
        hierarchy_type (str):
        date (datetime.date):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        processing_group_uuid=processing_group_uuid,
        client=client,
        hierarchy_type=hierarchy_type,
        date=date,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    processing_group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    date: datetime.date,
    page_size: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Purge billing hierarchy cycle entries for the processing group and hierarchy type where the cycle
    date is before the specified date

    Args:
        processing_group_uuid (str):
        hierarchy_type (str):
        date (datetime.date):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        processing_group_uuid=processing_group_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    processing_group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    date: datetime.date,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Purge billing hierarchy cycle entries for the processing group and hierarchy type where the cycle
    date is before the specified date

    Args:
        processing_group_uuid (str):
        hierarchy_type (str):
        date (datetime.date):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return (
        await asyncio_detailed(
            processing_group_uuid=processing_group_uuid,
            client=client,
            hierarchy_type=hierarchy_type,
            date=date,
            page_size=page_size,
        )
    ).parsed
