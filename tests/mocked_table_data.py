"""
Mocked table data for rhizome tests.

This module contains test data for various database tables and assertion functions
to verify the data structure and sanitization behavior.
"""

import datetime
from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Callable, Type

from rhizome.models.base import SanitizableModel
from rhizome.models.billing_event.app_metered_event import AppMeteredEvent
from rhizome.models.bookkeeper.fee_summary import FeeSummary


def get_mock_fee_summary() -> FeeSummary:
    """Get mock fee summary data based on production record 74347."""
    return FeeSummary(
        id=74347,
        uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        billing_entity_uuid="MERCHANT_UUID_EXAMPLE_123456",
        billing_date=datetime.date(2025, 1, 15),
        fee_category="Processing",
        fee_code="MW63DAWPN6JGY.S",
        currency="USD",
        total_period_units=Decimal("1.0000"),
        abs_period_units=Decimal("1.0000"),
        total_basis_amount=Decimal("9.990"),
        abs_basis_amount=Decimal("9.990"),
        total_fee_amount=Decimal("9.990"),
        fee_rate_uuid="FEE_RATE_UUID_EXAMPLE_789",
        request_uuid="REQUEST_UUID_EXAMPLE_456",
        invoice_info_uuid=None,
        fee_code_ledger_account_uuid=None,
        credit_ledger_account_uuid=None,
        debit_ledger_account_uuid=None,
        exclude_from_invoice=0,
        created_timestamp=datetime.datetime(2025, 1, 15, 10, 30, 0),
        modified_timestamp=datetime.datetime(2025, 1, 15, 10, 30, 0),
    )


def get_mock_dev_app_metered_event() -> AppMeteredEvent:
    """Get mock dev app metered event data based on dev record 1."""
    return AppMeteredEvent(
        id=1,
        uuid="HashHFsoa39Za8PAEn1rYUP7si",
        merchant_uuid="HashEzEYnSWUd",
        developer_app_uuid="Hash64P7p23ti",
        environment="dev::demo2",
        app_metered_uuid="HashAhHuBDAhM",
        count=1,
        basis_amount=None,
        basis_currency=None,
        action_timestamp=datetime.datetime(2024, 4, 29, 0, 0, 0),
        credit_for_trial=1,
        cos_event_uuid="HashFVNjufXJW5qoKCLzRftnr2",
        processed_timestamp=datetime.datetime(2024, 4, 30, 9, 25, 13, 646129),
        billing_event_uuid="HashG46KY3m1y88wg3pc19YuCL",
        created_timestamp=datetime.datetime(2024, 4, 30, 9, 24, 44, 236856),
    )


def get_mock_dev_fee_summary() -> FeeSummary:
    """Get mock dev fee summary data based on dev record 30."""
    return FeeSummary(
        id=30,
        uuid="HashDwRegsuuYDX9RnVzfZport",
        billing_entity_uuid="HashHvx2teX4epSXNfDrrx956N",
        billing_date=datetime.date(2024, 1, 1),
        fee_category="PLAN_RETAIL",
        fee_code="PaymentsPDVT",
        currency="GBP",
        total_period_units=Decimal("3.00"),
        abs_period_units=Decimal("3.00"),
        total_basis_amount=Decimal("0.00"),
        abs_basis_amount=Decimal("0.00"),
        total_fee_amount=Decimal("0.00"),
        fee_rate_uuid="Hash2BtY3zBxDEJzfEUGDRvSLQ",
        request_uuid="HashFZB5xUQ3fZK3Cq5CULKogo",
        invoice_info_uuid=None,
        fee_code_ledger_account_uuid=None,
        credit_ledger_account_uuid=None,
        debit_ledger_account_uuid=None,
        exclude_from_invoice=0,
        created_timestamp=datetime.datetime(2023, 10, 18, 11, 23, 57, 951306),
        modified_timestamp=datetime.datetime(2025, 4, 16, 13, 6, 42, 76246),
    )


