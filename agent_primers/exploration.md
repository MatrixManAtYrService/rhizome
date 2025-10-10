# System Exploration Workflow for AI Agents

## Overview

When implementing features that interact with external systems (like billing-bookkeeper, merchant services, etc.), you often need to understand the **current state** and **patterns** in the target environment before writing correct implementation code.

This document describes a three-phase workflow:

1. **Exploration**: Generate a Python script to query and analyze the target system
2. **Analysis**: Summarize findings and identify patterns
3. **Implementation**: Apply discoveries to your actual code

## When to Use This Workflow

Use this approach when:

- You need to understand how existing data is structured in production/staging
- You're writing tests and need to know realistic field values
- You're implementing features and need to follow existing patterns
- You need to validate assumptions about API responses or database schemas
- You're debugging and need to understand the current system state

## Choosing Your Tools: Stolon vs Rhizome

### Use **Stolon** when:
- You need to interact with HTTP APIs (REST endpoints)
- You're testing API request/response patterns
- You need to create, update, or delete resources via APIs
- You want to understand what the API returns for specific queries

### Use **Rhizome** when:
- You need to query database tables directly
- You want to analyze data patterns across many records
- You need to compute statistics or aggregate data
- You're looking for relationships between tables
- API endpoints don't expose the data you need

### Use **Both** when:
- You need to understand how API responses relate to database state
- You're validating that API operations correctly update the database
- You want to compare HTTP-accessible data with underlying DB records

## Exploration Script Structure

### Template Structure

```python
#!/usr/bin/env python3
"""
Explore [WHAT] in [ENVIRONMENT] environment.

This script queries the [SYSTEM_NAME] to understand [PURPOSE].
"""

from typing import Any
from sqlmodel import select

# Import the appropriate clients and models
from rhizome.client import RhizomeClient
from rhizome.environments.[env].[service] import [EnvironmentService]
from rhizome.models.[service].[table] import [Model]
from rhizome.models.table_list import [ServiceTable]


def explore_[feature]() -> None:
    """Query [environment] for [feature] and analyze patterns."""
    print(f"🔍 Exploring [feature] in [environment] environment...\n")

    # Connect to the environment
    rhizome_client = RhizomeClient(data_in_logs=False)
    service = [EnvironmentService](rhizome_client)

    # Get models
    Model = service.get_model([ServiceTable].[table_name])

    # Query for data
    results = service.select_all(
        select(Model)
        .where(Model.[field] == "[value]")
        .order_by(Model.[timestamp_field].desc())
        .limit(20),
        sanitize=False,  # Use False to get real UUIDs
    )

    # Analyze and print findings
    print_analysis(results)

    # Compute statistics
    stats = compute_statistics(results)

    # Print recommendations
    print_recommendations(stats)


if __name__ == "__main__":
    explore_[feature]()
```

## Example 1: Rhizome-Based Exploration (Database Queries)

**Scenario**: Understanding partner config patterns for resellers

