"""Merchant API methods for Clover environments."""

from typing import TYPE_CHECKING, Any, Unpack

if TYPE_CHECKING:
    from stolon.environments.base import HttpxKwargs


class MerchantAPI:
    """Mixin providing merchant-related API methods."""

    def get(self, path: str, **kwargs: Unpack["HttpxKwargs"]) -> dict[str, Any] | list[Any] | None:
        """Abstract method - must be implemented by the environment class."""
        raise NotImplementedError("Environment must implement get() method")

    def get_merchant_name(self, merchant_id: str) -> str:
        """
        Get merchant name from merchant ID.

        Args:
            merchant_id: Merchant ID (e.g., 'MSR15REPHS0N5')

        Returns:
            Merchant name

        Raises:
            ValueError: If the API response is invalid or missing the name field
        """
        data = self.get(f"/v3/merchants/{merchant_id}")
        if not isinstance(data, dict):
            raise ValueError(f"Expected dict response from merchant API, got {type(data)}")
        name = data.get("name")
        if not isinstance(name, str):
            raise ValueError(f"Expected merchant name to be a string, got {type(name)}")
        return name
