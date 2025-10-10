# Custom OpenAPI Client Templates

This directory contains custom Jinja2 templates for `openapi-python-client` to fix known bugs in the generated code.

## Templates

### `property_templates/property_macros.py.jinja`

**Issue**: The default template doesn't check for `None` before calling `isoparse()` on optional date/datetime fields, causing `TypeError: object of type 'NoneType' has no len()` when APIs return `null`.

**GitHub Issue**: https://github.com/openapi-generators/openapi-python-client/issues/997

**Fix**: Changed the condition to check if the value is truthy and not `Unset` before parsing (line 8):

```jinja2
if _{{ property.python_name }} and not isinstance(_{{ property.python_name }}, Unset):
    {{ property.python_name }} = {{ construct_function(...) }}
else:
    {{ property.python_name }} = UNSET
```

This ensures that when the API returns `null` (or any falsy value) for an optional date field, we treat it as `UNSET` rather than attempting to parse it with `isoparse()`.

## Usage

The `stolon sync spec` command automatically uses these custom templates via the `--custom-template-path` flag.

## Maintenance

When upgrading `openapi-python-client`, check if the upstream templates have fixed these issues and update or remove custom templates accordingly.
