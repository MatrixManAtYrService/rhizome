# Rhizome Sync Commands

This document describes the usage of the `rhizome sync` commands.

## `rhizome sync report`

### Purpose

The `rhizome sync report` command provides a comprehensive overview of the synchronization status for all environment/table pairs. It shows which tables have schemas, models, emplacements, and data files, helping you understand what needs to be implemented next.

### Usage

```bash
rhizome sync report [OPTIONS]
```

### Options

- `--env TEXT`: Limit the report to a specific environment. If not provided, all environments are included.

### Example

To see the sync status for all environments:

```bash
rhizome sync report
```

To see the sync status for just the dev environment:

```bash
rhizome sync report --env dev_billing_bookkeeper
```

### Output

The report shows:
- **Summary statistics** of complete, partially synced, and missing tables
- **Detailed table** with checkmarks showing what exists for each environment/table pair
- **Recommendations** for next steps (run schema sync, create models, etc.)

## `rhizome sync data`

### Purpose

The `rhizome sync data` command is used to fetch the first row of data from each table in a given environment and save it as a JSON file. This is useful for keeping a local snapshot of the expected data in each environment for testing and development purposes.

### Usage

```bash
rhizome sync data [OPTIONS]
```

### Options

-   `--env TEXT`: The environment to sync. If not provided, all environments are synced. The available environments are:
    -   `dev_billing_bookkeeper`
    -   `dev_billing_event`
    -   `demo_billing_bookkeeper`
    -   `demo_billing_event`
    -   `na_prod_billing`
    -   `na_prod_billing_bookkeeper`
    -   `na_prod_billing_event`
-   `--verbose`: Show the full stack trace on error.

### Example

To sync the data for the `dev_billing_bookkeeper` environment:

```bash
rhizome sync data --env dev_billing_bookkeeper
```

This will create a file named `{table_name}.json` for each table in the `dev_billing_bookkeeper` environment inside the `src/rhizome/environments/dev/expected_data/` directory.

## `rhizome sync schema`

### Purpose

The `rhizome sync schema` command fetches `CREATE TABLE` statements for database tables and saves them as `.sql` files. This command now automatically discovers all tables from the table enums (not just implemented ones) and attempts to sync schemas from each environment.

### Key Features

- **Automatic table discovery**: Reads all tables from `BillingBookkeeperTable`, `BillingEventTable`, and `BillingTable` enums
- **Environment independence**: Doesn't require tables to be implemented in environment `models` dictionaries
- **Graceful error handling**: If a table doesn't exist in an environment, it logs an error but continues
- **Change tracking**: Shows which schema files were created, updated, or unchanged
- **New file detection**: Clearly identifies newly created schema files

### Usage

```bash
rhizome sync schema [OPTIONS]
```

### Options

- `--env TEXT`: The environment to sync. If not provided, all environments are synced.
- `--verbose`: Show the full stack trace on error.

### Example

To sync schemas for all environments:

```bash
rhizome sync schema
```

To sync schemas for just the dev environment:

```bash
rhizome sync schema --env dev_billing_bookkeeper
```

### Output

The command provides:
- **Progress information**: Shows which environment and table is being synced
- **JSON summary**: Comprehensive change tracking with counts of new, changed, and unchanged files
- **File paths**: All tracked files are listed by category (new, trivial changes, etc.)

### File Naming Convention

Schema files are saved as: `src/rhizome/environments/{env_folder}/expected_data/{database}_{table}.sql`

Examples:
- `src/rhizome/environments/dev/expected_data/billing_bookkeeper_fee_summary.sql`
- `src/rhizome/environments/na_prod/expected_data/billing_event_app_metered_event.sql`

## Workflow and Integration

### Typical Development Workflow

