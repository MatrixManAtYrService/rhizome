from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_settlement_details import ApiSettlementDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    invoice_info_uuid: str,
    *,
    include_actions: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includeActions"] = include_actions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/settlement/feesbyinvoice/{invoice_info_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiSettlementDetails]:
    if response.status_code == 200:
        response_200 = ApiSettlementDetails.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiSettlementDetails.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiSettlementDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiSettlementDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_info_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_actions: Union[Unset, bool] = UNSET,
) -> Response[ApiSettlementDetails]:
    """Get fee summary data from settlement requests and invoice info using invoice info UUID

    Args:
        invoice_info_uuid (str):
        include_actions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSettlementDetails]
    """

    kwargs = _get_kwargs(
        invoice_info_uuid=invoice_info_uuid,
        include_actions=include_actions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_info_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_actions: Union[Unset, bool] = UNSET,
) -> Optional[ApiSettlementDetails]:
    """Get fee summary data from settlement requests and invoice info using invoice info UUID

    Args:
        invoice_info_uuid (str):
        include_actions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSettlementDetails
    """

    return sync_detailed(
        invoice_info_uuid=invoice_info_uuid,
        client=client,
        include_actions=include_actions,
    ).parsed


async def asyncio_detailed(
    invoice_info_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_actions: Union[Unset, bool] = UNSET,
) -> Response[ApiSettlementDetails]:
    """Get fee summary data from settlement requests and invoice info using invoice info UUID

    Args:
        invoice_info_uuid (str):
        include_actions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSettlementDetails]
    """

    kwargs = _get_kwargs(
        invoice_info_uuid=invoice_info_uuid,
        include_actions=include_actions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_info_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_actions: Union[Unset, bool] = UNSET,
) -> Optional[ApiSettlementDetails]:
    """Get fee summary data from settlement requests and invoice info using invoice info UUID

    Args:
        invoice_info_uuid (str):
        include_actions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSettlementDetails
    """

    return (
        await asyncio_detailed(
            invoice_info_uuid=invoice_info_uuid,
            client=client,
            include_actions=include_actions,
        )
    ).parsed
