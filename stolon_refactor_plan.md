# Stolon Refactor Plan: Proxy-Through Architecture

## 🎯 Current Status: Phase 1 Complete ✅

**Last Updated**: 2025-10-15

| Phase | Status | Completion Date |
|-------|--------|----------------|
| **Phase 1: Test Coverage** | ✅ **COMPLETE** | 2025-10-15 |
| **Phase 2: Proxy Implementation** | ⏳ Not Started | - |
| **Phase 3: Migration** | ⏳ Not Started | - |
| **Phase 4: OpenAPI Spec** | ⏳ Not Started | - |

### Phase 1 Deliverables ✅

**Test Files Created**:
- ✅ `tests/stolon/test_stolon_client.py` (6 tests, all passing)
- ✅ `tests/stolon/test_environment_base.py` (8 tests, all passing)
- ✅ `tests/stolon/test_stolon_integration.py` (3 tests, require `--external-infra`)

**Test Results**: 14/14 unit tests passing (0.02s runtime, no warnings)

**Coverage Achieved**:
- ✅ Token request/caching/invalidation
- ✅ Force refresh behavior
- ✅ 401 retry logic (critical!)
- ✅ GET/POST/DELETE methods
- ✅ Query parameters
- ✅ Custom timeouts
- ✅ Empty response handling

### Tests That Will Guide the Refactor 🧭

These tests verify the **current behavior** and will ensure the proxy refactor maintains compatibility:

**🔑 Critical Tests (Must Pass After Refactor)**:
1. **`test_request_401_retry_logic`** - Ensures 401 handling works identically in proxy mode
   - Verifies token refresh on auth failure
   - Confirms automatic retry with fresh token
   - This is THE most important test for proxy correctness

2. **`test_get_request_success`** - Basic GET request flow
   - Tests that proxy correctly forwards GET requests
   - Verifies response parsing

3. **`test_post_request_with_json_body`** - POST with JSON payload
   - Tests that proxy correctly forwards JSON bodies
   - Critical for write operations

**📊 Validation Tests (Confirm Behavior Parity)**:
4. **`test_request_with_params`** - Query parameter handling
5. **`test_request_with_custom_timeout`** - Timeout propagation
6. **`test_request_empty_response_returns_none`** - Empty response handling

**Integration Tests (End-to-End Validation)**:
7. **`test_stolon_end_to_end_get_request`** - Full flow with `--external-infra`
   - Run this BEFORE refactor (baseline)
   - Run this AFTER refactor with `use_proxy=True` (validation)
   - Both should produce identical results

**🎯 Refactor Success Criteria**:
- [ ] All 14 existing unit tests pass unchanged
- [ ] Integration test passes with `use_proxy=True`
- [ ] Integration test passes with `use_proxy=False` (backward compat)
- [ ] No changes required to call sites (except optional flag)

---

## Executive Summary

**Current Architecture**: Stolon client calls APIs directly, then informs stolon server about requests/responses for logging.

**Target Architecture**: Stolon client sends request intent to stolon server, which proxies the actual HTTP call, managing auth and logging automatically.

**Key Benefits**:
1. VPN requirement moves to stolon server only (can run on VPN-enabled machine)
2. Test runner can be on any machine on the LAN
3. Enables OpenAPI spec generation for cross-language clients
4. Centralizes auth management (tokens never leave server)
5. Better observability (all traffic flows through one point)

---

## Test Coverage Analysis

### Before Phase 1 (Historical)
1. **`tests/stolon/test_create_reseller.py`** - Requires `--external-infra`, comprehensive integration test
2. **`tests/conftest.py`** - Has `RunningStolonServer` fixture but minimal testing
3. **No unit tests** for stolon components in isolation

**Coverage Gaps (Historical)**:
1. ❌ No tests for `StolonClient.request_internal_token()`
2. ❌ No tests for token caching/invalidation
3. ❌ No tests for `Environment.get()` / `post()` / `delete()` methods
4. ❌ No tests for 401 retry logic
5. ❌ No tests for request/response logging
6. ❌ No mock-based tests (all require real infra)

