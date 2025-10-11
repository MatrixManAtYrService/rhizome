# Rhizome Table Versioning System

This document describes the table versioning architecture implemented in Rhizome to handle progressive schema changes across environments.

## Problem Statement

Database schema changes typically roll out progressively across environments:
1. **Dev environment** gets the new schema first
2. **Stage environment** receives the change after testing
3. **Production environments** get the change last

During this rollout period, different environments have different table schemas. Tests and applications need to work with tables that may or may not have certain columns depending on the environment.

## Architecture Overview

Rhizome uses a base class + versioned class inheritance pattern with environment-specific version tracking:

### Base Classes (Schema Definition)
- **Purpose**: Define common table structure shared across ALL versions
- **Implementation**: `table=False` - not actual database tables
- **Location**: `src/rhizome/models/{database}/{table}.py`
- **Usage**: For version-agnostic code that only uses fields guaranteed to exist across all versions

### Versioned Classes (Table Implementation)
- **Purpose**: Actual database table implementations with version-specific schemas
- **Implementation**: `table=True` with `__tablename__` - real database tables
- **Location**: `src/rhizome/models/{database}/{table}_v{N}.py`
- **Usage**: For version-specific code that depends on particular schema versions

### Environment Version Mapping
- **Purpose**: Track which table version each environment currently uses
- **Implementation**: `table_situation` dictionary in Environment classes, populated by `situate_table()` method
- **Location**: `src/rhizome/environments/{env}/{database}.py`
- **Access Method**: Use `get_versioned()` method to retrieve the appropriate versioned model for an environment

## Implementation Details

### Directory Structure
```
src/rhizome/models/
├── billing_bookkeeper/
│   ├── fee_summary.py          # Base class (table=False)
│   ├── fee_summary_v1.py       # V1 implementation (table=True)
│   └── fee_summary_v2.py       # Future V2 with new fields
├── billing_event/
│   ├── app_metered_event.py    # Base class (table=False)
│   ├── app_metered_event_v1.py # V1 implementation (table=True)
│   └── app_metered_event_v2.py # Future V2 with new fields
└── billing/
    ├── stage_charge.py         # Base class (table=False)
    ├── stage_charge_v1.py      # V1 implementation (table=True)
    └── stage_charge_v2.py      # Future V2 with new fields
```

### Example: Base Class Definition
```python
# src/rhizome/models/billing_bookkeeper/fee_summary.py
class FeeSummary(SanitizableModel, table=False):
    """Base FeeSummary model - defines common fields across all versions."""

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=26, unique=True)
    billing_entity_uuid: str = Field(max_length=26)
    # ... other common fields

    def sanitize(self) -> FeeSummary:
        """Return sanitized copy."""
        # ... sanitization logic
```

### Example: V1 Implementation (Current)
```python
# src/rhizome/models/billing_bookkeeper/fee_summary_v1.py
class FeeSummaryV1(FeeSummary, table=True):
    """
    Version 1 of the FeeSummary model.

    Currently a name-only inheritance from the base FeeSummary class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "fee_summary"
```

### Example: Future V2 Implementation
```python
# src/rhizome/models/billing_bookkeeper/fee_summary_v2.py
class FeeSummaryV2(FeeSummary, table=True):
    """
    Version 2 of the FeeSummary model.

    Adds new fields introduced in schema migration X.Y.Z:
    - processing_status: Track processing state
    - external_reference: Link to external billing system
    """

    __tablename__ = "fee_summary"

    # New fields in V2
    processing_status: str | None = Field(default=None, max_length=20)
    external_reference: str | None = Field(default=None, max_length=50)
```

### Environment Version Tracking
```python
# src/rhizome/environments/dev/billing_bookkeeper.py
class DevBillingBookkeeper(Environment):
    """Dev environment for billing_bookkeeper database."""

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        """Map table names to their versioned models and emplacements."""
        match table_name:
            case BillingBookkeeperTable.fee_summary:
                return (FeeSummaryV2, None)  # Dev has the new schema
            # ... other tables
        return (None, None)

# src/rhizome/environments/na_prod/billing_bookkeeper.py
class NorthAmericaBillingBookkeeper(Environment):
    """Production environment for billing_bookkeeper database."""

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        """Map table names to their versioned models and emplacements."""
        match table_name:
            case BillingBookkeeperTable.fee_summary:
                return (FeeSummaryV1, None)  # Prod still on old schema
            # ... other tables
        return (None, None)
```

## Usage Patterns

Rhizome provides the `get_versioned()` method on Environment classes to retrieve the appropriate versioned model for a given base class. This method enables version-agnostic programming while maintaining type safety.

