from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_fee_rate_report_action_error import ApiFeeRateReportActionError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fee_rate_error_report_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["feeRateErrorReportUuid"] = fee_rate_error_report_uuid

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/feeratereportactionerror",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiFeeRateReportActionError]:
    if response.status_code == 200:
        response_200 = ApiFeeRateReportActionError.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiFeeRateReportActionError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_rate_error_report_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiFeeRateReportActionError]:
    """Get fee rate report action errors by error report uuid

    Args:
        fee_rate_error_report_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeRateReportActionError]
    """

    kwargs = _get_kwargs(
        fee_rate_error_report_uuid=fee_rate_error_report_uuid,
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
    fee_rate_error_report_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiFeeRateReportActionError]:
    """Get fee rate report action errors by error report uuid

    Args:
        fee_rate_error_report_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeRateReportActionError
    """

    return sync_detailed(
        client=client,
        fee_rate_error_report_uuid=fee_rate_error_report_uuid,
        page_size=page_size,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_rate_error_report_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Response[ApiFeeRateReportActionError]:
    """Get fee rate report action errors by error report uuid

    Args:
        fee_rate_error_report_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeRateReportActionError]
    """

    kwargs = _get_kwargs(
        fee_rate_error_report_uuid=fee_rate_error_report_uuid,
        page_size=page_size,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fee_rate_error_report_uuid: str,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
) -> Optional[ApiFeeRateReportActionError]:
    """Get fee rate report action errors by error report uuid

    Args:
        fee_rate_error_report_uuid (str):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeRateReportActionError
    """

    return (
        await asyncio_detailed(
            client=client,
            fee_rate_error_report_uuid=fee_rate_error_report_uuid,
            page_size=page_size,
            page_number=page_number,
        )
    ).parsed
