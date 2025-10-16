"""Generate type-safe wrapper functions for OpenAPI-generated clients that proxy through stolon server."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import libcst as cst
import libcst.matchers as m
import structlog

logger = structlog.get_logger()


@dataclass
class ParameterInfo:
    """Information about a function parameter."""

    name: str
    type_annotation: str
    default: str | None = None


@dataclass
class FunctionInfo:
    """Information about a generated API function to wrap."""

    module_path: str  # Relative path like "billing_entity.create_billing_entity"
    api_function_name: str  # e.g., "create_billing_entity"
    variant: str  # "sync", "sync_detailed", "asyncio", "asyncio_detailed"
    parameters: list[ParameterInfo] = field(default_factory=lambda: [])
    return_type: str = "None"
    docstring: str = ""
    response_model: str | None = None  # Model class for parsing response


class ApiFunctionExtractor(cst.CSTVisitor):
    """Extract API function metadata from generated OpenAPI client files."""

    METADATA_DEPENDENCIES = (cst.metadata.ParentNodeProvider,)  # type: ignore[attr-defined]

    def __init__(self, module_path: str) -> None:
        """Initialize the extractor.

        Args:
            module_path: Relative module path (e.g., "billing_entity.create_billing_entity")
        """
        super().__init__()
        self.module_path = module_path
        self.functions: list[FunctionInfo] = []

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        """Visit function definitions and extract metadata."""
        func_name = node.name.value

        # Only process sync, sync_detailed, asyncio, asyncio_detailed
        if func_name not in {"sync", "sync_detailed", "asyncio", "asyncio_detailed"}:
            return

        # Extract the API function name from module path
        # e.g., "billing_entity.create_billing_entity" -> "create_billing_entity"
        api_function_name = self.module_path.split(".")[-1]

        # Extract parameters
        parameters = self._extract_parameters(node)

        # Extract return type
        return_type = self._extract_return_type(node)

        # Extract docstring
        docstring = self._extract_docstring(node)

        # Determine response model from return type
        response_model = self._extract_response_model(return_type, func_name)

        func_info = FunctionInfo(
            module_path=self.module_path,
            api_function_name=api_function_name,
            variant=func_name,
            parameters=parameters,
            return_type=return_type,
            docstring=docstring,
            response_model=response_model,
        )

        self.functions.append(func_info)
        logger.debug(
            "Extracted function",
            api_function=api_function_name,
            variant=func_name,
            parameters=len(parameters),
        )

    def _extract_parameters(self, node: cst.FunctionDef) -> list[ParameterInfo]:
        """Extract parameter information from function definition."""
        parameters: list[ParameterInfo] = []

        # Extract both regular params and keyword-only params
        # OpenAPI-generated functions use *, client: ..., body: ... syntax
        # So parameters are in kwonly_params, not params
        all_params = list(node.params.params)

        # Some functions have keyword-only params (after *), some don't
        if hasattr(node.params, "kwonly_params") and node.params.kwonly_params:
            all_params.extend(node.params.kwonly_params)

        for param in all_params:
            # Skip 'client' parameter as we'll replace it with StolonClient
            # param.name is always a Name or other specific type at this point
            if param.name.value == "client":
                continue

            param_name = param.name.value if hasattr(param.name, "value") else str(param.name)

            # Extract type annotation
            type_annotation = "Any"
            if param.annotation:
                type_annotation = cst.Module([]).code_for_node(param.annotation.annotation)

            # Extract default value
            default = None
            if param.default:
                default = cst.Module([]).code_for_node(param.default)

            parameters.append(
                ParameterInfo(
                    name=param_name,
                    type_annotation=type_annotation,
                    default=default,
                )
            )

        return parameters

    def _extract_return_type(self, node: cst.FunctionDef) -> str:
        """Extract return type annotation from function definition."""
        if node.returns:
            return cst.Module([]).code_for_node(node.returns.annotation)
        return "None"

    def _extract_docstring(self, node: cst.FunctionDef) -> str:
        """Extract docstring from function definition."""
        if not isinstance(node.body, cst.IndentedBlock) or not node.body.body:
            return ""

        first_stmt = node.body.body[0]
        if (
            m.matches(first_stmt, m.SimpleStatementLine(body=[m.Expr(value=m.SimpleString())]))
            and isinstance(first_stmt, cst.SimpleStatementLine)
            and first_stmt.body
        ):
            expr_stmt = first_stmt.body[0]
            if isinstance(expr_stmt, cst.Expr) and isinstance(expr_stmt.value, cst.SimpleString):
                # Remove quotes and clean up
                docstring = expr_stmt.value.value
                # Remove triple quotes if present
                if (
                    docstring.startswith('"""')
                    and docstring.endswith('"""')
                    or docstring.startswith("'''")
                    and docstring.endswith("'''")
                ):
                    docstring = docstring[3:-3]
                return docstring.strip()
        return ""

    def _extract_response_model(self, return_type: str, variant: str) -> str | None:
        """Extract the response model class name from return type.

        Args:
            return_type: The return type annotation (e.g., "Optional[ApiBillingEntity]")
            variant: Function variant (sync, sync_detailed, etc.)

        Returns:
            Simple model class name if found (e.g., "ApiBillingEntity"), None otherwise.
            Returns None for complex types like Union, list, etc.
        """
        # For detailed variants, return type is Response[Model]
        if "detailed" in variant and "Response[" in return_type:
            # Extract: Response[ApiBillingEntity] -> ApiBillingEntity
            start = return_type.find("[") + 1
            end = return_type.rfind("]")
            if start > 0 and end > start:
                inner_type = return_type[start:end].strip()
                # Only return if it's a simple type (starts with capital, no special characters)
                if self._is_simple_model_type(inner_type):
                    return inner_type

        # For non-detailed variants, return type is Optional[Model] or Model
        if "Optional[" in return_type:
            # Extract: Optional[ApiBillingEntity] -> ApiBillingEntity
            start = return_type.find("[") + 1
            end = return_type.rfind("]")
            if start > 0 and end > start:
                inner_type = return_type[start:end].strip()
                # Only return if it's a simple type
                if self._is_simple_model_type(inner_type):
                    return inner_type

        # If no Optional/Response wrapper, check if it's a simple model
        if self._is_simple_model_type(return_type):
            return return_type

        return None

    def _is_simple_model_type(self, type_str: str) -> bool:
        """Check if a type string is a simple model class (not Union, list, dict, etc.).

        Args:
            type_str: Type annotation string

        Returns:
            True if it's a simple model class name, False otherwise
        """
        # Skip built-in types
        if type_str in {"None", "Any", "dict", "list", "str", "int", "bool", "float"}:
            return False

        # Skip complex types (Union, list, dict, etc.)
        if any(keyword in type_str for keyword in ["Union[", "list[", "dict[", "List[", "Dict[", "Optional["]):
            return False

        # Skip types with special characters (except underscore)
        if any(char in type_str for char in ["[", "]", ",", "|", '"', "'"]):
            return False

        # Must start with capital letter (standard for model classes)
        return not (not type_str or not type_str[0].isupper())