### Pattern 1: Totally Version-Agnostic (Recommended for Portable Code)

Use `get_versioned()` with base classes. Only access fields guaranteed to exist in all versions. This pattern makes your code work across any environment regardless of schema version.

```python
from rhizome.models.billing_bookkeeper.fee_summary import FeeSummary as FeeSummaryModel
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from sqlmodel import select

# Get the versioned model for this environment
db = DevBillingBookkeeper(client)
FeeSummary = db.get_versioned(FeeSummaryModel)

# Write code using only fields from the base class - works in any environment
fees = db.select_all(
    select(FeeSummary).where(FeeSummary.billing_entity_uuid == target_uuid)
)
for fee in fees:
    print(fee.uuid, fee.total_fee_amount)  # Base fields work everywhere
```

**When to use**: Default choice for most code. Use when your logic only needs fields present in all schema versions.

### Pattern 2: Version-Agnostic with Runtime Edge Cases

Use `get_versioned()` with base classes, but handle specific versions when needed via `match/case`. This pattern is version-agnostic 90% of the time but can access version-specific fields in the 10% of cases that need them.

```python
from rhizome.models.billing_bookkeeper.fee_summary import FeeSummary as FeeSummaryModel
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1
from rhizome.models.billing_bookkeeper.fee_summary_v2 import FeeSummaryV2
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from sqlmodel import select

# Get the versioned model for this environment
db = DevBillingBookkeeper(client)
FeeSummary = db.get_versioned(FeeSummaryModel)

# Query using base class
fee = db.select_first(select(FeeSummary).where(FeeSummary.uuid == target_uuid))

# Handle version-specific fields at runtime
match fee:
    case FeeSummaryV2():
        # Type checker knows this is V2 with processing_status field
        print(f"Processing status: {fee.processing_status}")
    case FeeSummaryV1():
        # Type checker knows this is V1 without that field
        print("V1 fee - no processing status field")
    case _:
        raise TypeError(f"Unknown fee summary version: {type(fee)}")
```

**When to use**: When you need version-specific fields occasionally but want most of your code to remain version-agnostic.

### Pattern 3: Totally Version-Explicit (Not Portable)

Import and use versioned classes directly. This ties your code to a specific schema version and will fail in environments using different versions.

```python
from rhizome.models.billing_bookkeeper.fee_summary_v2 import FeeSummaryV2
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from sqlmodel import select

db = DevBillingBookkeeper(client)

# Query directly with V2 class
fees = db.select_all(
    select(FeeSummaryV2).where(FeeSummaryV2.processing_status == "PENDING")
)
for fee in fees:
    print(fee.processing_status)  # V2-specific field
```

**When to use**: Only when you know the target environment and need version-specific fields throughout your logic. This approach fails in environments using different versions (e.g., if production uses V1).

### Pattern 4: Environment-Specific Aliases

Use type aliases on environment classes for environment-specific but version-agnostic code. This provides compile-time type safety for the specific version an environment uses.

```python
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from sqlmodel import select

# DevBillingBookkeeper.FeeSummary is a type alias to FeeSummaryV1
db = DevBillingBookkeeper(client)
fees = db.select_all(
    select(DevBillingBookkeeper.FeeSummary).where(
        DevBillingBookkeeper.FeeSummary.billing_entity_uuid == target_uuid
    )
)
for fee in fees:
    print(fee.uuid, fee.total_fee_amount)  # Type checker knows V1 fields
```

**When to use**: When you need type checking for environment-specific code (scripts, tests) that you know will only run in particular environments. This provides better IDE support and type safety than Pattern 1, while being more portable than Pattern 3.

## Testing Strategy

### Dual Test Coverage
Tests use multiple approaches to ensure compatibility:

```python
# Pattern 1: Version-agnostic test - uses get_versioned() with base class
def test_fee_calculation_all_environments(client):
    from rhizome.models.billing_bookkeeper.fee_summary import FeeSummary as FeeSummaryModel
    from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper

    db = DevBillingBookkeeper(client)
    FeeSummary = db.get_versioned(FeeSummaryModel)
    # Test logic using only common fields

# Pattern 3: Version-specific test - uses V2 class directly
def test_processing_status_tracking():
    from rhizome.models.billing_bookkeeper.fee_summary_v2 import FeeSummaryV2
    # Test logic using V2-specific fields
```

### Environment Combinations
Parameterized tests cover all environment/version combinations:

