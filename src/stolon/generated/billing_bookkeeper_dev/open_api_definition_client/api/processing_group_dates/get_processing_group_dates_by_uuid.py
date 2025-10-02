from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_processing_group_dates import ApiProcessingGroupDates
from ...types import Response


def _get_kwargs(
    uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/processgroupdates/{uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiProcessingGroupDates]:
    if response.status_code == 200:
        response_200 = ApiProcessingGroupDates.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiProcessingGroupDates]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiProcessingGroupDates]:
    """Get processing group dates by UUID

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiProcessingGroupDates]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiProcessingGroupDates]:
    """Get processing group dates by UUID

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiProcessingGroupDates
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiProcessingGroupDates]:
    """Get processing group dates by UUID

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiProcessingGroupDates]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiProcessingGroupDates]:
    """Get processing group dates by UUID

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiProcessingGroupDates
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
