"""Dev environment HTTP API access."""

from stolon.api import BillingEventDev, BookkeeperDev, MerchantAPI
from stolon.environments.base import Environment


class DevHttp(Environment, MerchantAPI, BookkeeperDev, BillingEventDev):
    """Dev environment HTTP API access."""

    @property
    def name(self) -> str:
        return "dev"

    @property
    def domain(self) -> str:
        return "dev1.dev.clover.com"
