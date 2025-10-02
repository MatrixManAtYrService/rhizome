from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee_ctd import FeeCtd
    from ..models.fee_summary import FeeSummary
    from ..models.fee_ytd import FeeYtd
    from ..models.invoice_info import InvoiceInfo
    from ..models.settlement import Settlement
    from ..models.settlement_action import SettlementAction


T = TypeVar("T", bound="Fees")


@_attrs_define
class Fees:
    """
    Attributes:
        fee_ctds (Union[Unset, list['FeeCtd']]):
        fee_ytds (Union[Unset, list['FeeYtd']]):
        fee_summaries (Union[Unset, list['FeeSummary']]):
        invoice_infos (Union[Unset, list['InvoiceInfo']]):
        settlements (Union[Unset, list['Settlement']]):
        settlement_actions (Union[Unset, list['SettlementAction']]):
    """

    fee_ctds: Union[Unset, list["FeeCtd"]] = UNSET
    fee_ytds: Union[Unset, list["FeeYtd"]] = UNSET
    fee_summaries: Union[Unset, list["FeeSummary"]] = UNSET
    invoice_infos: Union[Unset, list["InvoiceInfo"]] = UNSET
    settlements: Union[Unset, list["Settlement"]] = UNSET
    settlement_actions: Union[Unset, list["SettlementAction"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_ctds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_ctds, Unset):
            fee_ctds = []
            for fee_ctds_item_data in self.fee_ctds:
                fee_ctds_item = fee_ctds_item_data.to_dict()
                fee_ctds.append(fee_ctds_item)

        fee_ytds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_ytds, Unset):
            fee_ytds = []
            for fee_ytds_item_data in self.fee_ytds:
                fee_ytds_item = fee_ytds_item_data.to_dict()
                fee_ytds.append(fee_ytds_item)

        fee_summaries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_summaries, Unset):
            fee_summaries = []
            for fee_summaries_item_data in self.fee_summaries:
                fee_summaries_item = fee_summaries_item_data.to_dict()
                fee_summaries.append(fee_summaries_item)

        invoice_infos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invoice_infos, Unset):
            invoice_infos = []
            for invoice_infos_item_data in self.invoice_infos:
                invoice_infos_item = invoice_infos_item_data.to_dict()
                invoice_infos.append(invoice_infos_item)

        settlements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.settlements, Unset):
            settlements = []
            for settlements_item_data in self.settlements:
                settlements_item = settlements_item_data.to_dict()
                settlements.append(settlements_item)

        settlement_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.settlement_actions, Unset):
            settlement_actions = []
            for settlement_actions_item_data in self.settlement_actions:
                settlement_actions_item = settlement_actions_item_data.to_dict()
                settlement_actions.append(settlement_actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_ctds is not UNSET:
            field_dict["feeCtds"] = fee_ctds
        if fee_ytds is not UNSET:
            field_dict["feeYtds"] = fee_ytds
        if fee_summaries is not UNSET:
            field_dict["feeSummaries"] = fee_summaries
        if invoice_infos is not UNSET:
            field_dict["invoiceInfos"] = invoice_infos
        if settlements is not UNSET:
            field_dict["settlements"] = settlements
        if settlement_actions is not UNSET:
            field_dict["settlementActions"] = settlement_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fee_ctd import FeeCtd
        from ..models.fee_summary import FeeSummary
        from ..models.fee_ytd import FeeYtd
        from ..models.invoice_info import InvoiceInfo
        from ..models.settlement import Settlement
        from ..models.settlement_action import SettlementAction

        d = dict(src_dict)
        fee_ctds = []
        _fee_ctds = d.pop("feeCtds", UNSET)
        for fee_ctds_item_data in _fee_ctds or []:
            fee_ctds_item = FeeCtd.from_dict(fee_ctds_item_data)

            fee_ctds.append(fee_ctds_item)

        fee_ytds = []
        _fee_ytds = d.pop("feeYtds", UNSET)
        for fee_ytds_item_data in _fee_ytds or []:
            fee_ytds_item = FeeYtd.from_dict(fee_ytds_item_data)

            fee_ytds.append(fee_ytds_item)

        fee_summaries = []
        _fee_summaries = d.pop("feeSummaries", UNSET)
        for fee_summaries_item_data in _fee_summaries or []:
            fee_summaries_item = FeeSummary.from_dict(fee_summaries_item_data)

            fee_summaries.append(fee_summaries_item)

        invoice_infos = []
        _invoice_infos = d.pop("invoiceInfos", UNSET)
        for invoice_infos_item_data in _invoice_infos or []:
            invoice_infos_item = InvoiceInfo.from_dict(invoice_infos_item_data)

            invoice_infos.append(invoice_infos_item)

        settlements = []
        _settlements = d.pop("settlements", UNSET)
        for settlements_item_data in _settlements or []:
            settlements_item = Settlement.from_dict(settlements_item_data)

            settlements.append(settlements_item)

        settlement_actions = []
        _settlement_actions = d.pop("settlementActions", UNSET)
        for settlement_actions_item_data in _settlement_actions or []:
            settlement_actions_item = SettlementAction.from_dict(settlement_actions_item_data)

            settlement_actions.append(settlement_actions_item)

        fees = cls(
            fee_ctds=fee_ctds,
            fee_ytds=fee_ytds,
            fee_summaries=fee_summaries,
            invoice_infos=invoice_infos,
            settlements=settlements,
            settlement_actions=settlement_actions,
        )

        fees.additional_properties = d
        return fees

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