```python
#!/usr/bin/env python3
"""Explore reseller partner configs in demo environment."""

from typing import Any
from sqlmodel import select

from rhizome.client import RhizomeClient
from rhizome.environments.demo.billing_bookkeeper import DemoBillingBookkeeper
from rhizome.models.billing_bookkeeper.billing_entity import BillingEntity
from rhizome.models.billing_bookkeeper.partner_config import PartnerConfig
from rhizome.models.table_list import BillingBookkeeperTable


def explore_partner_configs() -> None:
    """Query demo for resellers and their partner configs."""
    print("🔍 Exploring partner configs in demo...\n")

    # Connect to environment
    client = RhizomeClient(data_in_logs=False)
    demo_bb = DemoBillingBookkeeper(client)

    # Get models
    BillingEntityModel = demo_bb.get_model(BillingBookkeeperTable.billing_entity)
    PartnerConfigModel = demo_bb.get_model(BillingBookkeeperTable.partner_config)

    # Query for resellers
    resellers = demo_bb.select_all(
        select(BillingEntityModel)
        .where(BillingEntityModel.entity_type == "RESELLER")
        .order_by(BillingEntityModel.created_timestamp.desc())
        .limit(20),
        sanitize=False,
    )

    print(f"📊 Found {len(resellers)} resellers\n")

    # Track statistics
    stats: dict[str, dict[str, int]] = {
        "settlement_method": {},
        "invoice_method": {},
        "hierarchy_type": {},
    }

    # Analyze each reseller's configs
    for reseller in resellers:
        print(f"Reseller: {reseller.name}")
        print(f"  UUID: {reseller.uuid}")

        # Get partner configs for this reseller
        configs = demo_bb.select_all(
            select(PartnerConfigModel)
            .where(PartnerConfigModel.billing_entity_uuid == reseller.uuid),
            sanitize=False,
        )

        for config in configs:
            print(f"  Config: {config.hierarchy_type}")
            print(f"    Settlement: {config.settlement_method}")
            print(f"    Invoice: {config.invoice_method}")

            # Update statistics
            stats["settlement_method"][config.settlement_method or "None"] = (
                stats["settlement_method"].get(config.settlement_method or "None", 0) + 1
            )
            stats["invoice_method"][config.invoice_method or "None"] = (
                stats["invoice_method"].get(config.invoice_method or "None", 0) + 1
            )

        print()

    # Print summary statistics
    print("\n📈 SUMMARY STATISTICS\n")
    for field_name, field_stats in stats.items():
        print(f"\n{field_name.replace('_', ' ').title()}:")
        sorted_stats = sorted(field_stats.items(), key=lambda x: x[1], reverse=True)
        for value, count in sorted_stats:
            percentage = (count / sum(field_stats.values())) * 100
            print(f"  {value}: {count} ({percentage:.1f}%)")

    # Print recommendations
    print("\n💡 RECOMMENDED DEFAULTS\n")
    for field_name, field_stats in stats.items():
        if field_stats:
            most_common = max(field_stats.items(), key=lambda x: x[1])
            print(f"  {field_name}: {most_common[0]}")


if __name__ == "__main__":
    explore_partner_configs()
```

## Example 2: Stolon-Based Exploration (HTTP APIs)

**Scenario**: Understanding what fields an API endpoint returns

```python
#!/usr/bin/env python3
"""Explore merchant API responses in dev environment."""

from typing import Any
import json

from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp


def explore_merchant_api() -> None:
    """Test merchant API endpoints to understand response structure."""
    print("🔍 Exploring merchant APIs in dev...\n")

    # Connect to dev environment
    client = StolonClient(data_in_logs=False)
    dev = DevHttp(client)

    # Test merchant creation response
    print("=== Testing Merchant Creation ===\n")
    test_merchant_data = {
        "name": "Test Exploration Merchant",
        "owner": {
            "name": "Test Owner",
            "email": "test@example.com"
        }
    }

    try:
        response = dev.post("/v3/merchants", json=test_merchant_data)
        print("✓ Merchant created successfully")
        print(f"Response keys: {list(response.keys())}")
        print(f"Merchant ID: {response.get('id')}")
        print(f"Full response:\n{json.dumps(response, indent=2)}")

        merchant_id = response.get('id')

        # Test GET to see what fields are returned
        print("\n=== Testing Merchant GET ===\n")
        get_response = dev.get(f"/v3/merchants/{merchant_id}")
        print(f"GET response keys: {list(get_response.keys())}")
        print(f"Fields present: {json.dumps({k: type(v).__name__ for k, v in get_response.items()}, indent=2)}")

        # Clean up (if DELETE is supported)
        dev.delete(f"/v3/merchants/{merchant_id}")
        print("\n✓ Cleanup successful")

    except Exception as e:
        print(f"⚠️  Error: {e}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response.text}")


if __name__ == "__main__":
    explore_merchant_api()
```

## Example 3: Combined Approach (Stolon + Rhizome)

**Scenario**: Validate that API creates correct database records

