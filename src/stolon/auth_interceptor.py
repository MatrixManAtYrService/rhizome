"""Browser-based authentication with automatic token extraction."""

import threading
import time
from typing import Optional

import uvicorn
from fastapi import APIRouter, FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

STOLON_AUTH_PORT = 49152  # High port number to avoid collisions

# Create router at module level - this resolves the pyright issues
router = APIRouter()

# Global state for the current auth session
_current_auth_session: Optional["AuthServer"] = None


class AuthServer:
    """Authentication server for capturing tokens."""

    def __init__(self, clover_domain: str) -> None:
        self.clover_domain = clover_domain
        self.captured_token: str | None = None
        self.app = self._create_app()

    def _create_app(self) -> FastAPI:
        """Create and configure the FastAPI application."""
        global _current_auth_session
        _current_auth_session = self

        app = FastAPI()

        # Configure CORS for browser extension communication
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Include our router
        app.include_router(router)
        return app


@router.get("/", response_class=HTMLResponse)
async def auth_page() -> str:
    """Serve the main authentication page."""
    if not _current_auth_session:
        return "<h1>No active auth session</h1>"

    clover_url = f"https://{_current_auth_session.clover_domain}/admin"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Stolon Authentication</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta charset="utf-8">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                margin: 0; padding: 40px; background: #f8f9fa; min-height: 100vh;
                display: flex; flex-direction: column; align-items: center; justify-content: center;
            }}
            .container {{
                max-width: 600px; background: white; padding: 40px; border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
            .logo {{ text-align: center; margin-bottom: 30px; font-size: 32px; }}
            .section {{ margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 8px; }}
            .token-section {{ background: #fff3cd; border-left: 4px solid #ffc107; }}
            .instructions {{ background: #e3f2fd; border-left: 4px solid #1976d2; }}
            .button {{
                background: #007cba; color: white; padding: 12px 24px; border: none;
                border-radius: 6px; cursor: pointer; font-size: 16px; text-decoration: none;
                display: inline-block; margin: 10px 5px;
            }}
            .button:hover {{ background: #005a87; }}
            .token-input {{
                width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px;
                font-size: 14px; font-family: monospace; margin: 10px 0; box-sizing: border-box;
            }}
            .status {{ text-align: center; margin: 20px 0; font-weight: 500; }}
            ol {{ margin: 15px 0; padding-left: 20px; }}
            li {{ margin: 5px 0; }}
            code {{ background: #f1f3f4; padding: 2px 6px; border-radius: 3px; font-family: monospace; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">Stolon Authentication</div>

            <div class="section token-section">
                <h3>Enter Internal Session Token</h3>
                <p>After logging into Clover admin, extract and paste your <code>internalSession</code> token here:</p>
                <form onsubmit="submitToken(event)">
                    <input type="text" class="token-input" id="manualToken"
                           placeholder="Paste internalSession token here..." required>
                    <br>
                    <button type="submit" class="button">Submit Token</button>
                </form>
            </div>

            <div class="section instructions">
                <h3>How to get your token:</h3>
                <ol>
                    <li><strong>Open Clover admin:</strong>
                        <button class="button" onclick="openCloverAdmin()">
                            Open {_current_auth_session.clover_domain}/admin
                        </button>
                    </li>
                    <li><strong>Log in</strong> with your credentials</li>
                    <li><strong>Open developer tools</strong> (F12 or right-click → Inspect)</li>
                    <li><strong>Go to Application tab</strong> → Storage → Cookies → <code>https://{_current_auth_session.clover_domain}</code></li>
                    <li><strong>Find the <code>internalSession</code> cookie</strong> and copy its value</li>
                    <li><strong>Paste it above</strong> and click Submit Token</li>
                </ol>
            </div>

            <div id="status" class="status"></div>
        </div>

        <script>
            function openCloverAdmin() {{
                // Open Clover admin in new tab
                window.open('{clover_url}', '_blank', 'width=1200,height=800');
            }}

            function submitToken(event) {{
                event.preventDefault();
                const token = document.getElementById('manualToken').value.trim();
                if (!token) {{
                    alert('Please enter a token');
                    return;
                }}

                // Show loading state
                const button = event.target.querySelector('button[type="submit"]');
                const originalText = button.textContent;
                button.textContent = 'Submitting...';
                button.disabled = true;

                fetch('/auth/submit', {{
                    method: 'POST',
                    headers: {{'Content-Type': 'application/x-www-form-urlencoded'}},
                    body: 'token=' + encodeURIComponent(token)
                }})
                .then(response => {{
                    if (response.ok) {{
                        document.getElementById('status').innerHTML =
                            '<div style="color: #155724; background: #d4edda; ' +
                            'padding: 15px; border-radius: 5px; margin: 15px 0;">' +
                            '✅ Token submitted successfully! This tab will close in 3 seconds...</div>';
                        setTimeout(() => window.close(), 3000);
                    }} else {{
                        throw new Error('Token submission failed');
                    }}
                }})
                .catch(error => {{
                    document.getElementById('status').innerHTML =
                        '<div style="color: #721c24; background: #f8d7da; ' +
                        'padding: 15px; border-radius: 5px; margin: 15px 0;">' +
                        '❌ Error submitting token. Please try again.</div>';
                    button.textContent = originalText;
                    button.disabled = false;
                }});
            }}
        </script>
    </body>
    </html>
    """


@router.get("/auth/callback", response_class=HTMLResponse)
async def auth_callback() -> str:
    """Handle callback from Clover admin (if we could redirect back)."""
    return """
    <html><body>
        <h2>Checking for authentication...</h2>
        <script>
            // Try to get the cookie and send it back
            const cookies = document.cookie.split(';');
            let token = null;
            for (let cookie of cookies) {
                const [key, value] = cookie.trim().split('=');
                if (key === 'internalSession') {
                    token = value;
                    break;
                }
            }

            if (token) {
                fetch('/auth/submit', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    body: 'token=' + encodeURIComponent(token)
                });
            }

            window.close();
        </script>
    </body></html>
    """


@router.post("/auth/submit")
async def submit_token(token: str = Form(...)) -> JSONResponse:
    """Handle token submission."""
    if _current_auth_session:
        _current_auth_session.captured_token = token
    return JSONResponse({"success": True})


@router.get("/auth/check")
async def check_token() -> JSONResponse:
    """Handle AJAX requests to check if token was captured."""
    if _current_auth_session and _current_auth_session.captured_token:
        return JSONResponse({"token": _current_auth_session.captured_token})
    return JSONResponse({"token": None})


@router.get("/stolon/status")
async def stolon_status() -> JSONResponse:
    """Handle status check from browser extension."""
    if not _current_auth_session:
        return JSONResponse({"waiting_for_token": False, "domain": ""})

    waiting = _current_auth_session.captured_token is None
    return JSONResponse({"waiting_for_token": waiting, "domain": _current_auth_session.clover_domain})


def start_auth_server(clover_domain: str) -> tuple[AuthServer, int]:
    """Start the authentication server and return server instance and port."""
    server = AuthServer(clover_domain)

    # Run the server in a background thread
    def run_server() -> None:
        uvicorn.run(server.app, host="localhost", port=STOLON_AUTH_PORT, log_level="error")

    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()

    # Give the server a moment to start
    time.sleep(0.5)

    return server, STOLON_AUTH_PORT