### After Phase 1 ✅ (Current)

**Unit Tests (No Infrastructure Required)**:
- ✅ **6 tests** in `test_stolon_client.py` covering token management
- ✅ **8 tests** in `test_environment_base.py` covering HTTP operations
- ✅ All critical paths have test coverage
- ✅ 401 retry logic thoroughly tested
- ✅ Mock-based, run in <0.1s

**Integration Tests (Require `--external-infra`)**:
- ✅ **3 tests** in `test_stolon_integration.py` for end-to-end validation
- ✅ Token caching validation
- ✅ Multiple environment instances

**Coverage Status**:
1. ✅ **COVERED**: `StolonClient.request_internal_token()`
2. ✅ **COVERED**: Token caching/invalidation
3. ✅ **COVERED**: `Environment.get()` / `post()` / `delete()` methods
4. ✅ **COVERED**: 401 retry logic
5. ⚠️ **PARTIAL**: Request/response logging (tested indirectly)
6. ✅ **COVERED**: Mock-based tests (14 tests)

---

## Recommendation: **YES**, Add Test Coverage First

**Rationale**:
- Current architecture is simpler to test (client makes direct HTTP calls)
- Once we have tests, refactor with confidence
- Tests will catch regressions during proxy architecture implementation
- Mock-based tests won't require `--external-infra`

---

## Phase 1: Add Test Coverage (Pre-Refactor) ✅ COMPLETE

**Status**: ✅ Complete (2025-10-15)
**Files Created**: 3 test files, 17 tests total
**Test Results**: 14/14 unit tests passing, 3 integration tests ready

### 1.1 Create Mock-Based Unit Tests ✅

**File**: `tests/stolon/test_stolon_client.py`

```python
"""Unit tests for StolonClient (no --external-infra required)."""

import pytest
from unittest.mock import Mock, patch, MagicMock
from stolon.client import StolonClient, HttpHandle
from trifolium.config import Home


@pytest.fixture
def mock_home(tmp_path):
    """Mock home with stolon port file."""
    home = Mock(spec=Home)
    port_file = tmp_path / "stolon_port"
    port_file.write_text("62382")
    home.get_stolon_port.return_value = 62382
    return home


@pytest.fixture
def stolon_client(mock_home):
    """StolonClient with mocked dependencies."""
    return StolonClient(home=mock_home, data_in_logs=False)


def test_base_url_from_port_file(stolon_client):
    """Test that base_url is constructed from port file."""
    assert stolon_client.base_url == "http://0.0.0.0:62382"


def test_base_url_missing_port_raises(mock_home):
    """Test that missing port file raises clear error."""
    mock_home.get_stolon_port.return_value = None
    client = StolonClient(home=mock_home, data_in_logs=False)

    with pytest.raises(RuntimeError, match="Stolon server port not found"):
        _ = client.base_url


@patch('stolon.client.httpx.Client')
def test_request_internal_token_success(mock_httpx_client_class, stolon_client):
    """Test successful token request."""
    # Setup mock response
    mock_response = Mock()
    mock_response.json.return_value = {
        "token": "test_token_123",
        "domain": "dev1.dev.clover.com",
        "cached": False
    }
    mock_response.raise_for_status = Mock()

    mock_client = Mock()
    mock_client.post.return_value = mock_response
    mock_client.__enter__.return_value = mock_client
    mock_client.__exit__.return_value = None
    mock_httpx_client_class.return_value = mock_client

    # Make request
    handle = stolon_client.request_internal_token("dev1.dev.clover.com")

    # Verify
    assert handle.token == "test_token_123"
    assert handle.domain == "dev1.dev.clover.com"
    assert handle.base_url == "https://dev1.dev.clover.com"

    mock_client.post.assert_called_once()
    call_args = mock_client.post.call_args
    assert call_args[0][0] == "http://0.0.0.0:62382/internal_token"
    assert call_args[1]["json"] == {"domain": "dev1.dev.clover.com"}


@patch('stolon.client.httpx.Client')
def test_invalidate_token_success(mock_httpx_client_class, stolon_client):
    """Test token invalidation."""
    mock_response = Mock()
    mock_response.raise_for_status = Mock()

    mock_client = Mock()
    mock_client.delete.return_value = mock_response
    mock_client.__enter__.return_value = mock_client
    mock_client.__exit__.return_value = None
    mock_httpx_client_class.return_value = mock_client

    # Invalidate token
    stolon_client.invalidate_token("dev1.dev.clover.com")

    # Verify
    mock_client.delete.assert_called_once_with(
        "http://0.0.0.0:62382/internal_token/dev1.dev.clover.com"
    )


@patch('stolon.client.httpx.Client')
def test_request_internal_token_with_force_refresh(mock_httpx_client_class, stolon_client):
    """Test force_refresh invalidates token first."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "token": "new_token_456",
        "domain": "dev1.dev.clover.com",
        "cached": False
    }
    mock_response.raise_for_status = Mock()
    mock_response.status_code = 200

    mock_client = Mock()
    mock_client.post.return_value = mock_response
    mock_client.delete.return_value = mock_response
    mock_client.__enter__.return_value = mock_client
    mock_client.__exit__.return_value = None
    mock_httpx_client_class.return_value = mock_client

    # Request with force_refresh
    handle = stolon_client.request_internal_token("dev1.dev.clover.com", force_refresh=True)

    # Verify invalidation happened first
    assert mock_client.delete.call_count == 1
    assert mock_client.post.call_count == 1
```

