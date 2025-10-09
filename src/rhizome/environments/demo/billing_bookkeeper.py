"""
Demo Bookkeeper environment configuration.

This module provides access to the billing-bookkeeper database in the
demo cluster through CloudSQL proxy port-forwarding.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from rhizome.environments.base import DatabaseConfig, Environment, PortForwardConfig, SecretManager
from rhizome.environments.demo.expected_data.billing_bookkeeper_adjust_action import AdjustActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_adjust_action_fee_code import AdjustActionFeeCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_adjust_action_type import AdjustActionTypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_adjust_reason import AdjustReasonDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_app_meter_action import AppMeterActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_app_meter_action_error import AppMeterActionErrorDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_app_meter_action_fee_code import AppMeterActionFeeCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_app_meter_action_type import AppMeterActionTypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_app_sub_action import AppSubActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_app_sub_action_error import AppSubActionErrorDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_app_sub_action_fee_code import AppSubActionFeeCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_app_sub_action_type import AppSubActionTypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_auto_adjust_advice import AutoAdjustAdviceDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_auto_adjust_qualifier import AutoAdjustQualifierDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_auto_adjust_rule import AutoAdjustRuleDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_archetype import BillingArchetypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_entity import BillingEntityDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_entity_config import BillingEntityConfigDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_event_history import BillingEventHistoryDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_hierarchy import BillingHierarchyDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_hierarchy_cycle import BillingHierarchyCycleDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_hierarchy_type import BillingHierarchyTypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_pseudo_entity import BillingPseudoEntityDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_billing_schedule import BillingScheduleDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_cellular_action import CellularActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_cellular_action_error import CellularActionErrorDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_cellular_action_fee_code import CellularActionFeeCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_cellular_action_type import CellularActionTypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_consumer_failure import ConsumerFailureDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_consumer_failure_history import ConsumerFailureHistoryDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_cycle_validation import CycleValidationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_cycle_validation_mutation import CycleValidationMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_deserializable_failure import DeserializableFailureDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_category import FeeCategoryDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_code import FeeCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_code_app import FeeCodeAppDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_code_ledger_account import FeeCodeLedgerAccountDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_ctd import FeeCtdDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_rate import FeeRateDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_rate_error_report import FeeRateErrorReportDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_rate_report_action_error import FeeRateReportActionErrorDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_summary import FeeSummaryDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_summary_mutation import FeeSummaryMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_tax import FeeTaxDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_tax_mutation import FeeTaxMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_fee_ytd import FeeYtdDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_flyway_schema_history import FlywaySchemaHistoryDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_invoice_alliance_code import InvoiceAllianceCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_invoice_info import InvoiceInfoDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_invoice_info_amount import InvoiceInfoAmountDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_invoice_info_mutation import InvoiceInfoMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_invoice_info_settlement import InvoiceInfoSettlementDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_invoice_info_settlement_mutation import InvoiceInfoSettlementMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_job_assassination_contract import JobAssassinationContractDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_jobrunr_backgroundjobservers import JobrunrBackgroundjobserversDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_jobrunr_jobs import JobrunrJobsDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_jobrunr_metadata import JobrunrMetadataDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_jobrunr_migrations import JobrunrMigrationsDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_jobrunr_recurring_jobs import JobrunrRecurringJobsDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account import LedgerAccountDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account_action import LedgerAccountActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account_balance import LedgerAccountBalanceDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account_key import LedgerAccountKeyDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account_key_app import LedgerAccountKeyAppDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account_key_purpose import LedgerAccountKeyPurposeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account_purpose import LedgerAccountPurposeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account_settlement import LedgerAccountSettlementDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_account_transition import LedgerAccountTransitionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_journal import LedgerJournalDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_ledger_journal_mutation import LedgerJournalMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_lexi_attribute import LexiAttributeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_lexi_rule import LexiRuleDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_look import LookDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_look_data import LookDataDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_merchant_detail import MerchantDetailDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_misc_action import MiscActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_misc_action_error import MiscActionErrorDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_misc_action_fee_code import MiscActionFeeCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_misc_action_type import MiscActionTypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_misc_specifier import MiscSpecifierDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_model_fee_summary import ModelFeeSummaryDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_monetary_adjustment import MonetaryAdjustmentDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_monetary_adjustment_mutation import MonetaryAdjustmentMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_monetary_rule_alias import MonetaryRuleAliasDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_monetary_rule_set import MonetaryRuleSetDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_monetary_rule_set_rule import MonetaryRuleSetRuleDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_partner_config import PartnerConfigDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_plan_action import PlanActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_plan_action_error import PlanActionErrorDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_plan_action_fee_code import PlanActionFeeCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_plan_action_type import PlanActionTypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_processing_group_dates import ProcessingGroupDatesDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_processing_note import ProcessingNoteDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_processing_note_mutation import ProcessingNoteMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_prototype_fee_rate import PrototypeFeeRateDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_prototype_fee_set import PrototypeFeeSetDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_revenue_action import RevenueActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_revenue_action_error import RevenueActionErrorDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_revenue_action_fee_code import RevenueActionFeeCodeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_revenue_action_type import RevenueActionTypeDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_revenue_share_group import RevenueShareGroupDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_server_config import ServerConfigDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_settlement import SettlementDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_settlement_action import SettlementActionDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_settlement_mutation import SettlementMutationDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_skip_fee_category_lexi_tag import SkipFeeCategoryLexiTagDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_tier_detail import TierDetailDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_tiered_pricing import TieredPricingDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_tiered_qualifier import TieredQualifierDemo
from rhizome.environments.demo.expected_data.billing_bookkeeper_tiered_rule import TieredRuleDemo
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
    BillingBookkeeperTable.adjust_action: (AdjustActionV1, AdjustActionDemo),
    BillingBookkeeperTable.adjust_action_fee_code: (AdjustActionFeeCodeV1, AdjustActionFeeCodeDemo),
    BillingBookkeeperTable.adjust_action_type: (AdjustActionTypeV1, AdjustActionTypeDemo),
    BillingBookkeeperTable.adjust_reason: (AdjustReasonV1, AdjustReasonDemo),
    BillingBookkeeperTable.app_meter_action: (AppMeterActionV1, AppMeterActionDemo),
    BillingBookkeeperTable.app_meter_action_error: (AppMeterActionErrorV1, AppMeterActionErrorDemo),
    BillingBookkeeperTable.app_meter_action_fee_code: (AppMeterActionFeeCodeV1, AppMeterActionFeeCodeDemo),
    BillingBookkeeperTable.app_meter_action_type: (AppMeterActionTypeV1, AppMeterActionTypeDemo),
    BillingBookkeeperTable.app_sub_action: (AppSubActionV1, AppSubActionDemo),
    BillingBookkeeperTable.app_sub_action_error: (AppSubActionErrorV1, AppSubActionErrorDemo),
    BillingBookkeeperTable.app_sub_action_fee_code: (AppSubActionFeeCodeV1, AppSubActionFeeCodeDemo),
    BillingBookkeeperTable.app_sub_action_type: (AppSubActionTypeV1, AppSubActionTypeDemo),
    BillingBookkeeperTable.auto_adjust_advice: (AutoAdjustAdviceV1, AutoAdjustAdviceDemo),
    BillingBookkeeperTable.auto_adjust_qualifier: (AutoAdjustQualifierV1, AutoAdjustQualifierDemo),
    BillingBookkeeperTable.auto_adjust_rule: (AutoAdjustRuleV1, AutoAdjustRuleDemo),
    BillingBookkeeperTable.billing_archetype: (BillingArchetypeV1, BillingArchetypeDemo),
    BillingBookkeeperTable.billing_entity: (BillingEntityV1, BillingEntityDemo),
    BillingBookkeeperTable.billing_entity_config: (BillingEntityConfigV1, BillingEntityConfigDemo),
    BillingBookkeeperTable.billing_event_history: (BillingEventHistoryV1, BillingEventHistoryDemo),
    BillingBookkeeperTable.billing_hierarchy: (BillingHierarchyV1, BillingHierarchyDemo),
    BillingBookkeeperTable.billing_hierarchy_cycle: (BillingHierarchyCycleV1, BillingHierarchyCycleDemo),
    BillingBookkeeperTable.billing_hierarchy_type: (BillingHierarchyTypeV1, BillingHierarchyTypeDemo),
    BillingBookkeeperTable.billing_pseudo_entity: (BillingPseudoEntityV1, BillingPseudoEntityDemo),
    BillingBookkeeperTable.billing_schedule: (BillingScheduleV1, BillingScheduleDemo),
    BillingBookkeeperTable.cellular_action: (CellularActionV1, CellularActionDemo),
    BillingBookkeeperTable.cellular_action_error: (CellularActionErrorV1, CellularActionErrorDemo),
    BillingBookkeeperTable.cellular_action_fee_code: (CellularActionFeeCodeV1, CellularActionFeeCodeDemo),
    BillingBookkeeperTable.cellular_action_type: (CellularActionTypeV1, CellularActionTypeDemo),
    BillingBookkeeperTable.consumer_failure: (ConsumerFailureV1, ConsumerFailureDemo),
    BillingBookkeeperTable.consumer_failure_history: (ConsumerFailureHistoryV1, ConsumerFailureHistoryDemo),
    BillingBookkeeperTable.cycle_validation: (CycleValidationV1, CycleValidationDemo),
    BillingBookkeeperTable.cycle_validation_mutation: (CycleValidationMutationV1, CycleValidationMutationDemo),
    BillingBookkeeperTable.deserializable_failure: (DeserializableFailureV1, DeserializableFailureDemo),
    BillingBookkeeperTable.fee_category: (FeeCategoryV1, FeeCategoryDemo),
    BillingBookkeeperTable.fee_code: (FeeCodeV1, FeeCodeDemo),
    BillingBookkeeperTable.fee_code_app: (FeeCodeAppV1, FeeCodeAppDemo),
    BillingBookkeeperTable.fee_code_ledger_account: (FeeCodeLedgerAccountV1, FeeCodeLedgerAccountDemo),
    BillingBookkeeperTable.fee_ctd: (FeeCtdV1, FeeCtdDemo),
    BillingBookkeeperTable.fee_rate: (FeeRateV1, FeeRateDemo),
    BillingBookkeeperTable.fee_rate_error_report: (FeeRateErrorReportV1, FeeRateErrorReportDemo),
    BillingBookkeeperTable.fee_rate_report_action_error: (FeeRateReportActionErrorV1, FeeRateReportActionErrorDemo),
    BillingBookkeeperTable.fee_summary: (FeeSummaryV1, FeeSummaryDemo),
    BillingBookkeeperTable.fee_summary_mutation: (FeeSummaryMutationV1, FeeSummaryMutationDemo),
    BillingBookkeeperTable.fee_tax: (FeeTaxV1, FeeTaxDemo),
    BillingBookkeeperTable.fee_tax_mutation: (FeeTaxMutationV1, FeeTaxMutationDemo),
    BillingBookkeeperTable.fee_ytd: (FeeYtdV1, FeeYtdDemo),
    BillingBookkeeperTable.flyway_schema_history: (FlywaySchemaHistoryV1, FlywaySchemaHistoryDemo),
    BillingBookkeeperTable.invoice_alliance_code: (InvoiceAllianceCodeV1, InvoiceAllianceCodeDemo),
    BillingBookkeeperTable.invoice_info: (InvoiceInfoV1, InvoiceInfoDemo),
    BillingBookkeeperTable.invoice_info_amount: (InvoiceInfoAmountV1, InvoiceInfoAmountDemo),
    BillingBookkeeperTable.invoice_info_mutation: (InvoiceInfoMutationV1, InvoiceInfoMutationDemo),
    BillingBookkeeperTable.invoice_info_settlement: (InvoiceInfoSettlementV1, InvoiceInfoSettlementDemo),
    BillingBookkeeperTable.invoice_info_settlement_mutation: (InvoiceInfoSettlementMutationV1, InvoiceInfoSettlementMutationDemo),
    BillingBookkeeperTable.job_assassination_contract: (JobAssassinationContractV1, JobAssassinationContractDemo),
    BillingBookkeeperTable.jobrunr_backgroundjobservers: (JobrunrBackgroundjobserversV1, JobrunrBackgroundjobserversDemo),
    BillingBookkeeperTable.jobrunr_jobs: (JobrunrJobsV1, JobrunrJobsDemo),
    BillingBookkeeperTable.jobrunr_metadata: (JobrunrMetadataV1, JobrunrMetadataDemo),
    BillingBookkeeperTable.jobrunr_migrations: (JobrunrMigrationsV1, JobrunrMigrationsDemo),
    BillingBookkeeperTable.jobrunr_recurring_jobs: (JobrunrRecurringJobsV1, JobrunrRecurringJobsDemo),
    BillingBookkeeperTable.ledger_account: (LedgerAccountV1, LedgerAccountDemo),
    BillingBookkeeperTable.ledger_account_action: (LedgerAccountActionV1, LedgerAccountActionDemo),
    BillingBookkeeperTable.ledger_account_balance: (LedgerAccountBalanceV1, LedgerAccountBalanceDemo),
    BillingBookkeeperTable.ledger_account_key: (LedgerAccountKeyV1, LedgerAccountKeyDemo),
    BillingBookkeeperTable.ledger_account_key_app: (LedgerAccountKeyAppV1, LedgerAccountKeyAppDemo),
    BillingBookkeeperTable.ledger_account_key_purpose: (LedgerAccountKeyPurposeV1, LedgerAccountKeyPurposeDemo),
    BillingBookkeeperTable.ledger_account_purpose: (LedgerAccountPurposeV1, LedgerAccountPurposeDemo),
    BillingBookkeeperTable.ledger_account_settlement: (LedgerAccountSettlementV1, LedgerAccountSettlementDemo),
    BillingBookkeeperTable.ledger_account_transition: (LedgerAccountTransitionV1, LedgerAccountTransitionDemo),
    BillingBookkeeperTable.ledger_journal: (LedgerJournalV1, LedgerJournalDemo),
    BillingBookkeeperTable.ledger_journal_mutation: (LedgerJournalMutationV1, LedgerJournalMutationDemo),
    BillingBookkeeperTable.lexi_attribute: (LexiAttributeV1, LexiAttributeDemo),
    BillingBookkeeperTable.lexi_rule: (LexiRuleV1, LexiRuleDemo),
    BillingBookkeeperTable.look: (LookV1, LookDemo),
    BillingBookkeeperTable.look_data: (LookDataV1, LookDataDemo),
    BillingBookkeeperTable.merchant_detail: (MerchantDetailV1, MerchantDetailDemo),
    BillingBookkeeperTable.misc_action: (MiscActionV1, MiscActionDemo),
    BillingBookkeeperTable.misc_action_error: (MiscActionErrorV1, MiscActionErrorDemo),
    BillingBookkeeperTable.misc_action_fee_code: (MiscActionFeeCodeV1, MiscActionFeeCodeDemo),
    BillingBookkeeperTable.misc_action_type: (MiscActionTypeV1, MiscActionTypeDemo),
    BillingBookkeeperTable.misc_specifier: (MiscSpecifierV1, MiscSpecifierDemo),
    BillingBookkeeperTable.model_fee_summary: (ModelFeeSummaryV1, ModelFeeSummaryDemo),
    BillingBookkeeperTable.monetary_adjustment: (MonetaryAdjustmentV1, MonetaryAdjustmentDemo),
    BillingBookkeeperTable.monetary_adjustment_mutation: (MonetaryAdjustmentMutationV1, MonetaryAdjustmentMutationDemo),
    BillingBookkeeperTable.monetary_rule_alias: (MonetaryRuleAliasV1, MonetaryRuleAliasDemo),
    BillingBookkeeperTable.monetary_rule_set: (MonetaryRuleSetV1, MonetaryRuleSetDemo),
    BillingBookkeeperTable.monetary_rule_set_rule: (MonetaryRuleSetRuleV1, MonetaryRuleSetRuleDemo),
    BillingBookkeeperTable.partner_config: (PartnerConfigV1, PartnerConfigDemo),
    BillingBookkeeperTable.plan_action: (PlanActionV1, PlanActionDemo),
    BillingBookkeeperTable.plan_action_error: (PlanActionErrorV1, PlanActionErrorDemo),
    BillingBookkeeperTable.plan_action_fee_code: (PlanActionFeeCodeV1, PlanActionFeeCodeDemo),
    BillingBookkeeperTable.plan_action_type: (PlanActionTypeV1, PlanActionTypeDemo),
    BillingBookkeeperTable.processing_group_dates: (ProcessingGroupDatesV1, ProcessingGroupDatesDemo),
    BillingBookkeeperTable.processing_note: (ProcessingNoteV1, ProcessingNoteDemo),
    BillingBookkeeperTable.processing_note_mutation: (ProcessingNoteMutationV1, ProcessingNoteMutationDemo),
    BillingBookkeeperTable.prototype_fee_rate: (PrototypeFeeRateV1, PrototypeFeeRateDemo),
    BillingBookkeeperTable.prototype_fee_set: (PrototypeFeeSetV1, PrototypeFeeSetDemo),
    BillingBookkeeperTable.revenue_action: (RevenueActionV1, RevenueActionDemo),
    BillingBookkeeperTable.revenue_action_error: (RevenueActionErrorV1, RevenueActionErrorDemo),
    BillingBookkeeperTable.revenue_action_fee_code: (RevenueActionFeeCodeV1, RevenueActionFeeCodeDemo),
    BillingBookkeeperTable.revenue_action_type: (RevenueActionTypeV1, RevenueActionTypeDemo),
    BillingBookkeeperTable.revenue_share_group: (RevenueShareGroupV1, RevenueShareGroupDemo),
    BillingBookkeeperTable.server_config: (ServerConfigV1, ServerConfigDemo),
    BillingBookkeeperTable.settlement: (SettlementV1, SettlementDemo),
    BillingBookkeeperTable.settlement_action: (SettlementActionV1, SettlementActionDemo),
    BillingBookkeeperTable.settlement_mutation: (SettlementMutationV1, SettlementMutationDemo),
    BillingBookkeeperTable.skip_fee_category_lexi_tag: (SkipFeeCategoryLexiTagV1, SkipFeeCategoryLexiTagDemo),
    BillingBookkeeperTable.tier_detail: (TierDetailV1, TierDetailDemo),
    BillingBookkeeperTable.tiered_pricing: (TieredPricingV1, TieredPricingDemo),
    BillingBookkeeperTable.tiered_qualifier: (TieredQualifierV1, TieredQualifierDemo),
    BillingBookkeeperTable.tiered_rule: (TieredRuleV1, TieredRuleDemo),
}


class DemoBillingBookkeeper(Environment):
    """Demo bookkeeper environment using CloudSQL."""

    def tables(self) -> list[StrEnum]:
        return list(BillingBookkeeperTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel], type[Emplacement[Any]]]:
        if not isinstance(table_name, BillingBookkeeperTable):
            raise ValueError(f"Expected BillingBookkeeperTable, got {type(table_name)}")
        if table_name not in models:
            raise NotImplementedError(f"Table {table_name} not yet implemented in models dictionary")
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
            sql_connection="clover-dev-managed:us-west1:billing-bookkeeper-demo2",
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
        return "DemoBillingBookkeeper"