1. **Add new tables to enums**: Add table names to the appropriate enum in `src/rhizome/models/table_list.py`
2. **Run sync report**: `rhizome sync report` to see which tables are missing schemas
3. **Run sync schema**: `rhizome sync schema` to fetch schemas for all tables from all environments
4. **Create models**: Based on the schemas, create base and versioned model classes
5. **Create emplacements**: Add expected data classes for each environment
6. **Update environment mappings**: Add entries to environment `models` dictionaries
7. **Run sync data**: `rhizome sync data` to fetch actual data samples
8. **Verify with sync report**: `rhizome sync report` to confirm everything is properly synced

### Integration with Table Discovery

The sync commands now work seamlessly with the centralized table enum approach:

- **Single source of truth**: All tables are defined in `src/rhizome/models/table_list.py`
- **Automatic discovery**: Sync commands automatically find all tables from enums
- **Progressive implementation**: You can add tables to enums and explore them with sync commands before implementing models/emplacements
- **Environment coverage**: Easily see which tables exist in which environments

### Change Detection

The sync schema command includes sophisticated change detection:

- **New files**: Shows `new_count` and lists newly created schema files
- **Trivial changes**: Detects minor changes like AUTO_INCREMENT value differences
- **Significant changes**: Identifies schema changes that require attention
- **Unchanged files**: Tracks files that were processed but had no changes

This helps you understand the impact of schema synchronization and identify when database schemas have evolved.

## Model and Emplacement Generation Guide

This section provides detailed guidance for generating models and emplacements when the sync report shows missing components.

### Understanding Sync Report Status Icons

- ✅ **Complete**: Schema + Model + Emplacement + Data all present
- ⚠️ **Ready for data sync**: Schema + Model + Emplacement present, but missing data (run `rhizome sync data`)
- 🔶 **Missing emplacement**: Schema + Model present, but missing emplacement classes
- 📄 **Schema only**: Only schema file exists, missing model and emplacement
- ❌ **Missing**: No components exist

### Automated Model Generation Workflow

When you see tables with "📄 Schema Only" status:

1. **Generate base and V1 model classes** for each table:
   ```bash
   # Use the general-purpose agent to generate models
   # Example prompt: "Generate SQLModel model classes for billing_event tables that have schemas but no models"
   ```

2. **Model generation follows this pattern**:
   ```python
   # Base model (table=False)
   # src/rhizome/models/{database}/{table}.py
   class {TableName}(RhizomeModel, table=False):
       """Base {TableName} model - defines common fields across all versions."""
       # Fields with proper types and constraints
       def sanitize(self) -> {TableName}:
           # Sanitization logic using helpers like sanitize_uuid_field

   # V1 model (table=True)
   # src/rhizome/models/{database}/{table}_v1.py
   class {TableName}V1({TableName}, table=True):
       """Version 1 of the {TableName} model."""
       __tablename__ = "{table_name}"
   ```

3. **Update model __init__.py**:
   - Add imports for both base and V1 classes
   - Update `__all__` list

### Automated Emplacement Generation Workflow

When you see tables with "🔶 Missing emplacement" status:

1. **Generate emplacement classes** for each environment:
   ```python
   # src/rhizome/environments/{env}/expected_data/{database}_{table}.py
   from __future__ import annotations

   from rhizome.models.base import Emplacement
   from rhizome.models.{database}.{table}_v1 import {TableName}V1

   class {TableName}{Environment}(Emplacement[{TableName}V1]):
       """Expected data for {TableName} in {environment} environment."""

       @classmethod
       def get_expected(cls) -> {TableName}V1:
           """Get expected {table} data for {environment} environment."""
           module_path = Path(__file__).parent
           file_path = module_path / "{database}_{table}.json"

           if not file_path.exists():
               raise NotImplementedError(
                   f"Expected data for {cls.__name__} not yet implemented. "
                   f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
               )

           with open(file_path) as f:
               data = json.load(f)
           return {TableName}V1.model_validate(data)
   ```

2. **Update environment files**:
   - Add imports for V1 models and emplacement classes
   - Add entries to `models` dictionary: `BillingEventTable.{table}: ({TableName}V1, {TableName}{Environment})`

### Improved Emplacement Strategy (Recommended)

