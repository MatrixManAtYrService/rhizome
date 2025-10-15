from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ach_transaction_extra import AchTransactionExtra
    from ..models.reference import Reference


T = TypeVar("T", bound="AchTransaction")


@_attrs_define
class AchTransaction:
    """Information about the bank account used for ACH payments

    Attributes:
        payment_ref (Union[Unset, Reference]):
        routing_number (Union[Unset, str]): Bank routing number for this transaction
        last4 (Union[Unset, str]): Last four digits of the bank account number
        auth_code (Union[Unset, str]): Authorization code, if successful
        reference_id (Union[Unset, str]): Reference identifier
        extra (Union[Unset, AchTransactionExtra]): Extra info stored as part of gateway/card transaction
        account_holder_name (Union[Unset, str]): Account holder name
        customer_id_state (Union[Unset, str]): Customer ID state
        customer_id_last_4 (Union[Unset, str]): Last 4 characters of customer ID
        account_type (Union[Unset, str]): Account yype
        check_type (Union[Unset, str]): Check type
        authorization_method (Union[Unset, str]): Authorization method
        token (Union[Unset, str]): Token for vaulted account
    """

    payment_ref: Union[Unset, "Reference"] = UNSET
    routing_number: Union[Unset, str] = UNSET
    last4: Union[Unset, str] = UNSET
    auth_code: Union[Unset, str] = UNSET
    reference_id: Union[Unset, str] = UNSET
    extra: Union[Unset, "AchTransactionExtra"] = UNSET
    account_holder_name: Union[Unset, str] = UNSET
    customer_id_state: Union[Unset, str] = UNSET
    customer_id_last_4: Union[Unset, str] = UNSET
    account_type: Union[Unset, str] = UNSET
    check_type: Union[Unset, str] = UNSET
    authorization_method: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_ref, Unset):
            payment_ref = self.payment_ref.to_dict()

        routing_number = self.routing_number

        last4 = self.last4

        auth_code = self.auth_code

        reference_id = self.reference_id

        extra: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        account_holder_name = self.account_holder_name

        customer_id_state = self.customer_id_state

        customer_id_last_4 = self.customer_id_last_4

        account_type = self.account_type

        check_type = self.check_type

        authorization_method = self.authorization_method

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_ref is not UNSET:
            field_dict["paymentRef"] = payment_ref
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if last4 is not UNSET:
            field_dict["last4"] = last4
        if auth_code is not UNSET:
            field_dict["authCode"] = auth_code
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if extra is not UNSET:
            field_dict["extra"] = extra
        if account_holder_name is not UNSET:
            field_dict["accountHolderName"] = account_holder_name
        if customer_id_state is not UNSET:
            field_dict["customerIdState"] = customer_id_state
        if customer_id_last_4 is not UNSET:
            field_dict["customerIdLast4"] = customer_id_last_4
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if check_type is not UNSET:
            field_dict["checkType"] = check_type
        if authorization_method is not UNSET:
            field_dict["authorizationMethod"] = authorization_method
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ach_transaction_extra import AchTransactionExtra
        from ..models.reference import Reference

        d = dict(src_dict)
        _payment_ref = d.pop("paymentRef", UNSET)
        payment_ref: Union[Unset, Reference]
        if _payment_ref and not isinstance(_payment_ref, Unset):
            payment_ref = Reference.from_dict(_payment_ref)

        else:
            payment_ref = UNSET

        routing_number = d.pop("routingNumber", UNSET)

        last4 = d.pop("last4", UNSET)

        auth_code = d.pop("authCode", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        _extra = d.pop("extra", UNSET)
        extra: Union[Unset, AchTransactionExtra]
        if _extra and not isinstance(_extra, Unset):
            extra = AchTransactionExtra.from_dict(_extra)

        else:
            extra = UNSET

        account_holder_name = d.pop("accountHolderName", UNSET)

        customer_id_state = d.pop("customerIdState", UNSET)

        customer_id_last_4 = d.pop("customerIdLast4", UNSET)

        account_type = d.pop("accountType", UNSET)

        check_type = d.pop("checkType", UNSET)

        authorization_method = d.pop("authorizationMethod", UNSET)

        token = d.pop("token", UNSET)

        ach_transaction = cls(
            payment_ref=payment_ref,
            routing_number=routing_number,
            last4=last4,
            auth_code=auth_code,
            reference_id=reference_id,
            extra=extra,
            account_holder_name=account_holder_name,
            customer_id_state=customer_id_state,
            customer_id_last_4=customer_id_last_4,
            account_type=account_type,
            check_type=check_type,
            authorization_method=authorization_method,
            token=token,
        )

        ach_transaction.additional_properties = d
        return ach_transaction

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
