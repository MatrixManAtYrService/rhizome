from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_merchant_offboarding import ApiMerchantOffboarding
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    merchant_uuid: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    params: dict[str, Any] = {}

    params["merchantUuid"] = merchant_uuid

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/offboarding",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiMerchantOffboarding]:
    if response.status_code == 200:
        response_200 = ApiMerchantOffboarding.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiMerchantOffboarding]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[ApiMerchantOffboarding]:
    """get all offboardings by step and option merchant uuid

    Args:
        merchant_uuid (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMerchantOffboarding]
    """

    kwargs = _get_kwargs(
        merchant_uuid=merchant_uuid,
        page_number=page_number,
        page_size=page_size,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[ApiMerchantOffboarding]:
    """get all offboardings by step and option merchant uuid

    Args:
        merchant_uuid (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMerchantOffboarding
    """

    return sync_detailed(
        client=client,
        merchant_uuid=merchant_uuid,
        page_number=page_number,
        page_size=page_size,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[ApiMerchantOffboarding]:
    """get all offboardings by step and option merchant uuid

    Args:
        merchant_uuid (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMerchantOffboarding]
    """

    kwargs = _get_kwargs(
        merchant_uuid=merchant_uuid,
        page_number=page_number,
        page_size=page_size,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    merchant_uuid: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[ApiMerchantOffboarding]:
    """get all offboardings by step and option merchant uuid

    Args:
        merchant_uuid (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMerchantOffboarding
    """

    return (
        await asyncio_detailed(
            client=client,
            merchant_uuid=merchant_uuid,
            page_number=page_number,
            page_size=page_size,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
