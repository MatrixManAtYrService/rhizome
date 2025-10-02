from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_adjust_action_fee_code import ApiAdjustActionFeeCode
from ...types import Response


def _get_kwargs(
    *,
    body: ApiAdjustActionFeeCode,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/adjustactionfeecode",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiAdjustActionFeeCode]:
    if response.status_code == 200:
        response_200 = ApiAdjustActionFeeCode.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiAdjustActionFeeCode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAdjustActionFeeCode,
) -> Response[ApiAdjustActionFeeCode]:
    """Create adjustment action fee code mapping

    Args:
        body (ApiAdjustActionFeeCode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAdjustActionFeeCode]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAdjustActionFeeCode,
) -> Optional[ApiAdjustActionFeeCode]:
    """Create adjustment action fee code mapping

    Args:
        body (ApiAdjustActionFeeCode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAdjustActionFeeCode
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAdjustActionFeeCode,
) -> Response[ApiAdjustActionFeeCode]:
    """Create adjustment action fee code mapping

    Args:
        body (ApiAdjustActionFeeCode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAdjustActionFeeCode]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAdjustActionFeeCode,
) -> Optional[ApiAdjustActionFeeCode]:
    """Create adjustment action fee code mapping

    Args:
        body (ApiAdjustActionFeeCode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAdjustActionFeeCode
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
