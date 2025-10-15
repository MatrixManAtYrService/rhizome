from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debit_refund import DebitRefund
    from ..models.reference import Reference
    from ..models.vaulted_card import VaultedCard


T = TypeVar("T", bound="CardTransaction")


@_attrs_define
class CardTransaction:
    """Information about the card used for credit/debit card payments

    Attributes:
        payment_ref (Union[Unset, Reference]):
        refund_ref (Union[Unset, Reference]):
        credit_ref (Union[Unset, Reference]):
        card_type (Union[Unset, str]): Indicates whether this merchant tender is editable
        entry_type (Union[Unset, str]): Indicates whether this merchant tender is editable
        first6 (Union[Unset, str]): First six digits of the card number
        last4 (Union[Unset, str]): Last four digits of the card number
        type_ (Union[Unset, str]): Type of card transaction
        auth_code (Union[Unset, str]): Authorization code, if successful
        reference_id (Union[Unset, str]): Reference identifier
        transaction_no (Union[Unset, str]): Transaction number
        state (Union[Unset, str]): State inferred from transaction type and whether the gateway captured the transaction
        beg_balance (Union[Unset, int]): Beginning balance
        end_balance (Union[Unset, int]): Ending balance
        avs_result (Union[Unset, str]): Address Verification Service (AVS) result
        cardholder_name (Union[Unset, str]): Name of cardholder
        token (Union[Unset, str]): Token for vaulted card which can be used for subsequent transactions
        vaulted_card (Union[Unset, VaultedCard]): Vaulted card which can be used for subsequent transactions
        gateway_tx_state (Union[Unset, str]): State as currently recorded. This differs from the legacy 'state' field;
            the legacy 'state' field is calculated from the 'type' field and whether the transaction was captured.
        currency (Union[Unset, str]): Currency code
        captured (Union[Unset, bool]):
        debit_refund (Union[Unset, DebitRefund]): Vaulted card which can be used for subsequent transactions
    """

    payment_ref: Union[Unset, "Reference"] = UNSET
    refund_ref: Union[Unset, "Reference"] = UNSET
    credit_ref: Union[Unset, "Reference"] = UNSET
    card_type: Union[Unset, str] = UNSET
    entry_type: Union[Unset, str] = UNSET
    first6: Union[Unset, str] = UNSET
    last4: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    auth_code: Union[Unset, str] = UNSET
    reference_id: Union[Unset, str] = UNSET
    transaction_no: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    beg_balance: Union[Unset, int] = UNSET
    end_balance: Union[Unset, int] = UNSET
    avs_result: Union[Unset, str] = UNSET
    cardholder_name: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    vaulted_card: Union[Unset, "VaultedCard"] = UNSET
    gateway_tx_state: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    captured: Union[Unset, bool] = UNSET
    debit_refund: Union[Unset, "DebitRefund"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_ref, Unset):
            payment_ref = self.payment_ref.to_dict()

        refund_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.refund_ref, Unset):
            refund_ref = self.refund_ref.to_dict()

        credit_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credit_ref, Unset):
            credit_ref = self.credit_ref.to_dict()

        card_type = self.card_type

        entry_type = self.entry_type

        first6 = self.first6

        last4 = self.last4

        type_ = self.type_

        auth_code = self.auth_code

        reference_id = self.reference_id

        transaction_no = self.transaction_no

        state = self.state

        beg_balance = self.beg_balance

        end_balance = self.end_balance

        avs_result = self.avs_result

        cardholder_name = self.cardholder_name

        token = self.token

        vaulted_card: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vaulted_card, Unset):
            vaulted_card = self.vaulted_card.to_dict()

        gateway_tx_state = self.gateway_tx_state

        currency = self.currency

        captured = self.captured

        debit_refund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.debit_refund, Unset):
            debit_refund = self.debit_refund.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_ref is not UNSET:
            field_dict["paymentRef"] = payment_ref
        if refund_ref is not UNSET:
            field_dict["refundRef"] = refund_ref
        if credit_ref is not UNSET:
            field_dict["creditRef"] = credit_ref
        if card_type is not UNSET:
            field_dict["cardType"] = card_type
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if first6 is not UNSET:
            field_dict["first6"] = first6
        if last4 is not UNSET:
            field_dict["last4"] = last4
        if type_ is not UNSET:
            field_dict["type"] = type_
        if auth_code is not UNSET:
            field_dict["authCode"] = auth_code
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if transaction_no is not UNSET:
            field_dict["transactionNo"] = transaction_no
        if state is not UNSET:
            field_dict["state"] = state
        if beg_balance is not UNSET:
            field_dict["begBalance"] = beg_balance
        if end_balance is not UNSET:
            field_dict["endBalance"] = end_balance
        if avs_result is not UNSET:
            field_dict["avsResult"] = avs_result
        if cardholder_name is not UNSET:
            field_dict["cardholderName"] = cardholder_name
        if token is not UNSET:
            field_dict["token"] = token
        if vaulted_card is not UNSET:
            field_dict["vaultedCard"] = vaulted_card
        if gateway_tx_state is not UNSET:
            field_dict["gatewayTxState"] = gateway_tx_state
        if currency is not UNSET:
            field_dict["currency"] = currency
        if captured is not UNSET:
            field_dict["captured"] = captured
        if debit_refund is not UNSET:
            field_dict["debitRefund"] = debit_refund

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debit_refund import DebitRefund
        from ..models.reference import Reference
        from ..models.vaulted_card import VaultedCard

        d = dict(src_dict)
        _payment_ref = d.pop("paymentRef", UNSET)
        payment_ref: Union[Unset, Reference]
        if _payment_ref and not isinstance(_payment_ref, Unset):
            payment_ref = Reference.from_dict(_payment_ref)

        else:
            payment_ref = UNSET

        _refund_ref = d.pop("refundRef", UNSET)
        refund_ref: Union[Unset, Reference]
        if _refund_ref and not isinstance(_refund_ref, Unset):
            refund_ref = Reference.from_dict(_refund_ref)

        else:
            refund_ref = UNSET

        _credit_ref = d.pop("creditRef", UNSET)
        credit_ref: Union[Unset, Reference]
        if _credit_ref and not isinstance(_credit_ref, Unset):
            credit_ref = Reference.from_dict(_credit_ref)

        else:
            credit_ref = UNSET

        card_type = d.pop("cardType", UNSET)

        entry_type = d.pop("entryType", UNSET)

        first6 = d.pop("first6", UNSET)

        last4 = d.pop("last4", UNSET)

        type_ = d.pop("type", UNSET)

        auth_code = d.pop("authCode", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        transaction_no = d.pop("transactionNo", UNSET)

        state = d.pop("state", UNSET)

        beg_balance = d.pop("begBalance", UNSET)

        end_balance = d.pop("endBalance", UNSET)

        avs_result = d.pop("avsResult", UNSET)

        cardholder_name = d.pop("cardholderName", UNSET)

        token = d.pop("token", UNSET)

        _vaulted_card = d.pop("vaultedCard", UNSET)
        vaulted_card: Union[Unset, VaultedCard]
        if _vaulted_card and not isinstance(_vaulted_card, Unset):
            vaulted_card = VaultedCard.from_dict(_vaulted_card)

        else:
            vaulted_card = UNSET

        gateway_tx_state = d.pop("gatewayTxState", UNSET)

        currency = d.pop("currency", UNSET)

        captured = d.pop("captured", UNSET)

        _debit_refund = d.pop("debitRefund", UNSET)
        debit_refund: Union[Unset, DebitRefund]
        if _debit_refund and not isinstance(_debit_refund, Unset):
            debit_refund = DebitRefund.from_dict(_debit_refund)

        else:
            debit_refund = UNSET

        card_transaction = cls(
            payment_ref=payment_ref,
            refund_ref=refund_ref,
            credit_ref=credit_ref,
            card_type=card_type,
            entry_type=entry_type,
            first6=first6,
            last4=last4,
            type_=type_,
            auth_code=auth_code,
            reference_id=reference_id,
            transaction_no=transaction_no,
            state=state,
            beg_balance=beg_balance,
            end_balance=end_balance,
            avs_result=avs_result,
            cardholder_name=cardholder_name,
            token=token,
            vaulted_card=vaulted_card,
            gateway_tx_state=gateway_tx_state,
            currency=currency,
            captured=captured,
            debit_refund=debit_refund,
        )

        card_transaction.additional_properties = d
        return card_transaction

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
