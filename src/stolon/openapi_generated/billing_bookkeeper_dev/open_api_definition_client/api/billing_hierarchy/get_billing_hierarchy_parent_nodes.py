import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_billing_hierarchy_level_node import ApiBillingHierarchyLevelNode
from ...types import UNSET, Response


def _get_kwargs(
    billing_entity_uuid: str,
    *,
    hierarchy_type: str,
    date: datetime.date,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["hierarchyType"] = hierarchy_type

    json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/hierarchy/parentnodes/{billing_entity_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiBillingHierarchyLevelNode]:
    if response.status_code == 200:
        response_200 = ApiBillingHierarchyLevelNode.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiBillingHierarchyLevelNode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    date: datetime.date,
) -> Response[ApiBillingHierarchyLevelNode]:
    """Get parent nodes of billing entity for specified hierarchy type

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiBillingHierarchyLevelNode]
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
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    date: datetime.date,
) -> Optional[ApiBillingHierarchyLevelNode]:
    """Get parent nodes of billing entity for specified hierarchy type

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiBillingHierarchyLevelNode
    """

    return sync_detailed(
        billing_entity_uuid=billing_entity_uuid,
        client=client,
        hierarchy_type=hierarchy_type,
        date=date,
    ).parsed


async def asyncio_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    date: datetime.date,
) -> Response[ApiBillingHierarchyLevelNode]:
    """Get parent nodes of billing entity for specified hierarchy type

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiBillingHierarchyLevelNode]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hierarchy_type: str,
    date: datetime.date,
) -> Optional[ApiBillingHierarchyLevelNode]:
    """Get parent nodes of billing entity for specified hierarchy type

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiBillingHierarchyLevelNode
    """

    return (
        await asyncio_detailed(
            billing_entity_uuid=billing_entity_uuid,
            client=client,
            hierarchy_type=hierarchy_type,
            date=date,
        )
    ).parsed
