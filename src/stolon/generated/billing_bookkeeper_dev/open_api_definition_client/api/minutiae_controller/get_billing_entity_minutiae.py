from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billing_entity_uuid: Union[Unset, str] = UNSET,
    entity_uuid: Union[Unset, str] = UNSET,
    as_of_date: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    only_effective: Union[Unset, bool] = UNSET,
    fees: Union[Unset, bool] = UNSET,
    actions: Union[Unset, bool] = UNSET,
    action_errors: Union[Unset, bool] = UNSET,
    ledgers: Union[Unset, bool] = UNSET,
    monetary: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billingEntityUuid"] = billing_entity_uuid

    params["entityUuid"] = entity_uuid

    params["asOfDate"] = as_of_date

    params["startDate"] = start_date

    params["endDate"] = end_date

    params["limit"] = limit

    params["onlyEffective"] = only_effective

    params["fees"] = fees

    params["actions"] = actions

    params["actionErrors"] = action_errors

    params["ledgers"] = ledgers

    params["monetary"] = monetary

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/minutiae/billingEntity",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: Union[Unset, str] = UNSET,
    entity_uuid: Union[Unset, str] = UNSET,
    as_of_date: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    only_effective: Union[Unset, bool] = UNSET,
    fees: Union[Unset, bool] = UNSET,
    actions: Union[Unset, bool] = UNSET,
    action_errors: Union[Unset, bool] = UNSET,
    ledgers: Union[Unset, bool] = UNSET,
    monetary: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        as_of_date (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        limit (Union[Unset, int]):
        only_effective (Union[Unset, bool]):
        fees (Union[Unset, bool]):
        actions (Union[Unset, bool]):
        action_errors (Union[Unset, bool]):
        ledgers (Union[Unset, bool]):
        monetary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        entity_uuid=entity_uuid,
        as_of_date=as_of_date,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        only_effective=only_effective,
        fees=fees,
        actions=actions,
        action_errors=action_errors,
        ledgers=ledgers,
        monetary=monetary,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    billing_entity_uuid: Union[Unset, str] = UNSET,
    entity_uuid: Union[Unset, str] = UNSET,
    as_of_date: Union[Unset, str] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    only_effective: Union[Unset, bool] = UNSET,
    fees: Union[Unset, bool] = UNSET,
    actions: Union[Unset, bool] = UNSET,
    action_errors: Union[Unset, bool] = UNSET,
    ledgers: Union[Unset, bool] = UNSET,
    monetary: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        as_of_date (Union[Unset, str]):
        start_date (Union[Unset, str]):
        end_date (Union[Unset, str]):
        limit (Union[Unset, int]):
        only_effective (Union[Unset, bool]):
        fees (Union[Unset, bool]):
        actions (Union[Unset, bool]):
        action_errors (Union[Unset, bool]):
        ledgers (Union[Unset, bool]):
        monetary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        entity_uuid=entity_uuid,
        as_of_date=as_of_date,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        only_effective=only_effective,
        fees=fees,
        actions=actions,
        action_errors=action_errors,
        ledgers=ledgers,
        monetary=monetary,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