**IMPORTANT**: The strategy shown above is now **superseded** by an improved approach that prevents confusion between "not implemented" vs "data not synced". Use this pattern for all new emplacement classes:

#### The Problem
The original pattern with `raise NotImplementedError` caused confusion:
- `rhizome sync report` would show data as ready to sync
- `rhizome sync data` would successfully create JSON files
- But tests would still be skipped with "Test data not yet implemented"
- Users couldn't tell if the issue was missing implementation or missing data

#### The Solution: Smart JSON File Detection

**Template for new emplacement classes:**
```python
"""Expected data for {table} table in {environment} environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.{database}.{table}_v1 import {TableName}V1


class {TableName}{Environment}(Emplacement[{TableName}V1]):
    """Expected data for {TableName} in {environment} environment."""

    @classmethod
    def get_expected(cls) -> {TableName}V1:
        """Get expected {table} data for {environment} environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "{database}_{table}.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return {TableName}V1.model_validate(data)
```

#### Key Benefits
1. **Only raises NotImplementedError when JSON file is actually missing**
2. **Provides clear guidance**: Tells users exactly what command to run
3. **Automatically works**: Once JSON file is created, no code changes needed
4. **Prevents sync confusion**: Clear distinction between implementation vs data issues

#### Migration Strategy for Existing Files
For existing emplacement classes that already have the old pattern:

1. **Batch update using general-purpose agent** with this pattern
2. **Files with existing JSON**: Replace NotImplementedError with JSON reading
3. **Files without JSON**: Use the smart detection pattern
4. **Add required imports**: `import json` and `from pathlib import Path`

#### Workflow Integration
This strategy integrates seamlessly with the sync workflow:

