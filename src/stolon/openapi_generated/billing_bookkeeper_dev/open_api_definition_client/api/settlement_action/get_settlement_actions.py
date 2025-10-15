from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_settlement_action import ApiSettlementAction
from ...types import UNSET, Response


def _get_kwargs(
    *,
    settlement_uuid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["settlementUuid"] = settlement_uuid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/settlementaction",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiSettlementAction, list["ApiSettlementAction"]]]:
    if response.status_code == 200:
        response_200 = ApiSettlementAction.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiSettlementAction.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ApiSettlementAction.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiSettlementAction, list["ApiSettlementAction"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    settlement_uuid: str,
) -> Response[Union[ApiSettlementAction, list["ApiSettlementAction"]]]:
    """Get settlement actions

    Args:
        settlement_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSettlementAction, list['ApiSettlementAction']]]
    """

    kwargs = _get_kwargs(
        settlement_uuid=settlement_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    settlement_uuid: str,
) -> Optional[Union[ApiSettlementAction, list["ApiSettlementAction"]]]:
    """Get settlement actions

    Args:
        settlement_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSettlementAction, list['ApiSettlementAction']]
    """

    return sync_detailed(
        client=client,
        settlement_uuid=settlement_uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    settlement_uuid: str,
) -> Response[Union[ApiSettlementAction, list["ApiSettlementAction"]]]:
    """Get settlement actions

    Args:
        settlement_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSettlementAction, list['ApiSettlementAction']]]
    """

    kwargs = _get_kwargs(
        settlement_uuid=settlement_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    settlement_uuid: str,
) -> Optional[Union[ApiSettlementAction, list["ApiSettlementAction"]]]:
    """Get settlement actions

    Args:
        settlement_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSettlementAction, list['ApiSettlementAction']]
    """

    return (
        await asyncio_detailed(
            client=client,
            settlement_uuid=settlement_uuid,
        )
    ).parsed
