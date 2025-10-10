from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_device_type import ApiDeviceType
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    serial_number: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/devicetype/lookup/{serial_number}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiDeviceType, ResponseError]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiDeviceType.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiDeviceType.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiDeviceType, ResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    serial_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiDeviceType, ResponseError]]:
    """Get device type for the specified serial number

    Args:
        serial_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiDeviceType, ResponseError]]
    """

    kwargs = _get_kwargs(
        serial_number=serial_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    serial_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiDeviceType, ResponseError]]:
    """Get device type for the specified serial number

    Args:
        serial_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiDeviceType, ResponseError]
    """

    return sync_detailed(
        serial_number=serial_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    serial_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ApiDeviceType, ResponseError]]:
    """Get device type for the specified serial number

    Args:
        serial_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiDeviceType, ResponseError]]
    """

    kwargs = _get_kwargs(
        serial_number=serial_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    serial_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ApiDeviceType, ResponseError]]:
    """Get device type for the specified serial number

    Args:
        serial_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiDeviceType, ResponseError]
    """

    return (
        await asyncio_detailed(
            serial_number=serial_number,
            client=client,
        )
    ).parsed
