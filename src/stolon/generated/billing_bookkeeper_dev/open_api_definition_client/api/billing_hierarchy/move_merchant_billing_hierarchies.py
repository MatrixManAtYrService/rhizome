import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_billing_hierarchy import ApiBillingHierarchy
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: list[str],
    new_parent_billing_entity_uuid: str,
    date: datetime.date,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["newParentBillingEntityUuid"] = new_parent_billing_entity_uuid

    json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/hierarchy",
        "params": params,
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiBillingHierarchy]:
    if response.status_code == 200:
        response_200 = ApiBillingHierarchy.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiBillingHierarchy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    new_parent_billing_entity_uuid: str,
    date: datetime.date,
) -> Response[ApiBillingHierarchy]:
    """Move billing hierarchy merchants

    Args:
        new_parent_billing_entity_uuid (str):
        date (datetime.date):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiBillingHierarchy]
    """

    kwargs = _get_kwargs(
        body=body,
        new_parent_billing_entity_uuid=new_parent_billing_entity_uuid,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    new_parent_billing_entity_uuid: str,
    date: datetime.date,
) -> Optional[ApiBillingHierarchy]:
    """Move billing hierarchy merchants

    Args:
        new_parent_billing_entity_uuid (str):
        date (datetime.date):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiBillingHierarchy
    """

    return sync_detailed(
        client=client,
        body=body,
        new_parent_billing_entity_uuid=new_parent_billing_entity_uuid,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    new_parent_billing_entity_uuid: str,
    date: datetime.date,
) -> Response[ApiBillingHierarchy]:
    """Move billing hierarchy merchants

    Args:
        new_parent_billing_entity_uuid (str):
        date (datetime.date):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiBillingHierarchy]
    """

    kwargs = _get_kwargs(
        body=body,
        new_parent_billing_entity_uuid=new_parent_billing_entity_uuid,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    new_parent_billing_entity_uuid: str,
    date: datetime.date,
) -> Optional[ApiBillingHierarchy]:
    """Move billing hierarchy merchants

    Args:
        new_parent_billing_entity_uuid (str):
        date (datetime.date):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiBillingHierarchy
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            new_parent_billing_entity_uuid=new_parent_billing_entity_uuid,
            date=date,
        )
    ).parsed
