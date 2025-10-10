from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.developer_app_approval_status import DeveloperAppApprovalStatus
from ..models.developer_app_distribution import DeveloperAppDistribution
from ..models.developer_app_segment import DeveloperAppSegment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.developer_app_android_version import DeveloperAppAndroidVersion
    from ..models.developer_app_current_subscription import DeveloperAppCurrentSubscription
    from ..models.developer_app_developer import DeveloperAppDeveloper
    from ..models.developer_app_merchant import DeveloperAppMerchant
    from ..models.metereds import Metereds
    from ..models.permissions import Permissions
    from ..models.subscriptions import Subscriptions


T = TypeVar("T", bound="DeveloperApp")


@_attrs_define
class DeveloperApp:
    """
    Attributes:
        id (Union[Unset, str]):
        uuid (Union[Unset, str]):
        app_metered_uuid (Union[Unset, str]):
        developer_uuid (Union[Unset, str]):
        package_name (Union[Unset, str]):
        site_url (Union[Unset, str]):
        activation_url (Union[Unset, str]):
        support_phone (Union[Unset, str]):
        support_email (Union[Unset, str]):
        support_url (Union[Unset, str]):
        developer_name (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        filename_icon_small (Union[Unset, str]):
        filename_icon_large (Union[Unset, str]):
        system_app (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        created_time (Union[Unset, int]):
        installed_time (Union[Unset, int]):
        approval_status (Union[Unset, DeveloperAppApprovalStatus]):
        distribution (Union[Unset, DeveloperAppDistribution]):
        developer (Union[Unset, DeveloperAppDeveloper]):
        merchant (Union[Unset, DeveloperAppMerchant]):
        android_version (Union[Unset, DeveloperAppAndroidVersion]):
        current_subscription (Union[Unset, DeveloperAppCurrentSubscription]):
        subscriptions (Union[Unset, Subscriptions]):
        metereds (Union[Unset, Metereds]):
        available_subscriptions (Union[Unset, Subscriptions]):
        available_metereds (Union[Unset, Metereds]):
        permissions (Union[Unset, Permissions]):
        segment (Union[Unset, DeveloperAppSegment]):
        paid_app_has_trial (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    app_metered_uuid: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    site_url: Union[Unset, str] = UNSET
    activation_url: Union[Unset, str] = UNSET
    support_phone: Union[Unset, str] = UNSET
    support_email: Union[Unset, str] = UNSET
    support_url: Union[Unset, str] = UNSET
    developer_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    filename_icon_small: Union[Unset, str] = UNSET
    filename_icon_large: Union[Unset, str] = UNSET
    system_app: Union[Unset, bool] = UNSET
    hidden: Union[Unset, bool] = UNSET
    created_time: Union[Unset, int] = UNSET
    installed_time: Union[Unset, int] = UNSET
    approval_status: Union[Unset, DeveloperAppApprovalStatus] = UNSET
    distribution: Union[Unset, DeveloperAppDistribution] = UNSET
    developer: Union[Unset, "DeveloperAppDeveloper"] = UNSET
    merchant: Union[Unset, "DeveloperAppMerchant"] = UNSET
    android_version: Union[Unset, "DeveloperAppAndroidVersion"] = UNSET
    current_subscription: Union[Unset, "DeveloperAppCurrentSubscription"] = UNSET
    subscriptions: Union[Unset, "Subscriptions"] = UNSET
    metereds: Union[Unset, "Metereds"] = UNSET
    available_subscriptions: Union[Unset, "Subscriptions"] = UNSET
    available_metereds: Union[Unset, "Metereds"] = UNSET
    permissions: Union[Unset, "Permissions"] = UNSET
    segment: Union[Unset, DeveloperAppSegment] = UNSET
    paid_app_has_trial: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        app_metered_uuid = self.app_metered_uuid

        developer_uuid = self.developer_uuid

        package_name = self.package_name

        site_url = self.site_url

        activation_url = self.activation_url

        support_phone = self.support_phone

        support_email = self.support_email

        support_url = self.support_url

        developer_name = self.developer_name

        name = self.name

        description = self.description

        filename_icon_small = self.filename_icon_small

        filename_icon_large = self.filename_icon_large

        system_app = self.system_app

        hidden = self.hidden

        created_time = self.created_time

        installed_time = self.installed_time

        approval_status: Union[Unset, str] = UNSET
        if not isinstance(self.approval_status, Unset):
            approval_status = self.approval_status.value

        distribution: Union[Unset, str] = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.value

        developer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.developer, Unset):
            developer = self.developer.to_dict()

        merchant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        android_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.android_version, Unset):
            android_version = self.android_version.to_dict()

        current_subscription: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.current_subscription, Unset):
            current_subscription = self.current_subscription.to_dict()

        subscriptions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        metereds: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metereds, Unset):
            metereds = self.metereds.to_dict()

        available_subscriptions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.available_subscriptions, Unset):
            available_subscriptions = self.available_subscriptions.to_dict()

        available_metereds: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.available_metereds, Unset):
            available_metereds = self.available_metereds.to_dict()

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        segment: Union[Unset, str] = UNSET
        if not isinstance(self.segment, Unset):
            segment = self.segment.value

        paid_app_has_trial = self.paid_app_has_trial

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if app_metered_uuid is not UNSET:
            field_dict["appMeteredUuid"] = app_metered_uuid
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if site_url is not UNSET:
            field_dict["siteUrl"] = site_url
        if activation_url is not UNSET:
            field_dict["activationUrl"] = activation_url
        if support_phone is not UNSET:
            field_dict["supportPhone"] = support_phone
        if support_email is not UNSET:
            field_dict["supportEmail"] = support_email
        if support_url is not UNSET:
            field_dict["supportUrl"] = support_url
        if developer_name is not UNSET:
            field_dict["developerName"] = developer_name
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if filename_icon_small is not UNSET:
            field_dict["filenameIconSmall"] = filename_icon_small
        if filename_icon_large is not UNSET:
            field_dict["filenameIconLarge"] = filename_icon_large
        if system_app is not UNSET:
            field_dict["systemApp"] = system_app
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if installed_time is not UNSET:
            field_dict["installedTime"] = installed_time
        if approval_status is not UNSET:
            field_dict["approvalStatus"] = approval_status
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if developer is not UNSET:
            field_dict["developer"] = developer
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if android_version is not UNSET:
            field_dict["androidVersion"] = android_version
        if current_subscription is not UNSET:
            field_dict["currentSubscription"] = current_subscription
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if metereds is not UNSET:
            field_dict["metereds"] = metereds
        if available_subscriptions is not UNSET:
            field_dict["availableSubscriptions"] = available_subscriptions
        if available_metereds is not UNSET:
            field_dict["availableMetereds"] = available_metereds
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if segment is not UNSET:
            field_dict["segment"] = segment
        if paid_app_has_trial is not UNSET:
            field_dict["paidAppHasTrial"] = paid_app_has_trial

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_app_android_version import DeveloperAppAndroidVersion
        from ..models.developer_app_current_subscription import DeveloperAppCurrentSubscription
        from ..models.developer_app_developer import DeveloperAppDeveloper
        from ..models.developer_app_merchant import DeveloperAppMerchant
        from ..models.metereds import Metereds
        from ..models.permissions import Permissions
        from ..models.subscriptions import Subscriptions

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        package_name = d.pop("packageName", UNSET)

        site_url = d.pop("siteUrl", UNSET)

        activation_url = d.pop("activationUrl", UNSET)

        support_phone = d.pop("supportPhone", UNSET)

        support_email = d.pop("supportEmail", UNSET)

        support_url = d.pop("supportUrl", UNSET)

        developer_name = d.pop("developerName", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        filename_icon_small = d.pop("filenameIconSmall", UNSET)

        filename_icon_large = d.pop("filenameIconLarge", UNSET)

        system_app = d.pop("systemApp", UNSET)

        hidden = d.pop("hidden", UNSET)

        created_time = d.pop("createdTime", UNSET)

        installed_time = d.pop("installedTime", UNSET)

        _approval_status = d.pop("approvalStatus", UNSET)
        approval_status: Union[Unset, DeveloperAppApprovalStatus]
        if _approval_status and not isinstance(_approval_status, Unset):
            approval_status = DeveloperAppApprovalStatus(_approval_status)

        else:
            approval_status = UNSET

        _distribution = d.pop("distribution", UNSET)
        distribution: Union[Unset, DeveloperAppDistribution]
        if _distribution and not isinstance(_distribution, Unset):
            distribution = DeveloperAppDistribution(_distribution)

        else:
            distribution = UNSET

        _developer = d.pop("developer", UNSET)
        developer: Union[Unset, DeveloperAppDeveloper]
        if _developer and not isinstance(_developer, Unset):
            developer = DeveloperAppDeveloper.from_dict(_developer)

        else:
            developer = UNSET

        _merchant = d.pop("merchant", UNSET)
        merchant: Union[Unset, DeveloperAppMerchant]
        if _merchant and not isinstance(_merchant, Unset):
            merchant = DeveloperAppMerchant.from_dict(_merchant)

        else:
            merchant = UNSET

        _android_version = d.pop("androidVersion", UNSET)
        android_version: Union[Unset, DeveloperAppAndroidVersion]
        if _android_version and not isinstance(_android_version, Unset):
            android_version = DeveloperAppAndroidVersion.from_dict(_android_version)

        else:
            android_version = UNSET

        _current_subscription = d.pop("currentSubscription", UNSET)
        current_subscription: Union[Unset, DeveloperAppCurrentSubscription]
        if _current_subscription and not isinstance(_current_subscription, Unset):
            current_subscription = DeveloperAppCurrentSubscription.from_dict(_current_subscription)

        else:
            current_subscription = UNSET

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: Union[Unset, Subscriptions]
        if _subscriptions and not isinstance(_subscriptions, Unset):
            subscriptions = Subscriptions.from_dict(_subscriptions)

        else:
            subscriptions = UNSET

        _metereds = d.pop("metereds", UNSET)
        metereds: Union[Unset, Metereds]
        if _metereds and not isinstance(_metereds, Unset):
            metereds = Metereds.from_dict(_metereds)

        else:
            metereds = UNSET

        _available_subscriptions = d.pop("availableSubscriptions", UNSET)
        available_subscriptions: Union[Unset, Subscriptions]
        if _available_subscriptions and not isinstance(_available_subscriptions, Unset):
            available_subscriptions = Subscriptions.from_dict(_available_subscriptions)

        else:
            available_subscriptions = UNSET

        _available_metereds = d.pop("availableMetereds", UNSET)
        available_metereds: Union[Unset, Metereds]
        if _available_metereds and not isinstance(_available_metereds, Unset):
            available_metereds = Metereds.from_dict(_available_metereds)

        else:
            available_metereds = UNSET

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, Permissions]
        if _permissions and not isinstance(_permissions, Unset):
            permissions = Permissions.from_dict(_permissions)

        else:
            permissions = UNSET

        _segment = d.pop("segment", UNSET)
        segment: Union[Unset, DeveloperAppSegment]
        if _segment and not isinstance(_segment, Unset):
            segment = DeveloperAppSegment(_segment)

        else:
            segment = UNSET

        paid_app_has_trial = d.pop("paidAppHasTrial", UNSET)

        developer_app = cls(
            id=id,
            uuid=uuid,
            app_metered_uuid=app_metered_uuid,
            developer_uuid=developer_uuid,
            package_name=package_name,
            site_url=site_url,
            activation_url=activation_url,
            support_phone=support_phone,
            support_email=support_email,
            support_url=support_url,
            developer_name=developer_name,
            name=name,
            description=description,
            filename_icon_small=filename_icon_small,
            filename_icon_large=filename_icon_large,
            system_app=system_app,
            hidden=hidden,
            created_time=created_time,
            installed_time=installed_time,
            approval_status=approval_status,
            distribution=distribution,
            developer=developer,
            merchant=merchant,
            android_version=android_version,
            current_subscription=current_subscription,
            subscriptions=subscriptions,
            metereds=metereds,
            available_subscriptions=available_subscriptions,
            available_metereds=available_metereds,
            permissions=permissions,
            segment=segment,
            paid_app_has_trial=paid_app_has_trial,
        )

        developer_app.additional_properties = d
        return developer_app

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
