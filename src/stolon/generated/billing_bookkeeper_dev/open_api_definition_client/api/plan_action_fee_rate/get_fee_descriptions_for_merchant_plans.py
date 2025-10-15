import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    plan_uuids: list[str],
    effective_date: Union[Unset, datetime.date] = UNSET,
    currency: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    json_plan_uuids = plan_uuids

    params["planUuids"] = json_plan_uuids

    json_effective_date: Union[Unset, str] = UNSET
    if not isinstance(effective_date, Unset):
        json_effective_date = effective_date.isoformat()
    params["effectiveDate"] = json_effective_date

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/planactionfeerate/{uuid}/feeDescriptions",
        "params": params,
    }

    _kwargs["headers"] = headers
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
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuids: list[str],
    effective_date: Union[Unset, datetime.date] = UNSET,
    currency: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, str] = UNSET,
) -> Response[ResponseError]:
    """Get fee descriptions for the provided plans

    Args:
        uuid (str):
        plan_uuids (list[str]):
        effective_date (Union[Unset, datetime.date]):
        currency (Union[Unset, str]):
        accept_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        plan_uuids=plan_uuids,
        effective_date=effective_date,
        currency=currency,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuids: list[str],
    effective_date: Union[Unset, datetime.date] = UNSET,
    currency: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, str] = UNSET,
) -> Optional[ResponseError]:
    """Get fee descriptions for the provided plans

    Args:
        uuid (str):
        plan_uuids (list[str]):
        effective_date (Union[Unset, datetime.date]):
        currency (Union[Unset, str]):
        accept_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        plan_uuids=plan_uuids,
        effective_date=effective_date,
        currency=currency,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuids: list[str],
    effective_date: Union[Unset, datetime.date] = UNSET,
    currency: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, str] = UNSET,
) -> Response[ResponseError]:
    """Get fee descriptions for the provided plans

    Args:
        uuid (str):
        plan_uuids (list[str]):
        effective_date (Union[Unset, datetime.date]):
        currency (Union[Unset, str]):
        accept_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        plan_uuids=plan_uuids,
        effective_date=effective_date,
        currency=currency,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuids: list[str],
    effective_date: Union[Unset, datetime.date] = UNSET,
    currency: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, str] = UNSET,
) -> Optional[ResponseError]:
    """Get fee descriptions for the provided plans

    Args:
        uuid (str):
        plan_uuids (list[str]):
        effective_date (Union[Unset, datetime.date]):
        currency (Union[Unset, str]):
        accept_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            plan_uuids=plan_uuids,
            effective_date=effective_date,
            currency=currency,
            accept_language=accept_language,
        )
    ).parsed
