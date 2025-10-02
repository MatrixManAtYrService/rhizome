from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission_app_permission import PermissionAppPermission


T = TypeVar("T", bound="Permission")


@_attrs_define
class Permission:
    """
    Attributes:
        app_permission (Union[Unset, PermissionAppPermission]):
        required (Union[Unset, bool]):
    """

    app_permission: Union[Unset, "PermissionAppPermission"] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_permission: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_permission, Unset):
            app_permission = self.app_permission.to_dict()

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_permission is not UNSET:
            field_dict["appPermission"] = app_permission
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_app_permission import PermissionAppPermission

        d = dict(src_dict)
        _app_permission = d.pop("appPermission", UNSET)
        app_permission: Union[Unset, PermissionAppPermission]
        if isinstance(_app_permission, Unset):
            app_permission = UNSET
        else:
            app_permission = PermissionAppPermission.from_dict(_app_permission)

        required = d.pop("required", UNSET)

        permission = cls(
            app_permission=app_permission,
            required=required,
        )

        permission.additional_properties = d
        return permission

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