def discover_api_functions(generated_client_path: Path) -> list[FunctionInfo]:
    """Discover all API functions in a generated client.

    Args:
        generated_client_path: Path to generated client (e.g., src/stolon/generated/billing_bookkeeper_dev)

    Returns:
        List of FunctionInfo objects
    """
    api_path = generated_client_path / "open_api_definition_client" / "api"

    if not api_path.exists():
        logger.warning("API path not found", path=str(api_path))
        return []

    all_functions: list[FunctionInfo] = []

    # Scan all API modules
    for api_file in api_path.rglob("*.py"):
        if api_file.name == "__init__.py":
            continue

        # Build module path relative to api directory
        # e.g., api/billing_entity/create_billing_entity.py -> billing_entity.create_billing_entity
        rel_path = api_file.relative_to(api_path)
        module_path = str(rel_path.with_suffix("")).replace("/", ".")

        try:
            source_code = api_file.read_text()
            module = cst.parse_module(source_code)

            # Wrap with metadata for parent node access
            wrapper = cst.metadata.MetadataWrapper(module)  # type: ignore[attr-defined]

            # Extract functions
            extractor = ApiFunctionExtractor(module_path)
            wrapper.visit(extractor)  # type: ignore[attr-defined]

            all_functions.extend(extractor.functions)

        except Exception as e:
            logger.warning(f"Failed to parse {api_file}: {e}")

    logger.info(
        "Discovered API functions",
        total=len(all_functions),
        files_scanned=len(list(api_path.rglob("*.py"))),
    )

    return all_functions


