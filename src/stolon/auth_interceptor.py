"""Browser-based authentication with automatic token extraction."""

import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse


class InterceptorHandler(BaseHTTPRequestHandler):
    """HTTP handler that provides a seamless authentication flow."""

    def log_message(self, format: str, *args: object) -> None:
        """Suppress default server logging."""
        pass

    def do_GET(self) -> None:
        """Handle GET requests."""
        parsed = urlparse(self.path)

        if parsed.path == "/":
            self.send_auth_page()
        elif parsed.path == "/auth/callback":
            self.handle_callback()
        elif parsed.path == "/auth/check":
            self.handle_token_check()
        elif parsed.path == "/stolon/status":
            self.handle_status_check()
        else:
            self.send_404()

    def do_POST(self) -> None:
        """Handle POST requests for token submission."""
        if self.path == "/auth/submit":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            params = parse_qs(post_data)

            if "token" in params:
                self.server.captured_token = params["token"][0]
                self.send_success_response()
            else:
                self.send_error_response("No token provided")
        else:
            self.send_404()

    def send_auth_page(self) -> None:
        """Send the main authentication page with automatic flow."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        callback_url = f"http://localhost:{self.server.server_port}/auth/callback"
        clover_url = f"https://{self.server.clover_domain}/admin"

        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Stolon Authentication</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    margin: 0; padding: 40px; background: #f8f9fa; min-height: 100vh;
                    display: flex; flex-direction: column; align-items: center; justify-content: center;
                }}
                .container {{ max-width: 600px; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
                .logo {{ text-align: center; margin-bottom: 30px; font-size: 32px; }}
                .step {{ margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #007cba; }}
                .step.active {{ background: #e3f2fd; border-left-color: #1976d2; }}
                .step.complete {{ background: #e8f5e8; border-left-color: #4caf50; }}
                .button {{
                    background: #007cba; color: white; padding: 12px 24px; border: none;
                    border-radius: 6px; cursor: pointer; font-size: 16px; text-decoration: none;
                    display: inline-block; margin: 10px 5px;
                }}
                .button:hover {{ background: #005a87; }}
                .button.secondary {{ background: #6c757d; }}
                .button.secondary:hover {{ background: #545b62; }}
                .status {{ text-align: center; margin: 20px 0; font-weight: 500; }}
                .spinner {{
                    border: 3px solid #f3f3f3; border-top: 3px solid #007cba;
                    border-radius: 50%; width: 30px; height: 30px;
                    animation: spin 1s linear infinite; margin: 0 auto;
                }}
                @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
                .hidden {{ display: none; }}
                .token-input {{
                    width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px;
                    font-size: 14px; font-family: monospace; margin: 10px 0;
                }}
                .manual-section {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">🔐 Stolon Authentication</div>

                <div id="step1" class="step active">
                    <strong>Step 1: Open Clover Admin</strong>
                    <p>Click the button below to open the Clover admin page where you'll log in:</p>
                    <button class="button" onclick="openCloverAdmin()">Open {self.server.clover_domain}/admin</button>
                </div>

                <div id="step2" class="step">
                    <strong>Step 2: Log In</strong>
                    <p>Log in with your security key when prompted on the Clover admin page.</p>
                </div>

                <div id="step3" class="step">
                    <strong>Step 3: Return Here</strong>
                    <p>After successful login, return to this tab and we'll automatically check for your session.</p>
                    <div id="checking" class="hidden">
                        <div class="spinner"></div>
                        <p>Checking for authentication...</p>
                    </div>
                    <button id="checkBtn" class="button hidden" onclick="checkAuthentication()">Check Authentication</button>
                </div>

                <div class="manual-section">
                    <details>
                        <summary style="cursor: pointer; color: #666;">🔧 Manual Token Entry (if automatic detection fails)</summary>
                        <div style="margin-top: 15px;">
                            <p>If automatic detection doesn't work, you can manually extract the token:</p>
                            <ol>
                                <li>Open browser developer tools (F12) on the Clover admin page</li>
                                <li>Go to Application/Storage → Cookies</li>
                                <li>Find the <code>internalSession</code> cookie and copy its value</li>
                                <li>Paste it below:</li>
                            </ol>
                            <form onsubmit="submitToken(event)">
                                <input type="text" class="token-input" id="manualToken" placeholder="Paste internalSession token here...">
                                <br>
                                <button type="submit" class="button">Submit Token</button>
                            </form>
                        </div>
                    </details>
                </div>

                <div id="status" class="status"></div>
            </div>

            <script>
                let checkInterval;

                function openCloverAdmin() {{
                    // Mark step 1 as complete
                    document.getElementById('step1').classList.remove('active');
                    document.getElementById('step1').classList.add('complete');

                    // Activate step 2
                    document.getElementById('step2').classList.add('active');

                    // Open Clover admin in new tab
                    window.open('{clover_url}', '_blank', 'width=1200,height=800');

                    // Wait a bit then show step 3
                    setTimeout(() => {{
                        document.getElementById('step2').classList.remove('active');
                        document.getElementById('step2').classList.add('complete');
                        document.getElementById('step3').classList.add('active');
                        document.getElementById('checkBtn').classList.remove('hidden');
                    }}, 3000);
                }}

                function checkAuthentication() {{
                    document.getElementById('checkBtn').classList.add('hidden');
                    document.getElementById('checking').classList.remove('hidden');
                    document.getElementById('status').textContent = 'Checking for session cookie...';

                    // Start polling for token
                    checkInterval = setInterval(async () => {{
                        try {{
                            const response = await fetch('/auth/check');
                            const data = await response.json();

                            if (data.token) {{
                                clearInterval(checkInterval);
                                document.getElementById('checking').classList.add('hidden');
                                document.getElementById('step3').classList.remove('active');
                                document.getElementById('step3').classList.add('complete');
                                document.getElementById('status').innerHTML = '✅ Authentication successful!<br>Token captured: ' + data.token;

                                // Auto-close after success
                                setTimeout(() => {{
                                    window.close();
                                }}, 3000);
                            }}
                        }} catch (e) {{
                            // Continue polling
                        }}
                    }}, 2000);

                    // Stop after 2 minutes
                    setTimeout(() => {{
                        if (checkInterval) {{
                            clearInterval(checkInterval);
                            document.getElementById('checking').classList.add('hidden');
                            document.getElementById('checkBtn').classList.remove('hidden');
                            document.getElementById('status').textContent = 'Automatic detection timed out. Try the manual method below.';
                        }}
                    }}, 120000);
                }}

                function submitToken(event) {{
                    event.preventDefault();
                    const token = document.getElementById('manualToken').value.trim();
                    if (!token) {{
                        alert('Please enter a token');
                        return;
                    }}

                    fetch('/auth/submit', {{
                        method: 'POST',
                        headers: {{'Content-Type': 'application/x-www-form-urlencoded'}},
                        body: 'token=' + encodeURIComponent(token)
                    }}).then(() => {{
                        document.getElementById('status').innerHTML = '✅ Token submitted successfully!';
                        setTimeout(() => window.close(), 2000);
                    }});
                }}
            </script>
        </body>
        </html>
        '''
        self.wfile.write(html.encode())

    def handle_callback(self) -> None:
        """Handle callback from Clover admin (if we could redirect back)."""
        # This might not work due to CORS, but we'll try
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = '''
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
        '''
        self.wfile.write(html.encode())

    def handle_token_check(self) -> None:
        """Handle AJAX requests to check if token was captured."""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        if hasattr(self.server, 'captured_token') and self.server.captured_token:
            response = f'{{"token": "{self.server.captured_token}"}}'
        else:
            response = '{"token": null}'

        self.wfile.write(response.encode())

    def handle_status_check(self) -> None:
        """Handle status check from browser extension."""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Check if we're waiting for a token
        waiting = not (hasattr(self.server, 'captured_token') and self.server.captured_token)
        response = f'{{"waiting_for_token": {str(waiting).lower()}, "domain": "{self.server.clover_domain}"}}'
        self.wfile.write(response.encode())

    def send_success_response(self) -> None:
        """Send success response."""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(b'{"success": true}')

    def send_error_response(self, message: str) -> None:
        """Send error response."""
        self.send_response(400)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = f'{{"error": "{message}"}}'
        self.wfile.write(response.encode())

    def send_404(self) -> None:
        """Send 404 response."""
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b'<h1>404 Not Found</h1>')


STOLON_AUTH_PORT = 49152  # High port number to avoid collisions

def start_auth_server(clover_domain: str) -> tuple[HTTPServer, int]:
    """Start the authentication server and return server instance and port."""
    server = HTTPServer(("localhost", STOLON_AUTH_PORT), InterceptorHandler)
    server.captured_token = None
    server.clover_domain = clover_domain
    port = server.server_port
    return server, port