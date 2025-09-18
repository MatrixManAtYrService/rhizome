"""
MetaData registry for environment-specific model isolation.

This module provides separate SQLModel registries for different
environment types to avoid table name conflicts when V1 and V2 models
use the same __tablename__.
"""

from __future__ import annotations

from sqlalchemy.orm import registry
from sqlmodel import SQLModel


# Create separate registries for each environment type
na_prod_registry = registry()
dev_demo_registry = registry()


class NaProdSQLModel(SQLModel, registry=na_prod_registry):
    """SQLModel base for na_prod environment models (V1)."""
    pass


class DevDemoSQLModel(SQLModel, registry=dev_demo_registry):
    """SQLModel base for dev/demo environment models (V2)."""
    pass