**File**: `tests/stolon/test_environment_base.py`

```python
"""Unit tests for stolon Environment base class."""

import pytest
from unittest.mock import Mock, patch, MagicMock
from stolon.environments.base import Environment
from stolon.client import StolonClient, HttpHandle
import httpx


class TestEnvironment(Environment):
    """Concrete test environment for unit tests."""

    @property
    def name(self) -> str:
        return "test"

    @property
    def domain(self) -> str:
        return "test.dev.clover.com"


@pytest.fixture
def mock_stolon_client():
    """Mock StolonClient."""
    client = Mock(spec=StolonClient)
    client.base_url = "http://0.0.0.0:62382"
    return client


@pytest.fixture
def test_env(mock_stolon_client):
    """Test environment instance."""
    return TestEnvironment(mock_stolon_client)


def test_ensure_authenticated_gets_token(test_env, mock_stolon_client):
    """Test that _ensure_authenticated requests token."""
    mock_handle = HttpHandle(
        token="test_token",
        domain="test.dev.clover.com",
        base_url="https://test.dev.clover.com"
    )
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Trigger authentication
    test_env._ensure_authenticated()

    # Verify
    assert test_env._handle == mock_handle
    mock_stolon_client.request_internal_token.assert_called_once_with(
        "test.dev.clover.com",
        force_refresh=False
    )


@patch('stolon.environments.base.httpx.Client')
def test_get_request_success(mock_httpx_client_class, test_env, mock_stolon_client):
    """Test successful GET request."""
    # Setup mock handle
    mock_handle = HttpHandle(
        token="test_token",
        domain="test.dev.clover.com",
        base_url="https://test.dev.clover.com"
    )
    mock_stolon_client.request_internal_token.return_value = mock_handle

    # Setup mock HTTP response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"result": "success"}'
    mock_response.json.return_value = {"result": "success"}
    mock_response.raise_for_status = Mock()

    mock_client = Mock()
    mock_client.request.return_value = mock_response
    mock_client.__enter__.return_value = mock_client
    mock_client.__exit__.return_value = None
    mock_httpx_client_class.return_value = mock_client

    # Make request
    result = test_env.get("/v3/test")

    # Verify
    assert result == {"result": "success"}
    mock_client.request.assert_called_once()
    call_args = mock_client.request.call_args
    assert call_args[0][0] == "GET"
    assert call_args[0][1] == "https://test.dev.clover.com/v3/test"


@patch('stolon.environments.base.httpx.Client')
def test_request_401_retry_logic(mock_httpx_client_class, test_env, mock_stolon_client):
    """Test that 401 triggers token refresh and retry."""
    # Setup mock handles (first expired, second fresh)
    expired_handle = HttpHandle(
        token="expired_token",
        domain="test.dev.clover.com",
        base_url="https://test.dev.clover.com"
    )
    fresh_handle = HttpHandle(
        token="fresh_token",
        domain="test.dev.clover.com",
        base_url="https://test.dev.clover.com"
    )
    mock_stolon_client.request_internal_token.side_effect = [expired_handle, fresh_handle]

    # Setup mock HTTP responses (401 then 200)
    mock_401_response = Mock()
    mock_401_response.status_code = 401

    mock_200_response = Mock()
    mock_200_response.status_code = 200
    mock_200_response.text = '{"result": "success_after_retry"}'
    mock_200_response.json.return_value = {"result": "success_after_retry"}
    mock_200_response.raise_for_status = Mock()

    mock_client = Mock()
    mock_client.request.side_effect = [mock_401_response, mock_200_response]
    mock_client.__enter__.return_value = mock_client
    mock_client.__exit__.return_value = None
    mock_httpx_client_class.return_value = mock_client

    # Make request (should retry after 401)
    result = test_env.get("/v3/test")

    # Verify
    assert result == {"result": "success_after_retry"}
    assert mock_client.request.call_count == 2  # Initial + retry
    assert mock_stolon_client.request_internal_token.call_count == 2  # Initial + refresh

    # Verify second call used force_refresh=True
    second_call_kwargs = mock_stolon_client.request_internal_token.call_args_list[1][1]
    assert second_call_kwargs["force_refresh"] is True
```

