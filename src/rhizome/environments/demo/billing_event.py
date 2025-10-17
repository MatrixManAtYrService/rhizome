"""
Demo Billing Event environment configuration.

This module provides access to the billing-event database in the
demo cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.environments.demo.expected_data.billing_event_app_metered_event import AppMeteredEventDemo
from rhizome.environments.demo.expected_data.billing_event_app_subscription_current import AppSubscriptionCurrentDemo
from rhizome.environments.demo.expected_data.billing_event_app_subscription_daily import AppSubscriptionDailyDemo
from rhizome.environments.demo.expected_data.billing_event_app_subscription_event import AppSubscriptionEventDemo
from rhizome.environments.demo.expected_data.billing_event_as_of_merchant import AsOfMerchantDemo
from rhizome.environments.demo.expected_data.billing_event_as_of_merchant_device import AsOfMerchantDeviceDemo
from rhizome.environments.demo.expected_data.billing_event_as_of_merchant_plan import AsOfMerchantPlanDemo
from rhizome.environments.demo.expected_data.billing_event_backfill_acceptance import BackfillAcceptanceDemo
from rhizome.environments.demo.expected_data.billing_event_billing_event_history import BillingEventHistoryDemo
from rhizome.environments.demo.expected_data.billing_event_cellular_arrears_acceptances import (
    CellularArrearsAcceptancesDemo,
)
from rhizome.environments.demo.expected_data.billing_event_cellular_billing_arrears_info import (
    CellularBillingArrearsInfoDemo,
)
from rhizome.environments.demo.expected_data.billing_event_consumer_failure import ConsumerFailureDemo
from rhizome.environments.demo.expected_data.billing_event_consumer_failure_history import ConsumerFailureHistoryDemo
from rhizome.environments.demo.expected_data.billing_event_deserializable_failure import DeserializableFailureDemo
from rhizome.environments.demo.expected_data.billing_event_event_filter import EventFilterDemo
from rhizome.environments.demo.expected_data.billing_event_event_ignored import EventIgnoredDemo
from rhizome.environments.demo.expected_data.billing_event_iccid_carrier import IccidCarrierDemo
from rhizome.environments.demo.expected_data.billing_event_job_assassination_contract import (
    JobAssassinationContractDemo,
)
from rhizome.environments.demo.expected_data.billing_event_jobrunr_backgroundjobservers import (
    JobrunrBackgroundjobserversDemo,
)
from rhizome.environments.demo.expected_data.billing_event_jobrunr_jobs import JobrunrJobsDemo
from rhizome.environments.demo.expected_data.billing_event_jobrunr_metadata import JobrunrMetadataDemo
from rhizome.environments.demo.expected_data.billing_event_jobrunr_migrations import JobrunrMigrationsDemo
from rhizome.environments.demo.expected_data.billing_event_jobrunr_recurring_jobs import JobrunrRecurringJobsDemo
from rhizome.environments.demo.expected_data.billing_event_look import LookDemo
from rhizome.environments.demo.expected_data.billing_event_look_data import LookDataDemo
from rhizome.environments.demo.expected_data.billing_event_managed_item import ManagedItemDemo
from rhizome.environments.demo.expected_data.billing_event_merchant_acceptance import MerchantAcceptanceDemo
from rhizome.environments.demo.expected_data.billing_event_merchant_evolution import MerchantEvolutionDemo
from rhizome.environments.demo.expected_data.billing_event_merchant_offboarding import MerchantOffboardingDemo
from rhizome.environments.demo.expected_data.billing_event_merchant_payment import MerchantPaymentDemo
from rhizome.environments.demo.expected_data.billing_event_merchant_payment_history import MerchantPaymentHistoryDemo
from rhizome.environments.demo.expected_data.billing_event_migrated_merchant import MigratedMerchantDemo
from rhizome.environments.demo.expected_data.billing_event_mlc_captured_event import MlcCapturedEventDemo
from rhizome.environments.demo.expected_data.billing_event_pending_event import PendingEventDemo
from rhizome.environments.demo.expected_data.billing_event_plan_billing_latest import PlanBillingLatestDemo
from rhizome.environments.demo.expected_data.billing_event_plan_meta import PlanMetaDemo
from rhizome.environments.demo.expected_data.billing_event_plan_trial import PlanTrialDemo
from rhizome.environments.demo.expected_data.billing_event_producer_failure import ProducerFailureDemo
from rhizome.environments.demo.expected_data.billing_event_producer_failure_history import ProducerFailureHistoryDemo
from rhizome.environments.demo.expected_data.billing_event_server_config import ServerConfigDemo
from rhizome.environments.demo.expected_data.billing_event_test_merchant_criteria import TestMerchantCriteriaDemo
from rhizome.environments.demo.expected_data.billing_event_uninstalled_app import UninstalledAppDemo
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing_event.app_metered_event_v1 import AppMeteredEventV1
from rhizome.models.billing_event.app_subscription_current_v1 import AppSubscriptionCurrentV1
from rhizome.models.billing_event.app_subscription_daily_v1 import AppSubscriptionDailyV1
from rhizome.models.billing_event.app_subscription_event_v1 import AppSubscriptionEventV1
from rhizome.models.billing_event.as_of_merchant_device_v1 import AsOfMerchantDeviceV1
from rhizome.models.billing_event.as_of_merchant_plan_v2 import AsOfMerchantPlanV2
from rhizome.models.billing_event.as_of_merchant_v2 import AsOfMerchantV2
from rhizome.models.billing_event.backfill_acceptance_v1 import BackfillAcceptanceV1
from rhizome.models.billing_event.billing_event_history_v1 import BillingEventHistoryV1
from rhizome.models.billing_event.cellular_arrears_acceptances_v1 import CellularArrearsAcceptancesV1
from rhizome.models.billing_event.cellular_billing_arrears_info_v1 import CellularBillingArrearsInfoV1
from rhizome.models.billing_event.consumer_failure_history_v1 import ConsumerFailureHistoryV1
from rhizome.models.billing_event.consumer_failure_v1 import ConsumerFailureV1
from rhizome.models.billing_event.deserializable_failure_v1 import DeserializableFailureV1
from rhizome.models.billing_event.event_filter_v1 import EventFilterV1
from rhizome.models.billing_event.event_ignored_v1 import EventIgnoredV1
from rhizome.models.billing_event.iccid_carrier_v1 import IccidCarrierV1
from rhizome.models.billing_event.job_assassination_contract_v1 import JobAssassinationContractV1
from rhizome.models.billing_event.jobrunr_backgroundjobservers_v1 import JobrunrBackgroundjobserversV1
from rhizome.models.billing_event.jobrunr_jobs_v1 import JobrunrJobsV1
from rhizome.models.billing_event.jobrunr_metadata_v1 import JobrunrMetadataV1
from rhizome.models.billing_event.jobrunr_migrations_v1 import JobrunrMigrationsV1
from rhizome.models.billing_event.jobrunr_recurring_jobs_v1 import JobrunrRecurringJobsV1
from rhizome.models.billing_event.look_data_v1 import LookDataV1
from rhizome.models.billing_event.look_v1 import LookV1
from rhizome.models.billing_event.managed_item_v1 import ManagedItemV1
from rhizome.models.billing_event.merchant_acceptance_v1 import MerchantAcceptanceV1
from rhizome.models.billing_event.merchant_evolution_v2 import MerchantEvolutionV2
from rhizome.models.billing_event.merchant_offboarding_v1 import MerchantOffboardingV1
from rhizome.models.billing_event.merchant_payment_history_v1 import MerchantPaymentHistoryV1
from rhizome.models.billing_event.merchant_payment_v1 import MerchantPaymentV1
from rhizome.models.billing_event.migrated_merchant_v1 import MigratedMerchantV1
from rhizome.models.billing_event.mlc_captured_event_v1 import MlcCapturedEventV1
from rhizome.models.billing_event.pending_event_v1 import PendingEventV1
from rhizome.models.billing_event.plan_billing_latest_v1 import PlanBillingLatestV1
from rhizome.models.billing_event.plan_meta_v1 import PlanMetaV1
from rhizome.models.billing_event.plan_trial_v1 import PlanTrialV1
from rhizome.models.billing_event.producer_failure_history_v1 import ProducerFailureHistoryV1
from rhizome.models.billing_event.producer_failure_v1 import ProducerFailureV1
from rhizome.models.billing_event.server_config_v1 import ServerConfigV1
from rhizome.models.billing_event.test_merchant_criteria_v1 import TestMerchantCriteriaV1
from rhizome.models.billing_event.uninstalled_app_v1 import UninstalledAppV1
from rhizome.models.table_list import BillingEventTable

models: dict[BillingEventTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]]]] = {
    BillingEventTable.app_metered_event: (AppMeteredEventV1, AppMeteredEventDemo),
    BillingEventTable.app_subscription_current: (AppSubscriptionCurrentV1, AppSubscriptionCurrentDemo),
    BillingEventTable.app_subscription_daily: (AppSubscriptionDailyV1, AppSubscriptionDailyDemo),
    BillingEventTable.app_subscription_event: (AppSubscriptionEventV1, AppSubscriptionEventDemo),
    BillingEventTable.as_of_merchant: (AsOfMerchantV2, AsOfMerchantDemo),
    BillingEventTable.as_of_merchant_device: (AsOfMerchantDeviceV1, AsOfMerchantDeviceDemo),
    BillingEventTable.as_of_merchant_plan: (AsOfMerchantPlanV2, AsOfMerchantPlanDemo),
    BillingEventTable.backfill_acceptance: (BackfillAcceptanceV1, BackfillAcceptanceDemo),
    BillingEventTable.billing_event_history: (BillingEventHistoryV1, BillingEventHistoryDemo),
    BillingEventTable.cellular_arrears_acceptances: (CellularArrearsAcceptancesV1, CellularArrearsAcceptancesDemo),
    BillingEventTable.cellular_billing_arrears_info: (CellularBillingArrearsInfoV1, CellularBillingArrearsInfoDemo),
    BillingEventTable.consumer_failure: (ConsumerFailureV1, ConsumerFailureDemo),
    BillingEventTable.consumer_failure_history: (ConsumerFailureHistoryV1, ConsumerFailureHistoryDemo),
    BillingEventTable.deserializable_failure: (DeserializableFailureV1, DeserializableFailureDemo),
    BillingEventTable.event_filter: (EventFilterV1, EventFilterDemo),
    BillingEventTable.event_ignored: (EventIgnoredV1, EventIgnoredDemo),
    BillingEventTable.iccid_carrier: (IccidCarrierV1, IccidCarrierDemo),
    BillingEventTable.job_assassination_contract: (JobAssassinationContractV1, JobAssassinationContractDemo),
    BillingEventTable.jobrunr_backgroundjobservers: (JobrunrBackgroundjobserversV1, JobrunrBackgroundjobserversDemo),
    BillingEventTable.jobrunr_jobs: (JobrunrJobsV1, JobrunrJobsDemo),
    BillingEventTable.jobrunr_metadata: (JobrunrMetadataV1, JobrunrMetadataDemo),
    BillingEventTable.jobrunr_migrations: (JobrunrMigrationsV1, JobrunrMigrationsDemo),
    BillingEventTable.jobrunr_recurring_jobs: (JobrunrRecurringJobsV1, JobrunrRecurringJobsDemo),
    BillingEventTable.look: (LookV1, LookDemo),
    BillingEventTable.look_data: (LookDataV1, LookDataDemo),
    BillingEventTable.managed_item: (ManagedItemV1, ManagedItemDemo),
    BillingEventTable.merchant_acceptance: (MerchantAcceptanceV1, MerchantAcceptanceDemo),
    BillingEventTable.merchant_evolution: (MerchantEvolutionV2, MerchantEvolutionDemo),
    BillingEventTable.merchant_offboarding: (MerchantOffboardingV1, MerchantOffboardingDemo),
    BillingEventTable.merchant_payment: (MerchantPaymentV1, MerchantPaymentDemo),
    BillingEventTable.merchant_payment_history: (MerchantPaymentHistoryV1, MerchantPaymentHistoryDemo),
    BillingEventTable.migrated_merchant: (MigratedMerchantV1, MigratedMerchantDemo),
    BillingEventTable.mlc_captured_event: (MlcCapturedEventV1, MlcCapturedEventDemo),
    BillingEventTable.pending_event: (PendingEventV1, PendingEventDemo),
    BillingEventTable.plan_billing_latest: (PlanBillingLatestV1, PlanBillingLatestDemo),
    BillingEventTable.plan_meta: (PlanMetaV1, PlanMetaDemo),
    BillingEventTable.plan_trial: (PlanTrialV1, PlanTrialDemo),
    BillingEventTable.producer_failure: (ProducerFailureV1, ProducerFailureDemo),
    BillingEventTable.producer_failure_history: (ProducerFailureHistoryV1, ProducerFailureHistoryDemo),
    BillingEventTable.server_config: (ServerConfigV1, ServerConfigDemo),
    BillingEventTable.test_merchant_criteria: (TestMerchantCriteriaV1, TestMerchantCriteriaDemo),
    BillingEventTable.uninstalled_app: (UninstalledAppV1, UninstalledAppDemo),
}


class DemoBillingEvent(Environment):
    """Demo billing event environment using CloudSQL."""

    # Type aliases for environment-specific model versions
    AppMeteredEvent: type[AppMeteredEventV1] = AppMeteredEventV1
    AppSubscriptionCurrent: type[AppSubscriptionCurrentV1] = AppSubscriptionCurrentV1
    AppSubscriptionDaily: type[AppSubscriptionDailyV1] = AppSubscriptionDailyV1
    AppSubscriptionEvent: type[AppSubscriptionEventV1] = AppSubscriptionEventV1
    AsOfMerchant: type[AsOfMerchantV2] = AsOfMerchantV2
    AsOfMerchantDevice: type[AsOfMerchantDeviceV1] = AsOfMerchantDeviceV1
    AsOfMerchantPlan: type[AsOfMerchantPlanV2] = AsOfMerchantPlanV2
    BackfillAcceptance: type[BackfillAcceptanceV1] = BackfillAcceptanceV1
    BillingEventHistory: type[BillingEventHistoryV1] = BillingEventHistoryV1
    CellularArrearsAcceptances: type[CellularArrearsAcceptancesV1] = CellularArrearsAcceptancesV1
    CellularBillingArrearsInfo: type[CellularBillingArrearsInfoV1] = CellularBillingArrearsInfoV1
    ConsumerFailure: type[ConsumerFailureV1] = ConsumerFailureV1
    ConsumerFailureHistory: type[ConsumerFailureHistoryV1] = ConsumerFailureHistoryV1
    DeserializableFailure: type[DeserializableFailureV1] = DeserializableFailureV1
    EventFilter: type[EventFilterV1] = EventFilterV1
    EventIgnored: type[EventIgnoredV1] = EventIgnoredV1
    IccidCarrier: type[IccidCarrierV1] = IccidCarrierV1
    JobAssassinationContract: type[JobAssassinationContractV1] = JobAssassinationContractV1
    JobrunrBackgroundjobservers: type[JobrunrBackgroundjobserversV1] = JobrunrBackgroundjobserversV1
    JobrunrJobs: type[JobrunrJobsV1] = JobrunrJobsV1
    JobrunrMetadata: type[JobrunrMetadataV1] = JobrunrMetadataV1
    JobrunrMigrations: type[JobrunrMigrationsV1] = JobrunrMigrationsV1
    JobrunrRecurringJobs: type[JobrunrRecurringJobsV1] = JobrunrRecurringJobsV1
    Look: type[LookV1] = LookV1
    LookData: type[LookDataV1] = LookDataV1
    ManagedItem: type[ManagedItemV1] = ManagedItemV1
    MerchantAcceptance: type[MerchantAcceptanceV1] = MerchantAcceptanceV1
    MerchantEvolution: type[MerchantEvolutionV2] = MerchantEvolutionV2
    MerchantOffboarding: type[MerchantOffboardingV1] = MerchantOffboardingV1
    MerchantPayment: type[MerchantPaymentV1] = MerchantPaymentV1
    MerchantPaymentHistory: type[MerchantPaymentHistoryV1] = MerchantPaymentHistoryV1
    MigratedMerchant: type[MigratedMerchantV1] = MigratedMerchantV1
    MlcCapturedEvent: type[MlcCapturedEventV1] = MlcCapturedEventV1
    PendingEvent: type[PendingEventV1] = PendingEventV1
    PlanBillingLatest: type[PlanBillingLatestV1] = PlanBillingLatestV1
    PlanMeta: type[PlanMetaV1] = PlanMetaV1
    PlanTrial: type[PlanTrialV1] = PlanTrialV1
    ProducerFailure: type[ProducerFailureV1] = ProducerFailureV1
    ProducerFailureHistory: type[ProducerFailureHistoryV1] = ProducerFailureHistoryV1
    ServerConfig: type[ServerConfigV1] = ServerConfigV1
    TestMerchantCriteria: type[TestMerchantCriteriaV1] = TestMerchantCriteriaV1
    UninstalledApp: type[UninstalledAppV1] = UninstalledAppV1

    def tables(self) -> list[StrEnum]:
        return list(BillingEventTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        if not isinstance(table_name, BillingEventTable):
            raise ValueError(f"Expected BillingEventTable, got {type(table_name)}")
        model_class, emplacement_class = models[table_name]
        if model_class is None:
            raise NotImplementedError(f"Model class for {table_name} not yet implemented")
        return model_class, emplacement_class

    def get_port_forward_config(self) -> PortForwardConfig:
        """Get port forwarding configuration for demo environment."""
        return PortForwardConfig(
            project="clover-dev-kubernetes",
            cluster="dev-us-west1-cluster",
            region="us-west1",
            server="https://dev-us-west1-ingress-nginx.dev.pdx13.clover.network",
            kube_context="gke_clover-dev-kubernetes_us-west1_dev-us-west1-cluster",
            kube_namespace="gke-cloudsql-access",
            kube_deployment="gke-cloudsql-access",
            sql_connection="clover-dev-managed:us-west1:billing-event-demo2",
            database_name="billing-event-dev",
            username="billing-event",
            secret_reference="op://Shared/EventBillingROCred-dev/password",
            secret_manager=SecretManager.ONEPASSWORD,
        )

    def get_database_config(self) -> DatabaseConfig:
        """Get database configuration using port forwarding."""
        port_forward_config = self.get_port_forward_config()
        return self.get_database_config_from_port_forward(port_forward_config)

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "DemoBillingEvent"

    @classmethod
    def database_id(cls) -> str:
        """Database identifier for server-side query execution."""
        return "demo_billing_event"
