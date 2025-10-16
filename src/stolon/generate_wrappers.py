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

    def _extract_inner_type_from_wrapper(self, return_type: str, wrapper: str) -> str | None:
        """Extract inner type from a wrapper type like Response[...] or Optional[...].

        Args:
            return_type: The full return type annotation
            wrapper: The wrapper to extract from (e.g., "Response[", "Optional[")

        Returns:
            Inner type string if found, None otherwise
        """
        if not return_type.startswith(wrapper) or not return_type.endswith("]"):
            return None

        start = return_type.find("[") + 1
        end = return_type.rfind("]")
        if start > 0 and end > start:
            return return_type[start:end].strip()
        return None

    def _model_from_inner_type(self, inner_type: str) -> str | None:
        """Extract model name from an inner type (handles list[Model] or Model).

        Args:
            inner_type: Inner type string (e.g., "list[Model]" or "Model")

        Returns:
            Model string ("list[Model]" or "Model") if found, None otherwise
        """
        if inner_type.startswith("list["):
            list_element = self._extract_list_element_type(inner_type)
            if list_element:
                return f"list[{list_element}]"
        elif self._is_simple_model_type(inner_type):
            return inner_type
        return None

    def _extract_response_model(self, return_type: str, variant: str) -> str | None:
        """Extract the response model class name from return type.

        Args:
            return_type: The return type annotation (e.g., "Optional[ApiBillingEntity]")
            variant: Function variant (sync, sync_detailed, etc.)

        Returns:
            Simple model class name if found (e.g., "ApiBillingEntity"),
            or "list[ModelName]" for list returns, None otherwise.
        """
        # For detailed variants, extract from Response[...]
        if "detailed" in variant and "Response[" in return_type:
            inner_type = self._extract_inner_type_from_wrapper(return_type, "Response[")
            if inner_type:
                model = self._model_from_inner_type(inner_type)
                if model:
                    return model

        # For non-detailed variants, extract from Optional[...]
        if "Optional[" in return_type:
            inner_type = self._extract_inner_type_from_wrapper(return_type, "Optional[")
            if inner_type:
                model = self._model_from_inner_type(inner_type)
                if model:
                    return model

        # Check top-level list or simple model
        model = self._model_from_inner_type(return_type)
        if model:
            return model

        return None

    def _extract_list_element_type(self, list_type: str) -> str | None:
        """Extract the element type from a list type annotation.

        Args:
            list_type: Type annotation like "list[Model]" or "list['Model']"

        Returns:
            Model name if found (e.g., "Model"), None otherwise
        """
        if not list_type.startswith("list[") or not list_type.endswith("]"):
            return None

        element_type = list_type[5:-1].strip()  # Extract "Model" from "list[Model]"

        # Remove quotes if present: list["Model"] -> Model
        if (element_type.startswith('"') and element_type.endswith('"')) or (
            element_type.startswith("'") and element_type.endswith("'")
        ):
            element_type = element_type[1:-1]

        # Check if it's a valid model name
        if element_type and element_type[0].isupper() and element_type.isalnum() or "_" in element_type:
            return element_type

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
    if "Any" in full_type_string:
        imports["typing_Any"] = "from typing import Any"
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


def generate_wrapper_code(
    func_info: FunctionInfo,
    service: str,
    env: str,
    domain: str,
    base_path: str = "",
) -> tuple[dict[str, str], str]:
    """Generate thin stub function code that invokes OpenAPI client on server.

    This generates a simple stub that:
    1. Serializes arguments
    2. Calls StolonClient.invoke_openapi() to execute function on server
    3. Deserializes and returns the result

    Args:
        func_info: Function metadata
        service: Service name (e.g., "billing_bookkeeper")
        env: Environment name (e.g., "dev")
        domain: Domain for the environment (e.g., "dev1.dev.clover.com")
        base_path: Base path (unused in new approach, kept for compatibility)

    Returns:
        Tuple of (imports_dict, function_code)
        - imports_dict maps import statement to a key for deduplication
        - function_code is the generated function body
    """
    # Convert return type to pipe union syntax
    return_type = convert_to_pipe_union(func_info.return_type)

    # Build imports - simpler now, just need stolon client and serialization
    service_underscore = service.replace("-", "_")
    imports = {
        "stolon_client": "from stolon.client import StolonClient",
        "stolon_models": "from stolon.models import OpenAPIService",
        "stolon_serialization": "from stolon.serialization import serialize_argument, deserialize_result",
    }

    # Add Response import for detailed variants
    if "detailed" in func_info.variant:
        imports["types_Response"] = (
            f"from stolon.openapi_generated.{service_underscore}_{env}.open_api_definition_client.types import Response"
        )

    # Add model imports for type annotations
    _add_model_imports(imports, func_info, return_type, service_underscore, env)

    # Add stdlib imports
    all_type_annotations = [return_type]
    all_type_annotations.extend(param.type_annotation for param in func_info.parameters)
    all_type_annotations.extend(param.default for param in func_info.parameters if param.default)
    full_type_string = " ".join(all_type_annotations)
    _add_stdlib_imports(imports, full_type_string, service_underscore, env)

    # Build function parameters
    param_str, _ = _build_function_params(func_info)

    # Build kwargs serialization
    kwarg_serializations: list[str] = []
    for param in func_info.parameters:
        kwarg_serializations.append(f'        "{param.name}": serialize_argument({param.name})')

    kwargs_dict = ",\n".join(kwarg_serializations)

    # Escape the return type string for use in generated code
    # Replace " with \" to safely embed in a double-quoted string
    escaped_return_type = func_info.return_type.replace('"', '\\"')

    # Build complete function code
    function_code = f'''
def {func_info.api_function_name}_{func_info.variant}(
    {param_str}
) -> {return_type}:
    """{func_info.docstring or f"{func_info.api_function_name} - invoked through stolon server"}

    This function invokes the OpenAPI-generated client function on the stolon server,
    enabling automatic token management, logging, and retry logic.

    Args:
        client: StolonClient instance for invoking server-side functions
        {chr(10).join(f"        {p.name}: {p.type_annotation}" for p in func_info.parameters)}

    Returns:
        {return_type}
    """
    # Serialize arguments for transport
    serialized_kwargs = {{
{kwargs_dict}
    }}

    # Invoke OpenAPI function on server
    response = client.invoke_openapi(
        service=OpenAPIService.{service_underscore.upper()}_{env.upper()},
        function_path="{func_info.module_path}",
        variant="{func_info.variant}",
        domain="{domain}",
        environment_name="{env}",
        kwargs=serialized_kwargs,
    )

    # Handle errors
    if not response.success:
        raise RuntimeError(f"OpenAPI invocation failed: {{response.error}}")

    # Deserialize result
    result = deserialize_result(
        response.result,
        "{escaped_return_type}",
        "{service_underscore}_{env}",
    )

    return result  # type: ignore[return-value]
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
