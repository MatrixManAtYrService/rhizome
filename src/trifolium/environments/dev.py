"""Dev environment unified access (Rhizome DB + Stolon HTTP)."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

# Generated API imports - moved to top level to avoid deep indentation
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.alliance_code import (
    create_invoice_alliance_code,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.billing_entity import (
    create_billing_entity,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.billing_hierarchy import (
    create_billing_hierarchy,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.billing_schedule import (
    create_billing_schedule,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.cellular_action_fee_code import (
    create_cellular_action_fee_code,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.fee_rate import create_fee_rate
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.partner_config import (
    create_partner_config,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.plan_action_fee_code import (
    create_plan_action_fee_code,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.processing_group_dates import (
    create_processing_group_dates,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.api.revenue_share_group import (
    create_revenue_share_group,
    delete_revenue_share_group_by_uuid,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.models import (
    api_billing_entity,
    api_billing_entity_entity_type,
    api_billing_hierarchy,
    api_billing_schedule,
    api_billing_schedule_frequency,
    api_cellular_action_fee_code,
    api_fee_rate,
    api_fee_rate_apply_type,
    api_invoice_alliance_code,
    api_partner_config,
    api_plan_action_fee_code,
    api_processing_group_dates,
    api_revenue_share_group,
)
from stolon.generated.billing_bookkeeper_dev.open_api_definition_client.types import UNSET

if TYPE_CHECKING:
    from rhizome.client import RhizomeClient
    from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
    from stolon.client import StolonClient
    from stolon.generated.billing_bookkeeper_dev.open_api_definition_client import AuthenticatedClient


class Dev:
    """
    Unified dev environment providing both database and HTTP API access.

    Usage:
        from trifolium.environments import dev
        from rhizome.client import RhizomeClient
        from stolon.client import StolonClient

        environment = dev.Dev(
            rhizome_client=RhizomeClient(),
            stolon_client=StolonClient()
        )

        # Database queries via Rhizome
        environment.db.billing_bookkeeper.select_first(...)

        # HTTP API calls via Stolon - generated client
        environment.api.billing_bookkeeper.create_entity(...)
    """

    def __init__(self, rhizome_client: RhizomeClient, stolon_client: StolonClient) -> None:
        """Initialize dev environment with clients.

        Args:
            rhizome_client: Client for database access
            stolon_client: Client for HTTP API access
        """
        self._rhizome_client = rhizome_client
        self._stolon_client = stolon_client
        self._db: DevDatabase | None = None
        self._api: DevAPI | None = None

    @property
    def db(self) -> DevDatabase:
        """Database access via Rhizome."""
        if self._db is None:
            self._db = DevDatabase(self._rhizome_client)
        return self._db

    @property
    def api(self) -> DevAPI:
        """HTTP API access via Stolon with generated client."""
        if self._api is None:
            self._api = DevAPI(self._stolon_client)
        return self._api


class DevDatabase:
    """Database access for dev environment."""

    def __init__(self, client: RhizomeClient) -> None:
        """Initialize database access.

        Args:
            client: Rhizome client for database connections
        """
        self._client = client
        self._billing_bookkeeper: DevBillingBookkeeper | None = None

    @property
    def billing_bookkeeper(self) -> DevBillingBookkeeper:
        """Billing Bookkeeper database access."""
        if self._billing_bookkeeper is None:
            from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper

            self._billing_bookkeeper = DevBillingBookkeeper(self._client)
        return self._billing_bookkeeper


class DevAPI:
    """HTTP API access for dev environment using generated OpenAPI clients."""

    def __init__(self, client: StolonClient) -> None:
        """Initialize API access.

        Args:
            client: Stolon client for HTTP requests
        """
        self._client = client
        self._billing_bookkeeper: DevBillingBookkeeperAPI | None = None
        self._resellers: DevResellersAPI | None = None

    @property
    def billing_bookkeeper(self) -> DevBillingBookkeeperAPI:
        """Billing Bookkeeper API access with generated client."""
        if self._billing_bookkeeper is None:
            self._billing_bookkeeper = DevBillingBookkeeperAPI(self._client)
        return self._billing_bookkeeper

    @property
    def resellers(self) -> "DevResellersAPI":
        """Resellers API access (meta.reseller table)."""
        if self._resellers is None:
            self._resellers = DevResellersAPI(self._client)
        return self._resellers


class DevBillingBookkeeperAPI:
    """
    Billing Bookkeeper API wrapper using generated OpenAPI client.

    This class wraps the generated API client to provide a cleaner interface
    for common operations without requiring direct imports of generated models.
    """

    def __init__(self, client: StolonClient) -> None:
        """Initialize Billing Bookkeeper API.

        Args:
            client: Stolon client for HTTP requests
        """
        self._client = client
        self._authenticated_client: AuthenticatedClient | None = None
        self._domain = "dev1.dev.clover.com"
        self._env_name = "dev"

    def _ensure_authenticated(self) -> AuthenticatedClient:
        """Ensure we have an authenticated client for the generated API."""
        if self._authenticated_client is None:
            import httpx
            import structlog

            logger = structlog.get_logger()

            # Get token from stolon
            handle = self._client.request_internal_token(self._domain)

            # Import generated client
            from stolon.generated.billing_bookkeeper_dev.open_api_definition_client import AuthenticatedClient

            # Define request/response logging hooks
            def log_request(request: httpx.Request) -> None:
                import os

                # Sanitize headers for logging
                sanitized_headers = {
                    k: ("***" if k.lower() in ["cookie", "authorization"] else v) for k, v in request.headers.items()
                }

                log_data = {
                    "method": request.method,
                    "url": str(request.url),
                    "headers": sanitized_headers,
                }

                # If debug mode is enabled, include request body
                if os.getenv("STOLON_DEBUG_REQUESTS") and hasattr(request, "content"):
                    try:
                        import json

                        body_text = request.content.decode("utf-8") if request.content else None
                        if body_text:
                            log_data["request_body"] = json.loads(body_text)
                    except Exception:
                        pass

                logger.info("Generated client making HTTP request", **log_data)

            def log_response(response: httpx.Response) -> None:
                # Get content length from header if available
                content_length_header = response.headers.get("content-length")
                content_length = int(content_length_header) if content_length_header else None

                log_data = {
                    "method": response.request.method,
                    "url": str(response.request.url),
                    "status_code": response.status_code,
                }

                if content_length is not None:
                    log_data["content_length"] = content_length

                # Log error details for non-2xx responses
                # Note: We can't access response.text or response.content here in the hook
                # as the response hasn't been read yet
                if response.status_code >= 400:
                    logger.error("Generated client HTTP request failed", **log_data)
                else:
                    logger.info("Generated client received HTTP response", **log_data)

            # Create authenticated client with logging hooks
            # Add /billing-bookkeeper path prefix to base URL
            billing_bookkeeper_base_url = f"{handle.base_url}/billing-bookkeeper"

            self._authenticated_client = AuthenticatedClient(
                base_url=billing_bookkeeper_base_url,
                token=handle.token,
                prefix="",  # Token goes in Cookie header
                headers={
                    "X-Clover-Appenv": f"{self._env_name}:{self._domain.split('.')[0]}",
                },
                cookies={
                    "internalSession": handle.token,
                },
                httpx_args={
                    "event_hooks": {
                        "request": [log_request],
                        "response": [log_response],
                    }
                },
            )
        return self._authenticated_client

    def create_entity(self, entity_uuid: str, entity_type: str, name: str) -> dict[str, Any]:
        """Create a billing entity.

        Args:
            entity_uuid: 13-character UUID for the entity
            entity_type: Type of entity (e.g., "RESELLER", "MERCHANT")
            name: Display name for the entity

        Returns:
            Created entity data

        Raises:
            Exception: If creation fails
        """
        client = self._ensure_authenticated()

        # Create model
        entity_model = api_billing_entity.ApiBillingEntity(
            entity_uuid=entity_uuid,
            entity_type=api_billing_entity_entity_type.ApiBillingEntityEntityType(entity_type),
            name=name,
        )

        # Call API
        response = create_billing_entity.sync_detailed(client=client, body=entity_model)

        if response.status_code != 200:
            raise Exception(f"Failed to create entity: {response.status_code} - {response.content}")

        # Return as dict
        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def create_alliance_code(
        self, billing_entity_uuid: str, alliance_code_value: str, invoice_count: int = 1
    ) -> dict[str, Any]:
        """Create an alliance code.

        Args:
            billing_entity_uuid: UUID of the billing entity
            alliance_code_value: Alliance code string (e.g., "MFF0001")
            invoice_count: Number of invoices (default: 1)

        Returns:
            Created alliance code data
        """
        client = self._ensure_authenticated()

        model = api_invoice_alliance_code.ApiInvoiceAllianceCode(
            billing_entity_uuid=billing_entity_uuid,
            alliance_code=alliance_code_value,
            invoice_count=invoice_count,
        )

        response = create_invoice_alliance_code.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create alliance code: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def create_revenue_share_group(
        self, revenue_share_group_name: str, short_desc: str, description: str
    ) -> dict[str, Any]:
        """Create a revenue share group.

        Args:
            revenue_share_group_name: Name of the revenue share group
            short_desc: Short description
            description: Full description

        Returns:
            Created revenue share group data
        """
        client = self._ensure_authenticated()

        model = api_revenue_share_group.ApiRevenueShareGroup(
            revenue_share_group=revenue_share_group_name,
            short_desc=short_desc,
            description=description,
        )

        response = create_revenue_share_group.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create revenue share group: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def delete_revenue_share_group(self, uuid: str) -> None:
        """Delete a revenue share group by UUID.

        Args:
            uuid: UUID of the revenue share group to delete
        """
        client = self._ensure_authenticated()
        delete_revenue_share_group_by_uuid.sync(client=client, uuid=uuid)

    def create_billing_schedule(
        self,
        billing_entity_uuid: str,
        effective_date: str,
        frequency: str,
        billing_day: int,
        next_billing_date: str,
        units_in_next_period: int,
        default_currency: str,
    ) -> dict[str, Any]:
        """Create a billing schedule.

        Args:
            billing_entity_uuid: UUID of the billing entity
            effective_date: Effective date (YYYY-MM-DD format)
            frequency: Billing frequency (e.g., "MONTHLY")
            billing_day: Billing day within billing period
            next_billing_date: Next billing date (YYYY-MM-DD format)
            units_in_next_period: Number of units in the next billing period
            default_currency: 3-letter currency code (e.g., "EUR", "USD")

        Returns:
            Created billing schedule data
        """
        client = self._ensure_authenticated()

        model = api_billing_schedule.ApiBillingSchedule(
            billing_entity_uuid=billing_entity_uuid,
            effective_date=datetime.strptime(effective_date, "%Y-%m-%d").date(),
            frequency=api_billing_schedule_frequency.ApiBillingScheduleFrequency(frequency),
            billing_day=billing_day,
            next_billing_date=datetime.strptime(next_billing_date, "%Y-%m-%d").date(),
            units_in_next_period=units_in_next_period,
            default_currency=default_currency,
        )

        response = create_billing_schedule.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create billing schedule: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def create_fee_rate(
        self,
        billing_entity_uuid: str,
        fee_category: str,
        fee_code: str,
        currency: str,
        effective_date: str,
        apply_type: str,
        per_item_amount: float,
        percentage: float | None = None,
    ) -> dict[str, Any]:
        """Create a fee rate.

        Args:
            billing_entity_uuid: UUID of the billing entity
            fee_category: Fee category (e.g., "PLAN_RETAIL")
            fee_code: Fee code (e.g., "PaymentsPDVT")
            currency: 3-letter currency code (e.g., "EUR", "USD")
            effective_date: Effective date (YYYY-MM-DD format)
            apply_type: Apply type (e.g., "DEFAULT")
            per_item_amount: Per-item rate amount
            percentage: Optional percentage rate

        Returns:
            Created fee rate data
        """
        client = self._ensure_authenticated()

        model = api_fee_rate.ApiFeeRate(
            billing_entity_uuid=billing_entity_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            effective_date=datetime.strptime(effective_date, "%Y-%m-%d").date(),
            apply_type=api_fee_rate_apply_type.ApiFeeRateApplyType(apply_type),
            per_item_amount=per_item_amount,
            percentage=percentage if percentage is not None else UNSET,
        )

        response = create_fee_rate.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create fee rate: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def create_processing_group_dates(
        self,
        billing_entity_uuid: str,
        hierarchy_type: str,
        cycle_date: str,
        posting_date: str,
        billing_date: str,
        settlement_date: str,
    ) -> dict[str, Any]:
        """Create processing group dates.

        Args:
            billing_entity_uuid: UUID of the billing entity
            hierarchy_type: Billing hierarchy type (e.g., "MERCHANT_SCHEDULE")
            cycle_date: Cycle date (YYYY-MM-DD format)
            posting_date: Posting date (YYYY-MM-DD format)
            billing_date: Billing date (YYYY-MM-DD format)
            settlement_date: Settlement date (YYYY-MM-DD format)

        Returns:
            Created processing group dates data
        """
        client = self._ensure_authenticated()

        model = api_processing_group_dates.ApiProcessingGroupDates(
            billing_entity_uuid=billing_entity_uuid,
            hierarchy_type=hierarchy_type,
            cycle_date=datetime.strptime(cycle_date, "%Y-%m-%d").date(),
            posting_date=datetime.strptime(posting_date, "%Y-%m-%d").date(),
            billing_date=datetime.strptime(billing_date, "%Y-%m-%d").date(),
            settlement_date=datetime.strptime(settlement_date, "%Y-%m-%d").date(),
        )

        response = create_processing_group_dates.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create processing group dates: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def create_billing_hierarchy(
        self,
        billing_entity_uuid: str,
        hierarchy_type: str,
        effective_date: str,
        parent_billing_hierarchy_uuid: str,
    ) -> dict[str, Any]:
        """Create a billing hierarchy.

        Args:
            billing_entity_uuid: UUID of the billing entity
            hierarchy_type: Hierarchy type (e.g., "MERCHANT_SCHEDULE", "MERCHANT_FEE_RATE")
            effective_date: Effective date (YYYY-MM-DD format)
            parent_billing_hierarchy_uuid: UUID of the parent billing hierarchy

        Returns:
            Created billing hierarchy data
        """
        client = self._ensure_authenticated()

        model = api_billing_hierarchy.ApiBillingHierarchy(
            billing_entity_uuid=billing_entity_uuid,
            hierarchy_type=hierarchy_type,
            effective_date=datetime.strptime(effective_date, "%Y-%m-%d").date(),
            parent_billing_hierarchy_uuid=parent_billing_hierarchy_uuid,
        )

        response = create_billing_hierarchy.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create billing hierarchy: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def create_partner_config(
        self,
        billing_entity_uuid: str,
        effective_date: str,
        hierarchy_type: str,
        settlement_method: str,
        invoice_method: str,
        revenue_share_group: str | None = None,
        post_method: str | None = None,
        plan_billing_method: str | None = None,
        invoice_number_format: str | None = None,
        seasonal_rule_set_uuid: str | None = None,
    ) -> dict[str, Any]:
        """Create a partner config.

        Args:
            billing_entity_uuid: UUID of the billing entity
            effective_date: Effective date (YYYY-MM-DD format)
            hierarchy_type: Hierarchy type (e.g., "MERCHANT_SCHEDULE")
            settlement_method: Settlement method (e.g., "Goleo")
            invoice_method: Invoice method (e.g., "MerchantDetail")
            revenue_share_group: Optional revenue share group
            post_method: Optional method used to post actions
            plan_billing_method: Optional method used to bill for plan SaaS fees
            invoice_number_format: Optional format used for invoice number
            seasonal_rule_set_uuid: Optional UUID of seasonal monetary rule set

        Returns:
            Created partner config data
        """
        client = self._ensure_authenticated()

        model = api_partner_config.ApiPartnerConfig(
            billing_entity_uuid=billing_entity_uuid,
            effective_date=datetime.strptime(effective_date, "%Y-%m-%d").date(),
            hierarchy_type=hierarchy_type,
            settlement_method=settlement_method,
            invoice_method=invoice_method,
            revenue_share_group=revenue_share_group if revenue_share_group is not None else UNSET,
            post_method=post_method if post_method is not None else UNSET,
            plan_billing_method=plan_billing_method if plan_billing_method is not None else UNSET,
            invoice_number_format=invoice_number_format if invoice_number_format is not None else UNSET,
            seasonal_rule_set_uuid=seasonal_rule_set_uuid if seasonal_rule_set_uuid is not None else UNSET,
        )

        response = create_partner_config.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create partner config: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def create_plan_action_fee_code(
        self,
        merchant_plan_uuid: str,
        plan_action_type: str,
        effective_date: str,
        fee_category: str,
        fee_code: str,
        device_type: str | None = None,
    ) -> dict[str, Any]:
        """Create a plan action fee code (global resource).

        Args:
            merchant_plan_uuid: 13-character UUID of the merchant plan
            plan_action_type: Plan action type (e.g., "PLAN_ASSIGN")
            effective_date: Effective date (YYYY-MM-DD format)
            fee_category: Fee category (e.g., "PLAN_RETAIL")
            fee_code: Fee code (e.g., "PaymentsPDVT.PRC")
            device_type: Optional device type

        Returns:
            Created plan action fee code data
        """
        client = self._ensure_authenticated()

        model = api_plan_action_fee_code.ApiPlanActionFeeCode(
            merchant_plan_uuid=merchant_plan_uuid,
            plan_action_type=plan_action_type,
            effective_date=datetime.strptime(effective_date, "%Y-%m-%d").date(),
            fee_category=fee_category,
            fee_code=fee_code,
            device_type=device_type if device_type is not None else UNSET,
        )

        response = create_plan_action_fee_code.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create plan action fee code: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")

    def create_cellular_action_fee_code(
        self,
        carrier: str,
        cellular_action_type: str,
        effective_date: str,
        fee_category: str,
        fee_code: str,
        merchant_plan_uuid: str | None = None,
    ) -> dict[str, Any]:
        """Create a cellular action fee code (global resource).

        Args:
            carrier: Cellular carrier (e.g., "AT&T")
            cellular_action_type: Cellular action type (e.g., "CELLULAR_ARREARS")
            effective_date: Effective date (YYYY-MM-DD format)
            fee_category: Fee category (e.g., "CELLULAR_RETAIL")
            fee_code: Fee code (e.g., "CellularArr.ATT")
            merchant_plan_uuid: Optional 13-character UUID of merchant plan

        Returns:
            Created cellular action fee code data
        """
        client = self._ensure_authenticated()

        model = api_cellular_action_fee_code.ApiCellularActionFeeCode(
            carrier=carrier,
            cellular_action_type=cellular_action_type,
            effective_date=datetime.strptime(effective_date, "%Y-%m-%d").date(),
            fee_category=fee_category,
            fee_code=fee_code,
            merchant_plan_uuid=merchant_plan_uuid if merchant_plan_uuid is not None else UNSET,
        )

        response = create_cellular_action_fee_code.sync_detailed(client=client, body=model)

        if response.status_code != 200:
            raise Exception(f"Failed to create cellular action fee code: {response.status_code} - {response.content}")

        if response.parsed:
            return response.parsed.to_dict()
        raise Exception("No response data returned")


class DevResellersAPI:
    """
    Resellers API wrapper for /v3/resellers endpoint.
    
    This API creates records in the meta.reseller table, which is separate
    from billing_bookkeeper.billing_entity. Both are needed for a complete reseller:
    - meta.reseller: The core reseller entity (visible in admin UI)
    - billing_bookkeeper.billing_entity: The billing configuration
    """

    def __init__(self, client: StolonClient) -> None:
        """Initialize Resellers API.

        Args:
            client: Stolon client for HTTP requests
        """
        self._client = client
        self._domain = "dev1.dev.clover.com"
        self._env_name = "dev"

    def create_reseller(
        self,
        name: str,
        owner_email: str,
        parent_reseller_id: str,
        merchant_plan_group_id: str,
        support_phone: str = "",
        support_email: str = "",
        locale: str = "en-US",
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create a reseller in meta.reseller table.

        Args:
            name: Reseller name
            owner_email: Email for the reseller owner account
            parent_reseller_id: ID of the parent reseller (e.g., "Y7TC6PNQMENF0")
            merchant_plan_group_id: ID of the merchant plan group (e.g., "B1DTBWV564MNE")
            support_phone: Support phone number
            support_email: Support email address
            locale: Locale (default: "en-US")
            **kwargs: Additional fields to include in the request

        Returns:
            Created reseller data including the UUID

        Raises:
            Exception: If creation fails
        """
        import httpx

        # Get authentication token
        handle = self._client.request_internal_token(self._domain)

        # Build the request payload with minimal required fields
        payload = {
            "name": name,
            "owner": {"email": owner_email},
            "parentReseller": {"id": parent_reseller_id},
            "merchantPlanGroup": {"id": merchant_plan_group_id},
            "locale": locale,
            "supportPhone": support_phone,
            "supportEmail": support_email,
            # Common defaults from the curl example
            "allowBlackhole": False,
            "alternateName": "",
            "code": None,
            "defaultPaymentProcessor": {"id": ""},
            "defaultProcessorKey": {"id": ""},
            "fdClientId": None,
            "filterApps": False,
            "forcePhone": False,
            "isBulkPurchaser": False,
            "isCodelessActivation": False,
            "isIntercomEnabled": True,
            "isNewBilling": True,
            "isRapidDepositEnabled": False,
            "isRkiIdentifier": False,
            "isSelfBoarding": False,
            "partnerSupportEmail": "",
            "rapidDepositServiceEntitlementNumber": "",
            "stationsOnClassic": True,
            "supportsNakedCredit": True,
            "supportsOutboundBoarding": False,
            "tasqCustomerNumber": "",
            "type": "UNKNOWN",
        }

        # Override with any additional kwargs
        payload.update(kwargs)

        # Make the HTTP request
        url = f"https://{self._domain}/v3/resellers"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Clover-Appenv": f"{self._env_name}:{self._domain.split('.')[0]}",
        }
        cookies = {"internalSession": handle.token}

        response = httpx.post(url, json=payload, headers=headers, cookies=cookies, timeout=30.0)

        if response.status_code not in (200, 201):
            raise Exception(f"Failed to create reseller: {response.status_code} - {response.text}")

        return response.json()
