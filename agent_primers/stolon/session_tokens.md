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

## Development Notes

### Extension Development
- Extension code lives in separate repository
- Uses Manifest V3 (Chrome/Edge) and WebExtensions API (Firefox)
- Service worker handles communication with Stolon server

### Server Development
- Auth server code in `src/stolon/auth_interceptor.py`
- Token capture logic in `src/stolon/get_internal_token.py`
- CLI integration in `src/stolon/cli.py`

### Testing
- Manual UI can be tested by visiting `http://localhost:49152` during token capture
- Extension integration requires actual Clover admin login
- Automated testing possible through mocked auth server responses