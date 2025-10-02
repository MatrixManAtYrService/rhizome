import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_billing_hierarchy import ApiBillingHierarchy
from ...types import UNSET, Response


def _get_kwargs(
    uuid: str,
    *,
    date: datetime.date,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/hierarchy/{uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiBillingHierarchy]:
    if response.status_code == 200:
        response_200 = ApiBillingHierarchy.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiBillingHierarchy.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiBillingHierarchy.from_dict(response.json())

        return response_404

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
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
) -> Response[ApiBillingHierarchy]:
    """Mark billing hierarchy as deleted

    Args:
        uuid (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiBillingHierarchy]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
) -> Optional[ApiBillingHierarchy]:
    """Mark billing hierarchy as deleted

    Args:
        uuid (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiBillingHierarchy
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        date=date,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
) -> Response[ApiBillingHierarchy]:
    """Mark billing hierarchy as deleted

    Args:
        uuid (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiBillingHierarchy]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: datetime.date,
) -> Optional[ApiBillingHierarchy]:
    """Mark billing hierarchy as deleted

    Args:
        uuid (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiBillingHierarchy
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            date=date,
        )
    ).parsed
