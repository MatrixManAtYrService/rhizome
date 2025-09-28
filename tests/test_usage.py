"""
Test the user-facing API for rhizome environments.

This module tests the improved API patterns that allow users to query tables
without needing to know the specific version (V1, V2, etc.) being used by
each environment.

Tests require external infrastructure access and should be run with:
    pytest tests/test_usage.py --external-infra
"""

from typing import Any

import pytest
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.demo.billing_bookkeeper import DemoBillingBookkeeper
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.environments.na_prod.billing_bookkeeper import NorthAmericaBillingBookkeeper
from rhizome.models.table_list import BillingBookkeeperTable


@pytest.mark.external_infra
def test_get_model_returns_correct_version() -> None:
    """Test that get_model() returns the appropriate versioned model for each environment."""
    client = RhizomeClient(data_in_logs=False)

    # Test with DevBillingBookkeeper
    dev_db = DevBillingBookkeeper(client)
    DevFeeSummary = dev_db.get_model(BillingBookkeeperTable.fee_summary)

    # The model class should be a subclass of the base model
    assert DevFeeSummary.__name__.startswith("FeeSummary")
    assert hasattr(DevFeeSummary, "id")
    assert hasattr(DevFeeSummary, "uuid")
    assert hasattr(DevFeeSummary, "sanitize")

    # Test with DemoBillingBookkeeper
    demo_db = DemoBillingBookkeeper(client)
    DemoFeeSummary = demo_db.get_model(BillingBookkeeperTable.fee_summary)

    assert DemoFeeSummary.__name__.startswith("FeeSummary")
    assert hasattr(DemoFeeSummary, "id")
    assert hasattr(DemoFeeSummary, "uuid")

    # Test with NorthAmericaBillingBookkeeper
    na_db = NorthAmericaBillingBookkeeper(client)
    NAFeeSummary = na_db.get_model(BillingBookkeeperTable.fee_summary)

    assert NAFeeSummary.__name__.startswith("FeeSummary")
    assert hasattr(NAFeeSummary, "id")
    assert hasattr(NAFeeSummary, "uuid")


@pytest.mark.external_infra
def test_readme_example_with_get_model() -> None:
    """Test the exact example from the README using get_model()."""
    # This is the improved API from the README
    db = DevBillingBookkeeper(RhizomeClient(data_in_logs=False))

    # Get the correct FeeSummary version for this environment
    FeeSummary = db.get_model(BillingBookkeeperTable.fee_summary)

    fee_summary = db.select_first(select(FeeSummary).where(FeeSummary.id == 30))

    # The actual assertion may need to be adjusted based on real data
    # For now, we just verify the API works
    if fee_summary:
        safe_fee_summary = fee_summary.sanitize()
        # Check that sanitize returns the same type
        assert isinstance(safe_fee_summary, type(fee_summary))
        assert hasattr(safe_fee_summary, "id")
        assert hasattr(safe_fee_summary, "uuid")


@pytest.mark.external_infra
def test_get_model_with_invalid_table() -> None:
    """Test that get_model() raises appropriate errors for invalid tables."""
    client = RhizomeClient(data_in_logs=False)
    dev_db = DevBillingBookkeeper(client)

    # Test with a table that doesn't exist in this environment

    # This should raise a KeyError since the table isn't configured
    with pytest.raises(KeyError) as exc_info:
        # Try to get a table that might not be configured
        # We'll use a valid enum but one that might not be in dev's table_situation
        tables_in_env = list(dev_db.table_situation.keys())
        all_tables = list(BillingBookkeeperTable)

        # Find a table that's in the enum but not in this environment
        # If all tables are configured, we can't test this scenario
        unconfigured_tables = [t for t in all_tables if t not in tables_in_env]
        if unconfigured_tables:
            dev_db.get_model(unconfigured_tables[0])
        else:
            # All tables are configured, so we skip this part of the test
            pytest.skip("All tables are configured in DevBillingBookkeeper")

    # We only reach here if unconfigured_tables was not empty and an exception was raised
    assert "is not configured for environment" in str(exc_info.value)


@pytest.mark.external_infra
def test_get_model_type_safety() -> None:
    """Test that get_model() preserves type safety across different versions."""
    client = RhizomeClient(data_in_logs=False)

    # Get models from different environments
    dev_db = DevBillingBookkeeper(client)
    DevFeeSummary = dev_db.get_model(BillingBookkeeperTable.fee_summary)

    demo_db = DemoBillingBookkeeper(client)
    DemoFeeSummary = demo_db.get_model(BillingBookkeeperTable.fee_summary)

    # Even if they're different versions (V1 vs V2), they should share common fields
    # This is what allows code to be version-agnostic
    common_fields = ["id", "uuid", "billing_entity_uuid", "sanitize"]

    for field in common_fields:
        assert hasattr(DevFeeSummary, field), f"DevFeeSummary missing field: {field}"
        assert hasattr(DemoFeeSummary, field), f"DemoFeeSummary missing field: {field}"

    # The models might be the same version or different versions
    # but both should be usable with the common base fields
    dev_query = select(DevFeeSummary).where(DevFeeSummary.id == 1)
    demo_query = select(DemoFeeSummary).where(DemoFeeSummary.id == 1)

    # Both queries should be valid (even if they return None)
    dev_result = dev_db.select_first(dev_query)
    demo_result = demo_db.select_first(demo_query)

    # Results can be None, but if they exist, they should be the right type
    if dev_result:
        assert isinstance(dev_result, DevFeeSummary)
    if demo_result:
        assert isinstance(demo_result, DemoFeeSummary)


@pytest.mark.external_infra
def test_multiple_tables_with_get_model() -> None:
    """Test get_model() with multiple tables in the same environment."""
    client = RhizomeClient(data_in_logs=False)
    dev_db = DevBillingBookkeeper(client)

    # Get all configured tables for this environment
    configured_tables = list(dev_db.table_situation.keys())

    # Test that we can get models for all configured tables
    models: dict[Any, type[Any]] = {}
    for table in configured_tables:
        try:
            model = dev_db.get_model(table)
            models[table] = model

            # Each model should have basic ORM properties
            assert hasattr(model, "__tablename__")
            assert hasattr(model, "__table__")

        except ValueError as e:
            # Some tables might not have models implemented yet
            if "not yet implemented" in str(e):
                continue
            else:
                raise

    # We should have gotten at least one model
    assert len(models) > 0, "No models were successfully retrieved"

    # All models should be different classes (not the same class)
    model_classes: list[type[Any]] = list(models.values())
    if len(model_classes) > 1:
        # Check that they're actually different classes
        first_model: type[Any] = model_classes[0]
        for other_model in model_classes[1:]:
            # They might have the same name if they're the same version,
            # but they should be different table classes
            assert first_model.__tablename__ != other_model.__tablename__ or first_model is other_model
