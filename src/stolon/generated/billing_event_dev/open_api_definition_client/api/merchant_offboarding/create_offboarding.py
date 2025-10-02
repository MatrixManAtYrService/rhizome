from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_merchant_offboarding import ApiMerchantOffboarding
from ...models.create_offboarding_request import CreateOffboardingRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateOffboardingRequest,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/offboarding",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    body: CreateOffboardingRequest,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[ApiMerchantOffboarding]:
    """Create offboarding

    Args:
        x_clover_appenv (Union[Unset, str]):
        body (CreateOffboardingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMerchantOffboarding]
    """

    kwargs = _get_kwargs(
        body=body,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateOffboardingRequest,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[ApiMerchantOffboarding]:
    """Create offboarding

    Args:
        x_clover_appenv (Union[Unset, str]):
        body (CreateOffboardingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMerchantOffboarding
    """

    return sync_detailed(
        client=client,
        body=body,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateOffboardingRequest,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[ApiMerchantOffboarding]:
    """Create offboarding

    Args:
        x_clover_appenv (Union[Unset, str]):
        body (CreateOffboardingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMerchantOffboarding]
    """

    kwargs = _get_kwargs(
        body=body,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateOffboardingRequest,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[ApiMerchantOffboarding]:
    """Create offboarding

    Args:
        x_clover_appenv (Union[Unset, str]):
        body (CreateOffboardingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMerchantOffboarding
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
