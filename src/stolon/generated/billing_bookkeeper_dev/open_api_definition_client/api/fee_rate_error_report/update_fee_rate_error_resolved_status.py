from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_fee_rate_error_report import ApiFeeRateErrorReport
from ...models.response_error import ResponseError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    resolved_status: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["resolvedStatus"] = resolved_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/feerateerrorreport/{uuid}/resolved",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiFeeRateErrorReport, ResponseError]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiFeeRateErrorReport.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiFeeRateErrorReport.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiFeeRateErrorReport, ResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    resolved_status: Union[Unset, bool] = UNSET,
) -> Response[Union[ApiFeeRateErrorReport, ResponseError]]:
    """Update the resolved status of a fee rate error report item

    Args:
        uuid (str):
        resolved_status (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiFeeRateErrorReport, ResponseError]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        resolved_status=resolved_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    resolved_status: Union[Unset, bool] = UNSET,
) -> Optional[Union[ApiFeeRateErrorReport, ResponseError]]:
    """Update the resolved status of a fee rate error report item

    Args:
        uuid (str):
        resolved_status (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiFeeRateErrorReport, ResponseError]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        resolved_status=resolved_status,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    resolved_status: Union[Unset, bool] = UNSET,
) -> Response[Union[ApiFeeRateErrorReport, ResponseError]]:
    """Update the resolved status of a fee rate error report item

    Args:
        uuid (str):
        resolved_status (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiFeeRateErrorReport, ResponseError]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        resolved_status=resolved_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    resolved_status: Union[Unset, bool] = UNSET,
) -> Optional[Union[ApiFeeRateErrorReport, ResponseError]]:
    """Update the resolved status of a fee rate error report item

    Args:
        uuid (str):
        resolved_status (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiFeeRateErrorReport, ResponseError]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            resolved_status=resolved_status,
        )
    ).parsed
