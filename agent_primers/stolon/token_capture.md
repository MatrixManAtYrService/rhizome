# Stolon Browser Extension Token Capture Integration

This document describes the browser extension integration that enables automatic token capture for the `stolon internal_token` command.

## Overview

The Clover Session Extension has been enhanced to automatically detect when Stolon is waiting for authentication tokens and seamlessly provide them without manual intervention. This eliminates the need for users to manually copy tokens from browser developer tools.

## How It Works

### Authentication Flow

1. **User initiates**: `stolon internal_token dev1.dev.clover.com`
2. **Stolon starts server**: Local HTTP server on port 49152
3. **Browser opens**: Stolon opens browser to `https://dev1.dev.clover.com/admin`
4. **User authenticates**: Normal login process (username/password, 2FA, etc.)
5. **Extension detects**: Content script detects successful authentication and available tokens
6. **User confirms**: Modal prompt asks "Send token to Stolon?"
7. **Token transfer**: Extension sends `internalSession` token to Stolon via HTTP POST
8. **Completion**: Stolon receives token and completes authentication flow

### Technical Architecture

#### Stolon Server (Port 49152)
- **Status endpoint**: `GET /stolon/status` - Returns if server is waiting for tokens
- **Token endpoint**: `POST /auth/submit` - Receives tokens from extension
- **CORS enabled**: Allows browser extension communication

#### Browser Extension Components
- **Background script**: Service worker managing Stolon communication
- **Content script**: Injected on `*.clover.com/admin*` pages for token detection
- **Popup enhancement**: Manual token sending option when extension icon is clicked

## User Installation Steps

### Prerequisites
- Clover Session Extension must be installed and enabled
- User must have access to extension source code for updates

### Extension Update Process

1. **Navigate to extension directory**:
   ```bash
   cd clover-session-extension
   ```

2. **Switch to integration branch**:
   ```bash
   git checkout stolon-integration
   ```

3. **Update browser extension**:
   - **Chrome**:
     - Go to `chrome://extensions/`
     - Find "Clover Session" extension
     - Click "Reload" button (🔄) to reload from disk
   - **Firefox**:
     - Go to `about:debugging#/runtime/this-firefox`
     - Find extension and click "Reload"

4. **Verify installation**:
   - Extension version should show "1.1"
   - Extension description should include "with Stolon Integration"

### First-Time Extension Installation
If extension is not already installed:

1. **Chrome**:
   - Go to `chrome://extensions/`
   - Enable "Developer mode" (top right toggle)
   - Click "Load unpacked"
   - Select the `clover-session-extension` directory
   - Ensure you're on the `stolon-integration` branch

2. **Firefox**:
   - Go to `about:debugging#/runtime/this-firefox`
   - Click "Load Temporary Add-on"
   - Select any file in the `clover-session-extension` directory

## Usage

### Automatic Mode (Recommended)
1. Run `stolon internal_token <domain>`
2. Browser opens to Clover admin page
3. Log in normally
4. Wait for extension modal: "🔐 Stolon Token Transfer"
5. Click "Send Token"
6. Stolon completes automatically

### Manual Mode (Fallback)
1. Run `stolon internal_token <domain>`
2. Browser opens to Clover admin page
3. Log in normally
4. Click extension icon in browser toolbar
5. Click "Send Internal Token" in popup
6. Stolon completes automatically

### Troubleshooting

#### Extension Not Detecting Stolon
- Verify Stolon is running and listening on port 49152
- Check browser console for CORS or network errors
- Ensure you're on a `*.clover.com/admin*` page

#### Modal Not Appearing
- Refresh the admin page after logging in
- Check if content script loaded (browser dev tools → Console)
- Verify extension permissions include `*.clover.com`

#### Token Send Failure
- Check that `internalSession` cookie exists
- Verify localhost:49152 permission in extension
- Look for CORS errors in browser console

## Security Considerations

### Local Communication Only
- All communication is between browser extension and local Stolon server
- No tokens are sent over external networks
- Communication limited to localhost:49152

### User Consent Required
- Extension always prompts before sending tokens
- Users can decline token transfer
- Manual fallback always available

### Token Scope
- Only `internalSession` tokens are captured
- Tokens are sent directly to waiting Stolon process
- No token storage or persistence in extension

## Development Notes

### Port Configuration
- Fixed port 49152 (defined in `STOLON_AUTH_PORT` constant)
- High port number chosen to avoid common service conflicts
- Same port hardcoded in both Python and JavaScript

### Extension Permissions
- `host_permissions`: `*.clover.com` and `localhost:49152`
- `permissions`: `cookies`, `tabs`, `scripting`
- Minimal required permissions for functionality

### Browser Compatibility
- Manifest V3 (Chrome/Edge)
- WebExtensions API (Firefox)
- Service worker background script (not persistent)

## Future Enhancements

### Potential Improvements
1. **Multi-domain support**: Handle multiple Clover domains simultaneously
2. **Token refresh**: Automatic token renewal for long-running sessions
3. **Error recovery**: Retry logic for failed token transfers
4. **Logging**: Optional verbose logging for debugging

### Extension Distribution
- Consider packaging as .crx/.xpi for easier distribution
- Add to internal extension catalog if available
- Automated installation scripts for development teams