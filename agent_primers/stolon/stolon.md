# Stolon - HTTP API Access Layer

## Overview

Stolon is the HTTP API access layer that complements Rhizome's database access layer. While both are part of the Trifolium project and share similar architectural principles, they serve different purposes:

- **Rhizome**: Provides access to Clover's databases (MySQL, CloudSQL)
- **Stolon**: Provides access to Clover's HTTP APIs and services

The biological metaphor continues:
- **Rhizomes** grow underground (database connections through port-forwarding and tunnels)
- **Stolons** grow aboveground (HTTP connections through public or internal APIs)

## Key Differences from Rhizome

### 1. Connection Type
- **Rhizome**: SQL connections via port-forwarding, kubectl, CloudSQL proxy
- **Stolon**: HTTP/REST connections via authenticated API endpoints

### 2. Authentication
- **Rhizome**: Database credentials from 1Password/Pybritive, SQL authentication
- **Stolon**: OAuth tokens, API keys, bearer tokens, session management

### 3. Data Format
- **Rhizome**: Tabular data with SQLModel ORM, structured schemas
- **Stolon**: JSON responses, potentially varied formats per endpoint

### 4. Infrastructure Requirements
- **Rhizome**: Kubernetes access, port-forwarding, VPN for production databases
- **Stolon**: API endpoints (may be public or require VPN), auth servers

## Stolon Architecture

### Server Component (`stolon serve`)

The Stolon server will handle:

1. **Authentication Management**
   - OAuth flow orchestration
   - Token refresh and rotation
   - Session management across different API providers
   - Credential caching and secure storage

2. **Request Proxying**
   - Intercept client requests
   - Add appropriate authentication headers
   - Handle rate limiting and retries
   - Transform requests/responses as needed

3. **API Discovery**
   - Catalog available endpoints
   - Track API versions and capabilities
   - Provide metadata about request/response formats

4. **Tribal Knowledge Capture**
   - Which APIs require which auth methods
   - Endpoint-specific quirks and requirements
   - Environment-specific API URLs and configurations

### Client Component

Similar to Rhizome's client, Stolon's client will provide a simple interface:

```python
from stolon.client import StolonClient
from stolon.environments import DevMerchantAPI

api = DevMerchantAPI(StolonClient())
merchant_data = api.get("/v3/merchants/{merchant_id}")
```

## Current Implementation Status

Based on the git status showing new Stolon files:

```
A  src/stolon/__init__.py
A  src/stolon/auth_interceptor.py
A  src/stolon/cli.py
```

The implementation is beginning with:

### 1. CLI Entry Point (`stolon/cli.py`)

Expected to provide commands like:
```bash
# Start the Stolon server
stolon serve

# Check API connectivity
stolon test

# List available APIs
stolon list-apis

# Get API access token (for debugging)
stolon auth <api_name>
```

### 2. Auth Interceptor (`stolon/auth_interceptor.py`)

This module likely handles:
- Intercepting outgoing requests to add authentication
- Managing different auth strategies (OAuth, API key, etc.)
- Token refresh logic
- Credential retrieval from secure storage

### 3. Package Initialization (`stolon/__init__.py`)

Sets up the Stolon module structure and exports public APIs.

## How Stolon Server Will Work

### Startup Flow

1. **Initialize Server**
   ```bash
   stolon serve [--port 8001]
   ```

2. **Load Configuration**
   - Read API endpoint configurations
   - Initialize auth providers
   - Set up credential managers (1Password, Pybritive, etc.)

3. **Start HTTP Server**
   - Listen for client requests
   - Provide health check endpoint
   - Ready to proxy API calls

### Request Flow

1. **Client Request**
   ```python
   api.get("/v3/merchants/12345")
   ```

2. **Server Processing**
   - Identify target API and endpoint
   - Retrieve/refresh authentication credentials
   - Add auth headers (Bearer token, API key, etc.)
   - Forward request to actual API