### 1.2 Add Integration Test Fixture

**File**: `tests/stolon/test_stolon_integration.py` (requires `--external-infra`)

```python
"""Integration tests for stolon (requires --external-infra)."""

import pytest
from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp


@pytest.mark.external_infra
def test_stolon_end_to_end_get_request(stolon_server):
    """Test complete flow: client -> server -> auth -> API -> response."""
    client = StolonClient(home=stolon_server.home, data_in_logs=False)
    env = DevHttp(client)

    # Make a simple GET request to whoami endpoint
    result = env.get("/v1/employees/whoami")

    # Verify we got a response
    assert result is not None
    assert isinstance(result, dict)
    # Response should have employee info fields
    assert "id" in result or "name" in result
```

---

## Phase 2: Refactor to Proxy Architecture

### 2.1 New Server-Side Proxy Endpoint

**File**: `src/stolon/server.py` (additions)

```python
from stolon.models import ProxyRequest, ProxyResponse

@app.post("/proxy")
async def proxy_request(request: ProxyRequest) -> ProxyResponse:
    """
    Proxy an HTTP request through the stolon server.

    This endpoint:
    1. Receives request intent from client (method, path, body, params)
    2. Retrieves/refreshes authentication token
    3. Makes the actual HTTP call to target domain
    4. Returns response to client

    Benefits:
    - Client doesn't need VPN access
    - Server handles all auth token management
    - Logging happens automatically server-side
    """
    domain = request.domain
    method = request.method
    path = request.path

    # Get or refresh token (uses existing cache)
    token_response = await internal_token(InternalTokenRequest(domain=domain))
    token = token_response.token

    # Build full URL
    full_url = f"https://{domain}{path}"

    # Make the actual HTTP call
    headers = {
        "Cookie": f"internalSession={token}",
        "Content-Type": "application/json",
        "X-Clover-Appenv": f"{request.environment_name}:{domain.split('.')[0]}",
    }

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method,
            url=full_url,
            headers=headers,
            json=request.json_body,
            params=request.params,
            timeout=request.timeout or 30.0,
        )

        # Handle 401 - token expired, refresh and retry
        if response.status_code == 401:
            logger.warning(f"Received 401 for {domain}, refreshing token")
            # Invalidate cached token
            if domain in _token_cache:
                del _token_cache[domain]
            # Get fresh token
            token_response = await internal_token(InternalTokenRequest(domain=domain))
            token = token_response.token
            headers["Cookie"] = f"internalSession={token}"

            # Retry request
            response = await client.request(
                method=method,
                url=full_url,
                headers=headers,
                json=request.json_body,
                params=request.params,
                timeout=request.timeout or 30.0,
            )

        # Log request/response automatically
        logger.info(
            "Proxied HTTP request",
            method=method,
            url=full_url,
            status_code=response.status_code,
        )

        # Return response to client
        return ProxyResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            body=response.text,
        )
```

