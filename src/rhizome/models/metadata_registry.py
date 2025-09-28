"""
MetaData registry for database and environment-specific model isolation.

This module provides separate SQLModel registries for different
databases and environment types to avoid table name conflicts when
different databases have tables with the same name, or when V1 and V2
models use the same __tablename__.
"""

from __future__ import annotations

from sqlalchemy.orm import registry
from sqlmodel import SQLModel

# Create separate registries for each database
billing_registry = registry()
billing_event_registry = registry()
billing_bookkeeper_registry = registry()
meta_registry = registry()

# Environment-specific registries for schema versioning
na_prod_registry = registry()
dev_demo_registry = registry()


class BillingSQLModel(SQLModel, registry=billing_registry):
    """SQLModel base for billing database models."""

    pass


class BillingEventSQLModel(SQLModel, registry=billing_event_registry):
    """SQLModel base for billing_event database models."""

    pass


class BillingBookkeeperSQLModel(SQLModel, registry=billing_bookkeeper_registry):
    """SQLModel base for billing_bookkeeper database models."""

    pass


class MetaSQLModel(SQLModel, registry=meta_registry):
    """SQLModel base for meta database models."""

    pass


class NaProdSQLModel(SQLModel, registry=na_prod_registry):
    """SQLModel base for na_prod environment models (V1)."""

    pass


class DevDemoSQLModel(SQLModel, registry=dev_demo_registry):
    """SQLModel base for dev/demo environment models (V2)."""

    pass