1. **Create emplacement class**: Use smart detection pattern
2. **Run sync report**: Shows missing data (because JSON file doesn't exist)
3. **Run sync data**: Creates JSON file with real data
4. **Automatic functionality**: Emplacement class now works without modification
5. **Run tests**: All tests pass, no more skipped tests

### Common Patterns and Solutions

#### Reserved Attribute Names
SQLAlchemy reserves certain attribute names like `metadata`. Solutions:
```python
# Use different Python attribute name with column mapping
meta_data: str | None = Field(
    default=None,
    sa_column=Column("metadata", String(1024)),
    description="Optional metadata"
)
```

#### Tables Without Standard ID Primary Key
Some tables (like `flyway_schema_history`) use different primary key structures and don't have an `id` field:
```python
# Inherit from SQLModel directly instead of RhizomeModel
class FlywaySchemaHistory(SQLModel, table=False):
    """Special case: table with non-standard primary key."""

    # Use the actual primary key from the schema
    installed_rank: int = Field(primary_key=True, description="Installation rank")
    # ... other fields

    def sanitize(self: T) -> T:
        """Custom sanitize method for non-RhizomeModel tables."""
        return FlywaySchemaHistory(
            installed_rank=self.installed_rank,
            # ... other fields
        )
```

#### Field Type Mapping from SQL
- `varchar(N)` → `str` with `Field(max_length=N)`
- `int unsigned AUTO_INCREMENT` → `int | None = Field(default=None, primary_key=True)`
- `decimal(M,D)` → `Decimal` with `Field(max_digits=M, decimal_places=D)`
- `datetime(6)` → `datetime.datetime`
- `char(N)` → `str` with `Field(max_length=N)`
- `json` → `str` (stored as JSON string)
- `tinyint(1)` → `bool`

#### Enum Field Handling
For fields with constrained values:
```python
from enum import Enum

class {FieldName}Type(str, Enum):
    VALUE1 = "value1"
    VALUE2 = "value2"

# In model:
field_name: {FieldName}Type = Field(description="Field description")
```

#### UUID Field Sanitization
Always use the sanitization helper for UUID fields:
```python
from ...sanitize_helpers import sanitize_uuid_field

def sanitize(self) -> {ModelName}:
    return {ModelName}(
        uuid=sanitize_uuid_field(self.uuid, 32),  # Specify length
        # ... other fields
    )
```

### Environment-Specific Considerations

#### Dev Environment
- Usually has the most comprehensive table coverage
- Often includes tables not present in other environments
- Good source for understanding new schema additions

#### Demo Environment
- May have subset of tables compared to dev
- Often mirrors production more closely than dev

#### Production Environments
- Most stable schema versions
- May lag behind dev in schema updates
- Critical for understanding deployed state

### Batch Processing Approach

For large-scale model/emplacement generation:

1. **Use the general-purpose agent** for batch operations
2. **Process by category**:
   - First: Generate all missing models
   - Second: Generate all missing emplacements
   - Third: Update all environment registrations
3. **Verify with sync report** after each major step

### Troubleshooting Common Issues

#### Import Errors After Generation
- Check `__init__.py` files are updated with new imports
- Verify import paths match file locations
- Ensure environment files have correct model registrations

#### Sync Report Not Updating
- Restart any running rhizome processes
- Check for syntax errors in generated files
- Verify table names match enum values exactly

#### Missing Tables in Specific Environments
- Check if schema files exist for that environment
- Some tables may not exist in all environments
- Use environment-specific model registrations

### File Organization Best Practices

#### Model Files
```
src/rhizome/models/{database}/
├── __init__.py                    # Exports all models
├── {table}.py                     # Base model (table=False)
├── {table}_v1.py                  # V1 model (table=True)
└── {table}_v2.py                  # Future versions
```

#### Emplacement Files
```
src/rhizome/environments/{env}/expected_data/
├── {database}_{table}.py          # Emplacement classes
└── {database}_{table}.json        # Actual test data (from sync data)
```

#### Environment Registration
```
src/rhizome/environments/{env}/{database}.py
├── Imports for all V1 models and emplacement classes
├── models: dict mapping enum values to (ModelV1, EmplacementClass) tuples
└── DatabaseEnvironment implementation
```

### Next Steps After Model/Emplacement Generation

1. **Run sync report** to verify all components are registered
2. **Run sync data** to populate actual test data
3. **Review generated models** for any needed customizations
4. **Add real test data** to emplacement classes as needed
5. **Run tests** to ensure everything works correctly

## Environment-Scoped Schema Versioning (V1/V2 Models)

### Problem Statement

When database schemas evolve differently across environments, you may encounter:
- **Field mismatches**: Fields exist in dev/demo but not in na_prod (e.g., `request_uuid`, `modifier`)
- **SQL errors**: "Unknown column" errors when models include fields not present in certain environments
- **SQLAlchemy conflicts**: "Table already defined" errors when V1 and V2 models use the same `__tablename__`

### Solution: Environment-Scoped MetaData

The solution uses separate SQLAlchemy registries to avoid table conflicts while maintaining type safety.

#### 1. Create Separate MetaData Registries

```python
# src/rhizome/models/metadata_registry.py
from sqlalchemy.orm import registry
from sqlmodel import SQLModel

# Create separate registries for each environment type
na_prod_registry = registry()
dev_demo_registry = registry()

class NaProdSQLModel(SQLModel, registry=na_prod_registry):
    """SQLModel base for na_prod environment models (V1)."""
    pass

class DevDemoSQLModel(SQLModel, registry=dev_demo_registry):
    """SQLModel base for dev/demo environment models (V2)."""
    pass
```

#### 2. Create Version-Specific Models

**Base Model (table=False)** - Contains only fields present in ALL environments:
```python
# src/rhizome/models/billing_event/as_of_merchant.py
class AsOfMerchant(RhizomeModel, table=False):
    """Base AsOfMerchant model - fields present in all environments."""
    uuid: str = Field(...)
    merchant_uuid: str = Field(...)
    # ... other common fields
    # NO request_uuid here - not in all environments

    def sanitize(self: T) -> T:
        # Subclasses implement this
        raise NotImplementedError("Subclasses must implement sanitize()")
```

**V1 Model (na_prod)** - Uses NaProdSQLModel registry:
```python
# src/rhizome/models/billing_event/as_of_merchant_v1.py
from ..metadata_registry import NaProdSQLModel

class AsOfMerchantV1(AsOfMerchant, NaProdSQLModel, table=True):
    """V1 for na_prod - no request_uuid field."""
    __tablename__ = "as_of_merchant"

    def sanitize(self) -> AsOfMerchantV1:
        return AsOfMerchantV1(
            uuid=sanitize_uuid_field(self.uuid, 26),
            # ... other fields (NO request_uuid)
        )
```

**V2 Model (dev/demo)** - Uses DevDemoSQLModel registry:
```python
# src/rhizome/models/billing_event/as_of_merchant_v2.py
from ..metadata_registry import DevDemoSQLModel

class AsOfMerchantV2(AsOfMerchant, DevDemoSQLModel, table=True):
    """V2 for dev/demo - includes request_uuid field."""
    __tablename__ = "as_of_merchant"  # Same name, different registry!

    # Additional field in V2
    request_uuid: str | None = Field(default=None, max_length=26)

    def sanitize(self) -> AsOfMerchantV2:
        return AsOfMerchantV2(
            uuid=sanitize_uuid_field(self.uuid, 26),
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            # ... other fields
        )
```

#### 3. Environment-Specific Model Usage

**na_prod environment** imports and uses V1:
```python
# src/rhizome/environments/na_prod/billing_event.py
from rhizome.models.billing_event.as_of_merchant_v1 import AsOfMerchantV1

models: dict[BillingEventTable, tuple[type[RhizomeModel], type[Emplacement]]] = {
    BillingEventTable.as_of_merchant: (AsOfMerchantV1, AsOfMerchantNaProd),
    # ...
}
```

**dev/demo environments** import and use V2:
```python
# src/rhizome/environments/dev/billing_event.py
from rhizome.models.billing_event.as_of_merchant_v2 import AsOfMerchantV2

models: dict[BillingEventTable, tuple[type[RhizomeModel], type[Emplacement]]] = {
    BillingEventTable.as_of_merchant: (AsOfMerchantV2, AsOfMerchantDemo),
    # ...
}
```

### Key Benefits

1. **No SQLAlchemy Conflicts**: Separate registries allow same `__tablename__` in different models
2. **Type Safety**: Each environment gets correct model type with appropriate fields
3. **Static Analysis**: IDEs and mypy can provide accurate autocomplete and type checking
4. **SQL Compatibility**: Only fields that exist in each environment are included in queries

### User Experience

```python
# In na_prod environment - V1 model returned
na_merchant = na_env.select_first(select(AsOfMerchantV1).where(...))
# na_merchant.request_uuid  # ← Field doesn't exist (type safe!)

# In dev environment - V2 model returned
dev_merchant = dev_env.select_first(select(AsOfMerchantV2).where(...))
dev_merchant.request_uuid  # ← Field exists and accessible
```

### When to Use This Pattern

Apply environment-scoped versioning when:
- **Schema differences exist** across environments for the same logical table
- **SQL errors occur** due to missing columns in certain environments
- **You need type safety** to prevent accessing non-existent fields
- **All environments can't be updated simultaneously** (progressive rollouts)

### Implementation Checklist

1. ✅ Create `metadata_registry.py` with separate registries
2. ✅ Update base model to exclude environment-specific fields
3. ✅ Create V1 model inheriting from `NaProdSQLModel`
4. ✅ Create V2 model inheriting from `DevDemoSQLModel` with additional fields
5. ✅ Update environment imports to use appropriate version
6. ✅ Remove V1/V2 imports from models `__init__.py` to avoid conflicts
7. ✅ Test that all environments load without table conflicts
8. ✅ Verify `rhizome sync report` works across all environments

This pattern ensures that data flows work seamlessly when schemas match across environments, but provides compile-time type errors when attempting to access fields that don't exist in specific environments.
