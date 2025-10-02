import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_app_meter_action import ApiAppMeterAction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    plan_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["planUuid"] = plan_uuid

    params["developerAppUuid"] = developer_app_uuid

    params["appMeteredUuid"] = app_metered_uuid

    params["appMeterActionType"] = app_meter_action_type

    params["billingEntityUuid"] = billing_entity_uuid

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/appmeteraction",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiAppMeterAction]:
    if response.status_code == 200:
        response_200 = ApiAppMeterAction.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiAppMeterAction]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiAppMeterAction]:
    """Get app metered actions

    Args:
        plan_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        app_meter_action_type (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAppMeterAction]
    """

    kwargs = _get_kwargs(
        plan_uuid=plan_uuid,
        developer_app_uuid=developer_app_uuid,
        app_metered_uuid=app_metered_uuid,
        app_meter_action_type=app_meter_action_type,
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        start_date=start_date,
        end_date=end_date,
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
    plan_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiAppMeterAction]:
    """Get app metered actions

    Args:
        plan_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        app_meter_action_type (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAppMeterAction
    """

    return sync_detailed(
        client=client,
        plan_uuid=plan_uuid,
        developer_app_uuid=developer_app_uuid,
        app_metered_uuid=app_metered_uuid,
        app_meter_action_type=app_meter_action_type,
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        start_date=start_date,
        end_date=end_date,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiAppMeterAction]:
    """Get app metered actions

    Args:
        plan_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        app_meter_action_type (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAppMeterAction]
    """

    kwargs = _get_kwargs(
        plan_uuid=plan_uuid,
        developer_app_uuid=developer_app_uuid,
        app_metered_uuid=app_metered_uuid,
        app_meter_action_type=app_meter_action_type,
        billing_entity_uuid=billing_entity_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        start_date=start_date,
        end_date=end_date,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuid: Union[Unset, str] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiAppMeterAction]:
    """Get app metered actions

    Args:
        plan_uuid (Union[Unset, str]):
        developer_app_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        app_meter_action_type (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAppMeterAction
    """

    return (
        await asyncio_detailed(
            client=client,
            plan_uuid=plan_uuid,
            developer_app_uuid=developer_app_uuid,
            app_metered_uuid=app_metered_uuid,
            app_meter_action_type=app_meter_action_type,
            billing_entity_uuid=billing_entity_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            start_date=start_date,
            end_date=end_date,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