def get_mock_demo_app_metered_event() -> AppMeteredEvent:
    """Get mock demo app metered event data based on demo record 1."""
    return AppMeteredEvent(
        id=1,
        uuid="HashHFsoa39Za8PAEn1rYUP7si",
        merchant_uuid="HashEzEYnSWUd",
        developer_app_uuid="Hash64P7p23ti",
        environment="dev::demo2",
        app_metered_uuid="HashAhHuBDAhM",
        count=1,
        basis_amount=None,
        basis_currency=None,
        action_timestamp=datetime.datetime(2024, 4, 29, 0, 0, 0),
        credit_for_trial=1,
        cos_event_uuid="HashFVNjufXJW5qoKCLzRftnr2",
        processed_timestamp=datetime.datetime(2024, 4, 30, 9, 25, 13, 646129),
        billing_event_uuid="HashG46KY3m1y88wg3pc19YuCL",
        created_timestamp=datetime.datetime(2024, 4, 30, 9, 24, 44, 236856),
    )


def get_mock_demo_fee_summary() -> FeeSummary:
    """Get mock demo fee summary data based on demo record 30."""
    return FeeSummary(
        id=30,
        uuid="HashDwRegsuuYDX9RnVzfZport",
        billing_entity_uuid="HashHvx2teX4epSXNfDrrx956N",
        billing_date=datetime.date(2024, 1, 1),
        fee_category="PLAN_RETAIL",
        fee_code="PaymentsPDVT",
        currency="GBP",
        total_period_units=Decimal("3.00"),
        abs_period_units=Decimal("3.00"),
        total_basis_amount=Decimal("0.00"),
        abs_basis_amount=Decimal("0.00"),
        total_fee_amount=Decimal("0.00"),
        fee_rate_uuid="Hash2BtY3zBxDEJzfEUGDRvSLQ",
        request_uuid="HashFZB5xUQ3fZK3Cq5CULKogo",
        invoice_info_uuid=None,
        fee_code_ledger_account_uuid=None,
        credit_ledger_account_uuid=None,
        debit_ledger_account_uuid=None,
        exclude_from_invoice=0,
        created_timestamp=datetime.datetime(2023, 10, 18, 11, 23, 57, 951306),
        modified_timestamp=datetime.datetime(2025, 4, 29, 11, 20, 37, 501474),
    )


def get_mock_app_metered_event() -> AppMeteredEvent:
    """Get mock app metered event data based on production record 883 (sanitized)."""
    return AppMeteredEvent(
        id=883,
        uuid="Hash9V77timzh69Cy55VSsAXFV",
        merchant_uuid="HashFmpNZhreq",
        developer_app_uuid="HashFv1WBub7L",
        environment="usprod",
        app_metered_uuid="Hash21BKibhdo",
        count=1,
        basis_amount=None,
        basis_currency=None,
        action_timestamp=datetime.datetime(2025, 3, 1, 0, 0, 0),
        credit_for_trial=0,
        cos_event_uuid="HashEPRtjibFj8CaujQBHauc15",
        processed_timestamp=datetime.datetime(2025, 3, 6, 15, 30, 39, 97506),
        billing_event_uuid="HashBDe5zJnGpuZJ8HqUyjYpmM",
        created_timestamp=datetime.datetime(2025, 3, 3, 16, 3, 28, 240163),
    )


def assert_fee_summary(actual: FeeSummary, expected: FeeSummary) -> None:
    """Assert that actual fee summary matches expected sanitized structure."""
    assert actual is not None, "Fee summary should exist"
    
    # Check that UUID fields are sanitized (hashed)
    assert actual.billing_entity_uuid.startswith("Hash"), "billing_entity_uuid should be sanitized"
    assert actual.uuid.startswith("Hash"), "uuid should be sanitized"
    assert actual.fee_rate_uuid.startswith("Hash"), "fee_rate_uuid should be sanitized"
    assert actual.request_uuid.startswith("Hash"), "request_uuid should be sanitized"
    
    # Check that non-UUID fields match expected values
    assert actual.fee_code == expected.fee_code, f"Expected fee_code {expected.fee_code}, got {actual.fee_code}"
    assert actual.currency == expected.currency, f"Expected currency {expected.currency}, got {actual.currency}"
    assert actual.total_fee_amount == expected.total_fee_amount, f"Expected total_fee_amount {expected.total_fee_amount}, got {actual.total_fee_amount}"
    assert actual.id == expected.id, f"Expected id {expected.id}, got {actual.id}"
    assert actual.fee_category == expected.fee_category, f"Expected fee_category {expected.fee_category}, got {actual.fee_category}"