**File**: `src/stolon/models.py` (additions)

```python
from pydantic import BaseModel

class ProxyRequest(BaseModel):
    """Request to proxy an HTTP call through stolon server."""
    domain: str
    method: str  # GET, POST, DELETE, etc.
    path: str  # e.g., "/v3/merchants/ABC123"
    json_body: dict[str, Any] | None = None
    params: dict[str, Any] | None = None
    timeout: float | None = None
    environment_name: str  # For X-Clover-Appenv header

class ProxyResponse(BaseModel):
    """Response from proxied HTTP call."""
    status_code: int
    headers: dict[str, str]
    body: str  # JSON string or other response body
```

### 2.2 Update Client to Use Proxy

**File**: `src/stolon/client.py` (modifications)

```python
class StolonClient:
    """Client for communicating with the stolon server."""

    def proxy_request(
        self,
        domain: str,
        method: str,
        path: str,
        environment_name: str,
        json_body: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> ProxyResponse:
        """
        Proxy an HTTP request through the stolon server.

        This is the new primary method for making API calls. The server handles:
        - Authentication token management
        - 401 retry logic
        - Request/response logging

        Args:
            domain: Target domain (e.g., "dev1.dev.clover.com")
            method: HTTP method
            path: API path
            environment_name: Environment name for headers
            json_body: Optional JSON body for POST/PUT
            params: Optional query parameters
            timeout: Optional timeout in seconds

        Returns:
            ProxyResponse with status code, headers, and body
        """
        request = ProxyRequest(
            domain=domain,
            method=method,
            path=path,
            json_body=json_body,
            params=params,
            timeout=timeout,
            environment_name=environment_name,
        )

        with httpx.Client(timeout=timeout or 30.0) as client:
            response = client.post(
                f"{self.base_url}/proxy",
                json=request.model_dump(),
            )
            response.raise_for_status()

            proxy_response = ProxyResponse(**response.json())
            return proxy_response
```

### 2.3 Update Environment Base to Use Proxy

**File**: `src/stolon/environments/base.py` (modifications)

```python
class Environment(ABC):
    """Abstract base class for stolon environments."""

    def _request(self, method: str, path: str, **kwargs: Unpack[HttpxKwargs]) -> dict[str, Any] | list[Any] | None:
        """
        Make an authenticated HTTP request via stolon server proxy.

        NEW BEHAVIOR: Instead of making the HTTP call directly, this method now
        sends the request intent to the stolon server, which handles auth and proxying.
        """
        # Extract kwargs
        json_data: Any = kwargs.get("json")
        params: dict[str, Any] | None = kwargs.get("params")
        timeout_val: float | None = kwargs.get("timeout")

        # Call stolon server proxy endpoint
        proxy_response = self.client.proxy_request(
            domain=self.domain,
            method=method,
            path=path,
            environment_name=self.name,
            json_body=json_data,
            params=params,
            timeout=timeout_val,
        )

        # Parse response
        if proxy_response.status_code >= 400:
            logger = structlog.get_logger()
            logger.error(
                "HTTP request failed",
                method=method,
                path=path,
                status_code=proxy_response.status_code,
                response_body=proxy_response.body[:500],
            )
            raise httpx.HTTPStatusError(
                message=f"HTTP {proxy_response.status_code}",
                request=None,  # type: ignore
                response=None,  # type: ignore
            )

        # Return JSON if available
        if proxy_response.body:
            import json
            response_data: dict[str, Any] | list[Any] = json.loads(proxy_response.body)
            return response_data
        return None

    # get(), post(), delete() remain unchanged - they call _request()
```

