"""
Expected data for producer_failure table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.producer_failure_v1 import ProducerFailureV1


class ProducerFailureDemo(Emplacement[ProducerFailureV1]):
    """Expected data for ProducerFailure in demo environment."""

    @classmethod
    def get_expected(cls) -> ProducerFailureV1:
        """Get expected producer_failure data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
