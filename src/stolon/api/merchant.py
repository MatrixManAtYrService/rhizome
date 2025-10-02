"""Merchant API methods for Clover environments."""

from typing import Any


class MerchantAPI:
    """Mixin providing merchant-related API methods."""

    def get(self, path: str, **kwargs: Any) -> Any:
        """Abstract method - must be implemented by the environment class."""
        raise NotImplementedError("Environment must implement get() method")

    def get_merchant_name(self, merchant_id: str) -> str:
        """
        Get merchant name from merchant ID.

        Args:
            merchant_id: Merchant ID (e.g., 'MSR15REPHS0N5')

        Returns:
            Merchant name
        """
        data = self.get(f"/v3/merchants/{merchant_id}")
        return data["name"]