---

## Phase 3: Migration Strategy

### 3.1 Backward Compatibility Approach

**Option A: Feature Flag** (Recommended)

```python
# In StolonClient
def __init__(self, home: Home | None = None, *, data_in_logs: bool, use_proxy: bool = False):
    self.use_proxy = use_proxy  # Default False for backward compat
    # ... rest of init

# In Environment._request()
if self.client.use_proxy:
    # New proxy path
    return self._request_via_proxy(method, path, **kwargs)
else:
    # Old direct path (current implementation)
    return self._request_direct(method, path, **kwargs)
```

Enable with: `StolonClient(use_proxy=True)`

**Option B: Parallel Implementation** (Safer)

- Keep `stolon.environments.base.Environment` (current direct calls)
- Create `stolon.environments.proxy.ProxyEnvironment` (new proxy calls)
- Update test to use `ProxyEnvironment`
- Once stable, deprecate old `Environment`

### 3.2 Migration Steps

1. **Week 1**: Implement proxy endpoint + tests
2. **Week 2**: Update one API wrapper (e.g., `DevResellersAPI`) to use proxy
3. **Week 3**: Run full test suite with both modes, compare behavior
4. **Week 4**: Migrate remaining APIs, deprecate direct mode

---

## Phase 4: OpenAPI Spec Generation

Once proxy architecture is in place:

### 4.1 Generate OpenAPI Spec from Server

**File**: `src/stolon/openapi_spec.py`

```python
"""Generate OpenAPI specification for stolon proxy API."""

from fastapi.openapi.utils import get_openapi

def generate_stolon_openapi_spec():
    """Generate OpenAPI spec for stolon server."""
    from stolon.server import app

    openapi_schema = get_openapi(
        title="Stolon HTTP Proxy API",
        version="1.0.0",
        description="""
        Stolon provides authenticated proxy access to Clover HTTP APIs.

        Benefits:
        - VPN requirement only on stolon server (not clients)
        - Automatic authentication token management
        - Cross-language client support via OpenAPI generators
        - Centralized request/response logging
        """,
        routes=app.routes,
    )

    return openapi_schema

# CLI command: stolon spec --output stolon-api.yaml
```

### 4.2 Generate Clients for Other Languages

```bash
# Generate TypeScript client
openapi-generator-cli generate \
  -i stolon-api.yaml \
  -g typescript-axios \
  -o clients/typescript

# Generate Go client
openapi-generator-cli generate \
  -i stolon-api.yaml \
  -g go \
  -o clients/go

# Generate Rust client
openapi-generator-cli generate \
  -i stolon-api.yaml \
  -g rust \
  -o clients/rust
```

---

## Summary & Call Sites to Update

### Call Sites Using Stolon (Need Import Changes)

**Current Pattern**:
```python
from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp

client = StolonClient(data_in_logs=False)
env = DevHttp(client)
result = env.get("/v3/merchants/ABC123")
```

**After Refactor** (NO CHANGES NEEDED at call sites if using feature flag):
```python
from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp

# Just add use_proxy=True to enable new behavior
client = StolonClient(data_in_logs=False, use_proxy=True)
env = DevHttp(client)
result = env.get("/v3/merchants/ABC123")  # Same interface!
```

### Files That Will Need Updates

**Server-side** (new code):
- `src/stolon/server.py` - Add `/proxy` endpoint
- `src/stolon/models.py` - Add `ProxyRequest`/`ProxyResponse` models

**Client-side** (modifications):
- `src/stolon/client.py` - Add `proxy_request()` method
- `src/stolon/environments/base.py` - Update `_request()` to use proxy