```python
ENVIRONMENT_DATABASE_COMBINATIONS = [
    (NorthAmericaBillingBookkeeper, FeeSummaryV1),  # Prod uses V1
    (DevBillingBookkeeper, FeeSummaryV2),          # Dev uses V2
    (DemoBillingBookkeeper, FeeSummaryV1),         # Demo uses V1
]
```

## Migration Workflow

### Adding a New Schema Version

1. **Create the new versioned class**:
   ```bash
   # Copy and modify the latest version
   cp src/rhizome/models/billing_bookkeeper/fee_summary_v1.py \
      src/rhizome/models/billing_bookkeeper/fee_summary_v2.py
   ```

2. **Add new fields to the V2 class**:
   ```python
   class FeeSummaryV2(FeeSummary, table=True):
       __tablename__ = "fee_summary"

       # New field in V2
       processing_status: str | None = Field(default=None, max_length=20)
   ```

3. **Update environment `situate_table()` mappings** as schema deploys:
   ```python
   # First: Dev environment gets V2
   class DevBillingBookkeeper(Environment):
       def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
           match table_name:
               case BillingBookkeeperTable.fee_summary:
                   return (FeeSummaryV2, None)  # Updated to V2
               # ... other tables

   # Later: Production environments get V2
   class NorthAmericaBillingBookkeeper(Environment):
       def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
           match table_name:
               case BillingBookkeeperTable.fee_summary:
                   return (FeeSummaryV2, None)  # Updated to V2
               # ... other tables
   ```

4. **Add exports to __init__.py**:
   ```python
   from .fee_summary_v2 import FeeSummaryV2
   __all__ = ["FeeSummary", "FeeSummaryV1", "FeeSummaryV2"]
   ```

5. **Update test specifications** in `tests/mocked_table_data.py`:
   ```python
   TEST_DATA_SPECS = {
       FeeSummaryV2: {
           DevBillingBookkeeper: TestSpec(
               use_id=123,
               get_mock_data=lambda: FeeSummaryV2(..., processing_status="PENDING"),
               # ...
           ),
       },
   }
   ```

### Type Safety Benefits

The type checker enforces version compatibility:

```python
# ✅ Safe - uses field guaranteed to exist in all versions
def safe_function(fee: FeeSummary) -> str:
    return fee.uuid

# ❌ Type error - processing_status doesn't exist in base class
def unsafe_function(fee: FeeSummary) -> str:
    return fee.processing_status  # Type error!

# ✅ Safe - explicitly uses V2 which has the field
def v2_function(fee: FeeSummaryV2) -> str:
    return fee.processing_status  # OK!
```

## Benefits

1. **Progressive Rollouts**: Different environments can have different schema versions
2. **Type Safety**: Compiler prevents accessing fields that don't exist in target environment
3. **Version-Agnostic Code**: Common operations work across all schema versions
4. **Test Coverage**: Both version-agnostic and version-specific tests ensure compatibility
5. **Clear Migration Path**: Well-defined process for adding new schema versions
6. **Environment Tracking**: Easy to see which version each environment uses

## Best Practices

### For Framework/Library Code (Primary Use Case)

When writing maintainable, type-checked code that accepts dependency-injection via environment objects:

1. **Prefer Pattern 1** (version-agnostic with `get_versioned()`) for new code unless you specifically need version-specific fields
2. **Use `get_versioned()` method** to retrieve the environment-appropriate versioned model from base classes
3. **Use Pattern 2** (match/case) when you occasionally need version-specific fields but want most code version-agnostic
4. **Reserve Pattern 3** (direct version imports) only for code tied to specific environments
5. **Test both patterns** - version-agnostic tests for common logic, version-specific tests for new features

### For One-Off Scripts and Ad-Hoc Queries

When writing scripts to answer specific questions about data in a particular environment:

- **Pattern 4 is recommended** for environment-specific scripts and exploratory code
- Use environment-specific aliases (e.g., `DevBillingBookkeeper.FeeSummary`) for type safety and clarity
- **Pattern 3 is acceptable** as an alternative for readability in throwaway/exploratory code
- One-off scripts don't need to be portable across environments
- Direct version imports (e.g., `from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1`) can make scripts clearer when you know the target environment
- These scripts trade cross-environment portability for environment-specific clarity - acceptable for exploratory work but not for library code

### General Guidelines

1. **Document schema changes** in version class docstrings
2. **Update `situate_table()` mappings** promptly when schemas are deployed to new environments
3. **Keep base classes minimal** - only include fields that will exist in ALL future versions
4. **Choose pattern based on code lifecycle** - framework code needs portability, scripts can prioritize readability