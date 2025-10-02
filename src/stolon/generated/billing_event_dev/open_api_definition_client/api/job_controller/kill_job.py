from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.kill_job_response_200 import KillJobResponse200
from ...types import Response


def _get_kwargs(
    request_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/job/kill/{request_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[KillJobResponse200]:
    if response.status_code == 200:
        response_200 = KillJobResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[KillJobResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    request_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[KillJobResponse200]:
    """Requests that the job associated with the specified billing request UUID be marked for termination
    (be killed).

    Args:
        request_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KillJobResponse200]
    """

    kwargs = _get_kwargs(
        request_uuid=request_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    request_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[KillJobResponse200]:
    """Requests that the job associated with the specified billing request UUID be marked for termination
    (be killed).

    Args:
        request_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KillJobResponse200
    """

    return sync_detailed(
        request_uuid=request_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    request_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[KillJobResponse200]:
    """Requests that the job associated with the specified billing request UUID be marked for termination
    (be killed).

    Args:
        request_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KillJobResponse200]
    """

    kwargs = _get_kwargs(
        request_uuid=request_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    request_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[KillJobResponse200]:
    """Requests that the job associated with the specified billing request UUID be marked for termination
    (be killed).

    Args:
        request_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KillJobResponse200
    """

    return (
        await asyncio_detailed(
            request_uuid=request_uuid,
            client=client,
        )
    ).parsed
