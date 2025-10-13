"""Dev environment unified access (Rhizome DB + Stolon HTTP)."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

import httpx

# Environment-specific database class aliases
# These allow code in this module to use BillingEvent, BillingBookkeeper, Meta
# instead of the Dev-prefixed versions. This makes it easier to:
# 1. Move code to base.py (use the alias name instead of environment-specific name)
# 2. Create demo.py (just change the alias target: BillingEvent = DemoBillingEvent)
from rhizome.environments.dev.billing_event import DevBillingEvent as BillingEvent
from stolon.environments import base

# Generated API imports - Agreement K8s
from stolon.generated.agreement_k8s_dev.open_api_definition_client.api.acceptance_controller_impl import (
    create_acceptance,
    get_bulk_acceptances_service_scope,
)
from stolon.generated.agreement_k8s_dev.open_api_definition_client.api.agreement_controller import (
    get_latest_agreement,
)
from stolon.generated.agreement_k8s_dev.open_api_definition_client.models import (
    get_bulk_acceptances_service_scope_body,
    get_bulk_acceptances_service_scope_body_request_body,
)
from stolon.generated.agreement_k8s_dev.open_api_definition_client.models.acceptance import Acceptance

# Generated API imports - Billing Bookkeeper
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
    from stolon.generated.agreement_k8s_dev.open_api_definition_client import (
        AuthenticatedClient as AgreementAuthenticatedClient,
    )
    from stolon.generated.billing_bookkeeper_dev.open_api_definition_client import AuthenticatedClient
    from stolon.generated.billing_event_dev.open_api_definition_client import (
        AuthenticatedClient as BillingEventAuthenticatedClient,
    )

# Type aliases for agreement models (needed to avoid line-length issues with long import paths)
GetBulkAcceptancesServiceScopeBody = get_bulk_acceptances_service_scope_body.GetBulkAcceptancesServiceScopeBody
GetBulkAcceptancesServiceScopeBodyRequestBody = (
    get_bulk_acceptances_service_scope_body_request_body.GetBulkAcceptancesServiceScopeBodyRequestBody
)


class Environment:
    """
    Unified dev environment providing both database and HTTP API access.

    Usage:
        from trifolium.environments import dev
        from rhizome.client import RhizomeClient
        from stolon.client import StolonClient

        environment = dev.Environment(
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
        self.rhizome_client = rhizome_client
        self.stolon_client = stolon_client
        self._db: DevDatabase | None = None
        self._api: DevAPI | None = None

    @property
    def db(self) -> DevDatabase:
        """Database access via Rhizome."""
        if self._db is None:
            self._db = DevDatabase(self.rhizome_client)
        return self._db

    @property
    def api(self) -> DevAPI:
        """HTTP API access via Stolon with generated client."""
        if self._api is None:
            self._api = DevAPI(self.stolon_client)
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
        self._agreement: DevAgreementAPI | None = None

    @property
    def billing_bookkeeper(self) -> DevBillingBookkeeperAPI:
        """Billing Bookkeeper API access with generated client."""
        if self._billing_bookkeeper is None:
            self._billing_bookkeeper = DevBillingBookkeeperAPI(self._client)
        return self._billing_bookkeeper

    @property
    def resellers(self) -> DevResellersAPI:
        """Resellers API access (meta.reseller table)."""
        if self._resellers is None:
            self._resellers = DevResellersAPI(self._client)
        return self._resellers

    @property
    def agreement(self) -> DevAgreementAPI:
        """Agreement API access for merchant terms acceptance."""
        if self._agreement is None:
            self._agreement = DevAgreementAPI(self._client)
        return self._agreement


class DevBillingBookkeeperAPI(base.Environment):
    """
    Billing Bookkeeper API wrapper using generated OpenAPI client.

    This class wraps the generated API client to provide a cleaner interface
    for common operations without requiring direct imports of generated models.
    """

    @property
    def name(self) -> str:
        """Environment name."""
        return "dev"

    @property
    def domain(self) -> str:
        """Clover domain for this environment."""
        return "dev1.dev.clover.com"

    def __init__(self, client: StolonClient) -> None:
        """Initialize Billing Bookkeeper API.

        Args:
            client: Stolon client for HTTP requests
        """
        super().__init__(client)
        self._authenticated_client: AuthenticatedClient | None = None

    def _ensure_generated_client_authenticated(self) -> AuthenticatedClient:
        """
        Ensure we have an authenticated client for the generated OpenAPI client.

        This creates an AuthenticatedClient instance with logging hooks
        to ensure all requests flow through the same logging/observability
        infrastructure.
        """
        if self._authenticated_client is None:
            # Get authentication token via parent's method
            self._ensure_authenticated()
            assert self._handle is not None

            # Import generated client
            from stolon.generated.billing_bookkeeper_dev.open_api_definition_client import AuthenticatedClient

            # Add /billing-bookkeeper path prefix to base URL
            billing_bookkeeper_base_url = f"{self._handle.base_url}/billing-bookkeeper"

            # Create event hooks for logging (same as parent's _create_httpx_client)
            from collections.abc import Callable
            from contextlib import suppress

            def log_request_hook(request: httpx.Request) -> None:
                """Log HTTP request to stolon server (fire-and-forget)."""
                with suppress(Exception):
                    body_str: str | None = None
                    if request.content:
                        try:
                            body_str = request.content.decode("utf-8")
                        except Exception:
                            body_str = f"<binary data, {len(request.content)} bytes>"

                    httpx.post(
                        f"{self.client.base_url}/log_request",
                        json={
                            "method": request.method,
                            "url": str(request.url),
                            "data": body_str,
                        },
                        timeout=1.0,
                    )

            def log_response_hook(response: httpx.Response) -> None:
                """Log HTTP response to stolon server (fire-and-forget)."""
                body_str: str | None = None
                try:
                    if response.content:
                        body_str = response.content.decode("utf-8")
                except Exception:
                    pass

                with suppress(Exception):
                    httpx.post(
                        f"{self.client.base_url}/log_response",
                        json={
                            "method": response.request.method,
                            "url": str(response.request.url),
                            "status_code": response.status_code,
                            "data": body_str,
                        },
                        timeout=1.0,
                    )

            request_hooks: list[Callable[[httpx.Request], None]] = [log_request_hook]
            response_hooks: list[Callable[[httpx.Response], None]] = [log_response_hook]

            event_hooks = {
                "request": request_hooks,
                "response": response_hooks,
            }

            # Create authenticated client with logging hooks
            self._authenticated_client = AuthenticatedClient(
                base_url=billing_bookkeeper_base_url,
                token=self._handle.token,
                prefix="",  # Token goes in Cookie header
                headers={
                    "X-Clover-Appenv": f"{self.name}:{self.domain.split('.')[0]}",
                },
                cookies={
                    "internalSession": self._handle.token,
                },
                httpx_args={"event_hooks": event_hooks},
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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()
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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()

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
        client = self._ensure_generated_client_authenticated()

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


class DevResellersAPI(base.Environment):
    """
    Resellers API wrapper for /v3/resellers endpoint.

    This API creates records in the meta.reseller table, which is separate
    from billing_bookkeeper.billing_entity. Both are needed for a complete reseller:
    - meta.reseller: The core reseller entity (visible in admin UI)
    - billing_bookkeeper.billing_entity: The billing configuration
    """

    @property
    def name(self) -> str:
        """Environment name."""
        return "dev"

    @property
    def domain(self) -> str:
        """Clover domain for this environment."""
        return "dev1.dev.clover.com"

    def create_reseller(
        self,
        name: str,
        owner_email: str,
        parent_reseller_id: str,
        merchant_plan_group_id: str,
        support_phone: str = "",
        support_email: str = "",
        locale: str = "en-US",
        code: str | None = None,
        **kwargs: str | dict[str, str] | bool | None,
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
            code: Reseller code (if not provided, extracts first word from name)
            **kwargs: Additional fields to include in the request

        Returns:
            Created reseller data including the UUID

        Raises:
            Exception: If creation fails
        """
        # Extract code from name if not provided (e.g., "MFF" from "MFF Test Reseller 1234")
        if code is None:
            code = name.split()[0] if name else "UNKNOWN"

        # Use reasonable defaults if not provided (empty strings cause NPE on server)
        if not support_phone:
            support_phone = "1-888-111-1111"
        if not support_email:
            support_email = "trifolium@github.corp.clover.com"

        # Build the request payload with minimal required fields
        payload: dict[str, Any] = {
            "name": name,
            "owner": {"email": owner_email},
            "parentReseller": {"id": parent_reseller_id},
            "merchantPlanGroup": {"id": merchant_plan_group_id},
            "locale": locale,
            "supportPhone": support_phone,
            "supportEmail": support_email,
            "code": code,  # Required field
            # Common defaults from the curl example
            "allowBlackhole": False,
            # "alternateName": "",  # Commented out - may cause NPE
            # "defaultPaymentProcessor": {"id": ""},  # Commented out - may cause NPE when resolving empty ID
            # "defaultProcessorKey": {"id": ""},  # Commented out - may cause NPE when resolving empty ID
            # "fdClientId": None,  # Commented out - may cause NPE
            "filterApps": False,
            "forcePhone": False,
            "isBulkPurchaser": False,
            "isCodelessActivation": False,
            "isIntercomEnabled": True,
            "isNewBilling": True,
            "isRapidDepositEnabled": False,
            "isRkiIdentifier": False,
            "isSelfBoarding": False,
            # "partnerSupportEmail": "",  # Commented out - probably safe but not needed
            # "rapidDepositServiceEntitlementNumber": "",  # Commented out - probably safe but not needed
            "stationsOnClassic": True,
            "supportsNakedCredit": True,
            "supportsOutboundBoarding": False,
            # "tasqCustomerNumber": "",  # Commented out - probably safe but not needed
            "type": "UNKNOWN",
        }

        # Override with any additional kwargs
        payload.update(kwargs)

        # Use parent class's post method (handles auth, logging, retries)
        response = self.post("/v3/resellers", json=payload, timeout=30.0)

        if response is None:
            raise Exception("No response data returned from reseller creation")

        return response  # type: ignore[return-value]

    def create_merchant_plan_group(self, name: str) -> dict[str, Any]:
        """Create a merchant plan group.

        Args:
            name: Name of the plan group

        Returns:
            Created plan group data including ID (UUID)

        Raises:
            Exception: If creation fails
        """
        payload = {"name": name}
        response = self.post("/v3/merchant_plan_groups", json=payload, timeout=30.0)

        if response is None:
            raise Exception("No response data returned from merchant plan group creation")

        return response  # type: ignore[return-value]

    def create_merchant_plan(
        self,
        merchant_plan_group_id: str,
        name: str,
        plan_code: str,
        plan_type: str | None = None,
        default_plan: bool = False,
        tags: list[str] | None = None,
    ) -> dict[str, Any]:
        """Create a merchant plan within a plan group.

        Args:
            merchant_plan_group_id: ID of the parent plan group
            name: Name of the plan
            plan_code: Plan code (e.g., "MFF_TEST")
            plan_type: Optional plan type (e.g., "PAYMENTS", "REGISTER", "NO_HARDWARE")
            default_plan: Whether this should be the default plan in the group (default: False)
            tags: Optional list of tags (e.g., ["NO_HARDWARE"] for virtual/no-device plans)

        Returns:
            Created plan data including UUID and app bundle

        Raises:
            Exception: If creation fails
        """
        payload: dict[str, Any] = {
            "name": name,
            "planCode": plan_code,
            "defaultPlan": default_plan,
        }
        if plan_type:
            payload["type"] = plan_type
        if tags:
            payload["tags"] = tags

        endpoint = f"/v3/merchant_plan_groups/{merchant_plan_group_id}/merchant_plans"
        response = self.post(endpoint, json=payload, timeout=30.0)

        if response is None:
            raise Exception("No response data returned from merchant plan creation")

        return response  # type: ignore[return-value]

    def delete_merchant_plan(self, merchant_plan_group_id: str, plan_uuid: str) -> None:
        """Delete a merchant plan from a plan group.

        Args:
            merchant_plan_group_id: ID of the parent plan group
            plan_uuid: UUID of the plan to delete

        Raises:
            Exception: If deletion fails
        """
        endpoint = f"/v3/merchant_plan_groups/{merchant_plan_group_id}/merchant_plans/{plan_uuid}"
        self.delete(endpoint, timeout=30.0)

    def delete_merchant_plan_group(self, plan_group_id: str) -> None:
        """Delete a merchant plan group (must be empty).

        Args:
            plan_group_id: ID of the plan group to delete

        Raises:
            Exception: If deletion fails (e.g., group not empty)
        """
        endpoint = f"/v3/merchant_plan_groups/{plan_group_id}"
        self.delete(endpoint, timeout=30.0)

    def board_merchant(
        self,
        reseller_code: str,
        merchant_id: str,
        dba_name: str,
        legal_name: str,
        email: str,
        country: str = "US",
        currency: str = "USD",
        timezone: str = "America/Los_Angeles",
    ) -> dict[str, Any]:
        """Board a new merchant to a reseller via IPG endpoint.

        Args:
            reseller_code: Reseller code (e.g., "MFF")
            merchant_id: Unique merchant ID (MID)
            dba_name: Doing Business As name
            legal_name: Legal business name
            email: Contact email
            country: Country code (default: "US")
            currency: Currency code (default: "USD")
            timezone: Timezone (default: "America/Los_Angeles")

        Returns:
            Parsed response containing merchant UUID

        Raises:
            Exception: If boarding fails
        """
        # Build XML payload for merchant boarding
        xml_payload = f"""<?xml version="1.0" encoding="UTF-8"?>
<CloverBoardingRequest xmlns="com.clover.boarding">
  <RequestAction>Create</RequestAction>
  <MerchantDetail>
    <merchantNumber>{merchant_id}</merchantNumber>
    <mid>{merchant_id}</mid>
    <dbaName>{dba_name}</dbaName>
    <legalName>{legal_name}</legalName>
    <address>
      <address1>123 Test Street</address1>
      <address2>Suite 100</address2>
      <city>Test City</city>
      <state>CA</state>
      <zip>12345</zip>
      <country>{country}</country>
    </address>
    <contactInformation>
      <contactName>Test Contact</contactName>
      <phoneNumber>1234567890</phoneNumber>
      <email>{email}</email>
    </contactInformation>
    <reseller>{reseller_code}</reseller>
    <currency>{currency}</currency>
    <timeZone>{timezone}</timeZone>
    <supportPhone>1234567890</supportPhone>
  </MerchantDetail>
  <CardTypes>
    <CardType cardName="VISA"/>
  </CardTypes>
  <ShipAddress>
    <shipAddress>
      <shipName>Test Shipping Address</shipName>
      <address1>123 Test Street</address1>
      <address2>Suite 100</address2>
      <city>Test City</city>
      <state>CA</state>
      <zip>12345</zip>
    </shipAddress>
  </ShipAddress>
</CloverBoardingRequest>"""

        # Make request to boarding endpoint
        self._ensure_authenticated()
        assert self._handle is not None

        headers = {
            "Cookie": f"internalSession={self._handle.token}",
            "Content-Type": "application/xml",
            "X-Clover-Appenv": f"{self.name}:{self.domain.split('.')[0]}",
        }

        full_url = f"{self._handle.base_url}/cos/v1/partner/ipg/create_merchant"

        import xml.etree.ElementTree as ET

        with self._create_httpx_client() as client:
            response = client.post(
                full_url,
                headers=headers,
                content=xml_payload,
                timeout=30.0,
            )

            response.raise_for_status()

            # Parse XML response
            root = ET.fromstring(response.text)

            # Extract merchant UUID from response
            # Response format: <CloverBoardingResponse><UUID>...</UUID>...</CloverBoardingResponse>
            uuid_elem = root.find(".//{com.clover.boarding}UUID")
            merchant_uuid = uuid_elem.text if uuid_elem is not None else None

            if not merchant_uuid:
                raise Exception(f"No UUID found in boarding response: {response.text}")

            return {
                "merchant_uuid": merchant_uuid,
                "merchant_id": merchant_id,
                "dba_name": dba_name,
                "legal_name": legal_name,
                "reseller_code": reseller_code,
                "raw_response": response.text,
            }


class DevAgreementAPI(base.Environment):
    """
    Agreement API wrapper for merchant terms acceptance.

    This class provides helper methods for checking and creating merchant
    agreement acceptances, handling the agreement service at dev1.dev.clover.com.
    """

    @property
    def name(self) -> str:
        """Environment name."""
        return "dev"

    @property
    def domain(self) -> str:
        """Agreement service domain."""
        return "dev1.dev.clover.com"

    def __init__(self, client: StolonClient) -> None:
        """Initialize Agreement API.

        Args:
            client: Stolon client for HTTP requests
        """
        super().__init__(client)
        self._authenticated_client: AgreementAuthenticatedClient | None = None
        self._billing_event_client: BillingEventAuthenticatedClient | None = None

    def _ensure_agreement_client_authenticated(self) -> AgreementAuthenticatedClient:
        """
        Ensure we have an authenticated client for the agreement API.

        Returns:
            Authenticated client for agreement service
        """
        if self._authenticated_client is None:
            # Get authentication token via parent's method
            self._ensure_authenticated()
            assert self._handle is not None

            # Import generated client
            from stolon.generated.agreement_k8s_dev.open_api_definition_client import AuthenticatedClient

            # Add /agreement path prefix to base URL
            agreement_base_url = f"{self._handle.base_url}/agreement"

            # Create event hooks using parent's _create_httpx_client infrastructure
            # We need to extract the event_hooks from the parent's client
            parent_client = self._create_httpx_client()
            event_hooks = parent_client.event_hooks

            # Create authenticated client with logging hooks and proper auth
            self._authenticated_client = AuthenticatedClient(
                base_url=agreement_base_url,
                token=self._handle.token,
                prefix="",  # Token goes in Cookie header
                headers={
                    "X-Clover-Appenv": f"{self.name}:{self.domain.split('.')[0]}",
                },
                cookies={
                    "internalSession": self._handle.token,
                },
                httpx_args={"event_hooks": event_hooks},
            )

        return self._authenticated_client

    def _ensure_billing_event_client_authenticated(self) -> BillingEventAuthenticatedClient:
        """
        Ensure we have an authenticated client for the billing-event API.

        Returns:
            Authenticated client for billing-event service
        """
        if self._billing_event_client is None:
            # Get authentication token via parent's method
            self._ensure_authenticated()
            assert self._handle is not None

            # Import generated client
            from stolon.generated.billing_event_dev.open_api_definition_client import AuthenticatedClient

            # Add /billing-event path prefix to base URL
            billing_event_base_url = f"{self._handle.base_url}/billing-event"

            # Create event hooks using parent's _create_httpx_client infrastructure
            parent_client = self._create_httpx_client()
            event_hooks = parent_client.event_hooks

            # Create authenticated client with logging hooks and proper auth
            self._billing_event_client = AuthenticatedClient(
                base_url=billing_event_base_url,
                token=self._handle.token,
                prefix="",  # Token goes in Cookie header
                headers={
                    "X-Clover-Appenv": f"{self.name}:{self.domain.split('.')[0]}",
                },
                cookies={
                    "internalSession": self._handle.token,
                },
                httpx_args={"event_hooks": event_hooks},
            )

        return self._billing_event_client

    def has_merchant_accepted(self, merchant_uuid: str, agreement_type: str = "BILLING") -> Acceptance | None:
        """Check if merchant has accepted a specific agreement type.

        Args:
            merchant_uuid: Merchant UUID
            agreement_type: Agreement type to check (default: "BILLING")

        Returns:
            Acceptance object if merchant has accepted, None otherwise
        """
        client = self._ensure_agreement_client_authenticated()

        # Query bulk acceptances API using nested request body structure
        request_body = GetBulkAcceptancesServiceScopeBodyRequestBody()
        request_body["merchant_id"] = [merchant_uuid]

        bulk_request = GetBulkAcceptancesServiceScopeBody(request_body=request_body)
        acceptances = get_bulk_acceptances_service_scope.sync(
            client=client,
            body=bulk_request,
        )

        if not acceptances:
            return None

        # Find current acceptance for the specified agreement type
        for acceptance in acceptances:
            if acceptance.agreement_type == agreement_type and acceptance.current:
                return acceptance

        return None

    def ensure_merchant_acceptance(
        self, merchant_uuid: str, account_id: str, agreement_type: str = "BILLING", signer_name: str | None = None
    ) -> Acceptance:
        """Ensure merchant has accepted a specific agreement type.

        This method is idempotent - it checks if the merchant has already accepted
        the agreement, and only creates a new acceptance if needed.

        Args:
            merchant_uuid: Merchant UUID
            account_id: Merchant's account ID
            agreement_type: Agreement type (default: "BILLING")
            signer_name: Name of signer (default: "Test User for {merchant_uuid}")

        Returns:
            Acceptance object (either existing or newly created)

        Raises:
            Exception: If acceptance creation fails
        """
        # Check if merchant already has acceptance
        existing_acceptance = self.has_merchant_accepted(merchant_uuid, agreement_type)
        if existing_acceptance:
            return existing_acceptance

        # Create new acceptance
        client = self._ensure_agreement_client_authenticated()

        # Get the latest agreement for the specified type
        agreement_response = get_latest_agreement.sync_detailed(
            type_=agreement_type,
            client=client,
        )

        if agreement_response.status_code != 200:
            # Format error message with response details
            error_body = agreement_response.content.decode('utf-8') if agreement_response.content else "(no body)"
            raise Exception(
                f"Failed to fetch latest {agreement_type} agreement: HTTP {agreement_response.status_code}\n"
                f"{error_body}"
            )

        latest_agreement = agreement_response.parsed
        if not latest_agreement:
            raise Exception(f"Could not parse latest {agreement_type} agreement response")

        # Ensure agreement has an ID
        if not latest_agreement.id or latest_agreement.id is UNSET:
            raise Exception(f"Latest {agreement_type} agreement has no ID")

        # Create acceptance
        if signer_name is None:
            signer_name = f"Test User for {merchant_uuid}"

        # Use the billing-event backfill endpoint instead of the agreement API
        # This is the correct way to programmatically create acceptances
        from stolon.generated.billing_event_dev.open_api_definition_client.api.backfill_acceptance import create_4
        from stolon.generated.billing_event_dev.open_api_definition_client.models.api_backfill_acceptance import (
            ApiBackfillAcceptance,
        )
        from stolon.generated.billing_event_dev.open_api_definition_client.models.api_backfill_acceptance_type import (
            ApiBackfillAcceptanceType,
        )

        # Get authenticated client for billing-event service
        billing_event_client = self._ensure_billing_event_client_authenticated()

        # Create the backfill acceptance model
        backfill_body = ApiBackfillAcceptance(
            merchant_id=merchant_uuid,
            account_id=account_id,
            type_=ApiBackfillAcceptanceType(agreement_type),
            locale="en_US",
            comment=f"Acceptance created via trifolium for {merchant_uuid}",
        )
        # Add devices field via additional_properties (not in the generated model but required by API)
        backfill_body.additional_properties["devices"] = []

        # Call the backfill API
        backfill_response = create_4.sync_detailed(
            client=billing_event_client,
            body=backfill_body,
        )

        if backfill_response.status_code != 200:
            error_body = backfill_response.content.decode('utf-8') if backfill_response.content else "(no body)"
            raise Exception(
                f"Failed to backfill {agreement_type} acceptance for merchant {merchant_uuid}: "
                f"HTTP {backfill_response.status_code}\n{error_body}"
            )

        # Now fetch the acceptance from the agreement API to return the proper object
        acceptance = self.has_merchant_accepted(merchant_uuid, agreement_type)
        if not acceptance:
            raise Exception(
                f"Backfill succeeded but could not find {agreement_type} acceptance for merchant {merchant_uuid}"
            )

        return acceptance

    def wait_for_acceptance_propagation(
        self,
        rhizome_client: RhizomeClient,
        merchant_uuid: str,
        agreement_type: str = "BILLING",
        max_retries: int = 10,
        retry_delay: float = 1.0,
    ) -> dict[str, Any] | None:
        """Wait for acceptance to propagate to billing_event.merchant_acceptance.

        Args:
            rhizome_client: Rhizome client for database access
            merchant_uuid: Merchant UUID
            agreement_type: Agreement type (default: "BILLING")
            max_retries: Maximum number of retry attempts (default: 10)
            retry_delay: Delay between retries in seconds (default: 1.0)

        Returns:
            Dictionary with acceptance record data if found, None otherwise
        """
        import time

        from sqlmodel import desc, select

        billing_event_db = BillingEvent(rhizome_client)

        for attempt in range(1, max_retries + 1):
            acceptance_record = billing_event_db.select_first(
                select(BillingEvent.MerchantAcceptance)
                .where(BillingEvent.MerchantAcceptance.merchant_uuid == merchant_uuid)
                .where(BillingEvent.MerchantAcceptance.agreement_type == agreement_type)
                .order_by(desc(BillingEvent.MerchantAcceptance.acceptance_created_datetime)),
                sanitize=False,
            )

            if acceptance_record:
                return {
                    "merchant_uuid": acceptance_record.merchant_uuid,
                    "agreement_type": acceptance_record.agreement_type,
                    "agreement_id": str(acceptance_record.agreement_id),
                    "acceptance_created_datetime": acceptance_record.acceptance_created_datetime,
                    "created_timestamp": acceptance_record.created_timestamp,
                }

            if attempt < max_retries:
                time.sleep(retry_delay)

        return None
