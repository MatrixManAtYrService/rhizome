# Stolon Session Token Capture

This document explains how Stolon captures internal session tokens from Clover admin sessions for API authentication.

## Overview

Stolon provides automated session token capture to simplify access to Clover's internal APIs. Instead of manually extracting tokens from browser developer tools, users can use `stolon internal-token <domain>` to get authenticated access.

## Authentication Flow

### 1. User Preferences
First-time users are prompted to configure their token capture preference:

```bash
stolon internal-token dev1.dev.clover.com
```

**First-time setup prompt:**
- `auto` - Automatically capture tokens without asking (recommended)
- `prompt` - Ask for confirmation each time

Preferences are stored in `~/.config/trifolium/trifolium.json`.

### 2. Browser Extension Integration

**Required Extension:**
- **Repository**: `github.corp.clover.com:clover/clover-session-extension`
- **Branch**: `trifolium-integration`
- **Behavior**: Works identically to main branch + adds CLI token capture support

**Automatic Flow (with extension):**
1. Stolon opens browser to `https://{domain}/admin`
2. User logs in with credentials
3. Extension automatically detects Stolon waiting for authentication
4. Extension extracts `internalSession` cookie and sends to Stolon
5. Tab closes automatically after successful token transfer

### 3. Manual Fallback

If browser extension is not installed, users can manually extract tokens:

1. **Access fallback UI**: Visit `http://localhost:49152` (opens automatically)
2. **Log into Clover admin**: Click provided link to open admin page
3. **Extract token manually**:
   - Open browser developer tools (F12)
   - Navigate to Application → Storage → Cookies
   - Find `internalSession` cookie for the domain
   - Copy the cookie value
4. **Submit token**: Paste into the provided form

## Technical Implementation

### Server Component
- **Port**: Fixed at 49152 to avoid conflicts
- **Endpoints**:
  - `GET /` - Manual token entry UI
  - `POST /auth/submit` - Token submission endpoint
  - `GET /stolon/status` - Extension status check
- **CORS**: Enabled for browser extension communication

### Browser Extension Integration
The extension automatically:
- Detects when Stolon is waiting for tokens (`/stolon/status`)
- Extracts `internalSession` cookie after successful login
- Sends token to Stolon via HTTP POST
- Closes the tab after successful token transfer

### User Configuration
User preferences are managed through the trifolium configuration system:

```python
from trifolium.config import Home, InternalTokenPreference

home = Home()
config = home.load_config()

# Check user preference
if config.internal_token_preference == InternalTokenPreference.AUTO:
    # Proceed without confirmation
elif config.internal_token_preference == InternalTokenPreference.PROMPT:
    # Ask user for confirmation
```

## Usage Examples

### Basic Token Capture
```bash
# Get token for dev environment
stolon internal-token dev1.dev.clover.com

# Output:
# 🌐 Starting authentication server on http://localhost:49152
# 🔐 Opening browser for authentication with dev1.dev.clover.com
# ⏳ Waiting for authentication...
# ✅ Authentication successful!
# 🎫 Token: 908f78ff-5a5b-4e29-b8a5-c28b653e9b39
```

### Programmatic Usage
```python
from stolon.get_internal_token import get_internal_token

# Get token programmatically
token = get_internal_token("dev1.dev.clover.com")
print(f"Got token: {token}")
```

## Security Considerations

### Local-Only Communication
- All token communication happens locally (browser ↔ localhost:49152)
- No tokens are sent over external networks
- Extension only communicates with local Stolon server

### User Consent
- Extension always respects user preferences (auto vs prompt)
- Users can decline token capture at any time
- Manual fallback always available

### Token Scope
- Only captures `internalSession` tokens (not all cookies)
- Tokens are immediately passed to waiting Stolon process
- No persistent storage of tokens in extension or Stolon

## Troubleshooting

### Extension Not Working
- Verify extension is installed and enabled
- Check that you're on the `trifolium-integration` branch
- Ensure extension has permissions for `*.clover.com` and `localhost:49152`

### Manual UI Issues
- Character encoding problems: Fixed with `<meta charset="utf-8">`
- Port conflicts: Stolon uses fixed port 49152
- CORS errors: Extension permissions may need updating

### Token Capture Failures
- Verify you're logged into the correct Clover domain
- Check that `internalSession` cookie exists after login
- Ensure no browser extensions are blocking cookie access

## Automatic Token Refresh (401 Retry)

### Overview

Stolon provides automatic token refresh when tokens expire. When an HTTP request returns 401 (Unauthorized), the system automatically:
1. Invalidates the cached token
2. Prompts for new authentication
3. Retries the request with the fresh token

This happens transparently - no code changes needed in tests or scripts.

### Implementation

The retry logic is implemented using the `stamina` library in `src/stolon/retry_401.py`:

```python
from stolon.retry_401 import make_authenticated_get, make_authenticated_post

# Automatically retries on 401
response = make_authenticated_get(
    stolon_client,
    "dev1.dev.clover.com",
    "https://dev1.dev.clover.com/v3/internal/internal_accounts/current"
)
```

