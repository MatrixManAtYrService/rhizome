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
- **Implementation**: Enums in environment modules
- **Location**: `src/rhizome/environments/{env}/{database}.py`

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
class DevBillingBookkeeperModel(Enum):
    """Table version mapping for DevBillingBookkeeper environment."""
    FeeSummary = FeeSummaryV2  # Dev has the new schema
    
# src/rhizome/environments/na_prod/billing_bookkeeper.py  
class NorthAmericaBillingBookkeeperModel(Enum):
    """Table version mapping for NorthAmericaBillingBookkeeper environment."""
    FeeSummary = FeeSummaryV1  # Prod still on old schema
```

## Usage Patterns

### Version-Agnostic Code (Recommended)
Use base classes when your code only needs fields guaranteed to exist across all environments:

```python
from rhizome.models.billing_bookkeeper.fee_summary import FeeSummary

# This works regardless of environment schema version
def get_fee_amount(fee: FeeSummary) -> Decimal:
    return fee.total_fee_amount  # Field exists in all versions

# Query using base class - works with any version
statement = select(FeeSummary).where(FeeSummary.uuid == target_uuid)
```

### Version-Specific Code (When Necessary)
Use versioned classes when you need fields that don't exist in all versions:

```python
from rhizome.models.billing_bookkeeper.fee_summary_v2 import FeeSummaryV2

# This only works in environments with V2 schema
def get_processing_status(fee: FeeSummaryV2) -> str:
    return fee.processing_status  # Field only exists in V2

# Query using versioned class - only works with V2+ environments  
statement = select(FeeSummaryV2).where(FeeSummaryV2.processing_status == "PENDING")
```

### Environment-Aware Code
Access the specific version for an environment through version enums:

```python
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeperModel

# Get the specific version used in dev environment
DevFeeSummary = DevBillingBookkeeperModel.FeeSummary.value
statement = select(DevFeeSummary).where(DevFeeSummary.id == 123)
```

## Testing Strategy

### Dual Test Coverage
Tests use both approaches to ensure compatibility:

```python
# Version-agnostic test - uses base class
def test_fee_calculation_all_environments():
    from rhizome.models.billing_bookkeeper.fee_summary import FeeSummary
    # Test logic using only common fields

# Version-specific test - uses V2 class  
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

3. **Update environment version mappings** as schema deploys:
   ```python
   # First: Dev environment gets V2
   class DevBillingBookkeeperModel(Enum):
       FeeSummary = FeeSummaryV2
   
   # Later: Production environments get V2  
   class NorthAmericaBillingBookkeeperModel(Enum):
       FeeSummary = FeeSummaryV2
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

1. **Prefer base classes** for new code unless you specifically need version-specific fields
2. **Use version enums** when you need to query environment-specific table versions
3. **Test both patterns** - version-agnostic tests for common logic, version-specific tests for new features
4. **Document schema changes** in version class docstrings
5. **Update environment mappings** promptly when schemas are deployed
6. **Keep base classes minimal** - only include fields that will exist in ALL future versions