"""Dev environment HTTP API access."""

from stolon.environments.base import Environment


class DevHttp(Environment):
    """Dev environment HTTP API access."""

    @property
    def name(self) -> str:
        return "dev"

    @property
    def domain(self) -> str:
        return "dev1.dev.clover.com"

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
