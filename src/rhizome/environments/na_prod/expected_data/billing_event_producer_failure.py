"""
Expected data for producer_failure table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.producer_failure_v1 import ProducerFailureV1


class ProducerFailureNaProd(Emplacement[ProducerFailureV1]):
    """Expected data for ProducerFailure in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ProducerFailureV1:
        """Get expected producer_failure data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
