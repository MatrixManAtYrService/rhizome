from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ach_transaction import AchTransaction
    from ..models.additional_charge_amount import AdditionalChargeAmount
    from ..models.card_transaction import CardTransaction
    from ..models.device import Device
    from ..models.employee import Employee
    from ..models.order import Order
    from ..models.reference import Reference
    from ..models.service_charge import ServiceCharge
    from ..models.tender import Tender


T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    """List of payments

    Attributes:
        id (Union[Unset, str]):
        order (Union[Unset, Order]): The order with which the payment is associated.
        device (Union[Unset, Device]): Device which processed the transaction for this payment
        tender (Union[Unset, Tender]): The tender type associated with this payment, e.g. credit card, cash, etc.
        amount (Union[Unset, int]): Total amount paid with 2 implied decimal places
        tip_amount (Union[Unset, int]): Amount paid in tips with 2 implied decimal places
        tax_amount (Union[Unset, int]): Amount paid in tax with 2 implied decimal places
        cashback_amount (Union[Unset, int]): Amount given back in a cash back transaction with 2 implied decimal places
        cash_tendered (Union[Unset, int]): Amount of cash given by the customer with 2 implied decimal places
        external_payment_id (Union[Unset, str]): External payment identifier
        employee (Union[Unset, Employee]): Employee who processed the payment
        created_time (Union[Unset, int]): Time that the payment was recorded on the server (as milliseconds from epoch)
        client_created_time (Union[Unset, int]): Time that the payment was created by the client (as milliseconds from
            epoch)
        gateway_processing_time (Union[Unset, int]): Time when the payment transaction was processed by the gateway (as
            milliseconds from epoch)
        modified_time (Union[Unset, int]): Last time that the payment was modified (as milliseconds from epoch)
        offline (Union[Unset, bool]):
        result (Union[Unset, str]): Result of processing the payment
        card_transaction (Union[Unset, CardTransaction]): Information about the card used for credit/debit card payments
        ach_transaction (Union[Unset, AchTransaction]): Information about the bank account used for ACH payments
        service_charge (Union[Unset, ServiceCharge]): Amount recorded as a service charge
        additional_charges (Union[Unset, list['AdditionalChargeAmount']]):
        note (Union[Unset, str]):
        merchant (Union[Unset, Reference]):
    """

    id: Union[Unset, str] = UNSET
    order: Union[Unset, "Order"] = UNSET
    device: Union[Unset, "Device"] = UNSET
    tender: Union[Unset, "Tender"] = UNSET
    amount: Union[Unset, int] = UNSET
    tip_amount: Union[Unset, int] = UNSET
    tax_amount: Union[Unset, int] = UNSET
    cashback_amount: Union[Unset, int] = UNSET
    cash_tendered: Union[Unset, int] = UNSET
    external_payment_id: Union[Unset, str] = UNSET
    employee: Union[Unset, "Employee"] = UNSET
    created_time: Union[Unset, int] = UNSET
    client_created_time: Union[Unset, int] = UNSET
    gateway_processing_time: Union[Unset, int] = UNSET
    modified_time: Union[Unset, int] = UNSET
    offline: Union[Unset, bool] = UNSET
    result: Union[Unset, str] = UNSET
    card_transaction: Union[Unset, "CardTransaction"] = UNSET
    ach_transaction: Union[Unset, "AchTransaction"] = UNSET
    service_charge: Union[Unset, "ServiceCharge"] = UNSET
    additional_charges: Union[Unset, list["AdditionalChargeAmount"]] = UNSET
    note: Union[Unset, str] = UNSET
    merchant: Union[Unset, "Reference"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        device: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device, Unset):
            device = self.device.to_dict()

        tender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tender, Unset):
            tender = self.tender.to_dict()

        amount = self.amount

        tip_amount = self.tip_amount

        tax_amount = self.tax_amount

        cashback_amount = self.cashback_amount

        cash_tendered = self.cash_tendered

        external_payment_id = self.external_payment_id

        employee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.employee, Unset):
            employee = self.employee.to_dict()

        created_time = self.created_time

        client_created_time = self.client_created_time

        gateway_processing_time = self.gateway_processing_time

        modified_time = self.modified_time

        offline = self.offline

        result = self.result

        card_transaction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_transaction, Unset):
            card_transaction = self.card_transaction.to_dict()

        ach_transaction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ach_transaction, Unset):
            ach_transaction = self.ach_transaction.to_dict()

        service_charge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_charge, Unset):
            service_charge = self.service_charge.to_dict()

        additional_charges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.additional_charges, Unset):
            additional_charges = []
            for additional_charges_item_data in self.additional_charges:
                additional_charges_item = additional_charges_item_data.to_dict()
                additional_charges.append(additional_charges_item)

        note = self.note

        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if order is not UNSET:
            field_dict["order"] = order
        if device is not UNSET:
            field_dict["device"] = device
        if tender is not UNSET:
            field_dict["tender"] = tender
        if amount is not UNSET:
            field_dict["amount"] = amount
        if tip_amount is not UNSET:
            field_dict["tipAmount"] = tip_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if cashback_amount is not UNSET:
            field_dict["cashbackAmount"] = cashback_amount
        if cash_tendered is not UNSET:
            field_dict["cashTendered"] = cash_tendered
        if external_payment_id is not UNSET:
            field_dict["externalPaymentId"] = external_payment_id
        if employee is not UNSET:
            field_dict["employee"] = employee
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if client_created_time is not UNSET:
            field_dict["clientCreatedTime"] = client_created_time
        if gateway_processing_time is not UNSET:
            field_dict["gatewayProcessingTime"] = gateway_processing_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time
        if offline is not UNSET:
            field_dict["offline"] = offline
        if result is not UNSET:
            field_dict["result"] = result
        if card_transaction is not UNSET:
            field_dict["cardTransaction"] = card_transaction
        if ach_transaction is not UNSET:
            field_dict["achTransaction"] = ach_transaction
        if service_charge is not UNSET:
            field_dict["serviceCharge"] = service_charge
        if additional_charges is not UNSET:
            field_dict["additionalCharges"] = additional_charges
        if note is not UNSET:
            field_dict["note"] = note
        if merchant is not UNSET:
            field_dict["merchant"] = merchant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ach_transaction import AchTransaction
        from ..models.additional_charge_amount import AdditionalChargeAmount
        from ..models.card_transaction import CardTransaction
        from ..models.device import Device
        from ..models.employee import Employee
        from ..models.order import Order
        from ..models.reference import Reference
        from ..models.service_charge import ServiceCharge
        from ..models.tender import Tender

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _order = d.pop("order", UNSET)
        order: Union[Unset, Order]
        if _order and not isinstance(_order, Unset):
            order = Order.from_dict(_order)

        else:
            order = UNSET

        _device = d.pop("device", UNSET)
        device: Union[Unset, Device]
        if _device and not isinstance(_device, Unset):
            device = Device.from_dict(_device)

        else:
            device = UNSET

        _tender = d.pop("tender", UNSET)
        tender: Union[Unset, Tender]
        if _tender and not isinstance(_tender, Unset):
            tender = Tender.from_dict(_tender)

        else:
            tender = UNSET

        amount = d.pop("amount", UNSET)

        tip_amount = d.pop("tipAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        cashback_amount = d.pop("cashbackAmount", UNSET)

        cash_tendered = d.pop("cashTendered", UNSET)

        external_payment_id = d.pop("externalPaymentId", UNSET)

        _employee = d.pop("employee", UNSET)
        employee: Union[Unset, Employee]
        if _employee and not isinstance(_employee, Unset):
            employee = Employee.from_dict(_employee)

        else:
            employee = UNSET

        created_time = d.pop("createdTime", UNSET)

        client_created_time = d.pop("clientCreatedTime", UNSET)

        gateway_processing_time = d.pop("gatewayProcessingTime", UNSET)

        modified_time = d.pop("modifiedTime", UNSET)

        offline = d.pop("offline", UNSET)

        result = d.pop("result", UNSET)

        _card_transaction = d.pop("cardTransaction", UNSET)
        card_transaction: Union[Unset, CardTransaction]
        if _card_transaction and not isinstance(_card_transaction, Unset):
            card_transaction = CardTransaction.from_dict(_card_transaction)

        else:
            card_transaction = UNSET

        _ach_transaction = d.pop("achTransaction", UNSET)
        ach_transaction: Union[Unset, AchTransaction]
        if _ach_transaction and not isinstance(_ach_transaction, Unset):
            ach_transaction = AchTransaction.from_dict(_ach_transaction)

        else:
            ach_transaction = UNSET

        _service_charge = d.pop("serviceCharge", UNSET)
        service_charge: Union[Unset, ServiceCharge]
        if _service_charge and not isinstance(_service_charge, Unset):
            service_charge = ServiceCharge.from_dict(_service_charge)

        else:
            service_charge = UNSET

        additional_charges = []
        _additional_charges = d.pop("additionalCharges", UNSET)
        for additional_charges_item_data in _additional_charges or []:
            additional_charges_item = AdditionalChargeAmount.from_dict(additional_charges_item_data)

            additional_charges.append(additional_charges_item)

        note = d.pop("note", UNSET)

        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, Reference]
        if _merchant and not isinstance(_merchant, Unset):
            merchant = Reference.from_dict(_merchant)

        else:
            merchant = UNSET

        payment = cls(
            id=id,
            order=order,
            device=device,
            tender=tender,
            amount=amount,
            tip_amount=tip_amount,
            tax_amount=tax_amount,
            cashback_amount=cashback_amount,
            cash_tendered=cash_tendered,
            external_payment_id=external_payment_id,
            employee=employee,
            created_time=created_time,
            client_created_time=client_created_time,
            gateway_processing_time=gateway_processing_time,
            modified_time=modified_time,
            offline=offline,
            result=result,
            card_transaction=card_transaction,
            ach_transaction=ach_transaction,
            service_charge=service_charge,
            additional_charges=additional_charges,
            note=note,
            merchant=merchant,
        )

        payment.additional_properties = d
        return payment

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