### How It Works

**Retry Flow**:
1. **First attempt**: Uses cached token (fast, no user interaction)
2. **401 detected**: Invalidates cached token, raises `TokenExpiredError`
3. **Second attempt**: Prompts user for fresh authentication, retries request
4. **Success**: Returns response as if nothing happened

**Key Features**:
- **Transparent**: Caller doesn't need to handle 401 errors
- **User-friendly**: Clear prompts when re-authentication needed
- **Smart caching**: Only invalidates token when actually expired
- **Configurable**: Uses stamina for retry logic (2 attempts max)

### Usage Patterns

#### GET Requests
```python
from stolon.retry_401 import make_authenticated_get

response = make_authenticated_get(
    stolon_client=environment._stolon_client,
    domain="dev1.dev.clover.com",
    url="https://dev1.dev.clover.com/v3/resellers",
    headers={"X-Clover-Appenv": "dev:dev1"},
    timeout=10.0
)
data = response.json()
```

#### POST Requests
```python
from stolon.retry_401 import make_authenticated_post

response = make_authenticated_post(
    stolon_client=environment._stolon_client,
    domain="dev1.dev.clover.com",
    url="https://dev1.dev.clover.com/v3/resellers",
    json={"name": "Test Reseller"},
    headers={"X-Clover-Appenv": "dev:dev1"}
)
reseller = response.json()
```

#### Generic Requests
```python
from stolon.retry_401 import make_authenticated_request

response = make_authenticated_request(
    stolon_client=environment._stolon_client,
    domain="dev1.dev.clover.com",
    method="PUT",
    url="https://dev1.dev.clover.com/v3/resellers/ABC123",
    json={"name": "Updated Name"}
)
```

### Error Handling

The retry wrapper handles 401 errors automatically, but other errors are raised immediately:

```python
try:
    response = make_authenticated_get(stolon_client, domain, url)
except httpx.HTTPStatusError as e:
    if e.response.status_code == 404:
        print("Resource not found")
    elif e.response.status_code == 403:
        print("Permission denied")
    # Note: 401 is handled automatically, won't reach here
except httpx.ConnectError:
    print("Connection failed")
```

### Configuration

Retry behavior is configured via stamina:
- **Max attempts**: 2 (original + 1 retry)
- **Wait time**: 0.1s initial, 1.0s max (minimal delay)
- **Retry condition**: Only on `TokenExpiredError` (401)

To customize:
```python
@stamina.retry(
    on=TokenExpiredError,
    attempts=3,              # Increase retries
    wait_initial=0.5,        # Longer initial wait
    wait_max=5.0             # Longer max wait
)
def _make_request():
    # ... request logic
```

### Comparison with Direct httpx

**❌ Without retry wrapper** (manual token handling):
```python
handle = stolon_client.request_internal_token(domain)
response = httpx.get(url, cookies={"internalSession": handle.token})

if response.status_code == 401:
    # Token expired, get new one
    stolon_client.invalidate_token(domain)
    handle = stolon_client.request_internal_token(domain)
    response = httpx.get(url, cookies={"internalSession": handle.token})

response.raise_for_status()
```

**✅ With retry wrapper** (automatic):
```python
response = make_authenticated_get(stolon_client, domain, url)
# That's it! 401 handling is automatic
```

### Best Practices

**DO**:
- Use retry wrappers for all authenticated Clover API requests
- Let the system handle token refresh automatically
- Handle other HTTP errors explicitly (404, 403, etc.)

**DON'T**:
- Mix manual token handling with retry wrappers
- Catch and suppress 401 errors (let retry wrapper handle them)
- Cache responses across token refreshes

### Testing Considerations

When writing tests that use authenticated requests:

1. **Token expiration**: Tests may trigger re-authentication if token expires
2. **User interaction**: Re-authentication requires user to log in again
3. **Session scope**: Use module-scoped fixtures to minimize re-authentication

Example:
```python
@pytest.fixture(scope="module")
def authenticated_data(environment):
    """Fetch data once per module, reuse across tests."""
    response = make_authenticated_get(
        environment._stolon_client,
        "dev1.dev.clover.com",
        "https://dev1.dev.clover.com/v3/resellers"
    )
    return response.json()

def test_resellers_exist(authenticated_data):
    assert len(authenticated_data) > 0

def test_resellers_have_names(authenticated_data):
    assert all("name" in r for r in authenticated_data)
```

## Development Notes

### Extension Development
- Extension code lives in separate repository
- Uses Manifest V3 (Chrome/Edge) and WebExtensions API (Firefox)
- Service worker handles communication with Stolon server

### Server Development
- Auth server code in `src/stolon/auth_interceptor.py`
- Token capture logic in `src/stolon/get_internal_token.py`
- Retry wrapper in `src/stolon/retry_401.py`
- CLI integration in `src/stolon/cli.py`

### Testing
- Manual UI can be tested by visiting `http://localhost:49152` during token capture
- Extension integration requires actual Clover admin login
- Automated testing possible through mocked auth server responses
- Retry logic tested through stamina's built-in retry mechanisms