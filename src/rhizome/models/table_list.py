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
    flyway_schema_history = auto()
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
