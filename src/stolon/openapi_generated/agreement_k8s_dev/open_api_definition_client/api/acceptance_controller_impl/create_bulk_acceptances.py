from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acceptance import Acceptance
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_: str,
    *,
    body: list["Acceptance"],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/acceptances/bulk/{type_}",
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
) -> Optional[list["Acceptance"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Acceptance.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Acceptance"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["Acceptance"],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[list["Acceptance"]]:
    """
    Args:
        type_ (str):
        x_clover_appenv (Union[Unset, str]):
        body (list['Acceptance']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Acceptance']]
    """

    kwargs = _get_kwargs(
        type_=type_,
        body=body,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["Acceptance"],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[list["Acceptance"]]:
    """
    Args:
        type_ (str):
        x_clover_appenv (Union[Unset, str]):
        body (list['Acceptance']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Acceptance']
    """

    return sync_detailed(
        type_=type_,
        client=client,
        body=body,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["Acceptance"],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[list["Acceptance"]]:
    """
    Args:
        type_ (str):
        x_clover_appenv (Union[Unset, str]):
        body (list['Acceptance']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Acceptance']]
    """

    kwargs = _get_kwargs(
        type_=type_,
        body=body,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["Acceptance"],
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[list["Acceptance"]]:
    """
    Args:
        type_ (str):
        x_clover_appenv (Union[Unset, str]):
        body (list['Acceptance']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Acceptance']
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            body=body,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
