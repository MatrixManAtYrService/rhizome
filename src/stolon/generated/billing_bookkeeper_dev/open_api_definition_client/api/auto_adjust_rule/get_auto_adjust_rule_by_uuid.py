from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_auto_adjust_rule_set import ApiAutoAdjustRuleSet
from ...types import Response


def _get_kwargs(
    uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/autoadjustrule/{uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiAutoAdjustRuleSet]:
    if response.status_code == 200:
        response_200 = ApiAutoAdjustRuleSet.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiAutoAdjustRuleSet.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiAutoAdjustRuleSet.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiAutoAdjustRuleSet]:
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
) -> Response[ApiAutoAdjustRuleSet]:
    """Get auto-adjust rule by UUID

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAutoAdjustRuleSet]
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
) -> Optional[ApiAutoAdjustRuleSet]:
    """Get auto-adjust rule by UUID

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAutoAdjustRuleSet
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiAutoAdjustRuleSet]:
    """Get auto-adjust rule by UUID

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAutoAdjustRuleSet]
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
) -> Optional[ApiAutoAdjustRuleSet]:
    """Get auto-adjust rule by UUID

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAutoAdjustRuleSet
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
