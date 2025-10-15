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
    plan_uuids: Union[Unset, list[str]] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    plan_action_type: Union[Unset, str] = UNSET,
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

    params["feeCategory"] = fee_category

    params["feeCode"] = fee_code

    params["planActionType"] = plan_action_type

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/planactionfeecode",
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
    plan_uuids: Union[Unset, list[str]] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    plan_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Get plan action fee codes

    Args:
        date (datetime.date):
        plan_uuids (Union[Unset, list[str]]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        plan_action_type (Union[Unset, str]):
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
        plan_uuids=plan_uuids,
        fee_category=fee_category,
        fee_code=fee_code,
        plan_action_type=plan_action_type,
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
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    plan_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Get plan action fee codes

    Args:
        date (datetime.date):
        plan_uuids (Union[Unset, list[str]]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        plan_action_type (Union[Unset, str]):
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
        plan_uuids=plan_uuids,
        fee_category=fee_category,
        fee_code=fee_code,
        plan_action_type=plan_action_type,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    plan_uuids: Union[Unset, list[str]] = UNSET,
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    plan_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ResponseError]:
    """Get plan action fee codes

    Args:
        date (datetime.date):
        plan_uuids (Union[Unset, list[str]]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        plan_action_type (Union[Unset, str]):
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
        plan_uuids=plan_uuids,
        fee_category=fee_category,
        fee_code=fee_code,
        plan_action_type=plan_action_type,
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
    fee_category: Union[Unset, str] = UNSET,
    fee_code: Union[Unset, str] = UNSET,
    plan_action_type: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ResponseError]:
    """Get plan action fee codes

    Args:
        date (datetime.date):
        plan_uuids (Union[Unset, list[str]]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        plan_action_type (Union[Unset, str]):
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
            plan_uuids=plan_uuids,
            fee_category=fee_category,
            fee_code=fee_code,
            plan_action_type=plan_action_type,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
