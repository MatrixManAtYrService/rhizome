"""
North America Production Billing environment configuration.

This module provides access to the North America production billing database
through direct connection using pybritive for temporary credentials.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager, Tools
from rhizome.environments.na_prod.expected_data.billing_app_suppression import AppSuppressionNaProd
from rhizome.environments.na_prod.expected_data.billing_auto_debit_no_auth_config import AutoDebitNoAuthConfigNaProd
from rhizome.environments.na_prod.expected_data.billing_bank_routing import BankRoutingNaProd
from rhizome.environments.na_prod.expected_data.billing_bi_context import BiContextNaProd
from rhizome.environments.na_prod.expected_data.billing_biie_config import BiieConfigNaProd
from rhizome.environments.na_prod.expected_data.billing_biie_file_def import BiieFileDefNaProd
from rhizome.environments.na_prod.expected_data.billing_biie_file_instance import BiieFileInstanceNaProd
from rhizome.environments.na_prod.expected_data.billing_biie_file_instance_request import BiieFileInstanceRequestNaProd
from rhizome.environments.na_prod.expected_data.billing_biie_file_staging_data import BiieFileStagingDataNaProd
from rhizome.environments.na_prod.expected_data.billing_billing_business_initiative import (
    BillingBusinessInitiativeNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_billing_request import BillingRequestNaProd
from rhizome.environments.na_prod.expected_data.billing_billing_request_state import BillingRequestStateNaProd
from rhizome.environments.na_prod.expected_data.billing_charge_capture_error import ChargeCaptureErrorNaProd
from rhizome.environments.na_prod.expected_data.billing_charge_invoice_number import ChargeInvoiceNumberNaProd
from rhizome.environments.na_prod.expected_data.billing_charge_post_date import ChargePostDateNaProd
from rhizome.environments.na_prod.expected_data.billing_charge_state_attempt import ChargeStateAttemptNaProd
from rhizome.environments.na_prod.expected_data.billing_combined_charge import CombinedChargeNaProd
from rhizome.environments.na_prod.expected_data.billing_combined_charge_tree import CombinedChargeTreeNaProd
from rhizome.environments.na_prod.expected_data.billing_combined_disbursement import CombinedDisbursementNaProd
from rhizome.environments.na_prod.expected_data.billing_combined_disbursement_tree import CombinedDisbursementTreeNaProd
from rhizome.environments.na_prod.expected_data.billing_corollary_data import CorollaryDataNaProd
from rhizome.environments.na_prod.expected_data.billing_country_suppression import CountrySuppressionNaProd
from rhizome.environments.na_prod.expected_data.billing_disbursement_invoice_number import (
    DisbursementInvoiceNumberNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_email_audit import EmailAuditNaProd
from rhizome.environments.na_prod.expected_data.billing_email_developer_charge import EmailDeveloperChargeNaProd
from rhizome.environments.na_prod.expected_data.billing_explanation import ExplanationNaProd
from rhizome.environments.na_prod.expected_data.billing_explanation_data import ExplanationDataNaProd
from rhizome.environments.na_prod.expected_data.billing_export_tracker import ExportTrackerNaProd
from rhizome.environments.na_prod.expected_data.billing_fee import FeeNaProd
from rhizome.environments.na_prod.expected_data.billing_fee_exception import FeeExceptionNaProd
from rhizome.environments.na_prod.expected_data.billing_flight_check import FlightCheckNaProd
from rhizome.environments.na_prod.expected_data.billing_flight_check_archive import FlightCheckArchiveNaProd
from rhizome.environments.na_prod.expected_data.billing_flight_check_execution import FlightCheckExecutionNaProd
from rhizome.environments.na_prod.expected_data.billing_invoice_charge import InvoiceChargeNaProd
from rhizome.environments.na_prod.expected_data.billing_job_lock import JobLockNaProd
from rhizome.environments.na_prod.expected_data.billing_merchant_device_info import MerchantDeviceInfoNaProd
from rhizome.environments.na_prod.expected_data.billing_merchant_queue_sensitive import MerchantQueueSensitiveNaProd
from rhizome.environments.na_prod.expected_data.billing_merchant_subscription_action import (
    MerchantSubscriptionActionNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_merchant_suppression import MerchantSuppressionNaProd
from rhizome.environments.na_prod.expected_data.billing_merchant_suppression_by_app import (
    MerchantSuppressionByAppNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_merchant_terms_acceptance import MerchantTermsAcceptanceNaProd
from rhizome.environments.na_prod.expected_data.billing_merchant_terms_acceptance_events import (
    MerchantTermsAcceptanceEventsNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_merchant_terms_acceptance_failed_event_log import (
    MerchantTermsAcceptanceFailedEventLogNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_merchant_terms_missing_acceptance import (
    MerchantTermsMissingAcceptanceNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_offboarding import OffboardingNaProd
from rhizome.environments.na_prod.expected_data.billing_plan_authorization_settings import (
    PlanAuthorizationSettingsNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_plan_meta import PlanMetaNaProd
from rhizome.environments.na_prod.expected_data.billing_plan_meta_history import PlanMetaHistoryNaProd
from rhizome.environments.na_prod.expected_data.billing_producer_failure import ProducerFailureNaProd
from rhizome.environments.na_prod.expected_data.billing_promo import PromoNaProd
from rhizome.environments.na_prod.expected_data.billing_promo_control import PromoControlNaProd
from rhizome.environments.na_prod.expected_data.billing_remit_merchant_details import RemitMerchantDetailsNaProd
from rhizome.environments.na_prod.expected_data.billing_reseller_app_rev_share import ResellerAppRevShareNaProd
from rhizome.environments.na_prod.expected_data.billing_reseller_invoice_alliance import ResellerInvoiceAllianceNaProd
from rhizome.environments.na_prod.expected_data.billing_reseller_plan_fee import ResellerPlanFeeNaProd
from rhizome.environments.na_prod.expected_data.billing_reseller_plan_rev_share import ResellerPlanRevShareNaProd
from rhizome.environments.na_prod.expected_data.billing_reseller_suppression import ResellerSuppressionNaProd
from rhizome.environments.na_prod.expected_data.billing_reseller_usage_job_config import ResellerUsageJobConfigNaProd
from rhizome.environments.na_prod.expected_data.billing_rev_share import RevShareNaProd
from rhizome.environments.na_prod.expected_data.billing_seasonal_reseller_info import SeasonalResellerInfoNaProd
from rhizome.environments.na_prod.expected_data.billing_server_config import ServerConfigNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_app_metered_event import StageAppMeteredEventNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_charge import StageChargeNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_charge_capture_error import StageChargeCaptureErrorNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_charge_history import StageChargeHistoryNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_charge_state_attempt import StageChargeStateAttemptNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_charge_update import StageChargeUpdateNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_email import StageEmailNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_email_merchant_charge import (
    StageEmailMerchantChargeNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_stage_infolease_charge_attempt import (
    StageInfoleaseChargeAttemptNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_stage_infolease_disbursement_attempt import (
    StageInfoleaseDisbursementAttemptNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_stage_merchant_app_charge import StageMerchantAppChargeNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_merchant_plan_charge import StageMerchantPlanChargeNaProd
from rhizome.environments.na_prod.expected_data.billing_stage_vendor_disbursement_error import (
    StageVendorDisbursementErrorNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_stage_vendor_disbursement_state_attempt import (
    StageVendorDisbursementStateAttemptNaProd,
)
from rhizome.environments.na_prod.expected_data.billing_suppression_metrics import SuppressionMetricsNaProd
from rhizome.environments.na_prod.expected_data.billing_vat_vendor_disbursement import VatVendorDisbursementNaProd
from rhizome.environments.na_prod.expected_data.billing_vendor_disbursement_error import VendorDisbursementErrorNaProd
from rhizome.environments.na_prod.expected_data.billing_vendor_disbursement_state_attempt import (
    VendorDisbursementStateAttemptNaProd,
)
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing.app_suppression_v1 import AppSuppressionV1
from rhizome.models.billing.auto_debit_no_auth_config_v1 import AutoDebitNoAuthConfigV1
from rhizome.models.billing.bank_routing_v1 import BankRoutingV1
from rhizome.models.billing.bi_context_v1 import BiContextV1
from rhizome.models.billing.biie_config_v1 import BiieConfigV1
from rhizome.models.billing.biie_file_def_v1 import BiieFileDefV1
from rhizome.models.billing.biie_file_instance_request_v1 import BiieFileInstanceRequestV1
from rhizome.models.billing.biie_file_instance_v1 import BiieFileInstanceV1
from rhizome.models.billing.biie_file_staging_data_v1 import BiieFileStagingDataV1
from rhizome.models.billing.billing_business_initiative_v1 import BillingBusinessInitiativeV1
from rhizome.models.billing.billing_request_state_v1 import BillingRequestStateV1
from rhizome.models.billing.billing_request_v1 import BillingRequestV1
from rhizome.models.billing.charge_capture_error_v1 import ChargeCaptureErrorV1
from rhizome.models.billing.charge_invoice_number_v1 import ChargeInvoiceNumberV1
from rhizome.models.billing.charge_post_date_v1 import ChargePostDateV1
from rhizome.models.billing.charge_state_attempt_v1 import ChargeStateAttemptV1
from rhizome.models.billing.combined_charge_tree_v1 import CombinedChargeTreeV1
from rhizome.models.billing.combined_charge_v1 import CombinedChargeV1
from rhizome.models.billing.combined_disbursement_tree_v1 import CombinedDisbursementTreeV1
from rhizome.models.billing.combined_disbursement_v1 import CombinedDisbursementV1
from rhizome.models.billing.corollary_data_v1 import CorollaryDataV1
from rhizome.models.billing.country_suppression_v1 import CountrySuppressionV1
from rhizome.models.billing.disbursement_invoice_number_v1 import DisbursementInvoiceNumberV1
from rhizome.models.billing.email_audit_v1 import EmailAuditV1
from rhizome.models.billing.email_developer_charge_v1 import EmailDeveloperChargeV1
from rhizome.models.billing.explanation_data_v1 import ExplanationDataV1
from rhizome.models.billing.explanation_v1 import ExplanationV1
from rhizome.models.billing.export_tracker_v1 import ExportTrackerV1
from rhizome.models.billing.fee_exception_v1 import FeeExceptionV1
from rhizome.models.billing.fee_v1 import FeeV1
from rhizome.models.billing.flight_check_archive_v1 import FlightCheckArchiveV1
from rhizome.models.billing.flight_check_execution_v1 import FlightCheckExecutionV1
from rhizome.models.billing.flight_check_v1 import FlightCheckV1
from rhizome.models.billing.invoice_charge_v1 import InvoiceChargeV1
from rhizome.models.billing.job_lock_v1 import JobLockV1
from rhizome.models.billing.merchant_device_info_v1 import MerchantDeviceInfoV1
from rhizome.models.billing.merchant_queue_sensitive_v1 import MerchantQueueSensitiveV1
from rhizome.models.billing.merchant_subscription_action_v1 import MerchantSubscriptionActionV1
from rhizome.models.billing.merchant_suppression_by_app_v1 import MerchantSuppressionByAppV1
from rhizome.models.billing.merchant_suppression_v1 import MerchantSuppressionV1
from rhizome.models.billing.merchant_terms_acceptance_events_v1 import MerchantTermsAcceptanceEventsV1
from rhizome.models.billing.merchant_terms_acceptance_failed_event_log_v1 import MerchantTermsAcceptanceFailedEventLogV1
from rhizome.models.billing.merchant_terms_acceptance_v1 import MerchantTermsAcceptanceV1
from rhizome.models.billing.merchant_terms_missing_acceptance_v1 import MerchantTermsMissingAcceptanceV1
from rhizome.models.billing.offboarding_v1 import OffboardingV1
from rhizome.models.billing.plan_authorization_settings_v1 import PlanAuthorizationSettingsV1
from rhizome.models.billing.plan_meta_history_v1 import PlanMetaHistoryV1
from rhizome.models.billing.plan_meta_v1 import PlanMetaV1
from rhizome.models.billing.producer_failure_v1 import ProducerFailureV1
from rhizome.models.billing.promo_control_v1 import PromoControlV1
from rhizome.models.billing.promo_v1 import PromoV1
from rhizome.models.billing.remit_merchant_details_v1 import RemitMerchantDetailsV1
from rhizome.models.billing.reseller_app_rev_share_v1 import ResellerAppRevShareV1
from rhizome.models.billing.reseller_invoice_alliance_v1 import ResellerInvoiceAllianceV1
from rhizome.models.billing.reseller_plan_fee_v1 import ResellerPlanFeeV1
from rhizome.models.billing.reseller_plan_rev_share_v1 import ResellerPlanRevShareV1
from rhizome.models.billing.reseller_suppression_v1 import ResellerSuppressionV1
from rhizome.models.billing.reseller_usage_job_config_v1 import ResellerUsageJobConfigV1
from rhizome.models.billing.rev_share_v1 import RevShareV1
from rhizome.models.billing.seasonal_reseller_info_v1 import SeasonalResellerInfoV1
from rhizome.models.billing.server_config_v1 import ServerConfigV1
from rhizome.models.billing.stage_app_metered_event_v1 import StageAppMeteredEventV1
from rhizome.models.billing.stage_charge_capture_error_v1 import StageChargeCaptureErrorV1
from rhizome.models.billing.stage_charge_history_v1 import StageChargeHistoryV1
from rhizome.models.billing.stage_charge_state_attempt_v1 import StageChargeStateAttemptV1
from rhizome.models.billing.stage_charge_update_v1 import StageChargeUpdateV1
from rhizome.models.billing.stage_charge_v1 import StageChargeV1
from rhizome.models.billing.stage_email_merchant_charge_v1 import StageEmailMerchantChargeV1
from rhizome.models.billing.stage_email_v1 import StageEmailV1
from rhizome.models.billing.stage_infolease_charge_attempt_v1 import StageInfoleaseChargeAttemptV1
from rhizome.models.billing.stage_infolease_disbursement_attempt_v1 import StageInfoleaseDisbursementAttemptV1
from rhizome.models.billing.stage_merchant_app_charge_v1 import StageMerchantAppChargeV1
from rhizome.models.billing.stage_merchant_plan_charge_v1 import StageMerchantPlanChargeV1
from rhizome.models.billing.stage_vendor_disbursement_error_v1 import StageVendorDisbursementErrorV1
from rhizome.models.billing.stage_vendor_disbursement_state_attempt_v1 import StageVendorDisbursementStateAttemptV1
from rhizome.models.billing.suppression_metrics_v1 import SuppressionMetricsV1
from rhizome.models.billing.vat_vendor_disbursement_v1 import VatVendorDisbursementV1
from rhizome.models.billing.vendor_disbursement_error_v1 import VendorDisbursementErrorV1
from rhizome.models.billing.vendor_disbursement_state_attempt_v1 import VendorDisbursementStateAttemptV1
from rhizome.models.table_list import BillingTable

models: dict[BillingTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]] = {
    BillingTable.app_suppression: (AppSuppressionV1, AppSuppressionNaProd),
    BillingTable.auto_debit_no_auth_config: (AutoDebitNoAuthConfigV1, AutoDebitNoAuthConfigNaProd),
    BillingTable.bank_routing: (BankRoutingV1, BankRoutingNaProd),
    BillingTable.bi_context: (BiContextV1, BiContextNaProd),
    BillingTable.biie_config: (BiieConfigV1, BiieConfigNaProd),
    BillingTable.biie_file_def: (BiieFileDefV1, BiieFileDefNaProd),
    BillingTable.biie_file_instance: (BiieFileInstanceV1, BiieFileInstanceNaProd),
    BillingTable.biie_file_instance_request: (BiieFileInstanceRequestV1, BiieFileInstanceRequestNaProd),
    BillingTable.biie_file_staging_data: (BiieFileStagingDataV1, BiieFileStagingDataNaProd),
    BillingTable.billing_business_initiative: (BillingBusinessInitiativeV1, BillingBusinessInitiativeNaProd),
    BillingTable.billing_request: (BillingRequestV1, BillingRequestNaProd),
    BillingTable.billing_request_state: (BillingRequestStateV1, BillingRequestStateNaProd),
    BillingTable.charge_capture_error: (ChargeCaptureErrorV1, ChargeCaptureErrorNaProd),
    BillingTable.charge_invoice_number: (ChargeInvoiceNumberV1, ChargeInvoiceNumberNaProd),
    BillingTable.charge_post_date: (ChargePostDateV1, ChargePostDateNaProd),
    BillingTable.charge_state_attempt: (ChargeStateAttemptV1, ChargeStateAttemptNaProd),
    BillingTable.combined_charge: (CombinedChargeV1, CombinedChargeNaProd),
    BillingTable.combined_charge_tree: (CombinedChargeTreeV1, CombinedChargeTreeNaProd),
    BillingTable.combined_disbursement: (CombinedDisbursementV1, CombinedDisbursementNaProd),
    BillingTable.combined_disbursement_tree: (CombinedDisbursementTreeV1, CombinedDisbursementTreeNaProd),
    BillingTable.corollary_data: (CorollaryDataV1, CorollaryDataNaProd),
    BillingTable.country_suppression: (CountrySuppressionV1, CountrySuppressionNaProd),
    BillingTable.disbursement_invoice_number: (DisbursementInvoiceNumberV1, DisbursementInvoiceNumberNaProd),
    BillingTable.email_audit: (EmailAuditV1, EmailAuditNaProd),
    BillingTable.email_developer_charge: (EmailDeveloperChargeV1, EmailDeveloperChargeNaProd),
    BillingTable.explanation: (ExplanationV1, ExplanationNaProd),
    BillingTable.explanation_data: (ExplanationDataV1, ExplanationDataNaProd),
    BillingTable.export_tracker: (ExportTrackerV1, ExportTrackerNaProd),
    BillingTable.fee: (FeeV1, FeeNaProd),
    BillingTable.fee_exception: (FeeExceptionV1, FeeExceptionNaProd),
    BillingTable.flight_check: (FlightCheckV1, FlightCheckNaProd),
    BillingTable.flight_check_archive: (FlightCheckArchiveV1, FlightCheckArchiveNaProd),
    BillingTable.flight_check_execution: (FlightCheckExecutionV1, FlightCheckExecutionNaProd),
    BillingTable.invoice_charge: (InvoiceChargeV1, InvoiceChargeNaProd),
    BillingTable.job_lock: (JobLockV1, JobLockNaProd),
    BillingTable.merchant_device_info: (MerchantDeviceInfoV1, MerchantDeviceInfoNaProd),
    BillingTable.merchant_queue_sensitive: (MerchantQueueSensitiveV1, MerchantQueueSensitiveNaProd),
    BillingTable.merchant_subscription_action: (MerchantSubscriptionActionV1, MerchantSubscriptionActionNaProd),
    BillingTable.merchant_suppression: (MerchantSuppressionV1, MerchantSuppressionNaProd),
    BillingTable.merchant_suppression_by_app: (MerchantSuppressionByAppV1, MerchantSuppressionByAppNaProd),
    BillingTable.merchant_terms_acceptance: (MerchantTermsAcceptanceV1, MerchantTermsAcceptanceNaProd),
    BillingTable.merchant_terms_acceptance_events: (
        MerchantTermsAcceptanceEventsV1,
        MerchantTermsAcceptanceEventsNaProd,
    ),
    BillingTable.merchant_terms_acceptance_failed_event_log: (
        MerchantTermsAcceptanceFailedEventLogV1,
        MerchantTermsAcceptanceFailedEventLogNaProd,
    ),
    BillingTable.merchant_terms_missing_acceptance: (
        MerchantTermsMissingAcceptanceV1,
        MerchantTermsMissingAcceptanceNaProd,
    ),
    BillingTable.offboarding: (OffboardingV1, OffboardingNaProd),
    BillingTable.plan_authorization_settings: (PlanAuthorizationSettingsV1, PlanAuthorizationSettingsNaProd),
    BillingTable.plan_meta: (PlanMetaV1, PlanMetaNaProd),
    BillingTable.plan_meta_history: (PlanMetaHistoryV1, PlanMetaHistoryNaProd),
    BillingTable.producer_failure: (ProducerFailureV1, ProducerFailureNaProd),
    BillingTable.promo: (PromoV1, PromoNaProd),
    BillingTable.promo_control: (PromoControlV1, PromoControlNaProd),
    BillingTable.remit_merchant_details: (RemitMerchantDetailsV1, RemitMerchantDetailsNaProd),
    BillingTable.reseller_app_rev_share: (ResellerAppRevShareV1, ResellerAppRevShareNaProd),
    BillingTable.reseller_invoice_alliance: (ResellerInvoiceAllianceV1, ResellerInvoiceAllianceNaProd),
    BillingTable.reseller_plan_fee: (ResellerPlanFeeV1, ResellerPlanFeeNaProd),
    BillingTable.reseller_plan_rev_share: (ResellerPlanRevShareV1, ResellerPlanRevShareNaProd),
    BillingTable.reseller_suppression: (ResellerSuppressionV1, ResellerSuppressionNaProd),
    BillingTable.reseller_usage_job_config: (ResellerUsageJobConfigV1, ResellerUsageJobConfigNaProd),
    BillingTable.rev_share: (RevShareV1, RevShareNaProd),
    BillingTable.seasonal_reseller_info: (SeasonalResellerInfoV1, SeasonalResellerInfoNaProd),
    BillingTable.server_config: (ServerConfigV1, ServerConfigNaProd),
    BillingTable.stage_app_metered_event: (StageAppMeteredEventV1, StageAppMeteredEventNaProd),
    BillingTable.stage_charge: (StageChargeV1, StageChargeNaProd),
    BillingTable.stage_charge_capture_error: (StageChargeCaptureErrorV1, StageChargeCaptureErrorNaProd),
    BillingTable.stage_charge_history: (StageChargeHistoryV1, StageChargeHistoryNaProd),
    BillingTable.stage_charge_state_attempt: (StageChargeStateAttemptV1, StageChargeStateAttemptNaProd),
    BillingTable.stage_charge_update: (StageChargeUpdateV1, StageChargeUpdateNaProd),
    BillingTable.stage_email: (StageEmailV1, StageEmailNaProd),
    BillingTable.stage_email_merchant_charge: (StageEmailMerchantChargeV1, StageEmailMerchantChargeNaProd),
    BillingTable.stage_infolease_charge_attempt: (StageInfoleaseChargeAttemptV1, StageInfoleaseChargeAttemptNaProd),
    BillingTable.stage_infolease_disbursement_attempt: (
        StageInfoleaseDisbursementAttemptV1,
        StageInfoleaseDisbursementAttemptNaProd,
    ),
    BillingTable.stage_merchant_app_charge: (StageMerchantAppChargeV1, StageMerchantAppChargeNaProd),
    BillingTable.stage_merchant_plan_charge: (StageMerchantPlanChargeV1, StageMerchantPlanChargeNaProd),
    BillingTable.stage_vendor_disbursement_error: (StageVendorDisbursementErrorV1, StageVendorDisbursementErrorNaProd),
    BillingTable.stage_vendor_disbursement_state_attempt: (
        StageVendorDisbursementStateAttemptV1,
        StageVendorDisbursementStateAttemptNaProd,
    ),
    BillingTable.suppression_metrics: (SuppressionMetricsV1, SuppressionMetricsNaProd),
    BillingTable.vat_vendor_disbursement: (VatVendorDisbursementV1, VatVendorDisbursementNaProd),
    BillingTable.vendor_disbursement_error: (VendorDisbursementErrorV1, VendorDisbursementErrorNaProd),
    BillingTable.vendor_disbursement_state_attempt: (
        VendorDisbursementStateAttemptV1,
        VendorDisbursementStateAttemptNaProd,
    ),
}


class NorthAmericaBilling(Environment):
    """North America production billing environment using direct database connection."""

    # Type aliases for environment-specific model versions
    AppSuppression: type[AppSuppressionV1] = AppSuppressionV1
    AutoDebitNoAuthConfig: type[AutoDebitNoAuthConfigV1] = AutoDebitNoAuthConfigV1
    BankRouting: type[BankRoutingV1] = BankRoutingV1
    BiContext: type[BiContextV1] = BiContextV1
    BiieConfig: type[BiieConfigV1] = BiieConfigV1
    BiieFileDef: type[BiieFileDefV1] = BiieFileDefV1
    BiieFileInstance: type[BiieFileInstanceV1] = BiieFileInstanceV1
    BiieFileInstanceRequest: type[BiieFileInstanceRequestV1] = BiieFileInstanceRequestV1
    BiieFileStagingData: type[BiieFileStagingDataV1] = BiieFileStagingDataV1
    BillingBusinessInitiative: type[BillingBusinessInitiativeV1] = BillingBusinessInitiativeV1
    BillingRequest: type[BillingRequestV1] = BillingRequestV1
    BillingRequestState: type[BillingRequestStateV1] = BillingRequestStateV1
    ChargeCaptureError: type[ChargeCaptureErrorV1] = ChargeCaptureErrorV1
    ChargeInvoiceNumber: type[ChargeInvoiceNumberV1] = ChargeInvoiceNumberV1
    ChargePostDate: type[ChargePostDateV1] = ChargePostDateV1
    ChargeStateAttempt: type[ChargeStateAttemptV1] = ChargeStateAttemptV1
    CombinedCharge: type[CombinedChargeV1] = CombinedChargeV1
    CombinedChargeTree: type[CombinedChargeTreeV1] = CombinedChargeTreeV1
    CombinedDisbursement: type[CombinedDisbursementV1] = CombinedDisbursementV1
    CombinedDisbursementTree: type[CombinedDisbursementTreeV1] = CombinedDisbursementTreeV1
    CorollaryData: type[CorollaryDataV1] = CorollaryDataV1
    CountrySuppression: type[CountrySuppressionV1] = CountrySuppressionV1
    DisbursementInvoiceNumber: type[DisbursementInvoiceNumberV1] = DisbursementInvoiceNumberV1
    EmailAudit: type[EmailAuditV1] = EmailAuditV1
    EmailDeveloperCharge: type[EmailDeveloperChargeV1] = EmailDeveloperChargeV1
    Explanation: type[ExplanationV1] = ExplanationV1
    ExplanationData: type[ExplanationDataV1] = ExplanationDataV1
    ExportTracker: type[ExportTrackerV1] = ExportTrackerV1
    Fee: type[FeeV1] = FeeV1
    FeeException: type[FeeExceptionV1] = FeeExceptionV1
    FlightCheck: type[FlightCheckV1] = FlightCheckV1
    FlightCheckArchive: type[FlightCheckArchiveV1] = FlightCheckArchiveV1
    FlightCheckExecution: type[FlightCheckExecutionV1] = FlightCheckExecutionV1
    InvoiceCharge: type[InvoiceChargeV1] = InvoiceChargeV1
    JobLock: type[JobLockV1] = JobLockV1
    MerchantDeviceInfo: type[MerchantDeviceInfoV1] = MerchantDeviceInfoV1
    MerchantQueueSensitive: type[MerchantQueueSensitiveV1] = MerchantQueueSensitiveV1
    MerchantSubscriptionAction: type[MerchantSubscriptionActionV1] = MerchantSubscriptionActionV1
    MerchantSuppression: type[MerchantSuppressionV1] = MerchantSuppressionV1
    MerchantSuppressionByApp: type[MerchantSuppressionByAppV1] = MerchantSuppressionByAppV1
    MerchantTermsAcceptance: type[MerchantTermsAcceptanceV1] = MerchantTermsAcceptanceV1
    Offboarding: type[OffboardingV1] = OffboardingV1
    PlanAuthorizationSettings: type[PlanAuthorizationSettingsV1] = PlanAuthorizationSettingsV1
    PlanMeta: type[PlanMetaV1] = PlanMetaV1
    PlanMetaHistory: type[PlanMetaHistoryV1] = PlanMetaHistoryV1
    ProducerFailure: type[ProducerFailureV1] = ProducerFailureV1
    Promo: type[PromoV1] = PromoV1
    PromoControl: type[PromoControlV1] = PromoControlV1
    RemitMerchantDetails: type[RemitMerchantDetailsV1] = RemitMerchantDetailsV1
    ResellerAppRevShare: type[ResellerAppRevShareV1] = ResellerAppRevShareV1
    ResellerInvoiceAlliance: type[ResellerInvoiceAllianceV1] = ResellerInvoiceAllianceV1
    ResellerPlanFee: type[ResellerPlanFeeV1] = ResellerPlanFeeV1
    ResellerPlanRevShare: type[ResellerPlanRevShareV1] = ResellerPlanRevShareV1
    ResellerSuppression: type[ResellerSuppressionV1] = ResellerSuppressionV1
    ResellerUsageJobConfig: type[ResellerUsageJobConfigV1] = ResellerUsageJobConfigV1
    RevShare: type[RevShareV1] = RevShareV1
    SeasonalResellerInfo: type[SeasonalResellerInfoV1] = SeasonalResellerInfoV1
    ServerConfig: type[ServerConfigV1] = ServerConfigV1
    StageAppMeteredEvent: type[StageAppMeteredEventV1] = StageAppMeteredEventV1
    StageCharge: type[StageChargeV1] = StageChargeV1
    StageChargeCaptureError: type[StageChargeCaptureErrorV1] = StageChargeCaptureErrorV1
    StageChargeHistory: type[StageChargeHistoryV1] = StageChargeHistoryV1
    StageChargeStateAttempt: type[StageChargeStateAttemptV1] = StageChargeStateAttemptV1
    StageChargeUpdate: type[StageChargeUpdateV1] = StageChargeUpdateV1
    StageEmail: type[StageEmailV1] = StageEmailV1
    StageEmailMerchantCharge: type[StageEmailMerchantChargeV1] = StageEmailMerchantChargeV1
    StageInfoleaseChargeAttempt: type[StageInfoleaseChargeAttemptV1] = StageInfoleaseChargeAttemptV1
    StageMerchantAppCharge: type[StageMerchantAppChargeV1] = StageMerchantAppChargeV1
    StageMerchantPlanCharge: type[StageMerchantPlanChargeV1] = StageMerchantPlanChargeV1
    StageVendorDisbursementError: type[StageVendorDisbursementErrorV1] = StageVendorDisbursementErrorV1
    SuppressionMetrics: type[SuppressionMetricsV1] = SuppressionMetricsV1
    VatVendorDisbursement: type[VatVendorDisbursementV1] = VatVendorDisbursementV1
    VendorDisbursementError: type[VendorDisbursementErrorV1] = VendorDisbursementErrorV1

    def tables(self) -> list[StrEnum]:
        return list(BillingTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        if not isinstance(table_name, BillingTable):
            raise ValueError(f"Expected BillingTable, got {type(table_name)}")
        model_class, emplacement_class = models[table_name]
        if model_class is None:
            raise NotImplementedError(f"Model class for {table_name} not yet implemented")
        if emplacement_class is None:
            raise NotImplementedError(f"Emplacement class for {table_name} not yet implemented")
        return model_class, emplacement_class

    @classmethod
    def get_database_config(cls, tools: Tools) -> DatabaseConfig:
        """Get database configuration using pybritive temporary credentials."""
        import asyncio

        # Use the static method with tools parameter
        return asyncio.run(
            Environment.get_database_config_from_credentials(
                tools=tools,
                secret_reference="Resources/COS-RO-USProd/COS-RO-USProd-profile",
                secret_manager=SecretManager.PYBRITIVE,
                database_name="billing",
            )
        )

    @classmethod
    def get_port_forward_config(cls) -> PortForwardConfig | None:
        """No port forwarding needed - direct connection."""
        return None

    @property
    def name(self) -> str:
        """Environment name for display purposes in logs and debugging, not used for connections."""
        return "NorthAmericaBilling"

    @classmethod
    def database_id(cls) -> str:
        """Database identifier for server-side query execution."""
        return "na_prod_billing"

    def get_connection_string(self) -> str:
        """Build the connection string for this environment."""
        from urllib.parse import quote_plus

        db_config = self.get_database_config(self.client.tools)
        encoded_password = quote_plus(db_config.password)
        connection_string = f"mysql+pymysql://{db_config.username}:{encoded_password}@{db_config.host}:{db_config.port}/{db_config.database}?ssl_verify_cert=false"

        # Log connection details
        mysql_command = (
            f"mysql --user={db_config.username} --password=[REDACTED] --host={db_config.host} "
            f"--port={db_config.port} --batch --skip-ssl-verify-server-cert {db_config.database}"
        )
        self._log_connection_if_new(db_config, mysql_command)

        return connection_string
