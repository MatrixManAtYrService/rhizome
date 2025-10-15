from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_app_rates_params import ApiAppRatesParams
from ...models.produce_app_rates_events_response_200 import ProduceAppRatesEventsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ApiAppRatesParams,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_clover_appenv, Unset):
        headers["X-Clover-Appenv"] = x_clover_appenv

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/messaging/apps",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProduceAppRatesEventsResponse200]:
    if response.status_code == 200:
        response_200 = ProduceAppRatesEventsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProduceAppRatesEventsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAppRatesParams,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[ProduceAppRatesEventsResponse200]:
    """Produces app rates billing events for developer uuids and/or app uuids in the body.  These app rates
    events are used to configure bookkeeper for app billing.

    Args:
        x_clover_appenv (Union[Unset, str]):
        body (ApiAppRatesParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProduceAppRatesEventsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        x_clover_appenv=x_clover_appenv,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAppRatesParams,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[ProduceAppRatesEventsResponse200]:
    """Produces app rates billing events for developer uuids and/or app uuids in the body.  These app rates
    events are used to configure bookkeeper for app billing.

    Args:
        x_clover_appenv (Union[Unset, str]):
        body (ApiAppRatesParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProduceAppRatesEventsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        x_clover_appenv=x_clover_appenv,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAppRatesParams,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Response[ProduceAppRatesEventsResponse200]:
    """Produces app rates billing events for developer uuids and/or app uuids in the body.  These app rates
    events are used to configure bookkeeper for app billing.

    Args:
        x_clover_appenv (Union[Unset, str]):
        body (ApiAppRatesParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProduceAppRatesEventsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        x_clover_appenv=x_clover_appenv,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiAppRatesParams,
    x_clover_appenv: Union[Unset, str] = UNSET,
) -> Optional[ProduceAppRatesEventsResponse200]:
    """Produces app rates billing events for developer uuids and/or app uuids in the body.  These app rates
    events are used to configure bookkeeper for app billing.

    Args:
        x_clover_appenv (Union[Unset, str]):
        body (ApiAppRatesParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProduceAppRatesEventsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_clover_appenv=x_clover_appenv,
        )
    ).parsed
