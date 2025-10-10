import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    plan_uuids: list[str],
    currency: str,
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    billing_method: Union[Unset, str] = UNSET,
    rule_aliases: Union[Unset, list[str]] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_clover_appenv: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Clover-Appenv"] = x_clover_appenv

    params: dict[str, Any] = {}

    json_plan_uuids = plan_uuids

    params["planUuids"] = json_plan_uuids

    params["currency"] = currency

    params["merchantUuid"] = merchant_uuid

    params["resellerUuid"] = reseller_uuid

    params["billingMethod"] = billing_method

    json_rule_aliases: Union[Unset, list[str]] = UNSET
    if not isinstance(rule_aliases, Unset):
        json_rule_aliases = rule_aliases

    params["ruleAliases"] = json_rule_aliases

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/pricing/plan",
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
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuids: list[str],
    currency: str,
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    billing_method: Union[Unset, str] = UNSET,
    rule_aliases: Union[Unset, list[str]] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_clover_appenv: str,
) -> Response[ResponseError]:
    """Get plan pricing for the requested merchant plans, currency, billing method, and as-of date

    Args:
        plan_uuids (list[str]):
        currency (str):
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        billing_method (Union[Unset, str]):
        rule_aliases (Union[Unset, list[str]]):
        date (Union[Unset, datetime.date]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        plan_uuids=plan_uuids,
        currency=currency,
        merchant_uuid=merchant_uuid,
        reseller_uuid=reseller_uuid,
        billing_method=billing_method,
        rule_aliases=rule_aliases,
        date=date,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuids: list[str],
    currency: str,
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    billing_method: Union[Unset, str] = UNSET,
    rule_aliases: Union[Unset, list[str]] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_clover_appenv: str,
) -> Optional[ResponseError]:
    """Get plan pricing for the requested merchant plans, currency, billing method, and as-of date

    Args:
        plan_uuids (list[str]):
        currency (str):
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        billing_method (Union[Unset, str]):
        rule_aliases (Union[Unset, list[str]]):
        date (Union[Unset, datetime.date]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return sync_detailed(
        client=client,
        plan_uuids=plan_uuids,
        currency=currency,
        merchant_uuid=merchant_uuid,
        reseller_uuid=reseller_uuid,
        billing_method=billing_method,
        rule_aliases=rule_aliases,
        date=date,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuids: list[str],
    currency: str,
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    billing_method: Union[Unset, str] = UNSET,
    rule_aliases: Union[Unset, list[str]] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_clover_appenv: str,
) -> Response[ResponseError]:
    """Get plan pricing for the requested merchant plans, currency, billing method, and as-of date

    Args:
        plan_uuids (list[str]):
        currency (str):
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        billing_method (Union[Unset, str]):
        rule_aliases (Union[Unset, list[str]]):
        date (Union[Unset, datetime.date]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseError]
    """

    kwargs = _get_kwargs(
        plan_uuids=plan_uuids,
        currency=currency,
        merchant_uuid=merchant_uuid,
        reseller_uuid=reseller_uuid,
        billing_method=billing_method,
        rule_aliases=rule_aliases,
        date=date,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    plan_uuids: list[str],
    currency: str,
    merchant_uuid: Union[Unset, str] = UNSET,
    reseller_uuid: Union[Unset, str] = UNSET,
    billing_method: Union[Unset, str] = UNSET,
    rule_aliases: Union[Unset, list[str]] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    x_clover_appenv: str,
) -> Optional[ResponseError]:
    """Get plan pricing for the requested merchant plans, currency, billing method, and as-of date

    Args:
        plan_uuids (list[str]):
        currency (str):
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        billing_method (Union[Unset, str]):
        rule_aliases (Union[Unset, list[str]]):
        date (Union[Unset, datetime.date]):
        x_clover_appenv (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseError
    """

    return (
        await asyncio_detailed(
            client=client,
            plan_uuids=plan_uuids,
            currency=currency,
            merchant_uuid=merchant_uuid,
            reseller_uuid=reseller_uuid,
            billing_method=billing_method,
            rule_aliases=rule_aliases,
            date=date,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