```python
#!/usr/bin/env python3
"""Explore how billing hierarchy API calls affect database state."""

from typing import Any
import time

from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp
from rhizome.client import RhizomeClient
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.models.billing_bookkeeper.billing_hierarchy import BillingHierarchy
from rhizome.models.table_list import BillingBookkeeperTable
from sqlmodel import select


def explore_hierarchy_creation() -> None:
    """Test how API calls translate to database records."""
    print("🔍 Exploring hierarchy API → DB relationship...\n")

    # Setup both clients
    stolon_client = StolonClient(data_in_logs=False)
    dev_http = DevHttp(stolon_client)

    rhizome_client = RhizomeClient(data_in_logs=False)
    dev_bb = DevBillingBookkeeper(rhizome_client)

    # Get the model
    HierarchyModel = dev_bb.get_model(BillingBookkeeperTable.billing_hierarchy)

    # Create via API
    print("=== Creating via API ===\n")
    api_data = {
        "billingEntityUuid": "TEST_ENTITY_123",
        "hierarchyType": "MERCHANT_SCHEDULE",
        "effectiveDate": "2025-12-01",
        "parentBillingHierarchyUuid": "PARENT_UUID_123"
    }

    try:
        api_response = dev_http.post("/billing-bookkeeper/v1/hierarchy", json=api_data)
        created_uuid = api_response.get("uuid")
        print(f"✓ API created hierarchy with UUID: {created_uuid}")
        print(f"API response keys: {list(api_response.keys())}")

        # Wait for propagation
        time.sleep(1)

        # Query database
        print("\n=== Querying Database ===\n")
        db_record = dev_bb.select_first(
            select(HierarchyModel).where(HierarchyModel.uuid == created_uuid),
            sanitize=False,
        )

        if db_record:
            print("✓ Found record in database")
            print(f"DB fields present: {list(db_record.__dict__.keys())}")
            print(f"\nAPI → DB field mapping:")
            for api_key in api_data.keys():
                db_key = ''.join(['_' + c.lower() if c.isupper() else c for c in api_key]).lstrip('_')
                db_value = getattr(db_record, db_key, "NOT FOUND")
                print(f"  {api_key} → {db_key}: {db_value}")

            # Check for fields in DB but not in API response
            db_only_fields = set(db_record.__dict__.keys()) - set(api_response.keys())
            print(f"\nFields in DB but not in API response:")
            for field in sorted(db_only_fields):
                if not field.startswith('_'):
                    print(f"  {field}: {getattr(db_record, field)}")
        else:
            print("⚠️  Record not found in database")

    except Exception as e:
        print(f"⚠️  Error: {e}")


if __name__ == "__main__":
    explore_hierarchy_creation()
```

## Available Environments and Services

### Rhizome Environments

```python
# Dev environment
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.environments.dev.merchant import DevMerchant
from rhizome.environments.dev.auth import DevAuth

# Demo environment
from rhizome.environments.demo.billing_bookkeeper import DemoBillingBookkeeper
from rhizome.environments.demo.merchant import DemoMerchant
```

### Stolon Environments

```python
# Dev HTTP client
from stolon.client import StolonClient
from stolon.environments.dev.http import DevHttp

# Initialize
client = StolonClient(data_in_logs=False)
dev = DevHttp(client)

# Make requests
dev.get("/path")
dev.post("/path", json={...})
dev.put("/path", json={...})
dev.delete("/path")
```

### Finding Models

Models are organized by service and table:

```python
from rhizome.models.billing_bookkeeper.billing_entity import BillingEntity
from rhizome.models.billing_bookkeeper.partner_config import PartnerConfig
from rhizome.models.billing_bookkeeper.billing_hierarchy import BillingHierarchy
from rhizome.models.table_list import BillingBookkeeperTable

# Get model dynamically
service = DevBillingBookkeeper(client)
Model = service.get_model(BillingBookkeeperTable.partner_config)
```

To explore available tables:

```python
from rhizome.models.table_list import BillingBookkeeperTable

# List all available tables
print([attr for attr in dir(BillingBookkeeperTable) if not attr.startswith('_')])
```

## Key Rhizome Query Patterns

### Basic SELECT with WHERE

```python
results = service.select_all(
    select(Model)
    .where(Model.field == "value")
    .where(Model.other_field > 100),
    sanitize=False,  # False = real UUIDs, True = hashed
)
```

### Ordering and Limiting

```python
recent_items = service.select_all(
    select(Model)
    .order_by(Model.created_timestamp.desc())
    .limit(10),
    sanitize=False,
)
```

### Select Specific Fields

```python
field_values = service.select_all(
    select(Model.field_name, Model.other_field)
    .where(Model.status == "ACTIVE"),
    sanitize=False,
)
```

### Handling NULL Values

```python
# Find records where field is NOT NULL
with_parent = service.select_all(
    select(Model)
    .where(Model.parent_id.is_not(None)),
    sanitize=False,
)

# Find records where field IS NULL
without_parent = service.select_all(
    select(Model)
    .where(Model.parent_id.is_(None)),
    sanitize=False,
)
```

### Pattern Matching

```python
# Find records where field starts with prefix
matching_records = service.select_all(
    select(Model)
    .where(Model.name.like("PREFIX%")),
    sanitize=False,
)
```

