from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schema_type import SchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field import Field
    from ..models.logical_type import LogicalType
    from ..models.schema_object_props import SchemaObjectProps


T = TypeVar("T", bound="Schema")


@_attrs_define
class Schema:
    """
    Attributes:
        type_ (Union[Unset, SchemaType]):
        logical_type (Union[Unset, LogicalType]):
        enum_symbols (Union[Unset, list[str]]):
        enum_default (Union[Unset, str]):
        doc (Union[Unset, str]):
        fixed_size (Union[Unset, int]):
        union (Union[Unset, bool]):
        types (Union[Unset, list['Schema']]):
        name (Union[Unset, str]):
        fields (Union[Unset, list['Field']]):
        error (Union[Unset, bool]):
        full_name (Union[Unset, str]):
        element_type (Union[Unset, Schema]):
        namespace (Union[Unset, str]):
        value_type (Union[Unset, Schema]):
        nullable (Union[Unset, bool]):
        aliases (Union[Unset, list[str]]):
        object_props (Union[Unset, SchemaObjectProps]):
    """

    type_: Union[Unset, SchemaType] = UNSET
    logical_type: Union[Unset, "LogicalType"] = UNSET
    enum_symbols: Union[Unset, list[str]] = UNSET
    enum_default: Union[Unset, str] = UNSET
    doc: Union[Unset, str] = UNSET
    fixed_size: Union[Unset, int] = UNSET
    union: Union[Unset, bool] = UNSET
    types: Union[Unset, list["Schema"]] = UNSET
    name: Union[Unset, str] = UNSET
    fields: Union[Unset, list["Field"]] = UNSET
    error: Union[Unset, bool] = UNSET
    full_name: Union[Unset, str] = UNSET
    element_type: Union[Unset, "Schema"] = UNSET
    namespace: Union[Unset, str] = UNSET
    value_type: Union[Unset, "Schema"] = UNSET
    nullable: Union[Unset, bool] = UNSET
    aliases: Union[Unset, list[str]] = UNSET
    object_props: Union[Unset, "SchemaObjectProps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        logical_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.logical_type, Unset):
            logical_type = self.logical_type.to_dict()

        enum_symbols: Union[Unset, list[str]] = UNSET
        if not isinstance(self.enum_symbols, Unset):
            enum_symbols = self.enum_symbols

        enum_default = self.enum_default

        doc = self.doc

        fixed_size = self.fixed_size

        union = self.union

        types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item = types_item_data.to_dict()
                types.append(types_item)

        name = self.name

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        error = self.error

        full_name = self.full_name

        element_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.element_type, Unset):
            element_type = self.element_type.to_dict()

        namespace = self.namespace

        value_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.to_dict()

        nullable = self.nullable

        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        object_props: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_props, Unset):
            object_props = self.object_props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if logical_type is not UNSET:
            field_dict["logicalType"] = logical_type
        if enum_symbols is not UNSET:
            field_dict["enumSymbols"] = enum_symbols
        if enum_default is not UNSET:
            field_dict["enumDefault"] = enum_default
        if doc is not UNSET:
            field_dict["doc"] = doc
        if fixed_size is not UNSET:
            field_dict["fixedSize"] = fixed_size
        if union is not UNSET:
            field_dict["union"] = union
        if types is not UNSET:
            field_dict["types"] = types
        if name is not UNSET:
            field_dict["name"] = name
        if fields is not UNSET:
            field_dict["fields"] = fields
        if error is not UNSET:
            field_dict["error"] = error
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if value_type is not UNSET:
            field_dict["valueType"] = value_type
        if nullable is not UNSET:
            field_dict["nullable"] = nullable
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if object_props is not UNSET:
            field_dict["objectProps"] = object_props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field import Field
        from ..models.logical_type import LogicalType
        from ..models.schema_object_props import SchemaObjectProps

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, SchemaType]
        if _type_ and not isinstance(_type_, Unset):
            type_ = SchemaType(_type_)

        else:
            type_ = UNSET

        _logical_type = d.pop("logicalType", UNSET)
        logical_type: Union[Unset, LogicalType]
        if _logical_type and not isinstance(_logical_type, Unset):
            logical_type = LogicalType.from_dict(_logical_type)

        else:
            logical_type = UNSET

        enum_symbols = cast(list[str], d.pop("enumSymbols", UNSET))

        enum_default = d.pop("enumDefault", UNSET)

        doc = d.pop("doc", UNSET)

        fixed_size = d.pop("fixedSize", UNSET)

        union = d.pop("union", UNSET)

        types = []
        _types = d.pop("types", UNSET)
        for types_item_data in _types or []:
            types_item = Schema.from_dict(types_item_data)

            types.append(types_item)

        name = d.pop("name", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = Field.from_dict(fields_item_data)

            fields.append(fields_item)

        error = d.pop("error", UNSET)

        full_name = d.pop("fullName", UNSET)

        _element_type = d.pop("elementType", UNSET)
        element_type: Union[Unset, Schema]
        if _element_type and not isinstance(_element_type, Unset):
            element_type = Schema.from_dict(_element_type)

        else:
            element_type = UNSET

        namespace = d.pop("namespace", UNSET)

        _value_type = d.pop("valueType", UNSET)
        value_type: Union[Unset, Schema]
        if _value_type and not isinstance(_value_type, Unset):
            value_type = Schema.from_dict(_value_type)

        else:
            value_type = UNSET

        nullable = d.pop("nullable", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        _object_props = d.pop("objectProps", UNSET)
        object_props: Union[Unset, SchemaObjectProps]
        if _object_props and not isinstance(_object_props, Unset):
            object_props = SchemaObjectProps.from_dict(_object_props)

        else:
            object_props = UNSET

        schema = cls(
            type_=type_,
            logical_type=logical_type,
            enum_symbols=enum_symbols,
            enum_default=enum_default,
            doc=doc,
            fixed_size=fixed_size,
            union=union,
            types=types,
            name=name,
            fields=fields,
            error=error,
            full_name=full_name,
            element_type=element_type,
            namespace=namespace,
            value_type=value_type,
            nullable=nullable,
            aliases=aliases,
            object_props=object_props,
        )

        schema.additional_properties = d
        return schema

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
