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
    currency: str,
    plan_uuid: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    params["currency"] = currency

    params["planUuid"] = plan_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/abstraction/planpricing/details",
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
    currency: str,
    plan_uuid: Union[Unset, str] = UNSET,
) -> Response[ResponseError]:
    """Get details of a plan pricing abstraction

    Args:
        date (datetime.date):
        currency (str):
        plan_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        date=date,
        currency=currency,
        plan_uuid=plan_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    currency: str,
    plan_uuid: Union[Unset, str] = UNSET,
) -> Optional[ResponseError]:
    """Get details of a plan pricing abstraction

    Args:
        date (datetime.date):
        currency (str):
        plan_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        client=client,
        date=date,
        currency=currency,
        plan_uuid=plan_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    currency: str,
    plan_uuid: Union[Unset, str] = UNSET,
) -> Response[ResponseError]:
    """Get details of a plan pricing abstraction

    Args:
        date (datetime.date):
        currency (str):
        plan_uuid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        date=date,
        currency=currency,
        plan_uuid=plan_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
    currency: str,
    plan_uuid: Union[Unset, str] = UNSET,
) -> Optional[ResponseError]:
    """Get details of a plan pricing abstraction

    Args:
        date (datetime.date):
        currency (str):
        plan_uuid (Union[Unset, str]):

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
            currency=currency,
            plan_uuid=plan_uuid,
        )
    ).parsed
