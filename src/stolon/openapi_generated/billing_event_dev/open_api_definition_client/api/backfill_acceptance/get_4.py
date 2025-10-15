from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_4_response_200 import Get4Response200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    merchant_uuid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["merchantUuid"] = merchant_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/backfill_acceptance",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Get4Response200]:
    if response.status_code == 200:
        response_200 = Get4Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Get4Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: str,
) -> Response[Get4Response200]:
    """Retrieve backfilled acceptances by merchant ID and agreement type

    Args:
        merchant_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get4Response200]
    """

    kwargs = _get_kwargs(
        merchant_uuid=merchant_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: str,
) -> Optional[Get4Response200]:
    """Retrieve backfilled acceptances by merchant ID and agreement type

    Args:
        merchant_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get4Response200
    """

    return sync_detailed(
        client=client,
        merchant_uuid=merchant_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: str,
) -> Response[Get4Response200]:
    """Retrieve backfilled acceptances by merchant ID and agreement type

    Args:
        merchant_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get4Response200]
    """

    kwargs = _get_kwargs(
        merchant_uuid=merchant_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: str,
) -> Optional[Get4Response200]:
    """Retrieve backfilled acceptances by merchant ID and agreement type

    Args:
        merchant_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get4Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            merchant_uuid=merchant_uuid,
        )
    ).parsed
