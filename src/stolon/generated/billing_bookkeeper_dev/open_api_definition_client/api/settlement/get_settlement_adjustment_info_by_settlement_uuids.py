from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_settlement_adjust_info import ApiSettlementAdjustInfo
from ...types import UNSET, Response


def _get_kwargs(
    *,
    settlement_uuids: list[str],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_settlement_uuids = settlement_uuids

    params["settlementUuids"] = json_settlement_uuids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/settlement/feesbysettlements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiSettlementAdjustInfo, list["ApiSettlementAdjustInfo"]]]:
    if response.status_code == 200:
        response_200 = ApiSettlementAdjustInfo.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiSettlementAdjustInfo.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ApiSettlementAdjustInfo.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiSettlementAdjustInfo, list["ApiSettlementAdjustInfo"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    settlement_uuids: list[str],
) -> Response[Union[ApiSettlementAdjustInfo, list["ApiSettlementAdjustInfo"]]]:
    """Get fee summary data from settlement requests and invoice info using settlement UUID

    Args:
        settlement_uuids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSettlementAdjustInfo, list['ApiSettlementAdjustInfo']]]
    """

    kwargs = _get_kwargs(
        settlement_uuids=settlement_uuids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    settlement_uuids: list[str],
) -> Optional[Union[ApiSettlementAdjustInfo, list["ApiSettlementAdjustInfo"]]]:
    """Get fee summary data from settlement requests and invoice info using settlement UUID

    Args:
        settlement_uuids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSettlementAdjustInfo, list['ApiSettlementAdjustInfo']]
    """

    return sync_detailed(
        client=client,
        settlement_uuids=settlement_uuids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    settlement_uuids: list[str],
) -> Response[Union[ApiSettlementAdjustInfo, list["ApiSettlementAdjustInfo"]]]:
    """Get fee summary data from settlement requests and invoice info using settlement UUID

    Args:
        settlement_uuids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSettlementAdjustInfo, list['ApiSettlementAdjustInfo']]]
    """

    kwargs = _get_kwargs(
        settlement_uuids=settlement_uuids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    settlement_uuids: list[str],
) -> Optional[Union[ApiSettlementAdjustInfo, list["ApiSettlementAdjustInfo"]]]:
    """Get fee summary data from settlement requests and invoice info using settlement UUID

    Args:
        settlement_uuids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSettlementAdjustInfo, list['ApiSettlementAdjustInfo']]
    """

    return (
        await asyncio_detailed(
            client=client,
            settlement_uuids=settlement_uuids,
        )
    ).parsed
