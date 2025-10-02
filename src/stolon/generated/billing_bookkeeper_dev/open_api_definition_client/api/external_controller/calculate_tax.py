from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    billing_entity_uuid: str,
    *,
    date: Union[Unset, str] = UNSET,
    product_code: str,
    amount: str,
    currency: str,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    params: dict[str, Any] = {}

    params["date"] = date

    params["productCode"] = product_code

    params["amount"] = amount

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/external/calculatetax/{billing_entity_uuid}",
        "params": params,
    }

    _kwargs["headers"] = headers
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
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    product_code: str,
    amount: str,
    currency: str,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        billing_entity_uuid (str):
        date (Union[Unset, str]):
        product_code (str):
        amount (str):
        currency (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        date=date,
        product_code=product_code,
        amount=amount,
        currency=currency,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    product_code: str,
    amount: str,
    currency: str,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        billing_entity_uuid (str):
        date (Union[Unset, str]):
        product_code (str):
        amount (str):
        currency (str):
        x_clover_appenv (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        date=date,
        product_code=product_code,
        amount=amount,
        currency=currency,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
