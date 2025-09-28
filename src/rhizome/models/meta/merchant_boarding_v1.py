"""
SQLModel definition for the merchant_boarding table, version 1.

This module provides the V1 implementation of the MerchantBoarding model.
Currently, MerchantBoardingV1 is identical to the base MerchantBoarding class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .merchant_boarding import MerchantBoarding


class MerchantBoardingV1(MerchantBoarding, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantBoarding model.

    Currently a name-only inheritance from the base MerchantBoarding class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_boarding"

    def sanitize(self) -> MerchantBoardingV1:
        """Return a sanitized copy of this MerchantBoardingV1 instance."""
        return MerchantBoardingV1(
            account_funding=self.account_funding,
            account_status=self.account_status,
            account_status_modified_time=self.account_status_modified_time,
            ach_bank_id=self.ach_bank_id,
            agent_bank_indicator=self.agent_bank_indicator,
            alt_value_link_mid=self.alt_value_link_mid,
            auth_limit=self.auth_limit,
            bank_number=self.bank_number,
            bill_to_name=self.bill_to_name,
            business_type=self.business_type,
            charge_back_retrieval_address_flag=self.charge_back_retrieval_address_flag,
            client_representative=self.client_representative,
            created_time=self.created_time,
            credit_limit=self.credit_limit,
            daylight_savings=self.daylight_savings,
            direct_marketing=self.direct_marketing,
            dynamic_dba=self.dynamic_dba,
            emv_allowed=self.emv_allowed,
            external_merchant=self.external_merchant,
            fax_phone=self.fax_phone,
            foreign_domestic_indicator=self.foreign_domestic_indicator,
            id=self.id,
            internet_indicator=self.internet_indicator,
            lease_company_code=self.lease_company_code,
            link_from=self.link_from,
            link_to=self.link_to,
            mastercard_debit_accept=self.mastercard_debit_accept,
            merchant_auth_type=self.merchant_auth_type,
            merchant_data=self.merchant_data,
            merchant_id=self.merchant_id,
            merchant_type=self.merchant_type,
            modified_time=self.modified_time,
            multi_currency_indicator=self.multi_currency_indicator,
            multi_merchant_type=self.multi_merchant_type,
            non_mpa_indicator=self.non_mpa_indicator,
            parent_merchant_id=self.parent_merchant_id,
            participant_relationship=self.participant_relationship,
            partner_id=self.partner_id,
            preferred_merchant=self.preferred_merchant,
            previous_account_status=self.previous_account_status,
            process_mode=self.process_mode,
            process_settlement=self.process_settlement,
            receipt_dba=self.receipt_dba,
            recurring_flag=self.recurring_flag,
            relationship_manager=self.relationship_manager,
            retail_description=self.retail_description,
            sale_limit=self.sale_limit,
            salesman=self.salesman,
            seasonal=self.seasonal,
            signing_key=self.signing_key,
            source_indicator=self.source_indicator,
            store=self.store,
            sys_prin=self.sys_prin,
            tax_exempt=self.tax_exempt,
            tax_id=self.tax_id,
            trans_armor_indicator=self.trans_armor_indicator,
            trans_armor_key=self.trans_armor_key,
            value_link=self.value_link,
            value_link_mid=self.value_link_mid,
            vi_relationship_participant=self.vi_relationship_participant,
            visa_debit_accept=self.visa_debit_accept,
            visa_iram=self.visa_iram,
        )
