from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acknowledge_consumer_failure_response_200 import AcknowledgeConsumerFailureResponse200
from ...models.api_message_failure_update_response import ApiMessageFailureUpdateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    comment: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["comment"] = comment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/messaging/failures/consumer/{uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]]:
    if response.status_code == 200:
        response_200 = AcknowledgeConsumerFailureResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiMessageFailureUpdateResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiMessageFailureUpdateResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]]:
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
    comment: Union[Unset, str] = UNSET,
) -> Response[Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]]:
    """Acknowledges a consumer failure which deletes the failure and moves it to consumer failure history

    Args:
        uuid (str):
        comment (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        comment=comment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    comment: Union[Unset, str] = UNSET,
) -> Optional[Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]]:
    """Acknowledges a consumer failure which deletes the failure and moves it to consumer failure history

    Args:
        uuid (str):
        comment (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        comment=comment,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    comment: Union[Unset, str] = UNSET,
) -> Response[Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]]:
    """Acknowledges a consumer failure which deletes the failure and moves it to consumer failure history

    Args:
        uuid (str):
        comment (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        comment=comment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    comment: Union[Unset, str] = UNSET,
) -> Optional[Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]]:
    """Acknowledges a consumer failure which deletes the failure and moves it to consumer failure history

    Args:
        uuid (str):
        comment (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AcknowledgeConsumerFailureResponse200, ApiMessageFailureUpdateResponse]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            comment=comment,
        )
    ).parsed
