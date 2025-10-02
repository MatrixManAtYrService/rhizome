from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_settlement import ApiSettlement
from ...models.api_settlement_tax import ApiSettlementTax
from ...models.response_error import ResponseError
from ...types import Response


def _get_kwargs(
    billing_entity_uuid: str,
    *,
    body: list["ApiSettlementTax"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/settlement/entitytax/{billing_entity_uuid}",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ResponseError, list["ApiSettlement"]]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiSettlement.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ApiSettlement.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ResponseError, list["ApiSettlement"]]]:
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
    body: list["ApiSettlementTax"],
) -> Response[Union[ResponseError, list["ApiSettlement"]]]:
    """Set tax amounts for a collection of settlement requests for a billing entity

    Args:
        billing_entity_uuid (str):
        body (list['ApiSettlementTax']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseError, list['ApiSettlement']]]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSettlementTax"],
) -> Optional[Union[ResponseError, list["ApiSettlement"]]]:
    """Set tax amounts for a collection of settlement requests for a billing entity

    Args:
        billing_entity_uuid (str):
        body (list['ApiSettlementTax']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseError, list['ApiSettlement']]
    """

    return sync_detailed(
        billing_entity_uuid=billing_entity_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSettlementTax"],
) -> Response[Union[ResponseError, list["ApiSettlement"]]]:
    """Set tax amounts for a collection of settlement requests for a billing entity

    Args:
        billing_entity_uuid (str):
        body (list['ApiSettlementTax']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ResponseError, list['ApiSettlement']]]
    """

    kwargs = _get_kwargs(
        billing_entity_uuid=billing_entity_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    billing_entity_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["ApiSettlementTax"],
) -> Optional[Union[ResponseError, list["ApiSettlement"]]]:
    """Set tax amounts for a collection of settlement requests for a billing entity

    Args:
        billing_entity_uuid (str):
        body (list['ApiSettlementTax']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ResponseError, list['ApiSettlement']]
    """

    return (
        await asyncio_detailed(
            billing_entity_uuid=billing_entity_uuid,
            client=client,
            body=body,
        )
    ).parsed