3. **Response Handling**
   - Receive API response
   - Log for debugging (if enabled)
   - Transform if needed
   - Return to client

### Authentication Strategies

Different APIs will require different auth methods:

```python
class AuthStrategy:
    OAUTH = "oauth"          # GitHub, Google APIs
    API_KEY = "api_key"      # Internal services
    BEARER = "bearer"        # JWT tokens
    SESSION = "session"      # Cookie-based auth
    MUTUAL_TLS = "mtls"     # Certificate-based
```

## Environment Configuration

Similar to Rhizome's environment structure:

```
src/stolon/environments/
├── dev/
│   ├── merchant_api.py
│   ├── payment_api.py
│   └── reporting_api.py
├── demo/
│   └── ...
└── na_prod/
    └── ...
```

Each environment class would define:
- Base API URLs
- Authentication requirements
- Rate limits and retry policies
- Environment-specific headers or parameters

## Use Cases

### 1. Testing API Integrations
```python
def test_merchant_creation():
    api = DevMerchantAPI(StolonClient())
    response = api.post("/v3/merchants", data={
        "name": "Test Merchant",
        "address": "123 Main St"
    })
    assert response.status_code == 201
```

### 2. Cross-Environment API Validation
```python
def validate_api_response(env_class):
    api = env_class(StolonClient())
    response = api.get("/health")
    assert response.status_code == 200
```

### 3. Bulk API Operations
```python
def sync_merchant_data():
    api = ProdMerchantAPI(StolonClient())
    merchants = api.paginate("/v3/merchants", page_size=100)
    for merchant in merchants:
        process_merchant(merchant)
```

## Integration with Rhizome

Stolon and Rhizome can work together for complete data access:

```python
from rhizome.client import RhizomeClient
from rhizome.environments import DevBillingBookkeeper
from stolon.client import StolonClient
from stolon.environments import DevPaymentAPI

# Get data from database
db = DevBillingBookkeeper(RhizomeClient())
FeeSummary = db.get_model(BillingBookkeeperTable.fee_summary)
db_merchant = db.select_first(
    select(FeeSummary).where(FeeSummary.merchant_uuid == "abc123")
)

# Get data from API
api = DevPaymentAPI(StolonClient())
api_merchant = api.get(f"/v3/merchants/{db_merchant.merchant_uuid}")

# Compare or combine data
assert db_merchant.merchant_uuid == api_merchant["uuid"]
```

## Benefits of Stolon

### 1. Separation of Concerns
- API complexity hidden in server
- Tests focus on business logic
- Authentication handled transparently

### 2. Tribal Knowledge Preservation
- API quirks documented in code
- Authentication methods centralized
- Environment differences captured

### 3. Development Efficiency
- No need to manage tokens manually
- Automatic retry and rate limiting
- Consistent interface across all APIs

### 4. Testing Improvements
- Easy mocking for unit tests
- Simplified integration testing
- Cross-environment validation

## Future Enhancements

### 1. Request Recording and Replay
- Record API interactions for offline testing
- Replay scenarios for regression testing

### 2. API Schema Validation
- OpenAPI/Swagger integration
- Response validation against schemas
- Type generation for API responses

### 3. Performance Monitoring
- Track API latencies
- Monitor rate limit usage
- Alert on API degradation

### 4. Unified Query Language
- GraphQL-like queries across REST APIs
- Field selection and filtering
- Response transformation

## Summary

Stolon extends the Trifolium philosophy to HTTP APIs:
- **Rhizome** handles underground connections (databases)
- **Stolon** handles aboveground connections (APIs)

Together, they provide a complete data access layer that:
- Captures institutional knowledge
- Simplifies testing and development
- Provides type safety and validation
- Enables progressive environment migrations

The `stolon serve` command will start a local server that manages API authentication and request proxying, similar to how `rhizome serve` manages database connections and port forwarding.