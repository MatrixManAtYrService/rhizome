"""billing_event database models."""

from .app_metered_event import AppMeteredEvent
from .app_metered_event_v1 import AppMeteredEventV1
from .app_subscription_current import AppSubscriptionCurrent
from .app_subscription_current_v1 import AppSubscriptionCurrentV1
from .app_subscription_daily import AppSubscriptionDaily
from .app_subscription_daily_v1 import AppSubscriptionDailyV1
from .as_of_merchant import AsOfMerchant
# Note: V1 and V2 are imported directly by environment files to avoid table conflicts
# from .as_of_merchant_v1 import AsOfMerchantV1
# from .as_of_merchant_v2 import AsOfMerchantV2
from .as_of_merchant_device import AsOfMerchantDevice
from .as_of_merchant_device_v1 import AsOfMerchantDeviceV1
from .as_of_merchant_plan import AsOfMerchantPlan
# Note: V1 and V2 are imported directly by environment files to avoid table conflicts
# from .as_of_merchant_plan_v1 import AsOfMerchantPlanV1
# from .as_of_merchant_plan_v2 import AsOfMerchantPlanV2
from .backfill_acceptance import BackfillAcceptance
from .backfill_acceptance_v1 import BackfillAcceptanceV1
from .billing_event_history import BillingEventHistory
from .billing_event_history_v1 import BillingEventHistoryV1
from .cellular_arrears_acceptances import CellularArrearsAcceptances
from .cellular_arrears_acceptances_v1 import CellularArrearsAcceptancesV1
from .cellular_billing_arrears_info import CellularBillingArrearsInfo
from .cellular_billing_arrears_info_v1 import CellularBillingArrearsInfoV1
from .consumer_failure import ConsumerFailure
from .consumer_failure_v1 import ConsumerFailureV1
from .consumer_failure_history import ConsumerFailureHistory
from .consumer_failure_history_v1 import ConsumerFailureHistoryV1
from .deserializable_failure import DeserializableFailure
from .deserializable_failure_v1 import DeserializableFailureV1
from .event_filter import EventFilter
from .event_filter_v1 import EventFilterV1
from .event_ignored import EventIgnored
from .event_ignored_v1 import EventIgnoredV1
from .iccid_carrier import IccidCarrier
from .iccid_carrier_v1 import IccidCarrierV1
from .job_assassination_contract import JobAssassinationContract
from .job_assassination_contract_v1 import JobAssassinationContractV1
from .jobrunr_backgroundjobservers import JobrunrBackgroundjobservers
from .jobrunr_backgroundjobservers_v1 import JobrunrBackgroundjobserversV1
from .jobrunr_jobs import JobrunrJobs
from .jobrunr_jobs_v1 import JobrunrJobsV1
from .jobrunr_metadata import JobrunrMetadata
from .jobrunr_metadata_v1 import JobrunrMetadataV1
from .jobrunr_migrations import JobrunrMigrations
from .jobrunr_migrations_v1 import JobrunrMigrationsV1
from .jobrunr_recurring_jobs import JobrunrRecurringJobs
from .jobrunr_recurring_jobs_v1 import JobrunrRecurringJobsV1
from .look import Look
from .look_v1 import LookV1
from .look_data import LookData
from .look_data_v1 import LookDataV1
from .managed_item import ManagedItem
from .managed_item_v1 import ManagedItemV1
from .merchant_acceptance import MerchantAcceptance
from .merchant_acceptance_v1 import MerchantAcceptanceV1
from .merchant_evolution import MerchantEvolution
# Note: V1 and V2 are imported directly by environment files to avoid table conflicts
# from .merchant_evolution_v1 import MerchantEvolutionV1
# from .merchant_evolution_v2 import MerchantEvolutionV2
from .merchant_offboarding import MerchantOffboarding
from .merchant_offboarding_v1 import MerchantOffboardingV1
from .mlc_captured_event import MlcCapturedEvent
from .mlc_captured_event_v1 import MlcCapturedEventV1
from .merchant_payment import MerchantPayment
from .merchant_payment_v1 import MerchantPaymentV1
from .merchant_payment_history import MerchantPaymentHistory
from .merchant_payment_history_v1 import MerchantPaymentHistoryV1
from .migrated_merchant import MigratedMerchant
from .migrated_merchant_v1 import MigratedMerchantV1
from .pending_event import PendingEvent
from .pending_event_v1 import PendingEventV1
from .plan_billing_latest import PlanBillingLatest
from .plan_billing_latest_v1 import PlanBillingLatestV1
from .plan_meta import PlanMeta
from .plan_meta_v1 import PlanMetaV1
from .plan_trial import PlanTrial
from .plan_trial_v1 import PlanTrialV1
from .producer_failure import ProducerFailure
from .producer_failure_v1 import ProducerFailureV1
from .producer_failure_history import ProducerFailureHistory
from .producer_failure_history_v1 import ProducerFailureHistoryV1
from .server_config import ServerConfig
from .server_config_v1 import ServerConfigV1
from .test_merchant_criteria import TestMerchantCriteria
from .test_merchant_criteria_v1 import TestMerchantCriteriaV1
from .uninstalled_app import UninstalledApp
from .uninstalled_app_v1 import UninstalledAppV1

