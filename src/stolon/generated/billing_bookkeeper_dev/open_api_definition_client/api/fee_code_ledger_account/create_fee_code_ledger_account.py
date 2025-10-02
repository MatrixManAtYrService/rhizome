from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_fee_code_ledger_account import ApiFeeCodeLedgerAccount
from ...types import Response


def _get_kwargs(
    *,
    body: ApiFeeCodeLedgerAccount,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/feecodeledgeracct",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiFeeCodeLedgerAccount]:
    if response.status_code == 200:
        response_200 = ApiFeeCodeLedgerAccount.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiFeeCodeLedgerAccount.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiFeeCodeLedgerAccount]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiFeeCodeLedgerAccount,
) -> Response[ApiFeeCodeLedgerAccount]:
    """Create a fee-code-to-ledger-account mapping

    Args:
        body (ApiFeeCodeLedgerAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeCodeLedgerAccount]
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
    body: ApiFeeCodeLedgerAccount,
) -> Optional[ApiFeeCodeLedgerAccount]:
    """Create a fee-code-to-ledger-account mapping

    Args:
        body (ApiFeeCodeLedgerAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeCodeLedgerAccount
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiFeeCodeLedgerAccount,
) -> Response[ApiFeeCodeLedgerAccount]:
    """Create a fee-code-to-ledger-account mapping

    Args:
        body (ApiFeeCodeLedgerAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiFeeCodeLedgerAccount]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiFeeCodeLedgerAccount,
) -> Optional[ApiFeeCodeLedgerAccount]:
    """Create a fee-code-to-ledger-account mapping

    Args:
        body (ApiFeeCodeLedgerAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiFeeCodeLedgerAccount
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
