import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_app_meter_action_fee_code import ApiAppMeterActionFeeCode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date,
    plan_uuids: Union[Unset, list[str]] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    json_plan_uuids: Union[Unset, list[str]] = UNSET
    if not isinstance(plan_uuids, Unset):
        json_plan_uuids = plan_uuids

    params["planUuids"] = json_plan_uuids

    params["developerAppUuid"] = developer_app_uuid

    params["appMeteredUuid"] = app_metered_uuid

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    params["appMeterActionType"] = app_meter_action_type

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/appmeteractionfeecode",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiAppMeterActionFeeCode]:
    if response.status_code == 200:
        response_200 = ApiAppMeterActionFeeCode.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiAppMeterActionFeeCode]:
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
    plan_uuids: Union[Unset, list[str]] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiAppMeterActionFeeCode]:
    """Get app metered action fee codes

    Args:
        date (datetime.date):
        plan_uuids (Union[Unset, list[str]]):
        developer_app_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        app_meter_action_type (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAppMeterActionFeeCode]
    """

    kwargs = _get_kwargs(
        date=date,
        plan_uuids=plan_uuids,
        developer_app_uuid=developer_app_uuid,
        app_metered_uuid=app_metered_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        app_meter_action_type=app_meter_action_type,
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
    plan_uuids: Union[Unset, list[str]] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiAppMeterActionFeeCode]:
    """Get app metered action fee codes

    Args:
        date (datetime.date):
        plan_uuids (Union[Unset, list[str]]):
        developer_app_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        app_meter_action_type (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAppMeterActionFeeCode
    """

    return sync_detailed(
        client=client,
        date=date,
        plan_uuids=plan_uuids,
        developer_app_uuid=developer_app_uuid,
        app_metered_uuid=app_metered_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        app_meter_action_type=app_meter_action_type,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    plan_uuids: Union[Unset, list[str]] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiAppMeterActionFeeCode]:
    """Get app metered action fee codes

    Args:
        date (datetime.date):
        plan_uuids (Union[Unset, list[str]]):
        developer_app_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        app_meter_action_type (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAppMeterActionFeeCode]
    """

    kwargs = _get_kwargs(
        date=date,
        plan_uuids=plan_uuids,
        developer_app_uuid=developer_app_uuid,
        app_metered_uuid=app_metered_uuid,
        fee_category=fee_category,
        fee_code=fee_code,
        app_meter_action_type=app_meter_action_type,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    plan_uuids: Union[Unset, list[str]] = UNSET,
    developer_app_uuid: Union[Unset, str] = UNSET,
    app_metered_uuid: Union[Unset, str] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    app_meter_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiAppMeterActionFeeCode]:
    """Get app metered action fee codes

    Args:
        date (datetime.date):
        plan_uuids (Union[Unset, list[str]]):
        developer_app_uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        app_meter_action_type (Union[Unset, str]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAppMeterActionFeeCode
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            plan_uuids=plan_uuids,
            developer_app_uuid=developer_app_uuid,
            app_metered_uuid=app_metered_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            app_meter_action_type=app_meter_action_type,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
