"""
Table lists for all rhizome databases.

This module defines all tables tracked across different databases
and environments in rhizome.
"""

from __future__ import annotations

from enum import StrEnum, auto


class BillingTable(StrEnum):
    """Table identifiers for billing database."""

    stage_charge = auto()


class BillingBookkeeperTable(StrEnum):
    """Table identifiers for billing_bookkeeper database."""

    billing_entity = auto()
    fee_rate = auto()
    fee_summary = auto()
    invoice_info = auto()
    settlement = auto()


class BillingEventTable(StrEnum):
    """Table identifiers for billing_event database."""

    app_metered_event = auto()
    app_subscription_current = auto()
    app_subscription_daily = auto()
    app_subscription_event = auto()
    as_of_merchant = auto()
    as_of_merchant_device = auto()
    as_of_merchant_plan = auto()
    backfill_acceptance = auto()
    billing_event_history = auto()
    cellular_arrears_acceptances = auto()
    cellular_billing_arrears_info = auto()
    consumer_failure = auto()
    consumer_failure_history = auto()
    deserializable_failure = auto()
    event_filter = auto()
    event_ignored = auto()
    iccid_carrier = auto()
    job_assassination_contract = auto()
    jobrunr_backgroundjobservers = auto()
    jobrunr_jobs = auto()
    jobrunr_metadata = auto()
    jobrunr_migrations = auto()
    jobrunr_recurring_jobs = auto()
    look = auto()
    look_data = auto()
    managed_item = auto()
    merchant_acceptance = auto()
    merchant_evolution = auto()
    merchant_offboarding = auto()
    merchant_payment = auto()
    merchant_payment_history = auto()
    migrated_merchant = auto()
    mlc_captured_event = auto()
    pending_event = auto()
    plan_billing_latest = auto()
    plan_meta = auto()
    plan_trial = auto()
    producer_failure = auto()
    producer_failure_history = auto()
    server_config = auto()
    test_merchant_criteria = auto()
    uninstalled_app = auto()


class MetaTable(StrEnum):
    """Table identifiers for the meta database."""

    account = auto()
    country = auto()
    device_type = auto()
    server_feature = auto()
    merchant = auto()
    terminal_config_merchant_props = auto()
    reseller = auto()
    merchant_address = auto()
    merchant_gateway = auto()
    payment_processor = auto()
    processor_key = auto()
    merchant_plan = auto()
    app_bundle = auto()
    app_app_bundle = auto()
    merchant_plan_merchant_plan_group = auto()
    merchant_plan_group = auto()
    merchant_role = auto()
    locale = auto()
    timezones = auto()
    merchant_boarding = auto()
    merchant_creation_details = auto()
    device_provision = auto()
    device_events = auto()
    merchant_merchant_plan_history = auto()
    reseller_plan_trial = auto()
    merchant_app_subscription_history = auto()
    merchant_app = auto()
    developer_app = auto()
    app_permission = auto()
    developer = auto()
    app_subscription = auto()
    app_subscription_country = auto()
    app_metered_event = auto()
    app_metered = auto()
    app_metered_country = auto()
