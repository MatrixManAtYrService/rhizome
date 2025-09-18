"""
Expected data for jobrunr_migrations table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_migrations_v1 import JobrunrMigrationsV1


class JobrunrMigrationsDemo(Emplacement[JobrunrMigrationsV1]):
    """Expected data for JobrunrMigrations in demo environment."""

    @classmethod
    def get_expected(cls) -> JobrunrMigrationsV1:
        """Get expected jobrunr migrations data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )