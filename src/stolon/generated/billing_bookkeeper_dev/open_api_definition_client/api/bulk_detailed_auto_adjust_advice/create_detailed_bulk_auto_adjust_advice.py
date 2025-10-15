from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_bulk_auto_adjust_advice import ApiBulkAutoAdjustAdvice
from ...models.create_detailed_bulk_auto_adjust_advice_body import CreateDetailedBulkAutoAdjustAdviceBody
from ...models.response_error import ResponseError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CreateDetailedBulkAutoAdjustAdviceBody,
    rule_uuid: str,
    currency: str,
    reference: str,
    email_address: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["ruleUuid"] = rule_uuid

    params["currency"] = currency

    params["reference"] = reference

    params["emailAddress"] = email_address

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/autoadjustadvice/bulk/detailed",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiBulkAutoAdjustAdvice, ResponseError]]:
    if response.status_code == 200:
        response_200 = ResponseError.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiBulkAutoAdjustAdvice.from_dict(response.json())

        return response_400

    if response.status_code == 415:
        response_415 = ApiBulkAutoAdjustAdvice.from_dict(response.json())

        return response_415

    if response.status_code == 500:
        response_500 = ApiBulkAutoAdjustAdvice.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiBulkAutoAdjustAdvice, ResponseError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDetailedBulkAutoAdjustAdviceBody,
    rule_uuid: str,
    currency: str,
    reference: str,
    email_address: str,
) -> Response[Union[ApiBulkAutoAdjustAdvice, ResponseError]]:
    """Create bulk detailed auto-adjust advice

    Args:
        rule_uuid (str):
        currency (str):
        reference (str):
        email_address (str):
        body (CreateDetailedBulkAutoAdjustAdviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBulkAutoAdjustAdvice, ResponseError]]
    """

    kwargs = _get_kwargs(
        body=body,
        rule_uuid=rule_uuid,
        currency=currency,
        reference=reference,
        email_address=email_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDetailedBulkAutoAdjustAdviceBody,
    rule_uuid: str,
    currency: str,
    reference: str,
    email_address: str,
) -> Optional[Union[ApiBulkAutoAdjustAdvice, ResponseError]]:
    """Create bulk detailed auto-adjust advice

    Args:
        rule_uuid (str):
        currency (str):
        reference (str):
        email_address (str):
        body (CreateDetailedBulkAutoAdjustAdviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiBulkAutoAdjustAdvice, ResponseError]
    """

    return sync_detailed(
        client=client,
        body=body,
        rule_uuid=rule_uuid,
        currency=currency,
        reference=reference,
        email_address=email_address,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDetailedBulkAutoAdjustAdviceBody,
    rule_uuid: str,
    currency: str,
    reference: str,
    email_address: str,
) -> Response[Union[ApiBulkAutoAdjustAdvice, ResponseError]]:
    """Create bulk detailed auto-adjust advice

    Args:
        rule_uuid (str):
        currency (str):
        reference (str):
        email_address (str):
        body (CreateDetailedBulkAutoAdjustAdviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBulkAutoAdjustAdvice, ResponseError]]
    """

    kwargs = _get_kwargs(
        body=body,
        rule_uuid=rule_uuid,
        currency=currency,
        reference=reference,
        email_address=email_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDetailedBulkAutoAdjustAdviceBody,
    rule_uuid: str,
    currency: str,
    reference: str,
    email_address: str,
) -> Optional[Union[ApiBulkAutoAdjustAdvice, ResponseError]]:
    """Create bulk detailed auto-adjust advice

    Args:
        rule_uuid (str):
        currency (str):
        reference (str):
        email_address (str):
        body (CreateDetailedBulkAutoAdjustAdviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiBulkAutoAdjustAdvice, ResponseError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            rule_uuid=rule_uuid,
            currency=currency,
            reference=reference,
            email_address=email_address,
        )
    ).parsed