**Tests** (new files):
- `tests/stolon/test_stolon_client.py` - Unit tests with mocks
- `tests/stolon/test_environment_base.py` - Unit tests with mocks
- Update `tests/stolon/test_create_reseller.py` - Add `use_proxy=True` flag

**No changes needed**:
- ✅ `src/trifolium/environments/dev.py` - Uses `Environment` base class, transparent
- ✅ All existing test code - Just enable `use_proxy` flag in client creation
- ✅ Generated API wrappers - They call `Environment` methods, which handle the proxy internally

---

## Estimated Effort

- **Phase 1 (Tests)**: 2-3 days
- **Phase 2 (Proxy)**: 3-4 days
- **Phase 3 (Migration)**: 1 week
- **Phase 4 (OpenAPI)**: 2-3 days

**Total**: ~3 weeks for complete, tested, production-ready implementation

---

## 🚀 Next Steps for Phase 2

When ready to begin Phase 2 (Proxy Implementation), follow this sequence:

### Step 1: Add Proxy Models
**File**: `src/stolon/models.py`
- Add `ProxyRequest` model
- Add `ProxyResponse` model
- **Test command**: `python -c "from stolon.models import ProxyRequest, ProxyResponse; print('OK')"`

### Step 2: Implement Server Proxy Endpoint
**File**: `src/stolon/server.py`
- Add `/proxy` POST endpoint
- Implement 401 retry logic server-side
- Reuse existing token cache
- **Test command**: `curl -X POST http://localhost:62382/proxy -H "Content-Type: application/json" -d '{"domain":"dev1.dev.clover.com","method":"GET","path":"/v1/employees/whoami","environment_name":"dev"}'`

### Step 3: Add Client Proxy Method
**File**: `src/stolon/client.py`
- Add `proxy_request()` method
- Add `use_proxy` flag to `__init__()`
- **Test command**: Run existing unit tests, all should still pass

### Step 4: Update Environment Base (Feature Flag)
**File**: `src/stolon/environments/base.py`
- Add `_request_via_proxy()` method (new proxy path)
- Rename current `_request()` to `_request_direct()` (old direct path)
- Add conditional in `_request()` based on `self.client.use_proxy`
- **Test command**: `pytest tests/stolon/test_environment_base.py -v`

### Step 5: Integration Test with Proxy Mode
**File**: `tests/stolon/test_stolon_integration.py`
- Add `test_proxy_mode_matches_direct_mode()`
- Run same request with both modes, compare results
- **Test command**: `pytest tests/stolon/test_stolon_integration.py --external-infra -v`

### Step 6: Validation
Run the full test suite to ensure nothing broke:
```bash
# Unit tests (should all pass unchanged)
pytest tests/stolon/test_stolon_client.py tests/stolon/test_environment_base.py -v

# Integration tests with direct mode (baseline)
pytest tests/stolon/test_stolon_integration.py --external-infra -v

# Integration tests with proxy mode (new)
# (add use_proxy=True to client creation in tests)
pytest tests/stolon/test_stolon_integration.py --external-infra -v
```

**Success Criteria**:
- ✅ All 14 unit tests pass
- ✅ Integration tests pass with `use_proxy=False` (baseline)
- ✅ Integration tests pass with `use_proxy=True` (new mode)
- ✅ Both modes produce identical results

---

## 📝 Notes

**Phase 1 Learnings**:
- Mock-based testing worked excellently - fast, reliable, no infrastructure needed
- 401 retry logic test was straightforward to implement with mocks
- Context manager mocking required `__enter__ = Mock(return_value=mock_client)` pattern
- Test class naming: avoid `Test*` prefix for helper classes (causes pytest warnings)

**Phase 2 Considerations**:
- Keep feature flag (`use_proxy`) for backward compatibility during transition
- Server-side proxy endpoint should mirror existing 401 retry logic
- Token cache is already thread-safe on server (dictionary at module level)
- Integration tests will be critical for validating proxy correctness
