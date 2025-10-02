from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backfill_acceptances_job_params import ApiBackfillAcceptancesJobParams
from ...models.enqueue_create_backfill_acceptances_job_response_200 import (
    EnqueueCreateBackfillAcceptancesJobResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ApiBackfillAcceptancesJobParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job/backfillAcceptances",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EnqueueCreateBackfillAcceptancesJobResponse200]:
    if response.status_code == 200:
        response_200 = EnqueueCreateBackfillAcceptancesJobResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EnqueueCreateBackfillAcceptancesJobResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBackfillAcceptancesJobParams,
) -> Response[EnqueueCreateBackfillAcceptancesJobResponse200]:
    """Creates backfill acceptances in bulk.

    Args:
        body (ApiBackfillAcceptancesJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnqueueCreateBackfillAcceptancesJobResponse200]
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
    body: ApiBackfillAcceptancesJobParams,
) -> Optional[EnqueueCreateBackfillAcceptancesJobResponse200]:
    """Creates backfill acceptances in bulk.

    Args:
        body (ApiBackfillAcceptancesJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnqueueCreateBackfillAcceptancesJobResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBackfillAcceptancesJobParams,
) -> Response[EnqueueCreateBackfillAcceptancesJobResponse200]:
    """Creates backfill acceptances in bulk.

    Args:
        body (ApiBackfillAcceptancesJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnqueueCreateBackfillAcceptancesJobResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBackfillAcceptancesJobParams,
) -> Optional[EnqueueCreateBackfillAcceptancesJobResponse200]:
    """Creates backfill acceptances in bulk.

    Args:
        body (ApiBackfillAcceptancesJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnqueueCreateBackfillAcceptancesJobResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
