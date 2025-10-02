from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_app_meter_action import ApiAppMeterAction
from ...types import Response


def _get_kwargs(
    billing_entity_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/appmeteraction/unposted/{billing_entity_uuid}",
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
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiAppMeterAction]:
    """Get unposted app metered actions for billing entity

    Args:
        billing_entity_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAppMeterAction]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiAppMeterAction]:
    """Get unposted app metered actions for billing entity

    Args:
        billing_entity_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAppMeterAction
    """

    return sync_detailed(
        billing_entity_uuid=billing_entity_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiAppMeterAction]:
    """Get unposted app metered actions for billing entity

    Args:
        billing_entity_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAppMeterAction]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiAppMeterAction]:
    """Get unposted app metered actions for billing entity

    Args:
        billing_entity_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAppMeterAction
    """

    return (
        await asyncio_detailed(
            billing_entity_uuid=billing_entity_uuid,
            client=client,
        )
    ).parsed
