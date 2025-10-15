from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_tier_detail import ApiTierDetail
from ...types import UNSET, Response


def _get_kwargs(
    *,
    rule_uuid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ruleUuid"] = rule_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tierdetail",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiTierDetail]:
    if response.status_code == 200:
        response_200 = ApiTierDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiTierDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_uuid: str,
) -> Response[ApiTierDetail]:
    """Get tier details

    Args:
        rule_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTierDetail]
    """

    kwargs = _get_kwargs(
        rule_uuid=rule_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_uuid: str,
) -> Optional[ApiTierDetail]:
    """Get tier details

    Args:
        rule_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTierDetail
    """

    return sync_detailed(
        client=client,
        rule_uuid=rule_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_uuid: str,
) -> Response[ApiTierDetail]:
    """Get tier details

    Args:
        rule_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTierDetail]
    """

    kwargs = _get_kwargs(
        rule_uuid=rule_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_uuid: str,
) -> Optional[ApiTierDetail]:
    """Get tier details

    Args:
        rule_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTierDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            rule_uuid=rule_uuid,
        )
    ).parsed
