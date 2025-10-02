from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.properties_order_title import PropertiesOrderTitle
from ..types import UNSET, Unset

T = TypeVar("T", bound="Properties")


@_attrs_define
class Properties:
    """
    Attributes:
        default_currency (Union[Unset, str]):
        tips_enabled (Union[Unset, bool]):
        max_tip_percentage (Union[Unset, int]):
        receipt_properties (Union[Unset, str]):
        summary_hour (Union[Unset, int]):
        signature_threshold (Union[Unset, int]):
        has_default_employee (Union[Unset, bool]):
        tip_rate_default (Union[Unset, int]):
        on_paper_tip_signatures (Union[Unset, bool]):
        no_signature_program_eligible (Union[Unset, bool]):
        auto_logout (Union[Unset, bool]):
        order_title (Union[Unset, PropertiesOrderTitle]):
        order_title_max (Union[Unset, int]):
        reset_on_reporting_time (Union[Unset, bool]):
        notes_on_orders (Union[Unset, bool]):
        delete_orders (Union[Unset, bool]):
        remove_tax_enabled (Union[Unset, bool]):
        group_line_items (Union[Unset, bool]):
        alternate_inventory_names (Union[Unset, bool]):
        auto_print (Union[Unset, bool]):
        hardware_profile (Union[Unset, str]):
        infolease_suppress_billing (Union[Unset, bool]):
        infolease_suppress_plan_billing (Union[Unset, bool]):
        shipping_address (Union[Unset, str]):
        marketing_enabled (Union[Unset, bool]):
        marketing_preference_text (Union[Unset, str]):
        bank_marker (Union[Unset, int]):
        support_phone (Union[Unset, str]):
        support_email (Union[Unset, str]):
        manual_closeout (Union[Unset, bool]):
        show_closeout_orders (Union[Unset, bool]):
        send_closeout_email (Union[Unset, bool]):
        stay_in_category (Union[Unset, bool]):
        locale (Union[Unset, str]):
        timezone (Union[Unset, str]):
        vat (Union[Unset, bool]):
        vat_tax_name (Union[Unset, str]):
        app_billing_system (Union[Unset, str]):
        aba_account_number (Union[Unset, str]):
        dda_account_number (Union[Unset, str]):
        track_stock (Union[Unset, bool]):
        update_stock (Union[Unset, bool]):
        allow_clock_out_with_open_orders (Union[Unset, bool]):
        log_in_clock_in_prompt (Union[Unset, bool]):
        account_type (Union[Unset, str]):
        pin_length (Union[Unset, int]):
        cash_back_enabled (Union[Unset, bool]):
        case_back_options (Union[Unset, str]):
        cash_back_options (Union[Unset, str]):
        max_cash_back (Union[Unset, int]):
        hierarchy (Union[Unset, str]):
        has_consented (Union[Unset, bool]):
        merchant_boarding_status (Union[Unset, str]):
        alwaysrequire_signature (Union[Unset, bool]):
        printed_first_data_receipt_logo_enabled (Union[Unset, bool]):
        privacy_policy_mode (Union[Unset, str]):
        merchant_privacy_policy_url (Union[Unset, str]):
        disable_print_taxes_payment_on_receipts (Union[Unset, bool]):
    """

    default_currency: Union[Unset, str] = UNSET
    tips_enabled: Union[Unset, bool] = UNSET
    max_tip_percentage: Union[Unset, int] = UNSET
    receipt_properties: Union[Unset, str] = UNSET
    summary_hour: Union[Unset, int] = UNSET
    signature_threshold: Union[Unset, int] = UNSET
    has_default_employee: Union[Unset, bool] = UNSET
    tip_rate_default: Union[Unset, int] = UNSET
    on_paper_tip_signatures: Union[Unset, bool] = UNSET
    no_signature_program_eligible: Union[Unset, bool] = UNSET
    auto_logout: Union[Unset, bool] = UNSET
    order_title: Union[Unset, PropertiesOrderTitle] = UNSET
    order_title_max: Union[Unset, int] = UNSET
    reset_on_reporting_time: Union[Unset, bool] = UNSET
    notes_on_orders: Union[Unset, bool] = UNSET
    delete_orders: Union[Unset, bool] = UNSET
    remove_tax_enabled: Union[Unset, bool] = UNSET
    group_line_items: Union[Unset, bool] = UNSET
    alternate_inventory_names: Union[Unset, bool] = UNSET
    auto_print: Union[Unset, bool] = UNSET
    hardware_profile: Union[Unset, str] = UNSET
    infolease_suppress_billing: Union[Unset, bool] = UNSET
    infolease_suppress_plan_billing: Union[Unset, bool] = UNSET
    shipping_address: Union[Unset, str] = UNSET
    marketing_enabled: Union[Unset, bool] = UNSET
    marketing_preference_text: Union[Unset, str] = UNSET
    bank_marker: Union[Unset, int] = UNSET
    support_phone: Union[Unset, str] = UNSET
    support_email: Union[Unset, str] = UNSET
    manual_closeout: Union[Unset, bool] = UNSET
    show_closeout_orders: Union[Unset, bool] = UNSET
    send_closeout_email: Union[Unset, bool] = UNSET
    stay_in_category: Union[Unset, bool] = UNSET
    locale: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    vat: Union[Unset, bool] = UNSET
    vat_tax_name: Union[Unset, str] = UNSET
    app_billing_system: Union[Unset, str] = UNSET
    aba_account_number: Union[Unset, str] = UNSET
    dda_account_number: Union[Unset, str] = UNSET
    track_stock: Union[Unset, bool] = UNSET
    update_stock: Union[Unset, bool] = UNSET
    allow_clock_out_with_open_orders: Union[Unset, bool] = UNSET
    log_in_clock_in_prompt: Union[Unset, bool] = UNSET
    account_type: Union[Unset, str] = UNSET
    pin_length: Union[Unset, int] = UNSET
    cash_back_enabled: Union[Unset, bool] = UNSET
    case_back_options: Union[Unset, str] = UNSET
    cash_back_options: Union[Unset, str] = UNSET
    max_cash_back: Union[Unset, int] = UNSET
    hierarchy: Union[Unset, str] = UNSET
    has_consented: Union[Unset, bool] = UNSET
    merchant_boarding_status: Union[Unset, str] = UNSET
    alwaysrequire_signature: Union[Unset, bool] = UNSET
    printed_first_data_receipt_logo_enabled: Union[Unset, bool] = UNSET
    privacy_policy_mode: Union[Unset, str] = UNSET
    merchant_privacy_policy_url: Union[Unset, str] = UNSET
    disable_print_taxes_payment_on_receipts: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_currency = self.default_currency

        tips_enabled = self.tips_enabled

        max_tip_percentage = self.max_tip_percentage

        receipt_properties = self.receipt_properties

        summary_hour = self.summary_hour

        signature_threshold = self.signature_threshold

        has_default_employee = self.has_default_employee

        tip_rate_default = self.tip_rate_default

        on_paper_tip_signatures = self.on_paper_tip_signatures

        no_signature_program_eligible = self.no_signature_program_eligible

        auto_logout = self.auto_logout

        order_title: Union[Unset, str] = UNSET
        if not isinstance(self.order_title, Unset):
            order_title = self.order_title.value

        order_title_max = self.order_title_max

        reset_on_reporting_time = self.reset_on_reporting_time

        notes_on_orders = self.notes_on_orders

        delete_orders = self.delete_orders

        remove_tax_enabled = self.remove_tax_enabled

        group_line_items = self.group_line_items

        alternate_inventory_names = self.alternate_inventory_names

        auto_print = self.auto_print

        hardware_profile = self.hardware_profile

        infolease_suppress_billing = self.infolease_suppress_billing

        infolease_suppress_plan_billing = self.infolease_suppress_plan_billing

        shipping_address = self.shipping_address

        marketing_enabled = self.marketing_enabled

        marketing_preference_text = self.marketing_preference_text

        bank_marker = self.bank_marker

        support_phone = self.support_phone

        support_email = self.support_email

        manual_closeout = self.manual_closeout

        show_closeout_orders = self.show_closeout_orders

        send_closeout_email = self.send_closeout_email

        stay_in_category = self.stay_in_category

        locale = self.locale

        timezone = self.timezone

        vat = self.vat

        vat_tax_name = self.vat_tax_name

        app_billing_system = self.app_billing_system

        aba_account_number = self.aba_account_number

        dda_account_number = self.dda_account_number

        track_stock = self.track_stock

        update_stock = self.update_stock

        allow_clock_out_with_open_orders = self.allow_clock_out_with_open_orders

        log_in_clock_in_prompt = self.log_in_clock_in_prompt

        account_type = self.account_type

        pin_length = self.pin_length

        cash_back_enabled = self.cash_back_enabled

        case_back_options = self.case_back_options

        cash_back_options = self.cash_back_options

        max_cash_back = self.max_cash_back

        hierarchy = self.hierarchy

        has_consented = self.has_consented

        merchant_boarding_status = self.merchant_boarding_status

        alwaysrequire_signature = self.alwaysrequire_signature

        printed_first_data_receipt_logo_enabled = self.printed_first_data_receipt_logo_enabled

        privacy_policy_mode = self.privacy_policy_mode

        merchant_privacy_policy_url = self.merchant_privacy_policy_url

        disable_print_taxes_payment_on_receipts = self.disable_print_taxes_payment_on_receipts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if tips_enabled is not UNSET:
            field_dict["tipsEnabled"] = tips_enabled
        if max_tip_percentage is not UNSET:
            field_dict["maxTipPercentage"] = max_tip_percentage
        if receipt_properties is not UNSET:
            field_dict["receiptProperties"] = receipt_properties
        if summary_hour is not UNSET:
            field_dict["summaryHour"] = summary_hour
        if signature_threshold is not UNSET:
            field_dict["signatureThreshold"] = signature_threshold
        if has_default_employee is not UNSET:
            field_dict["hasDefaultEmployee"] = has_default_employee
        if tip_rate_default is not UNSET:
            field_dict["tipRateDefault"] = tip_rate_default
        if on_paper_tip_signatures is not UNSET:
            field_dict["onPaperTipSignatures"] = on_paper_tip_signatures
        if no_signature_program_eligible is not UNSET:
            field_dict["noSignatureProgramEligible"] = no_signature_program_eligible
        if auto_logout is not UNSET:
            field_dict["autoLogout"] = auto_logout
        if order_title is not UNSET:
            field_dict["orderTitle"] = order_title
        if order_title_max is not UNSET:
            field_dict["orderTitleMax"] = order_title_max
        if reset_on_reporting_time is not UNSET:
            field_dict["resetOnReportingTime"] = reset_on_reporting_time
        if notes_on_orders is not UNSET:
            field_dict["notesOnOrders"] = notes_on_orders
        if delete_orders is not UNSET:
            field_dict["deleteOrders"] = delete_orders
        if remove_tax_enabled is not UNSET:
            field_dict["removeTaxEnabled"] = remove_tax_enabled
        if group_line_items is not UNSET:
            field_dict["groupLineItems"] = group_line_items
        if alternate_inventory_names is not UNSET:
            field_dict["alternateInventoryNames"] = alternate_inventory_names
        if auto_print is not UNSET:
            field_dict["autoPrint"] = auto_print
        if hardware_profile is not UNSET:
            field_dict["hardwareProfile"] = hardware_profile
        if infolease_suppress_billing is not UNSET:
            field_dict["infoleaseSuppressBilling"] = infolease_suppress_billing
        if infolease_suppress_plan_billing is not UNSET:
            field_dict["infoleaseSuppressPlanBilling"] = infolease_suppress_plan_billing
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if marketing_enabled is not UNSET:
            field_dict["marketingEnabled"] = marketing_enabled
        if marketing_preference_text is not UNSET:
            field_dict["marketingPreferenceText"] = marketing_preference_text
        if bank_marker is not UNSET:
            field_dict["bankMarker"] = bank_marker
        if support_phone is not UNSET:
            field_dict["supportPhone"] = support_phone
        if support_email is not UNSET:
            field_dict["supportEmail"] = support_email
        if manual_closeout is not UNSET:
            field_dict["manualCloseout"] = manual_closeout
        if show_closeout_orders is not UNSET:
            field_dict["showCloseoutOrders"] = show_closeout_orders
        if send_closeout_email is not UNSET:
            field_dict["sendCloseoutEmail"] = send_closeout_email
        if stay_in_category is not UNSET:
            field_dict["stayInCategory"] = stay_in_category
        if locale is not UNSET:
            field_dict["locale"] = locale
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if vat is not UNSET:
            field_dict["vat"] = vat
        if vat_tax_name is not UNSET:
            field_dict["vatTaxName"] = vat_tax_name
        if app_billing_system is not UNSET:
            field_dict["appBillingSystem"] = app_billing_system
        if aba_account_number is not UNSET:
            field_dict["abaAccountNumber"] = aba_account_number
        if dda_account_number is not UNSET:
            field_dict["ddaAccountNumber"] = dda_account_number
        if track_stock is not UNSET:
            field_dict["trackStock"] = track_stock
        if update_stock is not UNSET:
            field_dict["updateStock"] = update_stock
        if allow_clock_out_with_open_orders is not UNSET:
            field_dict["allowClockOutWithOpenOrders"] = allow_clock_out_with_open_orders
        if log_in_clock_in_prompt is not UNSET:
            field_dict["logInClockInPrompt"] = log_in_clock_in_prompt
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if pin_length is not UNSET:
            field_dict["pinLength"] = pin_length
        if cash_back_enabled is not UNSET:
            field_dict["cashBackEnabled"] = cash_back_enabled
        if case_back_options is not UNSET:
            field_dict["caseBackOptions"] = case_back_options
        if cash_back_options is not UNSET:
            field_dict["cashBackOptions"] = cash_back_options
        if max_cash_back is not UNSET:
            field_dict["maxCashBack"] = max_cash_back
        if hierarchy is not UNSET:
            field_dict["hierarchy"] = hierarchy
        if has_consented is not UNSET:
            field_dict["hasConsented"] = has_consented
        if merchant_boarding_status is not UNSET:
            field_dict["merchantBoardingStatus"] = merchant_boarding_status
        if alwaysrequire_signature is not UNSET:
            field_dict["alwaysrequireSignature"] = alwaysrequire_signature
        if printed_first_data_receipt_logo_enabled is not UNSET:
            field_dict["printedFirstDataReceiptLogoEnabled"] = printed_first_data_receipt_logo_enabled
        if privacy_policy_mode is not UNSET:
            field_dict["privacyPolicyMode"] = privacy_policy_mode
        if merchant_privacy_policy_url is not UNSET:
            field_dict["merchantPrivacyPolicyUrl"] = merchant_privacy_policy_url
        if disable_print_taxes_payment_on_receipts is not UNSET:
            field_dict["disablePrintTaxesPaymentOnReceipts"] = disable_print_taxes_payment_on_receipts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_currency = d.pop("defaultCurrency", UNSET)

        tips_enabled = d.pop("tipsEnabled", UNSET)

        max_tip_percentage = d.pop("maxTipPercentage", UNSET)

        receipt_properties = d.pop("receiptProperties", UNSET)

        summary_hour = d.pop("summaryHour", UNSET)

        signature_threshold = d.pop("signatureThreshold", UNSET)

        has_default_employee = d.pop("hasDefaultEmployee", UNSET)

        tip_rate_default = d.pop("tipRateDefault", UNSET)

        on_paper_tip_signatures = d.pop("onPaperTipSignatures", UNSET)

        no_signature_program_eligible = d.pop("noSignatureProgramEligible", UNSET)

        auto_logout = d.pop("autoLogout", UNSET)

        _order_title = d.pop("orderTitle", UNSET)
        order_title: Union[Unset, PropertiesOrderTitle]
        if isinstance(_order_title, Unset):
            order_title = UNSET
        else:
            order_title = PropertiesOrderTitle(_order_title)

        order_title_max = d.pop("orderTitleMax", UNSET)

        reset_on_reporting_time = d.pop("resetOnReportingTime", UNSET)

        notes_on_orders = d.pop("notesOnOrders", UNSET)

        delete_orders = d.pop("deleteOrders", UNSET)

        remove_tax_enabled = d.pop("removeTaxEnabled", UNSET)

        group_line_items = d.pop("groupLineItems", UNSET)

        alternate_inventory_names = d.pop("alternateInventoryNames", UNSET)

        auto_print = d.pop("autoPrint", UNSET)

        hardware_profile = d.pop("hardwareProfile", UNSET)

        infolease_suppress_billing = d.pop("infoleaseSuppressBilling", UNSET)

        infolease_suppress_plan_billing = d.pop("infoleaseSuppressPlanBilling", UNSET)

        shipping_address = d.pop("shippingAddress", UNSET)

        marketing_enabled = d.pop("marketingEnabled", UNSET)

        marketing_preference_text = d.pop("marketingPreferenceText", UNSET)

        bank_marker = d.pop("bankMarker", UNSET)

        support_phone = d.pop("supportPhone", UNSET)

        support_email = d.pop("supportEmail", UNSET)

        manual_closeout = d.pop("manualCloseout", UNSET)

        show_closeout_orders = d.pop("showCloseoutOrders", UNSET)

        send_closeout_email = d.pop("sendCloseoutEmail", UNSET)

        stay_in_category = d.pop("stayInCategory", UNSET)

        locale = d.pop("locale", UNSET)

        timezone = d.pop("timezone", UNSET)

        vat = d.pop("vat", UNSET)

        vat_tax_name = d.pop("vatTaxName", UNSET)

        app_billing_system = d.pop("appBillingSystem", UNSET)

        aba_account_number = d.pop("abaAccountNumber", UNSET)

        dda_account_number = d.pop("ddaAccountNumber", UNSET)

        track_stock = d.pop("trackStock", UNSET)

        update_stock = d.pop("updateStock", UNSET)

        allow_clock_out_with_open_orders = d.pop("allowClockOutWithOpenOrders", UNSET)

        log_in_clock_in_prompt = d.pop("logInClockInPrompt", UNSET)

        account_type = d.pop("accountType", UNSET)

        pin_length = d.pop("pinLength", UNSET)

        cash_back_enabled = d.pop("cashBackEnabled", UNSET)

        case_back_options = d.pop("caseBackOptions", UNSET)

        cash_back_options = d.pop("cashBackOptions", UNSET)

        max_cash_back = d.pop("maxCashBack", UNSET)

        hierarchy = d.pop("hierarchy", UNSET)

        has_consented = d.pop("hasConsented", UNSET)

        merchant_boarding_status = d.pop("merchantBoardingStatus", UNSET)

        alwaysrequire_signature = d.pop("alwaysrequireSignature", UNSET)

        printed_first_data_receipt_logo_enabled = d.pop("printedFirstDataReceiptLogoEnabled", UNSET)

        privacy_policy_mode = d.pop("privacyPolicyMode", UNSET)

        merchant_privacy_policy_url = d.pop("merchantPrivacyPolicyUrl", UNSET)

        disable_print_taxes_payment_on_receipts = d.pop("disablePrintTaxesPaymentOnReceipts", UNSET)

        properties = cls(
            default_currency=default_currency,
            tips_enabled=tips_enabled,
            max_tip_percentage=max_tip_percentage,
            receipt_properties=receipt_properties,
            summary_hour=summary_hour,
            signature_threshold=signature_threshold,
            has_default_employee=has_default_employee,
            tip_rate_default=tip_rate_default,
            on_paper_tip_signatures=on_paper_tip_signatures,
            no_signature_program_eligible=no_signature_program_eligible,
            auto_logout=auto_logout,
            order_title=order_title,
            order_title_max=order_title_max,
            reset_on_reporting_time=reset_on_reporting_time,
            notes_on_orders=notes_on_orders,
            delete_orders=delete_orders,
            remove_tax_enabled=remove_tax_enabled,
            group_line_items=group_line_items,
            alternate_inventory_names=alternate_inventory_names,
            auto_print=auto_print,
            hardware_profile=hardware_profile,
            infolease_suppress_billing=infolease_suppress_billing,
            infolease_suppress_plan_billing=infolease_suppress_plan_billing,
            shipping_address=shipping_address,
            marketing_enabled=marketing_enabled,
            marketing_preference_text=marketing_preference_text,
            bank_marker=bank_marker,
            support_phone=support_phone,
            support_email=support_email,
            manual_closeout=manual_closeout,
            show_closeout_orders=show_closeout_orders,
            send_closeout_email=send_closeout_email,
            stay_in_category=stay_in_category,
            locale=locale,
            timezone=timezone,
            vat=vat,
            vat_tax_name=vat_tax_name,
            app_billing_system=app_billing_system,
            aba_account_number=aba_account_number,
            dda_account_number=dda_account_number,
            track_stock=track_stock,
            update_stock=update_stock,
            allow_clock_out_with_open_orders=allow_clock_out_with_open_orders,
            log_in_clock_in_prompt=log_in_clock_in_prompt,
            account_type=account_type,
            pin_length=pin_length,
            cash_back_enabled=cash_back_enabled,
            case_back_options=case_back_options,
            cash_back_options=cash_back_options,
            max_cash_back=max_cash_back,
            hierarchy=hierarchy,
            has_consented=has_consented,
            merchant_boarding_status=merchant_boarding_status,
            alwaysrequire_signature=alwaysrequire_signature,
            printed_first_data_receipt_logo_enabled=printed_first_data_receipt_logo_enabled,
            privacy_policy_mode=privacy_policy_mode,
            merchant_privacy_policy_url=merchant_privacy_policy_url,
            disable_print_taxes_payment_on_receipts=disable_print_taxes_payment_on_receipts,
        )

        properties.additional_properties = d
        return properties

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