def convert_to_pipe_union(type_annotation: str) -> str:
    """Convert Union[X, Y] and Optional[X] to pipe union syntax (X | Y) recursively.

    Handles nested types like Response[Union[X, Y]] -> Response[X | Y].

    Args:
        type_annotation: Type annotation string (e.g., "Union[X, Y]" or "Optional[X]")

    Returns:
        Converted type annotation using pipe union syntax (e.g., "X | Y" or "X | None")
    """
    type_annotation = type_annotation.strip()

    # Base case: no brackets, return as-is
    if "[" not in type_annotation:
        return type_annotation

    # Handle Optional[X] -> X | None
    if type_annotation.startswith("Optional[") and type_annotation.endswith("]"):
        inner_type = type_annotation[9:-1]  # Extract X from Optional[X]
        converted_inner = convert_to_pipe_union(inner_type)  # Recursive
        return f"{converted_inner} | None"

    # Handle Union[X, Y, Z] -> X | Y | Z
    if type_annotation.startswith("Union[") and type_annotation.endswith("]"):
        inner = type_annotation[6:-1]  # Remove "Union[" and "]"

        # Split by comma, but respect nested brackets
        types: list[str] = []
        current = ""
        depth = 0
        for char in inner:
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
            elif char == "," and depth == 0:
                types.append(current.strip())
                current = ""
                continue
            current += char
        if current:
            types.append(current.strip())

        # Convert each type recursively and join with pipe
        converted_types: list[str] = [convert_to_pipe_union(t) for t in types]
        return " | ".join(converted_types)

    # Handle generic types like Response[X], list[Y], dict[K, V]
    # Extract the wrapper and the content, convert content recursively
    bracket_pos = type_annotation.find("[")
    if bracket_pos > 0 and type_annotation.endswith("]"):
        wrapper = type_annotation[:bracket_pos]
        inner = type_annotation[bracket_pos + 1 : -1]
        converted_inner = convert_to_pipe_union(inner)
        return f"{wrapper}[{converted_inner}]"

    return type_annotation


def extract_model_names_from_type(type_annotation: str) -> set[str]:
    """Extract all model class names from a type annotation.

    Handles various formats like:
    - Response[Model]
    - Model | ResponseError
    - list["Model"]
    - Response[Model | list["Model"]]

    Args:
        type_annotation: Type annotation string

    Returns:
        Set of model class names found in the type annotation
    """
    import re

    models: set[str] = set()

    # Pattern to match capitalized identifiers (potential model names)
    # This will match things like ApiModel, ResponseError, etc.
    # Ignore built-in types, generic types, and standard library types
    builtins = {
        "None",
        "Any",
        "Response",
        "HTTPStatus",
        "UUID",  # from uuid module, handled separately
    }

    # Find all quoted strings (forward references like list["ModelName"])
    quoted_pattern = r'["\']([A-Z][a-zA-Z0-9_]*)["\']'
    for match in re.finditer(quoted_pattern, type_annotation):
        model_name = match.group(1)
        if model_name not in builtins:
            models.add(model_name)

    # Find all unquoted capitalized identifiers
    # Match word boundaries to avoid partial matches
    word_pattern = r"\b([A-Z][a-zA-Z0-9_]*)\b"
    for match in re.finditer(word_pattern, type_annotation):
        model_name = match.group(1)
        if model_name not in builtins:
            models.add(model_name)

    return models


def _camel_to_snake_case(model_name: str) -> str:
    """Convert CamelCase model name to snake_case module name.

    Args:
        model_name: CamelCase model name (e.g., "Create4Response200")

    Returns:
        snake_case module name (e.g., "create_4_response_200")
    """
    model_module = ""
    prev_char = ""
    for i, c in enumerate(model_name):
        # Add underscore before uppercase letter (if previous wasn't uppercase)
        # Add underscore before digit only if previous was a lowercase letter
        if i > 0 and (c.isupper() and not prev_char.isupper() or c.isdigit() and prev_char.islower()):
            model_module += "_"
        model_module += c.lower()
        prev_char = c
    return model_module


