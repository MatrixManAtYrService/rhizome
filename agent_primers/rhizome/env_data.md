# Rhizome Environment-Specific Data Architecture

This document describes the new environment-specific data architecture that replaces the centralized `mocked_table_data.py` approach.

## Problem Statement

Previously, test data was centralized in `tests/mocked_table_data.py`, which:
- Mixed test data for different environments in one place
- Used complex parameterization to handle environment/table combinations
- Made it difficult to manage environment-specific data variations
- Required maintaining separate mock and expected data structures

## New Architecture

### Core Components

#### 1. **StrEnum Table Lists**
Each database now has a `StrEnum` defining its tables:

```python
# src/rhizome/models/billing_bookkeeper/table_list.py
class BillingBookkeeperTable(StrEnum):
    fee_summary = auto()
    settlement = auto()
```

#### 2. **Generic Emplacement Classes**
Environment-specific data is defined using generic `Emplacement` classes:

```python
# src/rhizome/environments/dev/expected_data/billing_bookkeeper_fee_summary.py
class FeeSummaryDev(Emplacement[FeeSummaryV1]):
    @classmethod
    def get_expected(cls) -> FeeSummaryV1:
        return FeeSummaryV1(
            id=30,
            uuid="HashDwRegsuuYDX9RnVzfZport",
            # ... environment-specific test data
        )
```

#### 3. **Environment Table Mapping**
Each environment declares its table/model/data combinations via the `situate_table()` method:

```python
# src/rhizome/environments/dev/billing_bookkeeper.py
class DevBillingBookkeeper(Environment):
    def tables(self) -> list[StrEnum]:
        return list(BillingBookkeeperTable)

    def situate_table(self, table_name: StrEnum) -> tuple[type[RhizomeModel] | None, type[Emplacement[Any]] | None]:
        """Map table names to their versioned models and emplacements."""
        match table_name:
            case BillingBookkeeperTable.fee_summary:
                return (FeeSummaryV1, FeeSummaryDev)
            case BillingBookkeeperTable.settlement:
                return (SettlementV1, None)  # No test data yet
            case _:
                return (None, None)  # Unsupported table
```

The method returns a tuple of `(model_class, emplacement_class)` where either can be `None` if not configured for that table.

#### 4. **Runtime Table Situation**
The base `Environment` class automatically populates `table_situation` on initialization:

```python
# In Environment.__init__()
self.table_situation = {
    table: self.situate_table(table) for table in self.tables()
}
```

This creates a dictionary mapping each table to its `(model_class, emplacement_class)` tuple, used internally by the `get_versioned()` method.

#### 5. **The `get_versioned()` Method**
The `Environment` class provides a `get_versioned()` method to retrieve the environment-specific versioned model:

```python
# In your code
from rhizome.models.billing_bookkeeper.fee_summary import FeeSummary as FeeSummaryModel
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper

db = DevBillingBookkeeper(client)
FeeSummary = db.get_versioned(FeeSummaryModel)

# FeeSummary is now FeeSummaryV1 (or whatever version dev uses)
# The type checker knows it's compatible with FeeSummaryModel
fees = db.select_all(select(FeeSummary).where(FeeSummary.uuid == target_uuid))
```

The method uses generic TypeVars to provide type safety: you pass in the base class and get back a versioned class that's type-compatible with the base. This allows writing version-agnostic code that works across environments with different schema versions.

See `table_versioning.md` for detailed usage patterns and examples.

## Benefits

1. **Environment Isolation**: Each environment's data is in its own directory structure
2. **Type Safety**: Generic `Emplacement` classes ensure data matches model types; `get_versioned()` provides type-safe model retrieval
3. **Version Agnostic**: Write code once that works across environments with different schema versions
4. **Declarative**: Clear mapping of what tables/versions each environment uses via `situate_table()`
5. **Testable**: Easy to get expected data for any environment/table combination
6. **Maintainable**: Environment-specific changes don't affect other environments

## Directory Structure

