from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_app_sub_action_fee_code import ApiAppSubActionFeeCode
from ...types import Response


def _get_kwargs(
    *,
    body: ApiAppSubActionFeeCode,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/appsubactionfeecode",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiAppSubActionFeeCode]:
    if response.status_code == 200:
        response_200 = ApiAppSubActionFeeCode.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiAppSubActionFeeCode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAppSubActionFeeCode,
) -> Response[ApiAppSubActionFeeCode]:
    """Create app subscription action fee code mapping

    Args:
        body (ApiAppSubActionFeeCode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAppSubActionFeeCode]
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
    body: ApiAppSubActionFeeCode,
) -> Optional[ApiAppSubActionFeeCode]:
    """Create app subscription action fee code mapping

    Args:
        body (ApiAppSubActionFeeCode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAppSubActionFeeCode
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAppSubActionFeeCode,
) -> Response[ApiAppSubActionFeeCode]:
    """Create app subscription action fee code mapping

    Args:
        body (ApiAppSubActionFeeCode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAppSubActionFeeCode]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAppSubActionFeeCode,
) -> Optional[ApiAppSubActionFeeCode]:
    """Create app subscription action fee code mapping

    Args:
        body (ApiAppSubActionFeeCode):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAppSubActionFeeCode
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