def _add_stdlib_imports(imports: dict[str, str], full_type_string: str, service_underscore: str, env: str) -> None:
    """Add standard library imports based on type annotations.

    Args:
        imports: Dictionary to add imports to
        full_type_string: Combined string of all type annotations
        service_underscore: Service name with underscores
        env: Environment name
    """
    if "UUID" in full_type_string:
        imports["uuid_UUID"] = "from uuid import UUID"
    if "datetime" in full_type_string:
        imports["datetime"] = "import datetime"
    if "Union" in full_type_string:
        imports["typing_Union"] = "from typing import Union"
    if "Unset" in full_type_string or "UNSET" in full_type_string:
        imports["types_Unset_UNSET"] = (
            f"from stolon.openapi_generated.{service_underscore}_{env}.open_api_definition_client.types "
            f"import UNSET, Unset"
        )


def _add_model_imports(
    imports: dict[str, str],
    func_info: FunctionInfo,
    return_type: str,
    service_underscore: str,
    env: str,
) -> None:
    """Add model imports based on type annotations.

    Args:
        imports: Dictionary to add imports to
        func_info: Function metadata
        return_type: Converted return type annotation
        service_underscore: Service name with underscores
        env: Environment name
    """
    # Extract model names from return type and parameters
    model_names = extract_model_names_from_type(return_type)
    for param in func_info.parameters:
        model_names.update(extract_model_names_from_type(param.type_annotation))

    # Skip Union and Unset - handled separately
    skip_models = {"Union", "Unset"}

    for model_name in model_names:
        if model_name in skip_models:
            continue

        model_module = _camel_to_snake_case(model_name)
        imports[f"model_{model_name}"] = (
            f"from stolon.openapi_generated.{service_underscore}_{env}."
            f"open_api_definition_client.models.{model_module} "
            f"import {model_name}"
        )


def _build_imports(
    func_info: FunctionInfo,
    service: str,
    env: str,
    return_type: str,
    module_dir: str,
) -> dict[str, str]:
    """Build import statements for a wrapper function.

    Args:
        func_info: Function metadata
        service: Service name
        env: Environment name
        return_type: Converted return type annotation
        module_dir: Module directory name

    Returns:
        Dictionary mapping import keys to import statements
    """
    service_underscore = service.replace("-", "_")

    # Build base imports
    imports = {
        "typing_Any": "from typing import Any",
        "stolon_client": "from stolon.client import StolonClient",
        f"api_{func_info.api_function_name}": (
            f"from stolon.openapi_generated.{service_underscore}_{env}."
            f"open_api_definition_client.api.{module_dir} "
            f"import {func_info.api_function_name}"
        ),
        "json": "import json",
    }

    # Add Response and HTTPStatus imports for detailed variants
    if "detailed" in func_info.variant:
        imports["http_HTTPStatus"] = "from http import HTTPStatus"
        imports["types_Response"] = (
            f"from stolon.openapi_generated.{service_underscore}_{env}.open_api_definition_client.types import Response"
        )

    # Collect all type annotations and default values
    all_type_annotations = [return_type]
    all_type_annotations.extend(param.type_annotation for param in func_info.parameters)
    all_type_annotations.extend(param.default for param in func_info.parameters if param.default)
    full_type_string = " ".join(all_type_annotations)

    # Add standard library and model imports
    _add_stdlib_imports(imports, full_type_string, service_underscore, env)
    _add_model_imports(imports, func_info, return_type, service_underscore, env)

    return imports


def _build_function_params(func_info: FunctionInfo) -> tuple[str, str]:
    """Build function parameter strings.

    Args:
        func_info: Function metadata

    Returns:
        Tuple of (param_str, call_param_str) for function signature and call
    """
    params: list[str] = ["*", "client: StolonClient"]
    call_params: list[str] = []

    for param in func_info.parameters:
        if param.default:
            params.append(f"{param.name}: {param.type_annotation} = {param.default}")
        else:
            params.append(f"{param.name}: {param.type_annotation}")
        call_params.append(f"{param.name}={param.name}")

    param_str = ",\n    ".join(params)
    call_param_str = ", ".join(call_params)

    return param_str, call_param_str