```
src/rhizome/environments/
├── dev/
│   └── expected_data/
│       ├── billing_bookkeeper_fee_summary.py    # FeeSummaryDev
│       ├── billing_bookkeeper_settlement.py     # SettlementDev (todo)
│       ├── billing_event_app_metered_event.py   # AppMeteredEventDev (todo)
│       └── billing_event_app_subscription.py    # AppSubscriptionDev (todo)
├── demo/
│   └── expected_data/
│       ├── billing_bookkeeper_fee_summary.py    # FeeSummaryDemo (todo)
│       └── ...                                  # (todo)
└── na_prod/
    └── expected_data/
        ├── billing_bookkeeper_fee_summary.py    # FeeSummaryNaProd (todo)
        ├── billing_event_app_metered_event.py   # AppMeteredEventNaProd (todo)
        ├── billing_stage_charge.py              # StageChargeNaProd (todo)
        └── ...                                  # (todo)
```

## Implementation Status

### ✅ Completed
- [x] `RhizomeModel` base class (renamed from `SanitizableModel`)
- [x] Generic `Emplacement[T]` abstract base class
- [x] `StrEnum` table lists for all databases:
  - [x] `BillingBookkeeperTable`
  - [x] `BillingEventTable`
  - [x] `BillingTable`
  - [x] `MetaTable`
- [x] `Environment` base class with `tables()` and `situate_table()` methods
- [x] `get_versioned()` method for type-safe version-agnostic model retrieval
- [x] Complete `DevBillingBookkeeper` implementation with `FeeSummaryDev`

### 🚧 In Progress
- [ ] Complete expected_data directory structure for all environments
- [ ] Update all environment classes to use new architecture

### 📋 Todo - Expected Data Classes Needed

**Dev Environment:**
- [ ] `FeeSummaryDev` (✅ completed)
- [ ] `SettlementDev`
- [ ] `AppMeteredEventDev`
- [ ] `AppSubscriptionEventDev`

**Demo Environment:**
- [ ] `FeeSummaryDemo`
- [ ] `SettlementDemo`
- [ ] `AppMeteredEventDemo`
- [ ] `AppSubscriptionEventDemo`

**NA Prod Environment:**
- [ ] `FeeSummaryNaProd`
- [ ] `SettlementNaProd`
- [ ] `AppMeteredEventNaProd`
- [ ] `AppSubscriptionEventNaProd`
- [ ] `StageChargeNaProd`

### 📋 Todo - Environment Updates
- [ ] Update all environment classes to implement `tables()` and `situate_table()`
- [ ] Update `test_environment_access.py` to use new architecture
- [ ] Remove `tests/mocked_table_data.py`

## Implementation Guidelines

### For Missing Expected Data

When an environment/table combination doesn't have expected data yet, use this pattern:

```python
class TableNameEnvironment(Emplacement[ModelNameV1]):
    @classmethod
    def get_expected(cls) -> ModelNameV1:
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
```

### Adding New Expected Data

1. **Find real data**: Query the actual environment to find a representative record
2. **Create emplacement class**: Add to appropriate `expected_data/{database}_{table}.py`
3. **Update environment mapping**: Add to the `models` dict in the environment class
4. **Test**: Ensure the expected data matches the model structure

### Naming Conventions

- **Files**: `{database}_{table}.py` (e.g., `billing_bookkeeper_fee_summary.py`)
- **Classes**: `{TableName}{Environment}` (e.g., `FeeSummaryDev`, `AppMeteredEventNaProd`)
- **Data should be realistic**: Use actual data from the environment (sanitized for privacy)

## Usage in Tests

The new architecture enables clean test parameterization:

```python
# Test using version-agnostic code via get_versioned()
from rhizome.models.billing_bookkeeper.fee_summary import FeeSummary as FeeSummaryModel

def test_fee_summary_retrieval(client):
    db = DevBillingBookkeeper(client)
    FeeSummary = db.get_versioned(FeeSummaryModel)

    # Query using versioned model - works regardless of V1/V2/etc
    fees = db.select_all(select(FeeSummary).where(FeeSummary.uuid == target_uuid))
    assert len(fees) > 0

# Test using expected data from emplacements
for table_name, (model_class, emplacement_class) in env.table_situation.items():
    if emplacement_class is not None:
        expected_data = emplacement_class.get_expected()
        actual_data = query_database(model_class, table_name)
        emplacement_class().assert_match(actual_data, expected_data)
```

This provides automatic coverage of all table/environment combinations with type-safe expected data, while `get_versioned()` enables version-agnostic test logic.