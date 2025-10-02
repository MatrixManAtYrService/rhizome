from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    lexicon: str,
    *,
    body: list[str],
    dry_run: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["dryRun"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/lexi/{lexicon}/apply/words",
        "params": params,
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[int]:
    if response.status_code == 200:
        response_200 = cast(int, response.json())
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[int]:
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
    body: list[str],
    dry_run: Union[Unset, bool] = UNSET,
) -> Response[int]:
    """
    Args:
        lexicon (str):
        dry_run (Union[Unset, bool]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        lexicon=lexicon,
        body=body,
        dry_run=dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    lexicon: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    dry_run: Union[Unset, bool] = UNSET,
) -> Optional[int]:
    """
    Args:
        lexicon (str):
        dry_run (Union[Unset, bool]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return sync_detailed(
        lexicon=lexicon,
        client=client,
        body=body,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    lexicon: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    dry_run: Union[Unset, bool] = UNSET,
) -> Response[int]:
    """
    Args:
        lexicon (str):
        dry_run (Union[Unset, bool]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int]
    """

    kwargs = _get_kwargs(
        lexicon=lexicon,
        body=body,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    lexicon: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    dry_run: Union[Unset, bool] = UNSET,
) -> Optional[int]:
    """
    Args:
        lexicon (str):
        dry_run (Union[Unset, bool]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int
    """

    return (
        await asyncio_detailed(
            lexicon=lexicon,
            client=client,
            body=body,
            dry_run=dry_run,
        )
    ).parsed
