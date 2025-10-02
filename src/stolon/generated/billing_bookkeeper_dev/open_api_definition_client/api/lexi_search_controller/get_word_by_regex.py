from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_word_by_regex_response_200 import GetWordByRegexResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    lexicon: str,
    regex: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    params["lexicon"] = lexicon

    params["regex"] = regex

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/lexi/word/regex",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWordByRegexResponse200]:
    if response.status_code == 200:
        response_200 = GetWordByRegexResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWordByRegexResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    lexicon: str,
    regex: str,
) -> Response[GetWordByRegexResponse200]:
    """
    Args:
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        lexicon (str):
        regex (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWordByRegexResponse200]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_number=page_number,
        lexicon=lexicon,
        regex=regex,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    lexicon: str,
    regex: str,
) -> Optional[GetWordByRegexResponse200]:
    """
    Args:
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        lexicon (str):
        regex (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWordByRegexResponse200
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_number=page_number,
        lexicon=lexicon,
        regex=regex,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    lexicon: str,
    regex: str,
) -> Response[GetWordByRegexResponse200]:
    """
    Args:
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        lexicon (str):
        regex (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWordByRegexResponse200]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_number=page_number,
        lexicon=lexicon,
        regex=regex,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page_size: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    lexicon: str,
    regex: str,
) -> Optional[GetWordByRegexResponse200]:
    """
    Args:
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        lexicon (str):
        regex (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWordByRegexResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_number=page_number,
            lexicon=lexicon,
            regex=regex,
        )
    ).parsed
