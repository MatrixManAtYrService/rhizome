from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_consumer_failure_history import ApiConsumerFailureHistory
from ...models.api_message_failure_update_response import ApiMessageFailureUpdateResponse
from ...models.update_and_retry_consumer_failure_response_200 import UpdateAndRetryConsumerFailureResponse200
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    body: ApiConsumerFailureHistory,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/messaging/failures/consumer/{uuid}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateAndRetryConsumerFailureResponse200.from_dict(response.json())

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
) -> Response[Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]]:
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
    body: ApiConsumerFailureHistory,
) -> Response[Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]]:
    """Retry a consumer failure with an edited payload

    Args:
        uuid (str):
        body (ApiConsumerFailureHistory):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiConsumerFailureHistory,
) -> Optional[Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]]:
    """Retry a consumer failure with an edited payload

    Args:
        uuid (str):
        body (ApiConsumerFailureHistory):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiConsumerFailureHistory,
) -> Response[Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]]:
    """Retry a consumer failure with an edited payload

    Args:
        uuid (str):
        body (ApiConsumerFailureHistory):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiConsumerFailureHistory,
) -> Optional[Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]]:
    """Retry a consumer failure with an edited payload

    Args:
        uuid (str):
        body (ApiConsumerFailureHistory):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiMessageFailureUpdateResponse, UpdateAndRetryConsumerFailureResponse200]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
