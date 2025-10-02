from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_key_info import GatewayKeyInfo


T = TypeVar("T", bound="Gateway")


@_attrs_define
class Gateway:
    """
    Attributes:
        payment_processor_name (Union[Unset, str]):
        authorization_front_end (Union[Unset, str]):
        acquiring_back_end (Union[Unset, str]):
        payment_gateway_api (Union[Unset, str]):
        account_name (Union[Unset, str]):
        alt_mid (Union[Unset, str]):
        mid (Union[Unset, str]):
        abn (Union[Unset, str]):
        fns (Union[Unset, str]):
        tid (Union[Unset, str]):
        store_id (Union[Unset, str]):
        supports_tipping (Union[Unset, bool]):
        frontend_mid (Union[Unset, str]):
        backend_mid (Union[Unset, str]):
        mcc (Union[Unset, str]):
        token_type (Union[Unset, str]):
        group_id (Union[Unset, str]):
        debit_key_code (Union[Unset, str]):
        sred_code (Union[Unset, str]):
        supports_tip_adjust (Union[Unset, str]):
        supports_naked_credit (Union[Unset, str]):
        supports_multi_pay_token (Union[Unset, str]):
        key_prefix (Union[Unset, str]):
        key_info (Union[Unset, GatewayKeyInfo]):
        closing_time (Union[Unset, str]):
        new_batch_close_enabled (Union[Unset, bool]):
        production (Union[Unset, bool]):
    """

    payment_processor_name: Union[Unset, str] = UNSET
    authorization_front_end: Union[Unset, str] = UNSET
    acquiring_back_end: Union[Unset, str] = UNSET
    payment_gateway_api: Union[Unset, str] = UNSET
    account_name: Union[Unset, str] = UNSET
    alt_mid: Union[Unset, str] = UNSET
    mid: Union[Unset, str] = UNSET
    abn: Union[Unset, str] = UNSET
    fns: Union[Unset, str] = UNSET
    tid: Union[Unset, str] = UNSET
    store_id: Union[Unset, str] = UNSET
    supports_tipping: Union[Unset, bool] = UNSET
    frontend_mid: Union[Unset, str] = UNSET
    backend_mid: Union[Unset, str] = UNSET
    mcc: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    debit_key_code: Union[Unset, str] = UNSET
    sred_code: Union[Unset, str] = UNSET
    supports_tip_adjust: Union[Unset, str] = UNSET
    supports_naked_credit: Union[Unset, str] = UNSET
    supports_multi_pay_token: Union[Unset, str] = UNSET
    key_prefix: Union[Unset, str] = UNSET
    key_info: Union[Unset, "GatewayKeyInfo"] = UNSET
    closing_time: Union[Unset, str] = UNSET
    new_batch_close_enabled: Union[Unset, bool] = UNSET
    production: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_processor_name = self.payment_processor_name

        authorization_front_end = self.authorization_front_end

        acquiring_back_end = self.acquiring_back_end

        payment_gateway_api = self.payment_gateway_api

        account_name = self.account_name

        alt_mid = self.alt_mid

        mid = self.mid

        abn = self.abn

        fns = self.fns

        tid = self.tid

        store_id = self.store_id

        supports_tipping = self.supports_tipping

        frontend_mid = self.frontend_mid

        backend_mid = self.backend_mid

        mcc = self.mcc

        token_type = self.token_type

        group_id = self.group_id

        debit_key_code = self.debit_key_code

        sred_code = self.sred_code

        supports_tip_adjust = self.supports_tip_adjust

        supports_naked_credit = self.supports_naked_credit

        supports_multi_pay_token = self.supports_multi_pay_token

        key_prefix = self.key_prefix

        key_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        closing_time = self.closing_time

        new_batch_close_enabled = self.new_batch_close_enabled

        production = self.production

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_processor_name is not UNSET:
            field_dict["paymentProcessorName"] = payment_processor_name
        if authorization_front_end is not UNSET:
            field_dict["authorizationFrontEnd"] = authorization_front_end
        if acquiring_back_end is not UNSET:
            field_dict["acquiringBackEnd"] = acquiring_back_end
        if payment_gateway_api is not UNSET:
            field_dict["paymentGatewayApi"] = payment_gateway_api
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if alt_mid is not UNSET:
            field_dict["altMid"] = alt_mid
        if mid is not UNSET:
            field_dict["mid"] = mid
        if abn is not UNSET:
            field_dict["abn"] = abn
        if fns is not UNSET:
            field_dict["fns"] = fns
        if tid is not UNSET:
            field_dict["tid"] = tid
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if supports_tipping is not UNSET:
            field_dict["supportsTipping"] = supports_tipping
        if frontend_mid is not UNSET:
            field_dict["frontendMid"] = frontend_mid
        if backend_mid is not UNSET:
            field_dict["backendMid"] = backend_mid
        if mcc is not UNSET:
            field_dict["mcc"] = mcc
        if token_type is not UNSET:
            field_dict["tokenType"] = token_type
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if debit_key_code is not UNSET:
            field_dict["debitKeyCode"] = debit_key_code
        if sred_code is not UNSET:
            field_dict["sredCode"] = sred_code
        if supports_tip_adjust is not UNSET:
            field_dict["supportsTipAdjust"] = supports_tip_adjust
        if supports_naked_credit is not UNSET:
            field_dict["supportsNakedCredit"] = supports_naked_credit
        if supports_multi_pay_token is not UNSET:
            field_dict["supportsMultiPayToken"] = supports_multi_pay_token
        if key_prefix is not UNSET:
            field_dict["keyPrefix"] = key_prefix
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if closing_time is not UNSET:
            field_dict["closingTime"] = closing_time
        if new_batch_close_enabled is not UNSET:
            field_dict["newBatchCloseEnabled"] = new_batch_close_enabled
        if production is not UNSET:
            field_dict["production"] = production

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_key_info import GatewayKeyInfo

        d = dict(src_dict)
        payment_processor_name = d.pop("paymentProcessorName", UNSET)

        authorization_front_end = d.pop("authorizationFrontEnd", UNSET)

        acquiring_back_end = d.pop("acquiringBackEnd", UNSET)

        payment_gateway_api = d.pop("paymentGatewayApi", UNSET)

        account_name = d.pop("accountName", UNSET)

        alt_mid = d.pop("altMid", UNSET)

        mid = d.pop("mid", UNSET)

        abn = d.pop("abn", UNSET)

        fns = d.pop("fns", UNSET)

        tid = d.pop("tid", UNSET)

        store_id = d.pop("storeId", UNSET)

        supports_tipping = d.pop("supportsTipping", UNSET)

        frontend_mid = d.pop("frontendMid", UNSET)

        backend_mid = d.pop("backendMid", UNSET)

        mcc = d.pop("mcc", UNSET)

        token_type = d.pop("tokenType", UNSET)

        group_id = d.pop("groupId", UNSET)

        debit_key_code = d.pop("debitKeyCode", UNSET)

        sred_code = d.pop("sredCode", UNSET)

        supports_tip_adjust = d.pop("supportsTipAdjust", UNSET)

        supports_naked_credit = d.pop("supportsNakedCredit", UNSET)

        supports_multi_pay_token = d.pop("supportsMultiPayToken", UNSET)

        key_prefix = d.pop("keyPrefix", UNSET)

        _key_info = d.pop("keyInfo", UNSET)
        key_info: Union[Unset, GatewayKeyInfo]
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = GatewayKeyInfo.from_dict(_key_info)

        closing_time = d.pop("closingTime", UNSET)

        new_batch_close_enabled = d.pop("newBatchCloseEnabled", UNSET)

        production = d.pop("production", UNSET)

        gateway = cls(
            payment_processor_name=payment_processor_name,
            authorization_front_end=authorization_front_end,
            acquiring_back_end=acquiring_back_end,
            payment_gateway_api=payment_gateway_api,
            account_name=account_name,
            alt_mid=alt_mid,
            mid=mid,
            abn=abn,
            fns=fns,
            tid=tid,
            store_id=store_id,
            supports_tipping=supports_tipping,
            frontend_mid=frontend_mid,
            backend_mid=backend_mid,
            mcc=mcc,
            token_type=token_type,
            group_id=group_id,
            debit_key_code=debit_key_code,
            sred_code=sred_code,
            supports_tip_adjust=supports_tip_adjust,
            supports_naked_credit=supports_naked_credit,
            supports_multi_pay_token=supports_multi_pay_token,
            key_prefix=key_prefix,
            key_info=key_info,
            closing_time=closing_time,
            new_batch_close_enabled=new_batch_close_enabled,
            production=production,
        )

        gateway.additional_properties = d
        return gateway

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
