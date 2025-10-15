from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    r_id: str,
    *,
    fee_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Clover-Appenv"] = x_clover_appenv

    params: dict[str, Any] = {}

    params["feeUuid"] = fee_uuid

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/reseller/{r_id}/action",
        "params": params,
    }

    _kwargs["headers"] = headers
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
    r_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fee_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> Response[ResponseError]:
    """Get action by reseller

    Args:
        r_id (str):
        fee_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        r_id=r_id,
        fee_uuid=fee_uuid,
        page_size=page_size,
        page_number=page_number,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    r_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fee_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> Optional[ResponseError]:
    """Get action by reseller

    Args:
        r_id (str):
        fee_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        r_id=r_id,
        client=client,
        fee_uuid=fee_uuid,
        page_size=page_size,
        page_number=page_number,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    r_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fee_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> Response[ResponseError]:
    """Get action by reseller

    Args:
        r_id (str):
        fee_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        r_id=r_id,
        fee_uuid=fee_uuid,
        page_size=page_size,
        page_number=page_number,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    r_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fee_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    x_clover_appenv: str,
) -> Optional[ResponseError]:
    """Get action by reseller

    Args:
        r_id (str):
        fee_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return (
        await asyncio_detailed(
            r_id=r_id,
            client=client,
            fee_uuid=fee_uuid,
            page_size=page_size,
            page_number=page_number,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
