"""
Dev Bookkeeper environment configuration.

This module provides access to the billing-bookkeeper database in the
dev cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.environments.dev.expected_data.billing_bookkeeper_adjust_action import AdjustActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_adjust_action_fee_code import AdjustActionFeeCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_adjust_action_type import AdjustActionTypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_adjust_reason import AdjustReasonDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_app_meter_action import AppMeterActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_app_meter_action_error import AppMeterActionErrorDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_app_meter_action_fee_code import AppMeterActionFeeCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_app_meter_action_type import AppMeterActionTypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_app_sub_action import AppSubActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_app_sub_action_error import AppSubActionErrorDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_app_sub_action_fee_code import AppSubActionFeeCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_app_sub_action_type import AppSubActionTypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_auto_adjust_advice import AutoAdjustAdviceDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_auto_adjust_qualifier import AutoAdjustQualifierDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_auto_adjust_rule import AutoAdjustRuleDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_archetype import BillingArchetypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_entity import BillingEntityDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_entity_config import BillingEntityConfigDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_event_history import BillingEventHistoryDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_hierarchy import BillingHierarchyDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_hierarchy_cycle import BillingHierarchyCycleDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_hierarchy_type import BillingHierarchyTypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_pseudo_entity import BillingPseudoEntityDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_billing_schedule import BillingScheduleDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_cellular_action import CellularActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_cellular_action_error import CellularActionErrorDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_cellular_action_fee_code import CellularActionFeeCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_cellular_action_type import CellularActionTypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_consumer_failure import ConsumerFailureDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_consumer_failure_history import ConsumerFailureHistoryDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_cycle_validation import CycleValidationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_cycle_validation_mutation import CycleValidationMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_deserializable_failure import DeserializableFailureDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_category import FeeCategoryDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_code import FeeCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_code_app import FeeCodeAppDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_code_ledger_account import FeeCodeLedgerAccountDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_ctd import FeeCtdDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_rate import FeeRateDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_rate_error_report import FeeRateErrorReportDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_rate_report_action_error import FeeRateReportActionErrorDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_summary import FeeSummaryDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_summary_mutation import FeeSummaryMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_tax import FeeTaxDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_tax_mutation import FeeTaxMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_fee_ytd import FeeYtdDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_flyway_schema_history import FlywaySchemaHistoryDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_invoice_alliance_code import InvoiceAllianceCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_invoice_info import InvoiceInfoDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_invoice_info_amount import InvoiceInfoAmountDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_invoice_info_mutation import InvoiceInfoMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_invoice_info_settlement import InvoiceInfoSettlementDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_invoice_info_settlement_mutation import InvoiceInfoSettlementMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_job_assassination_contract import JobAssassinationContractDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_jobrunr_backgroundjobservers import JobrunrBackgroundjobserversDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_jobrunr_jobs import JobrunrJobsDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_jobrunr_metadata import JobrunrMetadataDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_jobrunr_migrations import JobrunrMigrationsDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_jobrunr_recurring_jobs import JobrunrRecurringJobsDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account import LedgerAccountDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account_action import LedgerAccountActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account_balance import LedgerAccountBalanceDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account_key import LedgerAccountKeyDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account_key_app import LedgerAccountKeyAppDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account_key_purpose import LedgerAccountKeyPurposeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account_purpose import LedgerAccountPurposeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account_settlement import LedgerAccountSettlementDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_account_transition import LedgerAccountTransitionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_journal import LedgerJournalDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_ledger_journal_mutation import LedgerJournalMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_lexi_attribute import LexiAttributeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_lexi_rule import LexiRuleDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_look import LookDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_look_data import LookDataDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_merchant_detail import MerchantDetailDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_misc_action import MiscActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_misc_action_error import MiscActionErrorDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_misc_action_fee_code import MiscActionFeeCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_misc_action_type import MiscActionTypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_misc_specifier import MiscSpecifierDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_model_fee_summary import ModelFeeSummaryDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_monetary_adjustment import MonetaryAdjustmentDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_monetary_adjustment_mutation import MonetaryAdjustmentMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_monetary_rule_alias import MonetaryRuleAliasDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_monetary_rule_set import MonetaryRuleSetDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_monetary_rule_set_rule import MonetaryRuleSetRuleDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_partner_config import PartnerConfigDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_plan_action import PlanActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_plan_action_error import PlanActionErrorDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_plan_action_fee_code import PlanActionFeeCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_plan_action_type import PlanActionTypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_processing_group_dates import ProcessingGroupDatesDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_processing_note import ProcessingNoteDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_processing_note_mutation import ProcessingNoteMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_prototype_fee_rate import PrototypeFeeRateDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_prototype_fee_set import PrototypeFeeSetDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_revenue_action import RevenueActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_revenue_action_error import RevenueActionErrorDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_revenue_action_fee_code import RevenueActionFeeCodeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_revenue_action_type import RevenueActionTypeDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_revenue_share_group import RevenueShareGroupDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_server_config import ServerConfigDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_settlement import SettlementDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_settlement_action import SettlementActionDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_settlement_mutation import SettlementMutationDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_skip_fee_category_lexi_tag import SkipFeeCategoryLexiTagDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_tier_detail import TierDetailDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_tiered_pricing import TieredPricingDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_tiered_qualifier import TieredQualifierDev
from rhizome.environments.dev.expected_data.billing_bookkeeper_tiered_rule import TieredRuleDev
from rhizome.models.base import Emplacement, RhizomeModel
from rhizome.models.billing_bookkeeper.adjust_action_v1 import AdjustActionV1
from rhizome.models.billing_bookkeeper.adjust_action_fee_code_v1 import AdjustActionFeeCodeV1
from rhizome.models.billing_bookkeeper.adjust_action_type_v1 import AdjustActionTypeV1
from rhizome.models.billing_bookkeeper.adjust_reason_v1 import AdjustReasonV1
from rhizome.models.billing_bookkeeper.app_meter_action_v1 import AppMeterActionV1
from rhizome.models.billing_bookkeeper.app_meter_action_error_v1 import AppMeterActionErrorV1
from rhizome.models.billing_bookkeeper.app_meter_action_fee_code_v1 import AppMeterActionFeeCodeV1
from rhizome.models.billing_bookkeeper.app_meter_action_type_v1 import AppMeterActionTypeV1
from rhizome.models.billing_bookkeeper.app_sub_action_v1 import AppSubActionV1
from rhizome.models.billing_bookkeeper.app_sub_action_error_v1 import AppSubActionErrorV1
from rhizome.models.billing_bookkeeper.app_sub_action_fee_code_v1 import AppSubActionFeeCodeV1
from rhizome.models.billing_bookkeeper.app_sub_action_type_v1 import AppSubActionTypeV1
from rhizome.models.billing_bookkeeper.auto_adjust_advice_v1 import AutoAdjustAdviceV1
from rhizome.models.billing_bookkeeper.auto_adjust_qualifier_v1 import AutoAdjustQualifierV1
from rhizome.models.billing_bookkeeper.auto_adjust_rule_v1 import AutoAdjustRuleV1
from rhizome.models.billing_bookkeeper.billing_archetype_v1 import BillingArchetypeV1
from rhizome.models.billing_bookkeeper.billing_entity_v1 import BillingEntityV1
from rhizome.models.billing_bookkeeper.billing_entity_config_v1 import BillingEntityConfigV1
from rhizome.models.billing_bookkeeper.billing_event_history_v1 import BillingEventHistoryV1
from rhizome.models.billing_bookkeeper.billing_hierarchy_v1 import BillingHierarchyV1
from rhizome.models.billing_bookkeeper.billing_hierarchy_cycle_v1 import BillingHierarchyCycleV1
from rhizome.models.billing_bookkeeper.billing_hierarchy_type_v1 import BillingHierarchyTypeV1
from rhizome.models.billing_bookkeeper.billing_pseudo_entity_v1 import BillingPseudoEntityV1
from rhizome.models.billing_bookkeeper.billing_schedule_v1 import BillingScheduleV1
from rhizome.models.billing_bookkeeper.cellular_action_v1 import CellularActionV1
from rhizome.models.billing_bookkeeper.cellular_action_error_v1 import CellularActionErrorV1
from rhizome.models.billing_bookkeeper.cellular_action_fee_code_v1 import CellularActionFeeCodeV1
from rhizome.models.billing_bookkeeper.cellular_action_type_v1 import CellularActionTypeV1
from rhizome.models.billing_bookkeeper.consumer_failure_v1 import ConsumerFailureV1
from rhizome.models.billing_bookkeeper.consumer_failure_history_v1 import ConsumerFailureHistoryV1
from rhizome.models.billing_bookkeeper.cycle_validation_v1 import CycleValidationV1
from rhizome.models.billing_bookkeeper.cycle_validation_mutation_v1 import CycleValidationMutationV1
from rhizome.models.billing_bookkeeper.deserializable_failure_v1 import DeserializableFailureV1
from rhizome.models.billing_bookkeeper.fee_category_v1 import FeeCategoryV1
from rhizome.models.billing_bookkeeper.fee_code_v1 import FeeCodeV1
from rhizome.models.billing_bookkeeper.fee_code_app_v1 import FeeCodeAppV1
from rhizome.models.billing_bookkeeper.fee_code_ledger_account_v1 import FeeCodeLedgerAccountV1
from rhizome.models.billing_bookkeeper.fee_ctd_v1 import FeeCtdV1
from rhizome.models.billing_bookkeeper.fee_rate_v1 import FeeRateV1
from rhizome.models.billing_bookkeeper.fee_rate_error_report_v1 import FeeRateErrorReportV1
from rhizome.models.billing_bookkeeper.fee_rate_report_action_error_v1 import FeeRateReportActionErrorV1
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1
from rhizome.models.billing_bookkeeper.fee_summary_mutation_v1 import FeeSummaryMutationV1
from rhizome.models.billing_bookkeeper.fee_tax_v1 import FeeTaxV1
from rhizome.models.billing_bookkeeper.fee_tax_mutation_v1 import FeeTaxMutationV1
from rhizome.models.billing_bookkeeper.fee_ytd_v1 import FeeYtdV1
from rhizome.models.billing_bookkeeper.flyway_schema_history_v1 import FlywaySchemaHistoryV1
from rhizome.models.billing_bookkeeper.invoice_alliance_code_v1 import InvoiceAllianceCodeV1
from rhizome.models.billing_bookkeeper.invoice_info_v1 import InvoiceInfoV1
from rhizome.models.billing_bookkeeper.invoice_info_amount_v1 import InvoiceInfoAmountV1
from rhizome.models.billing_bookkeeper.invoice_info_mutation_v1 import InvoiceInfoMutationV1
from rhizome.models.billing_bookkeeper.invoice_info_settlement_v1 import InvoiceInfoSettlementV1
from rhizome.models.billing_bookkeeper.invoice_info_settlement_mutation_v1 import InvoiceInfoSettlementMutationV1
from rhizome.models.billing_bookkeeper.job_assassination_contract_v1 import JobAssassinationContractV1
from rhizome.models.billing_bookkeeper.jobrunr_backgroundjobservers_v1 import JobrunrBackgroundjobserversV1
from rhizome.models.billing_bookkeeper.jobrunr_jobs_v1 import JobrunrJobsV1
from rhizome.models.billing_bookkeeper.jobrunr_metadata_v1 import JobrunrMetadataV1
from rhizome.models.billing_bookkeeper.jobrunr_migrations_v1 import JobrunrMigrationsV1
from rhizome.models.billing_bookkeeper.jobrunr_recurring_jobs_v1 import JobrunrRecurringJobsV1
from rhizome.models.billing_bookkeeper.ledger_account_v1 import LedgerAccountV1
from rhizome.models.billing_bookkeeper.ledger_account_action_v1 import LedgerAccountActionV1
from rhizome.models.billing_bookkeeper.ledger_account_balance_v1 import LedgerAccountBalanceV1
from rhizome.models.billing_bookkeeper.ledger_account_key_v1 import LedgerAccountKeyV1
from rhizome.models.billing_bookkeeper.ledger_account_key_app_v1 import LedgerAccountKeyAppV1
from rhizome.models.billing_bookkeeper.ledger_account_key_purpose_v1 import LedgerAccountKeyPurposeV1
from rhizome.models.billing_bookkeeper.ledger_account_purpose_v1 import LedgerAccountPurposeV1
from rhizome.models.billing_bookkeeper.ledger_account_settlement_v1 import LedgerAccountSettlementV1
from rhizome.models.billing_bookkeeper.ledger_account_transition_v1 import LedgerAccountTransitionV1
from rhizome.models.billing_bookkeeper.ledger_journal_v1 import LedgerJournalV1
from rhizome.models.billing_bookkeeper.ledger_journal_mutation_v1 import LedgerJournalMutationV1
from rhizome.models.billing_bookkeeper.lexi_attribute_v1 import LexiAttributeV1
from rhizome.models.billing_bookkeeper.lexi_rule_v1 import LexiRuleV1
from rhizome.models.billing_bookkeeper.look_v1 import LookV1
from rhizome.models.billing_bookkeeper.look_data_v1 import LookDataV1
from rhizome.models.billing_bookkeeper.merchant_detail_v1 import MerchantDetailV1
from rhizome.models.billing_bookkeeper.misc_action_v1 import MiscActionV1
from rhizome.models.billing_bookkeeper.misc_action_error_v1 import MiscActionErrorV1
from rhizome.models.billing_bookkeeper.misc_action_fee_code_v1 import MiscActionFeeCodeV1
from rhizome.models.billing_bookkeeper.misc_action_type_v1 import MiscActionTypeV1
from rhizome.models.billing_bookkeeper.misc_specifier_v1 import MiscSpecifierV1
from rhizome.models.billing_bookkeeper.model_fee_summary_v1 import ModelFeeSummaryV1
from rhizome.models.billing_bookkeeper.monetary_adjustment_v1 import MonetaryAdjustmentV1
from rhizome.models.billing_bookkeeper.monetary_adjustment_mutation_v1 import MonetaryAdjustmentMutationV1
from rhizome.models.billing_bookkeeper.monetary_rule_alias_v1 import MonetaryRuleAliasV1
from rhizome.models.billing_bookkeeper.monetary_rule_set_v1 import MonetaryRuleSetV1
from rhizome.models.billing_bookkeeper.monetary_rule_set_rule_v1 import MonetaryRuleSetRuleV1
from rhizome.models.billing_bookkeeper.partner_config_v1 import PartnerConfigV1
from rhizome.models.billing_bookkeeper.plan_action_v1 import PlanActionV1
from rhizome.models.billing_bookkeeper.plan_action_error_v1 import PlanActionErrorV1
from rhizome.models.billing_bookkeeper.plan_action_fee_code_v1 import PlanActionFeeCodeV1
from rhizome.models.billing_bookkeeper.plan_action_type_v1 import PlanActionTypeV1
from rhizome.models.billing_bookkeeper.processing_group_dates_v1 import ProcessingGroupDatesV1
from rhizome.models.billing_bookkeeper.processing_note_v1 import ProcessingNoteV1
from rhizome.models.billing_bookkeeper.processing_note_mutation_v1 import ProcessingNoteMutationV1
from rhizome.models.billing_bookkeeper.prototype_fee_rate_v1 import PrototypeFeeRateV1
from rhizome.models.billing_bookkeeper.prototype_fee_set_v1 import PrototypeFeeSetV1
from rhizome.models.billing_bookkeeper.revenue_action_v1 import RevenueActionV1
from rhizome.models.billing_bookkeeper.revenue_action_error_v1 import RevenueActionErrorV1
from rhizome.models.billing_bookkeeper.revenue_action_fee_code_v1 import RevenueActionFeeCodeV1
from rhizome.models.billing_bookkeeper.revenue_action_type_v1 import RevenueActionTypeV1
from rhizome.models.billing_bookkeeper.revenue_share_group_v1 import RevenueShareGroupV1
from rhizome.models.billing_bookkeeper.server_config_v1 import ServerConfigV1
from rhizome.models.billing_bookkeeper.settlement_v1 import SettlementV1
from rhizome.models.billing_bookkeeper.settlement_action_v1 import SettlementActionV1
from rhizome.models.billing_bookkeeper.settlement_mutation_v1 import SettlementMutationV1
from rhizome.models.billing_bookkeeper.skip_fee_category_lexi_tag_v1 import SkipFeeCategoryLexiTagV1
from rhizome.models.billing_bookkeeper.tier_detail_v1 import TierDetailV1
from rhizome.models.billing_bookkeeper.tiered_pricing_v1 import TieredPricingV1
from rhizome.models.billing_bookkeeper.tiered_qualifier_v1 import TieredQualifierV1
from rhizome.models.billing_bookkeeper.tiered_rule_v1 import TieredRuleV1
from rhizome.models.table_list import BillingBookkeeperTable

models: dict[BillingBookkeeperTable, tuple[type[RhizomeModel] | None, type[Emplacement[Any]]]] = {
    BillingBookkeeperTable.adjust_action: (AdjustActionV1, AdjustActionDev),
    BillingBookkeeperTable.adjust_action_fee_code: (AdjustActionFeeCodeV1, AdjustActionFeeCodeDev),
    BillingBookkeeperTable.adjust_action_type: (AdjustActionTypeV1, AdjustActionTypeDev),
    BillingBookkeeperTable.adjust_reason: (AdjustReasonV1, AdjustReasonDev),
    BillingBookkeeperTable.app_meter_action: (AppMeterActionV1, AppMeterActionDev),
    BillingBookkeeperTable.app_meter_action_error: (AppMeterActionErrorV1, AppMeterActionErrorDev),
    BillingBookkeeperTable.app_meter_action_fee_code: (AppMeterActionFeeCodeV1, AppMeterActionFeeCodeDev),
    BillingBookkeeperTable.app_meter_action_type: (AppMeterActionTypeV1, AppMeterActionTypeDev),
    BillingBookkeeperTable.app_sub_action: (AppSubActionV1, AppSubActionDev),
    BillingBookkeeperTable.app_sub_action_error: (AppSubActionErrorV1, AppSubActionErrorDev),
    BillingBookkeeperTable.app_sub_action_fee_code: (AppSubActionFeeCodeV1, AppSubActionFeeCodeDev),
    BillingBookkeeperTable.app_sub_action_type: (AppSubActionTypeV1, AppSubActionTypeDev),
    BillingBookkeeperTable.auto_adjust_advice: (AutoAdjustAdviceV1, AutoAdjustAdviceDev),
    BillingBookkeeperTable.auto_adjust_qualifier: (AutoAdjustQualifierV1, AutoAdjustQualifierDev),
    BillingBookkeeperTable.auto_adjust_rule: (AutoAdjustRuleV1, AutoAdjustRuleDev),
    BillingBookkeeperTable.billing_archetype: (BillingArchetypeV1, BillingArchetypeDev),
    BillingBookkeeperTable.billing_entity: (BillingEntityV1, BillingEntityDev),
    BillingBookkeeperTable.billing_entity_config: (BillingEntityConfigV1, BillingEntityConfigDev),
    BillingBookkeeperTable.billing_event_history: (BillingEventHistoryV1, BillingEventHistoryDev),
    BillingBookkeeperTable.billing_hierarchy: (BillingHierarchyV1, BillingHierarchyDev),
    BillingBookkeeperTable.billing_hierarchy_cycle: (BillingHierarchyCycleV1, BillingHierarchyCycleDev),
    BillingBookkeeperTable.billing_hierarchy_type: (BillingHierarchyTypeV1, BillingHierarchyTypeDev),
    BillingBookkeeperTable.billing_pseudo_entity: (BillingPseudoEntityV1, BillingPseudoEntityDev),
    BillingBookkeeperTable.billing_schedule: (BillingScheduleV1, BillingScheduleDev),
    BillingBookkeeperTable.cellular_action: (CellularActionV1, CellularActionDev),
    BillingBookkeeperTable.cellular_action_error: (CellularActionErrorV1, CellularActionErrorDev),
    BillingBookkeeperTable.cellular_action_fee_code: (CellularActionFeeCodeV1, CellularActionFeeCodeDev),
    BillingBookkeeperTable.cellular_action_type: (CellularActionTypeV1, CellularActionTypeDev),
    BillingBookkeeperTable.consumer_failure: (ConsumerFailureV1, ConsumerFailureDev),
    BillingBookkeeperTable.consumer_failure_history: (ConsumerFailureHistoryV1, ConsumerFailureHistoryDev),
    BillingBookkeeperTable.cycle_validation: (CycleValidationV1, CycleValidationDev),
    BillingBookkeeperTable.cycle_validation_mutation: (CycleValidationMutationV1, CycleValidationMutationDev),
    BillingBookkeeperTable.deserializable_failure: (DeserializableFailureV1, DeserializableFailureDev),
    BillingBookkeeperTable.fee_category: (FeeCategoryV1, FeeCategoryDev),
    BillingBookkeeperTable.fee_code: (FeeCodeV1, FeeCodeDev),
    BillingBookkeeperTable.fee_code_app: (FeeCodeAppV1, FeeCodeAppDev),
    BillingBookkeeperTable.fee_code_ledger_account: (FeeCodeLedgerAccountV1, FeeCodeLedgerAccountDev),
    BillingBookkeeperTable.fee_ctd: (FeeCtdV1, FeeCtdDev),
    BillingBookkeeperTable.fee_rate: (FeeRateV1, FeeRateDev),
    BillingBookkeeperTable.fee_rate_error_report: (FeeRateErrorReportV1, FeeRateErrorReportDev),
    BillingBookkeeperTable.fee_rate_report_action_error: (FeeRateReportActionErrorV1, FeeRateReportActionErrorDev),
    BillingBookkeeperTable.fee_summary: (FeeSummaryV1, FeeSummaryDev),
    BillingBookkeeperTable.fee_summary_mutation: (FeeSummaryMutationV1, FeeSummaryMutationDev),
    BillingBookkeeperTable.fee_tax: (FeeTaxV1, FeeTaxDev),
    BillingBookkeeperTable.fee_tax_mutation: (FeeTaxMutationV1, FeeTaxMutationDev),
    BillingBookkeeperTable.fee_ytd: (FeeYtdV1, FeeYtdDev),
    BillingBookkeeperTable.flyway_schema_history: (FlywaySchemaHistoryV1, FlywaySchemaHistoryDev),
    BillingBookkeeperTable.invoice_alliance_code: (InvoiceAllianceCodeV1, InvoiceAllianceCodeDev),
    BillingBookkeeperTable.invoice_info: (InvoiceInfoV1, InvoiceInfoDev),
    BillingBookkeeperTable.invoice_info_amount: (InvoiceInfoAmountV1, InvoiceInfoAmountDev),
    BillingBookkeeperTable.invoice_info_mutation: (InvoiceInfoMutationV1, InvoiceInfoMutationDev),
    BillingBookkeeperTable.invoice_info_settlement: (InvoiceInfoSettlementV1, InvoiceInfoSettlementDev),
    BillingBookkeeperTable.invoice_info_settlement_mutation: (InvoiceInfoSettlementMutationV1, InvoiceInfoSettlementMutationDev),
    BillingBookkeeperTable.job_assassination_contract: (JobAssassinationContractV1, JobAssassinationContractDev),
    BillingBookkeeperTable.jobrunr_backgroundjobservers: (JobrunrBackgroundjobserversV1, JobrunrBackgroundjobserversDev),
    BillingBookkeeperTable.jobrunr_jobs: (JobrunrJobsV1, JobrunrJobsDev),
    BillingBookkeeperTable.jobrunr_metadata: (JobrunrMetadataV1, JobrunrMetadataDev),
    BillingBookkeeperTable.jobrunr_migrations: (JobrunrMigrationsV1, JobrunrMigrationsDev),
    BillingBookkeeperTable.jobrunr_recurring_jobs: (JobrunrRecurringJobsV1, JobrunrRecurringJobsDev),
    BillingBookkeeperTable.ledger_account: (LedgerAccountV1, LedgerAccountDev),
    BillingBookkeeperTable.ledger_account_action: (LedgerAccountActionV1, LedgerAccountActionDev),
    BillingBookkeeperTable.ledger_account_balance: (LedgerAccountBalanceV1, LedgerAccountBalanceDev),
    BillingBookkeeperTable.ledger_account_key: (LedgerAccountKeyV1, LedgerAccountKeyDev),
    BillingBookkeeperTable.ledger_account_key_app: (LedgerAccountKeyAppV1, LedgerAccountKeyAppDev),
    BillingBookkeeperTable.ledger_account_key_purpose: (LedgerAccountKeyPurposeV1, LedgerAccountKeyPurposeDev),
    BillingBookkeeperTable.ledger_account_purpose: (LedgerAccountPurposeV1, LedgerAccountPurposeDev),
    BillingBookkeeperTable.ledger_account_settlement: (LedgerAccountSettlementV1, LedgerAccountSettlementDev),
    BillingBookkeeperTable.ledger_account_transition: (LedgerAccountTransitionV1, LedgerAccountTransitionDev),
    BillingBookkeeperTable.ledger_journal: (LedgerJournalV1, LedgerJournalDev),
    BillingBookkeeperTable.ledger_journal_mutation: (LedgerJournalMutationV1, LedgerJournalMutationDev),
    BillingBookkeeperTable.lexi_attribute: (LexiAttributeV1, LexiAttributeDev),
    BillingBookkeeperTable.lexi_rule: (LexiRuleV1, LexiRuleDev),
    BillingBookkeeperTable.look: (LookV1, LookDev),
    BillingBookkeeperTable.look_data: (LookDataV1, LookDataDev),
    BillingBookkeeperTable.merchant_detail: (MerchantDetailV1, MerchantDetailDev),
    BillingBookkeeperTable.misc_action: (MiscActionV1, MiscActionDev),
    BillingBookkeeperTable.misc_action_error: (MiscActionErrorV1, MiscActionErrorDev),
    BillingBookkeeperTable.misc_action_fee_code: (MiscActionFeeCodeV1, MiscActionFeeCodeDev),
    BillingBookkeeperTable.misc_action_type: (MiscActionTypeV1, MiscActionTypeDev),
    BillingBookkeeperTable.misc_specifier: (MiscSpecifierV1, MiscSpecifierDev),
    BillingBookkeeperTable.model_fee_summary: (ModelFeeSummaryV1, ModelFeeSummaryDev),
    BillingBookkeeperTable.monetary_adjustment: (MonetaryAdjustmentV1, MonetaryAdjustmentDev),
    BillingBookkeeperTable.monetary_adjustment_mutation: (MonetaryAdjustmentMutationV1, MonetaryAdjustmentMutationDev),
    BillingBookkeeperTable.monetary_rule_alias: (MonetaryRuleAliasV1, MonetaryRuleAliasDev),
    BillingBookkeeperTable.monetary_rule_set: (MonetaryRuleSetV1, MonetaryRuleSetDev),
    BillingBookkeeperTable.monetary_rule_set_rule: (MonetaryRuleSetRuleV1, MonetaryRuleSetRuleDev),
    BillingBookkeeperTable.partner_config: (PartnerConfigV1, PartnerConfigDev),
    BillingBookkeeperTable.plan_action: (PlanActionV1, PlanActionDev),
    BillingBookkeeperTable.plan_action_error: (PlanActionErrorV1, PlanActionErrorDev),
    BillingBookkeeperTable.plan_action_fee_code: (PlanActionFeeCodeV1, PlanActionFeeCodeDev),
    BillingBookkeeperTable.plan_action_type: (PlanActionTypeV1, PlanActionTypeDev),
    BillingBookkeeperTable.processing_group_dates: (ProcessingGroupDatesV1, ProcessingGroupDatesDev),
    BillingBookkeeperTable.processing_note: (ProcessingNoteV1, ProcessingNoteDev),
    BillingBookkeeperTable.processing_note_mutation: (ProcessingNoteMutationV1, ProcessingNoteMutationDev),
    BillingBookkeeperTable.prototype_fee_rate: (PrototypeFeeRateV1, PrototypeFeeRateDev),
    BillingBookkeeperTable.prototype_fee_set: (PrototypeFeeSetV1, PrototypeFeeSetDev),
    BillingBookkeeperTable.revenue_action: (RevenueActionV1, RevenueActionDev),
    BillingBookkeeperTable.revenue_action_error: (RevenueActionErrorV1, RevenueActionErrorDev),
    BillingBookkeeperTable.revenue_action_fee_code: (RevenueActionFeeCodeV1, RevenueActionFeeCodeDev),
    BillingBookkeeperTable.revenue_action_type: (RevenueActionTypeV1, RevenueActionTypeDev),
    BillingBookkeeperTable.revenue_share_group: (RevenueShareGroupV1, RevenueShareGroupDev),
    BillingBookkeeperTable.server_config: (ServerConfigV1, ServerConfigDev),
    BillingBookkeeperTable.settlement: (SettlementV1, SettlementDev),
    BillingBookkeeperTable.settlement_action: (SettlementActionV1, SettlementActionDev),
    BillingBookkeeperTable.settlement_mutation: (SettlementMutationV1, SettlementMutationDev),
    BillingBookkeeperTable.skip_fee_category_lexi_tag: (SkipFeeCategoryLexiTagV1, SkipFeeCategoryLexiTagDev),
    BillingBookkeeperTable.tier_detail: (TierDetailV1, TierDetailDev),
    BillingBookkeeperTable.tiered_pricing: (TieredPricingV1, TieredPricingDev),
    BillingBookkeeperTable.tiered_qualifier: (TieredQualifierV1, TieredQualifierDev),
    BillingBookkeeperTable.tiered_rule: (TieredRuleV1, TieredRuleDev),
}


class DevBillingBookkeeper(Environment):
    """Development bookkeeper environment using CloudSQL."""

    def tables(self) -> list[StrEnum]:
        return list(BillingBookkeeperTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        # Cast the StrEnum to the specific table enum for type safety
        if not isinstance(table_name, BillingBookkeeperTable):
            raise ValueError(f"Expected BillingBookkeeperTable, got {type(table_name)}")
        if table_name not in models:
            raise NotImplementedError(f"Table {table_name} not yet implemented in models dictionary")
        model_class, emplacement_class = models[table_name]
        if model_class is None:
            raise NotImplementedError(f"Model class for {table_name} not yet implemented")
        return model_class, emplacement_class

    def get_port_forward_config(self) -> PortForwardConfig:
        """Get port forwarding configuration for dev environment."""
        return PortForwardConfig(
            project="clover-dev-kubernetes",
            cluster="dev-us-west1-cluster",
            region="us-west1",
            server="https://dev-us-west1-ingress-nginx.dev.pdx13.clover.network",
            kube_context="gke_clover-dev-kubernetes_us-west1_dev-us-west1-cluster",
            kube_namespace="gke-cloudsql-access",
            kube_deployment="gke-cloudsql-access",
            sql_connection="clover-dev-managed:us-west1:billing-bookkeeper",
            database_name="billing-bookkeeper-dev",
            username="billing-bookkeeper",
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
        return "DevBillingBookkeeper"
