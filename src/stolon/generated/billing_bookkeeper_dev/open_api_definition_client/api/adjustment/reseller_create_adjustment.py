from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_adjustment import ApiAdjustment
from ...types import Response


def _get_kwargs(
    r_id: str,
    *,
    body: ApiAdjustment,
    x_clover_appenv: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Clover-Appenv"] = x_clover_appenv

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/resellers/{r_id}/adjustment",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiAdjustment]:
    if response.status_code == 200:
        response_200 = ApiAdjustment.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiAdjustment]:
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
    body: ApiAdjustment,
    x_clover_appenv: str,
) -> Response[ApiAdjustment]:
    """Create adjustment for an entity that reseller can access

    Args:
        r_id (str):
        x_clover_appenv (str):
        body (ApiAdjustment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAdjustment]
    """

    kwargs = _get_kwargs(
        r_id=r_id,
        body=body,
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
    body: ApiAdjustment,
    x_clover_appenv: str,
) -> Optional[ApiAdjustment]:
    """Create adjustment for an entity that reseller can access

    Args:
        r_id (str):
        x_clover_appenv (str):
        body (ApiAdjustment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAdjustment
    """

    return sync_detailed(
        r_id=r_id,
        client=client,
        body=body,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    r_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAdjustment,
    x_clover_appenv: str,
) -> Response[ApiAdjustment]:
    """Create adjustment for an entity that reseller can access

    Args:
        r_id (str):
        x_clover_appenv (str):
        body (ApiAdjustment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAdjustment]
    """

    kwargs = _get_kwargs(
        r_id=r_id,
        body=body,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    r_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAdjustment,
    x_clover_appenv: str,
) -> Optional[ApiAdjustment]:
    """Create adjustment for an entity that reseller can access

    Args:
        r_id (str):
        x_clover_appenv (str):
        body (ApiAdjustment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAdjustment
    """

    return (
        await asyncio_detailed(
            r_id=r_id,
            client=client,
            body=body,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
