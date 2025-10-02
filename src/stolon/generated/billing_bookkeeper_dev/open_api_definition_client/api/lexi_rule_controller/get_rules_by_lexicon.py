from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.all_rules import AllRules
from ...types import Response


def _get_kwargs(
    lexicon: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/lexi/rule/lexicon/{lexicon}/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AllRules]:
    if response.status_code == 200:
        response_200 = AllRules.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AllRules]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    lexicon: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AllRules]:
    """
    Args:
        lexicon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllRules]
    """

    kwargs = _get_kwargs(
        lexicon=lexicon,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    lexicon: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AllRules]:
    """
    Args:
        lexicon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllRules
    """

    return sync_detailed(
        lexicon=lexicon,
        client=client,
    ).parsed


async def asyncio_detailed(
    lexicon: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AllRules]:
    """
    Args:
        lexicon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllRules]
    """

    kwargs = _get_kwargs(
        lexicon=lexicon,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    lexicon: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AllRules]:
    """
    Args:
        lexicon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllRules
    """

    return (
        await asyncio_detailed(
            lexicon=lexicon,
            client=client,
        )
    ).parsed
