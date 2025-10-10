from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_tiered_qualifier import ApiTieredQualifier
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rule_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ruleUuid"] = rule_uuid

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tieredqualifier",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiTieredQualifier]:
    if response.status_code == 200:
        response_200 = ApiTieredQualifier.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiTieredQualifier]:
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
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
) -> Response[ApiTieredQualifier]:
    """Get tiered qualifiers for a tiered pricing rule

    Args:
        rule_uuid (str):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTieredQualifier]
    """

    kwargs = _get_kwargs(
        rule_uuid=rule_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
) -> Optional[ApiTieredQualifier]:
    """Get tiered qualifiers for a tiered pricing rule

    Args:
        rule_uuid (str):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTieredQualifier
    """

    return sync_detailed(
        client=client,
        rule_uuid=rule_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
) -> Response[ApiTieredQualifier]:
    """Get tiered qualifiers for a tiered pricing rule

    Args:
        rule_uuid (str):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTieredQualifier]
    """

    kwargs = _get_kwargs(
        rule_uuid=rule_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_uuid: str,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
) -> Optional[ApiTieredQualifier]:
    """Get tiered qualifiers for a tiered pricing rule

    Args:
        rule_uuid (str):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTieredQualifier
    """

    return (
        await asyncio_detailed(
            client=client,
            rule_uuid=rule_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
        )
    ).parsed
