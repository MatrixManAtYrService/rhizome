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
           raise NotImplementedError(
               f"Expected data for {cls.__name__} not yet implemented. "
               f"Please add test data based on real data from this environment."
           )
   ```

2. **Update environment files**:
   - Add imports for V1 models and emplacement classes
   - Add entries to `models` dictionary: `BillingEventTable.{table}: ({TableName}V1, {TableName}{Environment})`

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