def _build_response_parsing(func_info: FunctionInfo, service: str, env: str) -> str:
    """Build response parsing logic for a wrapper function.

    Args:
        func_info: Function metadata
        service: Service name
        env: Environment name

    Returns:
        Response parsing code as a string
    """
    service_underscore = service.replace("-", "_")

    if "detailed" in func_info.variant:
        # Detailed variants return Response objects
        return f"""
    # Parse response into Response object (detailed variant)
    import json
    from http import HTTPStatus
    from stolon.openapi_generated.{service_underscore}_{env}.open_api_definition_client.types import Response

    # Parse body if JSON
    body_json = None
    if proxy_response.body:
        try:
            body_json = json.loads(proxy_response.body)
        except json.JSONDecodeError:
            pass

    # Parse response using generated function's parser
    # Explicit type annotation to help type checkers infer the Response[T] generic
    parsed: {func_info.response_model} | None
    if body_json and proxy_response.status_code == 200 and {func_info.response_model}:
        parsed = {func_info.response_model}.from_dict(body_json)
    else:
        parsed = None

    return Response(
        status_code=HTTPStatus(proxy_response.status_code),
        content=proxy_response.body.encode('utf-8') if proxy_response.body else b'',
        headers=proxy_response.headers,
        parsed=parsed,
    )
"""
    elif func_info.response_model:
        # Non-detailed variants with a response model
        return f"""
    # Parse response body
    import json
    if proxy_response.body and proxy_response.status_code == 200:
        try:
            body_json = json.loads(proxy_response.body)
            return {func_info.response_model}.from_dict(body_json)
        except (json.JSONDecodeError, KeyError, TypeError):
            pass
    return None
"""
    else:
        # No response model
        return """
    # No response model, return None
    return None
"""


def generate_wrapper_code(
    func_info: FunctionInfo,
    service: str,
    env: str,
    domain: str,
    base_path: str = "",
) -> tuple[dict[str, str], str]:
    """Generate wrapper function code for a single API function.

    Args:
        func_info: Function metadata
        service: Service name (e.g., "billing_bookkeeper")
        env: Environment name (e.g., "dev")
        domain: Domain for the environment (e.g., "dev1.dev.clover.com")
        base_path: Base path to prepend to all API paths (e.g., "/agreement")

    Returns:
        Tuple of (imports_dict, function_code)
        - imports_dict maps import statement to a key for deduplication
        - function_code is the generated function body
    """
    # Convert return type to pipe union syntax
    return_type = convert_to_pipe_union(func_info.return_type)

    # Extract module directory name
    module_dir = func_info.module_path.split(".")[0]

    # Build all components using helper functions
    imports = _build_imports(func_info, service, env, return_type, module_dir)
    param_str, call_param_str = _build_function_params(func_info)
    response_parsing = _build_response_parsing(func_info, service, env)

    # Build path construction logic
    if base_path:
        path_construction = f'''
    # Extract request parameters from generated function
    kwargs = {func_info.api_function_name}._get_kwargs({call_param_str})

    # Prepend base path to URL
    path = "{base_path}" + kwargs["url"]'''
    else:
        path_construction = f'''
    # Extract request parameters from generated function
    kwargs = {func_info.api_function_name}._get_kwargs({call_param_str})

    # Use path directly from generated function
    path = kwargs["url"]'''

    # Build complete function code
    function_code = f'''
def {func_info.api_function_name}_{func_info.variant}(
    {param_str}
) -> {return_type}:
    """{func_info.docstring or f"{func_info.api_function_name} - proxied through stolon server"}

    This function wraps the generated OpenAPI client to proxy requests through
    the stolon server, enabling automatic token management and logging.

    Args:
        client: StolonClient instance for proxying requests
        {chr(10).join(f"        {p.name}: {p.type_annotation}" for p in func_info.parameters)}

    Returns:
        {return_type}
    """
{path_construction}

    # Proxy request through stolon server
    proxy_response = client.proxy_request(
        domain="{domain}",
        method=kwargs["method"],
        path=path,
        environment_name="{env}",
        json_body=kwargs.get("json"),
        params=kwargs.get("params"),
        timeout=30.0,
    )
{response_parsing}
'''

    return imports, function_code


