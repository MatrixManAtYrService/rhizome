from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_base_job_params import ApiBaseJobParams
from ...models.enqueue_process_app_sub_events_job_response_200 import EnqueueProcessAppSubEventsJobResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: ApiBaseJobParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job/processAppSubEvents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EnqueueProcessAppSubEventsJobResponse200]:
    if response.status_code == 200:
        response_200 = EnqueueProcessAppSubEventsJobResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EnqueueProcessAppSubEventsJobResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBaseJobParams,
) -> Response[EnqueueProcessAppSubEventsJobResponse200]:
    """Enqueues daily job for processing app subscription events that occurred throughout the day

    Args:
        body (ApiBaseJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnqueueProcessAppSubEventsJobResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBaseJobParams,
) -> Optional[EnqueueProcessAppSubEventsJobResponse200]:
    """Enqueues daily job for processing app subscription events that occurred throughout the day

    Args:
        body (ApiBaseJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnqueueProcessAppSubEventsJobResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBaseJobParams,
) -> Response[EnqueueProcessAppSubEventsJobResponse200]:
    """Enqueues daily job for processing app subscription events that occurred throughout the day

    Args:
        body (ApiBaseJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnqueueProcessAppSubEventsJobResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBaseJobParams,
) -> Optional[EnqueueProcessAppSubEventsJobResponse200]:
    """Enqueues daily job for processing app subscription events that occurred throughout the day

    Args:
        body (ApiBaseJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnqueueProcessAppSubEventsJobResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
