from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    params["developerUuid"] = developer_uuid

    params["developerAppUuid"] = developer_app_uuid

    params["appSubscriptionUuid"] = app_subscription_uuid

    params["appMeteredUuid"] = app_metered_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/feecodeapp",
        "params": params,
    }

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
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
) -> Response[ResponseError]:
    """Get fee-code-to-app mappings by fee category and fee code, or by developer app UUID and either app
    subscription UUID or app metered UUID

    Args:
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_subscription_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        fee_category=fee_category,
        fee_code=fee_code,
        developer_uuid=developer_uuid,
        developer_app_uuid=developer_app_uuid,
        app_subscription_uuid=app_subscription_uuid,
        app_metered_uuid=app_metered_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
) -> Optional[ResponseError]:
    """Get fee-code-to-app mappings by fee category and fee code, or by developer app UUID and either app
    subscription UUID or app metered UUID

    Args:
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_subscription_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        client=client,
        fee_category=fee_category,
        fee_code=fee_code,
        developer_uuid=developer_uuid,
        developer_app_uuid=developer_app_uuid,
        app_subscription_uuid=app_subscription_uuid,
        app_metered_uuid=app_metered_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
) -> Response[ResponseError]:
    """Get fee-code-to-app mappings by fee category and fee code, or by developer app UUID and either app
    subscription UUID or app metered UUID

    Args:
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_subscription_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        fee_category=fee_category,
        fee_code=fee_code,
        developer_uuid=developer_uuid,
        developer_app_uuid=developer_app_uuid,
        app_subscription_uuid=app_subscription_uuid,
        app_metered_uuid=app_metered_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
) -> Optional[ResponseError]:
    """Get fee-code-to-app mappings by fee category and fee code, or by developer app UUID and either app
    subscription UUID or app metered UUID

    Args:
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_subscription_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            fee_category=fee_category,
            fee_code=fee_code,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            app_subscription_uuid=app_subscription_uuid,
            app_metered_uuid=app_metered_uuid,
        )
    ).parsed
