from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acceptance import Acceptance
from ...types import UNSET, Response, Unset


def _get_kwargs(
    acceptance_id: UUID,
    *,
    include_template_parameters: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includeTemplateParameters"] = include_template_parameters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/acceptances/{acceptance_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Acceptance]:
    if response.status_code == 200:
        response_200 = Acceptance.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Acceptance]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    acceptance_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    include_template_parameters: Union[Unset, bool] = UNSET,
) -> Response[Acceptance]:
    """
    Args:
        acceptance_id (UUID):
        include_template_parameters (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acceptance]
    """

    kwargs = _get_kwargs(
        acceptance_id=acceptance_id,
        include_template_parameters=include_template_parameters,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    acceptance_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    include_template_parameters: Union[Unset, bool] = UNSET,
) -> Optional[Acceptance]:
    """
    Args:
        acceptance_id (UUID):
        include_template_parameters (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acceptance
    """

    return sync_detailed(
        acceptance_id=acceptance_id,
        client=client,
        include_template_parameters=include_template_parameters,
    ).parsed


async def asyncio_detailed(
    acceptance_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    include_template_parameters: Union[Unset, bool] = UNSET,
) -> Response[Acceptance]:
    """
    Args:
        acceptance_id (UUID):
        include_template_parameters (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Acceptance]
    """

    kwargs = _get_kwargs(
        acceptance_id=acceptance_id,
        include_template_parameters=include_template_parameters,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    acceptance_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    include_template_parameters: Union[Unset, bool] = UNSET,
) -> Optional[Acceptance]:
    """
    Args:
        acceptance_id (UUID):
        include_template_parameters (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Acceptance
    """

    return (
        await asyncio_detailed(
            acceptance_id=acceptance_id,
            client=client,
            include_template_parameters=include_template_parameters,
        )
    ).parsed
