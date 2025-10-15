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
    parameters: list[ParameterInfo] = field(default_factory=list)
    return_type: str = "None"
    docstring: str = ""
    response_model: str | None = None  # Model class for parsing response


class ApiFunctionExtractor(cst.CSTVisitor):
    """Extract API function metadata from generated OpenAPI client files."""

    METADATA_DEPENDENCIES = (cst.metadata.ParentNodeProvider,)

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
        parameters = []

        for param in node.params.params:
            # Skip 'client' parameter as we'll replace it with StolonClient
            if isinstance(param.name, cst.Name) and param.name.value == "client":
                continue

            param_name = param.name.value if isinstance(param.name, cst.Name) else str(param.name)

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
        if node.body.body:
            first_stmt = node.body.body[0]
            if m.matches(first_stmt, m.SimpleStatementLine(body=[m.Expr(value=m.SimpleString())])):
                expr_stmt = first_stmt.body[0]
                if isinstance(expr_stmt, cst.Expr) and isinstance(expr_stmt.value, cst.SimpleString):
                    # Remove quotes and clean up
                    docstring = expr_stmt.value.value.strip('"""').strip("'''").strip()
                    return docstring
        return ""

    def _extract_response_model(self, return_type: str, variant: str) -> str | None:
        """Extract the response model class name from return type.

        Args:
            return_type: The return type annotation (e.g., "Optional[ApiBillingEntity]")
            variant: Function variant (sync, sync_detailed, etc.)

        Returns:
            Model class name if found, None otherwise
        """
        # For detailed variants, return type is Response[Model]
        if "detailed" in variant and "Response[" in return_type:
            # Extract: Response[ApiBillingEntity] -> ApiBillingEntity
            start = return_type.find("[") + 1
            end = return_type.rfind("]")
            if start > 0 and end > start:
                return return_type[start:end].strip()

        # For non-detailed variants, return type is Optional[Model] or Model
        if "Optional[" in return_type:
            # Extract: Optional[ApiBillingEntity] -> ApiBillingEntity
            start = return_type.find("[") + 1
            end = return_type.rfind("]")
            if start > 0 and end > start:
                return return_type[start:end].strip()

        # If no Optional/Response wrapper, it might be the model itself
        if return_type not in {"None", "Any", "dict", "list", "str", "int", "bool"}:
            return return_type

        return None


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

    all_functions = []

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
            wrapper = cst.metadata.MetadataWrapper(module)

            # Extract functions
            extractor = ApiFunctionExtractor(module_path)
            wrapper.visit(extractor)

            all_functions.extend(extractor.functions)

        except Exception as e:
            logger.warning(f"Failed to parse {api_file}: {e}")

    logger.info(
        "Discovered API functions",
        total=len(all_functions),
        files_scanned=len(list(api_path.rglob("*.py"))),
    )

    return all_functions


def convert_optional_to_union(type_annotation: str) -> str:
    """Convert Optional[X] to X | None.

    Args:
        type_annotation: Type annotation string (e.g., "Optional[ApiBillingEntity]")

    Returns:
        Converted type annotation using union syntax (e.g., "ApiBillingEntity | None")
    """
    # Convert Optional[X] to X | None
    if type_annotation.startswith("Optional[") and type_annotation.endswith("]"):
        inner_type = type_annotation[9:-1]  # Extract X from Optional[X]
        return f"{inner_type} | None"
    return type_annotation


