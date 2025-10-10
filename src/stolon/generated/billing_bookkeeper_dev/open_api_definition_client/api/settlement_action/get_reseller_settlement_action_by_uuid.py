from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_settlement_action import ApiSettlementAction
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    r_id: str,
    uuid: str,
    *,
    x_clover_appenv: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Clover-Appenv"] = x_clover_appenv

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/resellers/{r_id}/settlementaction/{uuid}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiSettlementAction, ResponseError]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiSettlementAction.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiSettlementAction.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiSettlementAction, ResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    r_id: str,
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: str,
) -> Response[Union[ApiSettlementAction, ResponseError]]:
    """Get a settlement action by UUID

    Args:
        r_id (str):
        uuid (str):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSettlementAction, ResponseError]]
    """

    kwargs = _get_kwargs(
        r_id=r_id,
        uuid=uuid,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    r_id: str,
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: str,
) -> Optional[Union[ApiSettlementAction, ResponseError]]:
    """Get a settlement action by UUID

    Args:
        r_id (str):
        uuid (str):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSettlementAction, ResponseError]
    """

    return sync_detailed(
        r_id=r_id,
        uuid=uuid,
        client=client,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    r_id: str,
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: str,
) -> Response[Union[ApiSettlementAction, ResponseError]]:
    """Get a settlement action by UUID

    Args:
        r_id (str):
        uuid (str):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSettlementAction, ResponseError]]
    """

    kwargs = _get_kwargs(
        r_id=r_id,
        uuid=uuid,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    r_id: str,
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_clover_appenv: str,
) -> Optional[Union[ApiSettlementAction, ResponseError]]:
    """Get a settlement action by UUID

    Args:
        r_id (str):
        uuid (str):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSettlementAction, ResponseError]
    """

    return (
        await asyncio_detailed(
            r_id=r_id,
            uuid=uuid,
            client=client,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