__all__ = [
    "AppMeteredEvent", "AppMeteredEventV1",
    "AppSubscriptionCurrent", "AppSubscriptionCurrentV1",
    "AppSubscriptionDaily", "AppSubscriptionDailyV1",
    "AsOfMerchant",  # V1/V2 imported directly by environments
    "AsOfMerchantDevice", "AsOfMerchantDeviceV1",
    "AsOfMerchantPlan",  # V1/V2 imported directly by environments
    "BackfillAcceptance", "BackfillAcceptanceV1",
    "BillingEventHistory", "BillingEventHistoryV1",
    "CellularArrearsAcceptances", "CellularArrearsAcceptancesV1",
    "CellularBillingArrearsInfo", "CellularBillingArrearsInfoV1",
    "ConsumerFailure", "ConsumerFailureV1",
    "ConsumerFailureHistory", "ConsumerFailureHistoryV1",
    "DeserializableFailure", "DeserializableFailureV1",
    "EventFilter", "EventFilterV1",
    "EventIgnored", "EventIgnoredV1",
    "IccidCarrier", "IccidCarrierV1",
    "JobAssassinationContract", "JobAssassinationContractV1",
    "JobrunrBackgroundjobservers", "JobrunrBackgroundjobserversV1",
    "JobrunrJobs", "JobrunrJobsV1",
    "JobrunrMetadata", "JobrunrMetadataV1",
    "JobrunrMigrations", "JobrunrMigrationsV1",
    "JobrunrRecurringJobs", "JobrunrRecurringJobsV1",
    "Look", "LookV1",
    "LookData", "LookDataV1",
    "ManagedItem", "ManagedItemV1",
    "MerchantAcceptance", "MerchantAcceptanceV1",
    "MerchantEvolution",
    "MerchantOffboarding", "MerchantOffboardingV1",
    "MerchantPayment", "MerchantPaymentV1",
    "MerchantPaymentHistory", "MerchantPaymentHistoryV1",
    "MigratedMerchant", "MigratedMerchantV1",
    "MlcCapturedEvent", "MlcCapturedEventV1",
    "PendingEvent", "PendingEventV1",
    "PlanBillingLatest", "PlanBillingLatestV1",
    "PlanMeta", "PlanMetaV1",
    "PlanTrial", "PlanTrialV1",
    "ProducerFailure", "ProducerFailureV1",
    "ProducerFailureHistory", "ProducerFailureHistoryV1",
    "ServerConfig", "ServerConfigV1",
    "TestMerchantCriteria", "TestMerchantCriteriaV1",
    "UninstalledApp", "UninstalledAppV1"
]
