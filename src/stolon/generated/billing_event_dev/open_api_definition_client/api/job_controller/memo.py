from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_base_job_params import ApiBaseJobParams
from ...models.memo_response_200 import MemoResponse200
from ...types import Response


def _get_kwargs(
    heading: str,
    *,
    body: ApiBaseJobParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/job/execMemo/{heading}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MemoResponse200]:
    if response.status_code == 200:
        response_200 = MemoResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MemoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    heading: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBaseJobParams,
) -> Response[MemoResponse200]:
    """Billing Event may post a memo to the bookkeeper via a job.

    Args:
        heading (str):
        body (ApiBaseJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemoResponse200]
    """

    kwargs = _get_kwargs(
        heading=heading,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    heading: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBaseJobParams,
) -> Optional[MemoResponse200]:
    """Billing Event may post a memo to the bookkeeper via a job.

    Args:
        heading (str):
        body (ApiBaseJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemoResponse200
    """

    return sync_detailed(
        heading=heading,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    heading: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBaseJobParams,
) -> Response[MemoResponse200]:
    """Billing Event may post a memo to the bookkeeper via a job.

    Args:
        heading (str):
        body (ApiBaseJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemoResponse200]
    """

    kwargs = _get_kwargs(
        heading=heading,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    heading: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiBaseJobParams,
) -> Optional[MemoResponse200]:
    """Billing Event may post a memo to the bookkeeper via a job.

    Args:
        heading (str):
        body (ApiBaseJobParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemoResponse200
    """

    return (
        await asyncio_detailed(
            heading=heading,
            client=client,
            body=body,
        )
    ).parsed
