import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_fee_summary_fee_category_report import ApiFeeSummaryFeeCategoryReport
from ...types import UNSET, Response


def _get_kwargs(
    billing_entity_uuid: str,
    *,
    start_date: datetime.date,
    end_date: datetime.date,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/summary/bycategorygroup/{billing_entity_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiFeeSummaryFeeCategoryReport]:
    if response.status_code == 200:
        response_200 = ApiFeeSummaryFeeCategoryReport.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiFeeSummaryFeeCategoryReport.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiFeeSummaryFeeCategoryReport.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiFeeSummaryFeeCategoryReport]:
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
    start_date: datetime.date,
    end_date: datetime.date,
) -> Response[ApiFeeSummaryFeeCategoryReport]:
    """Get fee summary totals grouped by fee categories by billing entity UUID and date range

    Args:
        billing_entity_uuid (str):
        start_date (datetime.date):
        end_date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeSummaryFeeCategoryReport]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: datetime.date,
    end_date: datetime.date,
) -> Optional[ApiFeeSummaryFeeCategoryReport]:
    """Get fee summary totals grouped by fee categories by billing entity UUID and date range

    Args:
        billing_entity_uuid (str):
        start_date (datetime.date):
        end_date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeSummaryFeeCategoryReport
    """

    return sync_detailed(
        billing_entity_uuid=billing_entity_uuid,
        client=client,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: datetime.date,
    end_date: datetime.date,
) -> Response[ApiFeeSummaryFeeCategoryReport]:
    """Get fee summary totals grouped by fee categories by billing entity UUID and date range

    Args:
        billing_entity_uuid (str):
        start_date (datetime.date):
        end_date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeSummaryFeeCategoryReport]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: datetime.date,
    end_date: datetime.date,
) -> Optional[ApiFeeSummaryFeeCategoryReport]:
    """Get fee summary totals grouped by fee categories by billing entity UUID and date range

    Args:
        billing_entity_uuid (str):
        start_date (datetime.date):
        end_date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeSummaryFeeCategoryReport
    """

    return (
        await asyncio_detailed(
            billing_entity_uuid=billing_entity_uuid,
            client=client,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
