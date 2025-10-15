import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_resolved_partner_config import ApiResolvedPartnerConfig
from ...types import UNSET, Response


def _get_kwargs(
    *,
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: datetime.date,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billingEntityUuid"] = billing_entity_uuid

    params["hierarchyType"] = hierarchy_type

    json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/partnerconfig/resolved",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiResolvedPartnerConfig]:
    if response.status_code == 200:
        response_200 = ApiResolvedPartnerConfig.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiResolvedPartnerConfig.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiResolvedPartnerConfig.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiResolvedPartnerConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: datetime.date,
) -> Response[ApiResolvedPartnerConfig]:
    """Get the partner configuration for a partner reseller or pseudo billing entity where the default
    values are resolved from parent entities in the specified schedule hierarchy.

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResolvedPartnerConfig]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: datetime.date,
) -> Optional[ApiResolvedPartnerConfig]:
    """Get the partner configuration for a partner reseller or pseudo billing entity where the default
    values are resolved from parent entities in the specified schedule hierarchy.

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResolvedPartnerConfig
    """

    return sync_detailed(
        client=client,
        billing_entity_uuid=billing_entity_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: datetime.date,
) -> Response[ApiResolvedPartnerConfig]:
    """Get the partner configuration for a partner reseller or pseudo billing entity where the default
    values are resolved from parent entities in the specified schedule hierarchy.

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResolvedPartnerConfig]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: datetime.date,
) -> Optional[ApiResolvedPartnerConfig]:
    """Get the partner configuration for a partner reseller or pseudo billing entity where the default
    values are resolved from parent entities in the specified schedule hierarchy.

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResolvedPartnerConfig
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_entity_uuid=billing_entity_uuid,
            hierarchy_type=hierarchy_type,
            date=date,
        )
    ).parsed