def generate_wrapper_code(
    func_info: FunctionInfo,
    service: str,
    env: str,
    domain: str,
) -> tuple[dict[str, str], str]:
    """Generate wrapper function code for a single API function.

    Args:
        func_info: Function metadata
        service: Service name (e.g., "billing_bookkeeper")
        env: Environment name (e.g., "dev")
        domain: Domain for the environment (e.g., "dev1.dev.clover.com")

    Returns:
        Tuple of (imports_dict, function_code)
        - imports_dict maps import statement to a key for deduplication
        - function_code is the generated function body
    """
    service_underscore = service.replace("-", "_")

    # Convert return type from Optional[X] to X | None
    return_type = convert_optional_to_union(func_info.return_type)

    # Build import statements as a dict for deduplication
    imports = {
        "typing_Any": "from typing import Any",
        "stolon_client": "from stolon.client import StolonClient",
        f"api_{func_info.api_function_name}": f"from stolon.generated.{service_underscore}_{env}.open_api_definition_client.api.{func_info.module_path} import {func_info.api_function_name}",
    }

    # Add Response and HTTPStatus imports for detailed variants
    if "detailed" in func_info.variant:
        imports["http_HTTPStatus"] = "from http import HTTPStatus"
        imports["types_Response"] = f"from stolon.generated.{service_underscore}_{env}.open_api_definition_client.types import Response"

    # Add JSON import (always needed)
    imports["json"] = "import json"

    # Add response model import if available
    if func_info.response_model:
        # Guess model module path (lowercase with underscores)
        model_module = "".join(["_" + c.lower() if c.isupper() else c for c in func_info.response_model]).lstrip("_")
        imports[f"model_{func_info.response_model}"] = (
            f"from stolon.generated.{service_underscore}_{env}.open_api_definition_client.models.{model_module} import {func_info.response_model}"
        )

    # Build function parameters
    params = ["*", "client: StolonClient"]
    call_params = []

    for param in func_info.parameters:
        if param.default:
            params.append(f"{param.name}: {param.type_annotation} = {param.default}")
        else:
            params.append(f"{param.name}: {param.type_annotation}")
        call_params.append(f"{param.name}={param.name}")

    param_str = ",\n    ".join(params)
    call_param_str = ", ".join(call_params)

    # Build response parsing logic based on variant
    if "detailed" in func_info.variant:
        # For detailed variants, we need to return a Response object
        response_parsing = f"""
    # Parse response into Response object (detailed variant)
    import json
    from http import HTTPStatus
    from stolon.generated.{service_underscore}_{env}.open_api_definition_client.types import Response

    # Parse body if JSON
    body_json = None
    if proxy_response.body:
        try:
            body_json = json.loads(proxy_response.body)
        except json.JSONDecodeError:
            pass

    # Parse response using generated function's parser
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
    else:
        # For non-detailed variants, return parsed model or None
        if func_info.response_model:
            response_parsing = f"""
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
            response_parsing = """
    # No response model, return None
    return None
"""

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
    # Extract request parameters from generated function
    kwargs = {func_info.api_function_name}._get_kwargs({call_param_str})

    # Proxy request through stolon server
    proxy_response = client.proxy_request(
        domain="{domain}",
        method=kwargs["method"],
        path=kwargs["url"],
        environment_name="{env}",
        json_body=kwargs.get("json"),
        params=kwargs.get("params"),
        timeout=30.0,
    )
{response_parsing}
'''

    # Return imports dict and function code separately for deduplication
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
        generated_client_path: Path to generated client directory
        output_path: Optional output path for wrapper files (default: src/stolon/api/{service}_{env})

    Returns:
        Dictionary mapping output file paths to generated code
    """
    # Determine output path
    if output_path is None:
        output_path = Path("src/stolon/api") / f"{service.replace('-', '_')}_{env}"

    # Domain mapping
    domain_map = {
        "dev": "dev1.dev.clover.com",
        "demo": "demo.clover.com",
        "prod": "www.clover.com",
        "apidev": "apidev1.dev.clover.com",  # For agreement-k8s
    }

    # Special case for agreement-k8s which uses apidev subdomain
    if service == "agreement-k8s" and env == "dev":
        domain = domain_map["apidev"]
    else:
        domain = domain_map.get(env, "dev1.dev.clover.com")

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
    generated_files = {}

    for module_key, module_functions in functions_by_module.items():
        # Collect all imports and function code
        all_imports: dict[str, str] = {}
        function_codes = []

        # Generate each function
        for func_info in module_functions:
            imports, func_code = generate_wrapper_code(func_info, service, env, domain)
            # Merge imports (dict ensures deduplication)
            all_imports.update(imports)
            function_codes.append(func_code)

        # Build complete module code
        header = f'''"""
Proxied wrapper functions for {service} {env} - {module_key}.

Auto-generated by stolon sync spec.
These wrappers route requests through the stolon server for automatic
token management, logging, and retry logic.
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
