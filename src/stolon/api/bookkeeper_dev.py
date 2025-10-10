"""Billing Bookkeeper API methods for Dev environment."""

from typing import TYPE_CHECKING, Any, Unpack

if TYPE_CHECKING:
    from stolon.client import StolonClient
    from stolon.environments.base import HttpxKwargs


class BookkeeperDev:
    """
    Mixin providing billing-bookkeeper API methods for Dev environment.

    This mixin uses the generated OpenAPI client for the billing-bookkeeper service.
    To generate/update the client, run:
        stolon sync spec --env dev --service billing-bookkeeper
    """

    client: "StolonClient"

    def get(self, path: str, **kwargs: Unpack["HttpxKwargs"]) -> dict[str, Any] | list[Any] | None:
        """Abstract method - must be implemented by the environment class."""
        raise NotImplementedError("Environment must implement get() method")

    def post(self, path: str, **kwargs: Unpack["HttpxKwargs"]) -> dict[str, Any] | list[Any] | None:
        """Abstract method - must be implemented by the environment class."""
        raise NotImplementedError("Environment must implement post() method")

    # Example method - you can add more methods that use the generated client
    # Once the client is generated, you'll be able to import and use it here
    # For example:
    #
    # def get_fee_summary(self, fee_summary_id: int) -> dict[str, Any]:
    #     """Get fee summary by ID."""
    #     return self.get(f"/v3/billing-bookkeeper/fee-summaries/{fee_summary_id}")