def assert_app_metered_event(actual: AppMeteredEvent, expected: AppMeteredEvent) -> None:
    """Assert that actual app metered event matches expected sanitized structure."""
    assert actual is not None, "App metered event should exist"
    
    # Check that UUID fields are sanitized (hashed)
    assert actual.uuid.startswith("Hash"), "uuid should be sanitized"
    assert actual.merchant_uuid.startswith("Hash"), "merchant_uuid should be sanitized"
    assert actual.developer_app_uuid.startswith("Hash"), "developer_app_uuid should be sanitized"
    assert actual.app_metered_uuid.startswith("Hash"), "app_metered_uuid should be sanitized"
    if actual.cos_event_uuid:
        assert actual.cos_event_uuid.startswith("Hash"), "cos_event_uuid should be sanitized"
    if actual.billing_event_uuid:
        assert actual.billing_event_uuid.startswith("Hash"), "billing_event_uuid should be sanitized"
    
    # Check that non-UUID fields match expected values
    assert actual.environment == expected.environment, f"Expected environment {expected.environment}, got {actual.environment}"
    assert actual.count == expected.count, f"Expected count {expected.count}, got {actual.count}"
    assert actual.id == expected.id, f"Expected id {expected.id}, got {actual.id}"


@dataclass
class TestDataSpec:
    """Specification for test data including mock generation and assertion."""
    
    model_class: Type[SanitizableModel]
    use_id: int
    get_mock_data: Callable[[], SanitizableModel]
    get_expected_data: Callable[[], SanitizableModel] 
    check_assertions: Callable[[SanitizableModel, SanitizableModel], None]


# Import environment classes for the registry
from rhizome.environments.demo.billing_event import DemoBillingEvent
from rhizome.environments.demo.bookeeper import DemoBookkeeper
from rhizome.environments.dev.billing_event import DevBillingEvent
from rhizome.environments.dev.bookeeper import DevBookkeeper
from rhizome.environments.na_prod.billing_event import NorthAmericaBillingEvent
from rhizome.environments.na_prod.bookeeper import NorthAmericaBookkeeper

# Registry of test data specifications by model class and environment class
TEST_DATA_SPECS: dict[Type[SanitizableModel], dict[Type[Any], TestDataSpec]] = {
    FeeSummary: {
        # For mocked tests, all environments use the same mock data
        NorthAmericaBookkeeper: TestDataSpec(
            model_class=FeeSummary,
            use_id=74347,  # Production record ID
            get_mock_data=get_mock_fee_summary,
            get_expected_data=get_mock_fee_summary,  # Real tests expect production data
            check_assertions=assert_fee_summary,
        ),
        DevBookkeeper: TestDataSpec(
            model_class=FeeSummary,
            use_id=30,  # Dev uses record ID 30
            get_mock_data=get_mock_fee_summary,  # Mocked tests use production mock data
            get_expected_data=get_mock_dev_fee_summary,  # Real tests expect dev data
            check_assertions=assert_fee_summary,
        ),
        DemoBookkeeper: TestDataSpec(
            model_class=FeeSummary,
            use_id=30,  # Demo uses record ID 30
            get_mock_data=get_mock_fee_summary,  # Mocked tests use production mock data
            get_expected_data=get_mock_demo_fee_summary,  # Real tests expect demo-specific data
            check_assertions=assert_fee_summary,
        ),
    },
    AppMeteredEvent: {
        # For mocked tests, all environments use the same mock data
        NorthAmericaBillingEvent: TestDataSpec(
            model_class=AppMeteredEvent, 
            use_id=883,  # Production record ID
            get_mock_data=get_mock_app_metered_event,
            get_expected_data=get_mock_app_metered_event,  # Real tests expect production data
            check_assertions=assert_app_metered_event,
        ),
        DevBillingEvent: TestDataSpec(
            model_class=AppMeteredEvent, 
            use_id=1,  # Dev uses record ID 1
            get_mock_data=get_mock_app_metered_event,  # Mocked tests use production mock data
            get_expected_data=get_mock_dev_app_metered_event,  # Real tests expect dev data
            check_assertions=assert_app_metered_event,
        ),
        DemoBillingEvent: TestDataSpec(
            model_class=AppMeteredEvent, 
            use_id=1,  # Demo uses record ID 1
            get_mock_data=get_mock_app_metered_event,  # Mocked tests use production mock data
            get_expected_data=get_mock_demo_app_metered_event,  # Real tests expect demo-specific data
            check_assertions=assert_app_metered_event,
        ),
    },
}