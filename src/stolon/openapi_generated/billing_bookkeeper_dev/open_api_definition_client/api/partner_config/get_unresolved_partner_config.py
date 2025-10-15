import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_partner_config import ApiPartnerConfig
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billingEntityUuid"] = billing_entity_uuid

    params["hierarchyType"] = hierarchy_type

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/partnerconfig",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiPartnerConfig, list["ApiPartnerConfig"]]]:
    if response.status_code == 200:
        response_200 = ApiPartnerConfig.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiPartnerConfig.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ApiPartnerConfig.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiPartnerConfig, list["ApiPartnerConfig"]]]:
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
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ApiPartnerConfig, list["ApiPartnerConfig"]]]:
    """Get the unresolved partner configuration for a reseller or pseudo billing entity

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiPartnerConfig, list['ApiPartnerConfig']]]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
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
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiPartnerConfig, list["ApiPartnerConfig"]]]:
    """Get the unresolved partner configuration for a reseller or pseudo billing entity

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiPartnerConfig, list['ApiPartnerConfig']]
    """

    return sync_detailed(
        client=client,
        billing_entity_uuid=billing_entity_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[Union[ApiPartnerConfig, list["ApiPartnerConfig"]]]:
    """Get the unresolved partner configuration for a reseller or pseudo billing entity

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiPartnerConfig, list['ApiPartnerConfig']]]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        hierarchy_type=hierarchy_type,
        date=date,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: str,
    hierarchy_type: str,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[Union[ApiPartnerConfig, list["ApiPartnerConfig"]]]:
    """Get the unresolved partner configuration for a reseller or pseudo billing entity

    Args:
        billing_entity_uuid (str):
        hierarchy_type (str):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiPartnerConfig, list['ApiPartnerConfig']]
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_entity_uuid=billing_entity_uuid,
            hierarchy_type=hierarchy_type,
            date=date,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
