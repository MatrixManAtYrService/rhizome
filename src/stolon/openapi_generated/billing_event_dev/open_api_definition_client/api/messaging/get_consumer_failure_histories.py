import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_consumer_failure_history import ApiConsumerFailureHistory
from ...models.get_consumer_failure_histories_response_200 import GetConsumerFailureHistoriesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    topic: Union[Unset, str] = UNSET,
    reference_id: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["topic"] = topic

    params["referenceId"] = reference_id

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
        "url": "/v1/messaging/failures/consumer/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetConsumerFailureHistoriesResponse200, list["ApiConsumerFailureHistory"]]]:
    if response.status_code == 200:
        response_200 = GetConsumerFailureHistoriesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiConsumerFailureHistory.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetConsumerFailureHistoriesResponse200, list["ApiConsumerFailureHistory"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    topic: Union[Unset, str] = UNSET,
    reference_id: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[GetConsumerFailureHistoriesResponse200, list["ApiConsumerFailureHistory"]]]:
    """Get consumer failure histories

    Args:
        topic (Union[Unset, str]):
        reference_id (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetConsumerFailureHistoriesResponse200, list['ApiConsumerFailureHistory']]]
    """

    kwargs = _get_kwargs(
        topic=topic,
        reference_id=reference_id,
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
    topic: Union[Unset, str] = UNSET,
    reference_id: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[GetConsumerFailureHistoriesResponse200, list["ApiConsumerFailureHistory"]]]:
    """Get consumer failure histories

    Args:
        topic (Union[Unset, str]):
        reference_id (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetConsumerFailureHistoriesResponse200, list['ApiConsumerFailureHistory']]
    """

    return sync_detailed(
        client=client,
        topic=topic,
        reference_id=reference_id,
        start_date=start_date,
        end_date=end_date,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    topic: Union[Unset, str] = UNSET,
    reference_id: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[GetConsumerFailureHistoriesResponse200, list["ApiConsumerFailureHistory"]]]:
    """Get consumer failure histories

    Args:
        topic (Union[Unset, str]):
        reference_id (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetConsumerFailureHistoriesResponse200, list['ApiConsumerFailureHistory']]]
    """

    kwargs = _get_kwargs(
        topic=topic,
        reference_id=reference_id,
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
    topic: Union[Unset, str] = UNSET,
    reference_id: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[GetConsumerFailureHistoriesResponse200, list["ApiConsumerFailureHistory"]]]:
    """Get consumer failure histories

    Args:
        topic (Union[Unset, str]):
        reference_id (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetConsumerFailureHistoriesResponse200, list['ApiConsumerFailureHistory']]
    """

    return (
        await asyncio_detailed(
            client=client,
            topic=topic,
            reference_id=reference_id,
            start_date=start_date,
            end_date=end_date,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
