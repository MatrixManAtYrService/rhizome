import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_billing_schedule import ApiBillingSchedule
from ...types import UNSET, Response


def _get_kwargs(
    *,
    billing_hierarchy_uuid: str,
    date: datetime.date,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billingHierarchyUuid"] = billing_hierarchy_uuid

    json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/schedule/forArchetype",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiBillingSchedule]:
    if response.status_code == 200:
        response_200 = ApiBillingSchedule.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiBillingSchedule.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiBillingSchedule.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiBillingSchedule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_hierarchy_uuid: str,
    date: datetime.date,
) -> Response[ApiBillingSchedule]:
    """Get a billing schedule for the archetype

    Args:
        billing_hierarchy_uuid (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiBillingSchedule]
    """

    kwargs = _get_kwargs(
        billing_hierarchy_uuid=billing_hierarchy_uuid,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_hierarchy_uuid: str,
    date: datetime.date,
) -> Optional[ApiBillingSchedule]:
    """Get a billing schedule for the archetype

    Args:
        billing_hierarchy_uuid (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiBillingSchedule
    """

    return sync_detailed(
        client=client,
        billing_hierarchy_uuid=billing_hierarchy_uuid,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_hierarchy_uuid: str,
    date: datetime.date,
) -> Response[ApiBillingSchedule]:
    """Get a billing schedule for the archetype

    Args:
        billing_hierarchy_uuid (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiBillingSchedule]
    """

    kwargs = _get_kwargs(
        billing_hierarchy_uuid=billing_hierarchy_uuid,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_hierarchy_uuid: str,
    date: datetime.date,
) -> Optional[ApiBillingSchedule]:
    """Get a billing schedule for the archetype

    Args:
        billing_hierarchy_uuid (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiBillingSchedule
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_hierarchy_uuid=billing_hierarchy_uuid,
            date=date,
        )
    ).parsed
