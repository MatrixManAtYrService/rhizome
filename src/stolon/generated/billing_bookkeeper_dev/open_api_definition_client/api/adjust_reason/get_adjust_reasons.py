from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_adjust_reason import ApiAdjustReason
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    adjust_reason: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["adjustReason"] = adjust_reason

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/adjustreason",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiAdjustReason]:
    if response.status_code == 200:
        response_200 = ApiAdjustReason.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiAdjustReason]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    adjust_reason: Union[Unset, str] = UNSET,
) -> Response[ApiAdjustReason]:
    """Get adjustment reasons optionally filtering by reason value

    Args:
        adjust_reason (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAdjustReason]
    """

    kwargs = _get_kwargs(
        adjust_reason=adjust_reason,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    adjust_reason: Union[Unset, str] = UNSET,
) -> Optional[ApiAdjustReason]:
    """Get adjustment reasons optionally filtering by reason value

    Args:
        adjust_reason (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAdjustReason
    """

    return sync_detailed(
        client=client,
        adjust_reason=adjust_reason,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    adjust_reason: Union[Unset, str] = UNSET,
) -> Response[ApiAdjustReason]:
    """Get adjustment reasons optionally filtering by reason value

    Args:
        adjust_reason (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAdjustReason]
    """

    kwargs = _get_kwargs(
        adjust_reason=adjust_reason,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    adjust_reason: Union[Unset, str] = UNSET,
) -> Optional[ApiAdjustReason]:
    """Get adjustment reasons optionally filtering by reason value

    Args:
        adjust_reason (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAdjustReason
    """

    return (
        await asyncio_detailed(
            client=client,
            adjust_reason=adjust_reason,
        )
    ).parsed