def generate_wrappers_for_service(
    service: str,
    env: str,
    generated_client_path: Path,
    output_path: Path | None = None,
) -> dict[str, str]:
    """Generate all wrapper functions for a service.

    Args:
        service: Service name (e.g., "billing-bookkeeper")
        env: Environment name (e.g., "dev")
        generated_client_path: Path to OpenAPI-generated client directory
        output_path: Optional output path for wrapper files (default: src/stolon/generated/{service}_{env})

    Returns:
        Dictionary mapping output file paths to generated code
    """
    # Determine output path
    if output_path is None:
        output_path = Path("src/stolon/generated") / f"{service.replace('-', '_')}_{env}"

    # Domain mapping for runtime API calls
    # Note: Some services use api* domains (like apidev1) for OpenAPI spec fetching,
    # but runtime API calls always use the standard domains below
    domain_map = {
        "dev": "dev1.dev.clover.com",
        "demo": "demo2.dev.clover.com",
        "prod": "www.clover.com",
    }

    # Base path mapping for services that use context path prefixes
    # These paths are prepended to all API paths from the OpenAPI spec
    base_path_map = {
        "agreement-k8s": "/agreement",
        "billing-event": "/billing-event",
    }

    domain = domain_map.get(env, "dev1.dev.clover.com")
    base_path = base_path_map.get(service, "")

    # Discover all API functions
    functions = discover_api_functions(generated_client_path)

    if not functions:
        logger.warning("No API functions discovered", service=service, env=env)
        return {}

    # Group functions by module path (to organize into files)
    from collections import defaultdict

    functions_by_module: dict[str, list[FunctionInfo]] = defaultdict(list)
    for func in functions:
        # Use the first part of module path as grouping key
        # e.g., "billing_entity.create_billing_entity" -> "billing_entity"
        module_key = func.module_path.split(".")[0] if "." in func.module_path else func.module_path
        functions_by_module[module_key].append(func)

    # Generate wrapper code for each module
    generated_files: dict[str, str] = {}

    for module_key, module_functions in functions_by_module.items():
        # Collect all imports and function code
        all_imports: dict[str, str] = {}
        function_codes: list[str] = []

        # Generate each function
        for func_info in module_functions:
            imports, func_code = generate_wrapper_code(func_info, service, env, domain, base_path)
            # Merge imports (dict ensures deduplication)
            all_imports.update(imports)
            function_codes.append(func_code)

        # Build complete module code
        header = f'''"""
Proxied wrapper functions for {service} {env} - {module_key}.

Auto-generated by stolon sync spec - do not edit directly.
These wrappers route requests through the stolon server for automatic
token management, logging, and retry logic.

The underlying OpenAPI client is in stolon.openapi_generated - DO NOT EDIT those files.
These wrapper files in stolon.generated can be customized if needed.
"""
'''

        # Combine: header + imports + functions
        imports_section = "\n".join(sorted(all_imports.values()))
        full_module_code = header + "\n" + imports_section + "\n\n" + "\n\n".join(function_codes)

        # Determine output file path
        output_file = output_path / f"{module_key}.py"
        generated_files[str(output_file)] = full_module_code

        logger.debug(
            "Generated wrapper module",
            module=module_key,
            functions=len(module_functions),
            output=str(output_file),
        )

    logger.info(
        "Generated wrapper modules",
        service=service,
        env=env,
        modules=len(generated_files),
        total_functions=len(functions),
    )

    return generated_files


def write_wrappers(generated_files: dict[str, str]) -> None:
    """Write generated wrapper files to disk.

    Args:
        generated_files: Dictionary mapping file paths to generated code
    """
    for file_path, code in generated_files.items():
        output_file = Path(file_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(code)
        logger.info("Wrote wrapper file", path=str(output_file))
