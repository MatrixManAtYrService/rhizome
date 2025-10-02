import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_monetary_rule_set_rule import ApiMonetaryRuleSetRule
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rule_set_uuid: Union[Unset, str] = UNSET,
    rule_uuid: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ruleSetUuid"] = rule_set_uuid

    params["ruleUuid"] = rule_uuid

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/monetaryruleset/rule",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiMonetaryRuleSetRule]:
    if response.status_code == 200:
        response_200 = ApiMonetaryRuleSetRule.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiMonetaryRuleSetRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_set_uuid: Union[Unset, str] = UNSET,
    rule_uuid: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiMonetaryRuleSetRule]:
    """Get monetary rule set rules

    Args:
        rule_set_uuid (Union[Unset, str]):
        rule_uuid (Union[Unset, str]):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMonetaryRuleSetRule]
    """

    kwargs = _get_kwargs(
        rule_set_uuid=rule_set_uuid,
        rule_uuid=rule_uuid,
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
    rule_set_uuid: Union[Unset, str] = UNSET,
    rule_uuid: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiMonetaryRuleSetRule]:
    """Get monetary rule set rules

    Args:
        rule_set_uuid (Union[Unset, str]):
        rule_uuid (Union[Unset, str]):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMonetaryRuleSetRule
    """

    return sync_detailed(
        client=client,
        rule_set_uuid=rule_set_uuid,
        rule_uuid=rule_uuid,
        date=date,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_set_uuid: Union[Unset, str] = UNSET,
    rule_uuid: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiMonetaryRuleSetRule]:
    """Get monetary rule set rules

    Args:
        rule_set_uuid (Union[Unset, str]):
        rule_uuid (Union[Unset, str]):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMonetaryRuleSetRule]
    """

    kwargs = _get_kwargs(
        rule_set_uuid=rule_set_uuid,
        rule_uuid=rule_uuid,
        date=date,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    rule_set_uuid: Union[Unset, str] = UNSET,
    rule_uuid: Union[Unset, str] = UNSET,
    date: Union[Unset, datetime.date] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiMonetaryRuleSetRule]:
    """Get monetary rule set rules

    Args:
        rule_set_uuid (Union[Unset, str]):
        rule_uuid (Union[Unset, str]):
        date (Union[Unset, datetime.date]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMonetaryRuleSetRule
    """

    return (
        await asyncio_detailed(
            client=client,
            rule_set_uuid=rule_set_uuid,
            rule_uuid=rule_uuid,
            date=date,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
