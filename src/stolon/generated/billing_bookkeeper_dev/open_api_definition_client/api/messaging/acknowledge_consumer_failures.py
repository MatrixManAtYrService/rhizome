from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_consumer_failure_update_response import ApiConsumerFailureUpdateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[str],
    comment: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["comment"] = comment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/messaging/failures/consumer",
        "params": params,
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiConsumerFailureUpdateResponse, list["ApiConsumerFailureUpdateResponse"]]]:
    if response.status_code == 200:
        response_200 = ApiConsumerFailureUpdateResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ApiConsumerFailureUpdateResponse.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ApiConsumerFailureUpdateResponse.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiConsumerFailureUpdateResponse, list["ApiConsumerFailureUpdateResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    comment: Union[Unset, str] = UNSET,
) -> Response[Union[ApiConsumerFailureUpdateResponse, list["ApiConsumerFailureUpdateResponse"]]]:
    """Acknowledges consumer failures which deletes the failures and moves them to consumer failure history

    Args:
        comment (Union[Unset, str]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiConsumerFailureUpdateResponse, list['ApiConsumerFailureUpdateResponse']]]
    """

    kwargs = _get_kwargs(
        body=body,
        comment=comment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    comment: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiConsumerFailureUpdateResponse, list["ApiConsumerFailureUpdateResponse"]]]:
    """Acknowledges consumer failures which deletes the failures and moves them to consumer failure history

    Args:
        comment (Union[Unset, str]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiConsumerFailureUpdateResponse, list['ApiConsumerFailureUpdateResponse']]
    """

    return sync_detailed(
        client=client,
        body=body,
        comment=comment,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    comment: Union[Unset, str] = UNSET,
) -> Response[Union[ApiConsumerFailureUpdateResponse, list["ApiConsumerFailureUpdateResponse"]]]:
    """Acknowledges consumer failures which deletes the failures and moves them to consumer failure history

    Args:
        comment (Union[Unset, str]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiConsumerFailureUpdateResponse, list['ApiConsumerFailureUpdateResponse']]]
    """

    kwargs = _get_kwargs(
        body=body,
        comment=comment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    comment: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiConsumerFailureUpdateResponse, list["ApiConsumerFailureUpdateResponse"]]]:
    """Acknowledges consumer failures which deletes the failures and moves them to consumer failure history

    Args:
        comment (Union[Unset, str]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiConsumerFailureUpdateResponse, list['ApiConsumerFailureUpdateResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            comment=comment,
        )
    ).parsed
