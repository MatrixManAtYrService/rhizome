from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_merchant_evolution import ApiMerchantEvolution
from ...types import Response


def _get_kwargs(
    merchant_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/merchant/evolution/{merchant_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiMerchantEvolution]:
    if response.status_code == 200:
        response_200 = ApiMerchantEvolution.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiMerchantEvolution.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiMerchantEvolution]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    merchant_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiMerchantEvolution]:
    """Get merchant evolution data for the specified merchant UUID

    Args:
        merchant_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMerchantEvolution]
    """

    kwargs = _get_kwargs(
        merchant_uuid=merchant_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    merchant_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiMerchantEvolution]:
    """Get merchant evolution data for the specified merchant UUID

    Args:
        merchant_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMerchantEvolution
    """

    return sync_detailed(
        merchant_uuid=merchant_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    merchant_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiMerchantEvolution]:
    """Get merchant evolution data for the specified merchant UUID

    Args:
        merchant_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMerchantEvolution]
    """

    kwargs = _get_kwargs(
        merchant_uuid=merchant_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    merchant_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiMerchantEvolution]:
    """Get merchant evolution data for the specified merchant UUID

    Args:
        merchant_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMerchantEvolution
    """

    return (
        await asyncio_detailed(
            merchant_uuid=merchant_uuid,
            client=client,
        )
    ).parsed
