from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    m_uuid: str,
    *,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    expand: Union[Unset, str] = UNSET,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    params: dict[str, Any] = {}

    params["startDate"] = start_date

    params["endDate"] = end_date

    params["expand"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/external/payments/{m_uuid}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    m_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    expand: Union[Unset, str] = UNSET,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        m_uuid (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        expand (Union[Unset, str]):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        m_uuid=m_uuid,
        start_date=start_date,
        end_date=end_date,
        expand=expand,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    m_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    expand: Union[Unset, str] = UNSET,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        m_uuid (str):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        expand (Union[Unset, str]):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        m_uuid=m_uuid,
        start_date=start_date,
        end_date=end_date,
        expand=expand,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