### Get First Match

```python
single_result = service.select_first(
    select(Model)
    .where(Model.uuid == "ABC123"),
    sanitize=False,
)
```

## Analysis Phase

After running your exploration script, document findings:

1. **Create an analysis document** (e.g., `analysis_[feature].md`)
2. **Summarize patterns discovered**:
   - Common field values
   - Required vs optional fields
   - Relationships between tables
   - API response structures
3. **Include statistics** (percentages, counts)
4. **Make recommendations** for implementation

Example analysis structure:

```markdown
# [Feature] Exploration Analysis

## Summary
Brief description of what was explored and why.

## Key Findings

1. **Field Patterns**
   - field_name: "common_value" (70%), "other_value" (30%)
   - optional_field: null in 50% of records

2. **Relationships**
   - Table A links to Table B via field_x
   - Parent hierarchies use UUIDs from Table C

3. **API Behavior**
   - POST returns fields: [a, b, c]
   - GET returns additional fields: [d, e, f]
   - Certain fields are computed server-side

## Recommendations

Based on findings, recommend:
- Which fields to include in test data
- Which values to use
- Which patterns to follow
```

## Implementation Phase

Apply discoveries to your actual code:

```python
# In your test or implementation code

# BEFORE exploration: guessing at field values
json_data = {
    "field1": "guess1",  # Is this right?
    "field2": "guess2",  # Do I need this?
    "field3": True,      # Is this required?
}

# AFTER exploration: using discovered patterns
json_data = {
    "field1": "Goleo",          # 70% of configs use this
    "field2": "MerchantDetail", # Most common pattern
    # field3 omitted - exploration showed it's optional
}
```

## Best Practices

### 1. Use `sanitize=False` When You Need Real IDs

```python
# For querying or matching against API responses
result = service.select_first(
    select(Model).where(Model.uuid == "ABC123"),
    sanitize=False,  # Returns real UUID
)

# For displaying to users (privacy protection)
result = service.select_first(
    select(Model).where(Model.uuid == "ABC123"),
    sanitize=True,  # Returns hashed UUID
)
```

### 2. Limit Query Scope

```python
# Don't fetch thousands of records
.limit(20)  # Sample size for pattern analysis

# Focus on recent data
.order_by(Model.created_timestamp.desc())
```

### 3. Handle Type Checking

```python
# Models may be returned as objects or tuples
for item in results:
    if isinstance(item, Model):
        value = item.field_name
    else:
        value = item.field_name  # Handle tuple case
```

### 4. Print Progress

```python
print("🔍 Starting exploration...")
print(f"📊 Found {len(results)} records")
print("✓ Analysis complete")
print("⚠️  Warning: unusual pattern detected")
```

### 5. Handle Errors Gracefully

```python
try:
    response = dev.post("/endpoint", json=data)
except Exception as e:
    print(f"⚠️  API Error: {e}")
    if hasattr(e, 'response'):
        print(f"Status: {e.response.status_code}")
        print(f"Body: {e.response.text}")
```

## Running Your Exploration Script

```bash
# Make it executable
chmod +x explore_feature.py

# Run it
./explore_feature.py

# Or run with python
python explore_feature.py
```

## When You Can't Access the Environment

**Important**: Some machines cannot access certain environments (e.g., production VPN restrictions).

If you're an AI agent and cannot run queries yourself:

1. **Generate the exploration script** as described above
2. **Ask the user to run it**: "I've created `explore_[feature].py`. Could you run this and share the output?"
3. **Analyze the output** they provide
4. **Use findings** to inform your implementation

## Summary Workflow

```
1. Agent identifies need for exploration
   └→ "I need to understand how partner_config works in production"

2. Agent generates exploration script
   └→ explore_partner_config.py (using rhizome/stolon)

3. Script is executed (by agent or user)
   └→ Queries database or APIs
   └→ Computes statistics
   └→ Prints findings

4. Agent analyzes output
   └→ Documents patterns
   └→ Makes recommendations

5. Agent applies findings to implementation
   └→ Uses discovered values in test fixtures
   └→ Follows observed patterns in production code
```

## Example Agent Prompt

When you (as an AI agent) need to explore:

> "I need to understand [FEATURE] in [ENVIRONMENT] before implementing [TASK]. Let me create an exploration script to query the [SERVICE] and analyze current patterns. This will help ensure my implementation matches production behavior."

Then generate an exploration script following the templates in this document.
