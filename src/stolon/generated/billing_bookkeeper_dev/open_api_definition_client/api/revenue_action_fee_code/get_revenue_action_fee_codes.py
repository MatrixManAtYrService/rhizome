import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date,
    revenue_action_type: Union[Unset, str] = UNSET,
    fee_category_group: Union[Unset, str] = UNSET,
    revenue_group: Union[Unset, str] = UNSET,
    revenue_share_group: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    params["revenueActionType"] = revenue_action_type

    params["feeCategoryGroup"] = fee_category_group

    params["revenueGroup"] = revenue_group

    params["revenueShareGroup"] = revenue_share_group

    params["developerUuid"] = developer_uuid

    params["developerAppUuid"] = developer_app_uuid

    params["appSubscriptionUuid"] = app_subscription_uuid

    params["appMeteredUuid"] = app_metered_uuid

    params["planUuid"] = plan_uuid

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/revenueactionfeecode",
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
    date: datetime.date,
    revenue_action_type: Union[Unset, str] = UNSET,
    fee_category_group: Union[Unset, str] = UNSET,
    revenue_group: Union[Unset, str] = UNSET,
    revenue_share_group: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Get revenue-action-to-fee-code mappings

    Args:
        date (datetime.date):
        revenue_action_type (Union[Unset, str]):
        fee_category_group (Union[Unset, str]):
        revenue_group (Union[Unset, str]):
        revenue_share_group (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_subscription_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        plan_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        date=date,
        revenue_action_type=revenue_action_type,
        fee_category_group=fee_category_group,
        revenue_group=revenue_group,
        revenue_share_group=revenue_share_group,
        developer_uuid=developer_uuid,
        developer_app_uuid=developer_app_uuid,
        app_subscription_uuid=app_subscription_uuid,
        app_metered_uuid=app_metered_uuid,
        plan_uuid=plan_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        page_size=page_size,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    revenue_action_type: Union[Unset, str] = UNSET,
    fee_category_group: Union[Unset, str] = UNSET,
    revenue_group: Union[Unset, str] = UNSET,
    revenue_share_group: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Get revenue-action-to-fee-code mappings

    Args:
        date (datetime.date):
        revenue_action_type (Union[Unset, str]):
        fee_category_group (Union[Unset, str]):
        revenue_group (Union[Unset, str]):
        revenue_share_group (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_subscription_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        plan_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        client=client,
        date=date,
        revenue_action_type=revenue_action_type,
        fee_category_group=fee_category_group,
        revenue_group=revenue_group,
        revenue_share_group=revenue_share_group,
        developer_uuid=developer_uuid,
        developer_app_uuid=developer_app_uuid,
        app_subscription_uuid=app_subscription_uuid,
        app_metered_uuid=app_metered_uuid,
        plan_uuid=plan_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    revenue_action_type: Union[Unset, str] = UNSET,
    fee_category_group: Union[Unset, str] = UNSET,
    revenue_group: Union[Unset, str] = UNSET,
    revenue_share_group: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Get revenue-action-to-fee-code mappings

    Args:
        date (datetime.date):
        revenue_action_type (Union[Unset, str]):
        fee_category_group (Union[Unset, str]):
        revenue_group (Union[Unset, str]):
        revenue_share_group (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_subscription_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        plan_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        date=date,
        revenue_action_type=revenue_action_type,
        fee_category_group=fee_category_group,
        revenue_group=revenue_group,
        revenue_share_group=revenue_share_group,
        developer_uuid=developer_uuid,
        developer_app_uuid=developer_app_uuid,
        app_subscription_uuid=app_subscription_uuid,
        app_metered_uuid=app_metered_uuid,
        plan_uuid=plan_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    revenue_action_type: Union[Unset, str] = UNSET,
    fee_category_group: Union[Unset, str] = UNSET,
    revenue_group: Union[Unset, str] = UNSET,
    revenue_share_group: Union[Unset, str] = UNSET,
    developer_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_subscription_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    plan_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Get revenue-action-to-fee-code mappings

    Args:
        date (datetime.date):
        revenue_action_type (Union[Unset, str]):
        fee_category_group (Union[Unset, str]):
        revenue_group (Union[Unset, str]):
        revenue_share_group (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_subscription_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        plan_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            revenue_action_type=revenue_action_type,
            fee_category_group=fee_category_group,
            revenue_group=revenue_group,
            revenue_share_group=revenue_share_group,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            app_subscription_uuid=app_subscription_uuid,
            app_metered_uuid=app_metered_uuid,
            plan_uuid=plan_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
