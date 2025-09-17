"""Sync status reporting functionality."""

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from rhizome.environments.environment_list import RhizomeEnvironment, environment_type
from rhizome.models.table_list import BillingBookkeeperTable, BillingEventTable, BillingTable


class SyncStatus(StrEnum):
    """Status levels for sync report."""

    SCHEMA_ONLY = "📄 Schema Only"
    SCHEMA_MODEL = "📄📦 Schema + Model"
    SCHEMA_MODEL_EMPLACEMENT = "📄📦🎯 Schema + Model + Emplacement"
    COMPLETE = "✅ Complete"
    MISSING = "❌ Missing"


@dataclass
class TableSyncStatus:
    """Status of a single table's synchronization."""

    environment: str
    table: str
    has_schema: bool
    has_model: bool
    has_emplacement: bool
    has_data: bool

    @property
    def status(self) -> SyncStatus:
        """Determine the sync status based on available components."""
        if not self.has_schema:
            return SyncStatus.MISSING

        if self.has_data and self.has_emplacement and self.has_model:
            return SyncStatus.COMPLETE
        elif self.has_emplacement and self.has_model:
            return SyncStatus.SCHEMA_MODEL_EMPLACEMENT
        elif self.has_model:
            return SyncStatus.SCHEMA_MODEL
        else:
            return SyncStatus.SCHEMA_ONLY

    @property
    def status_emoji(self) -> str:
        """Get a simple emoji for the status."""
        if self.status == SyncStatus.COMPLETE:
            return "✅"
        elif self.status == SyncStatus.SCHEMA_MODEL_EMPLACEMENT:
            return "⚠️"
        elif self.status == SyncStatus.SCHEMA_MODEL:
            return "🔶"
        elif self.status == SyncStatus.SCHEMA_ONLY:
            return "📄"
        else:
            return "❌"


def get_database_short_name(environment_name: str) -> str:
    """Extract database short name from environment name.

    Examples:
        dev_billing_bookkeeper -> billing_bookkeeper
        na_prod_billing_event -> billing_event
        na_prod_billing -> billing
    """
    # Handle underscore-separated environment names (from enum strings)
    if "_" in environment_name:
        # Remove environment prefixes (dev_, demo_, na_prod_)
        if environment_name.startswith("na_prod_"):
            return environment_name[8:]  # Remove "na_prod_"
        elif environment_name.startswith("dev_") or environment_name.startswith("demo_"):
            return environment_name[environment_name.index("_") + 1:]  # Remove first part
        else:
            return environment_name
    else:
        # Handle PascalCase environment names (from class names)
        # Remove common prefixes
        name = environment_name.replace("NorthAmerica", "").replace("Dev", "").replace("Demo", "")

        # Convert from PascalCase to snake_case
        result: list[str] = []
        for i, char in enumerate(name):
            if i > 0 and char.isupper():
                result.append("_")
            result.append(char.lower())
        return "".join(result)


def check_table_sync_status(
    env_enum: RhizomeEnvironment,
    env_name: str,
    table_name: str,
) -> TableSyncStatus:
    """Check the synchronization status for a single table."""
    # Get environment folder name
    env_str = str(env_enum)
    if env_str.startswith("na_prod_"):
        env_folder = "na_prod"
    else:
        env_folder = env_str.split("_")[0]

    # Get database short name
    db_short_name = get_database_short_name(env_name)

    # Build file paths
    base_path = Path(f"src/rhizome/environments/{env_folder}/expected_data")
    schema_path = base_path / f"{db_short_name}_{table_name}.sql"
    data_path = base_path / f"{db_short_name}_{table_name}.json"
    emplacement_path = base_path / f"{db_short_name}_{table_name}.py"

    # Check for model file
    # Database names use underscore in path (e.g., billing_bookkeeper)
    model_base_path = Path(f"src/rhizome/models/{db_short_name}")
    model_v1_path = model_base_path / f"{table_name}_v1.py"
    model_base_file = model_base_path / f"{table_name}.py"

    # Check what exists
    has_schema = schema_path.exists()
    has_data = data_path.exists()
    has_emplacement = emplacement_path.exists()
    has_model = model_v1_path.exists() or model_base_file.exists()

    return TableSyncStatus(
        environment=env_name,
        table=table_name,
        has_schema=has_schema,
        has_model=has_model,
        has_emplacement=has_emplacement,
        has_data=has_data,
    )


def _get_table_enum_for_environment(env_enum: RhizomeEnvironment) -> list[StrEnum] | None:
    """Get the table enum list for a given environment."""
    env_str = str(env_enum)

    if "billing_bookkeeper" in env_str:
        return list(BillingBookkeeperTable)
    elif "billing_event" in env_str:
        return list(BillingEventTable)
    elif "billing" in env_str and "bookkeeper" not in env_str and "event" not in env_str:
        return list(BillingTable)
    else:
        return None


def sync_report(env: RhizomeEnvironment | None = None) -> None:
    """Generate a report of sync status for all environment/table pairs."""
    console = Console()

    # Collect all statuses
    all_statuses: list[TableSyncStatus] = []

    environments_to_check = environment_type.items()
    if env:
        environments_to_check = [(env, environment_type[env])]

    for env_enum, env_class in environments_to_check:
        try:
            # Get table list without instantiating the environment
            # Look up the table enum directly
            table_list = _get_table_enum_for_environment(env_enum)
            if not table_list:
                console.print(f"[yellow]Warning: No table enum found for {env_enum}[/yellow]")
                continue

            # Get all tables for this environment
            for table_name in table_list:
                status = check_table_sync_status(env_enum, str(env_enum), str(table_name))
                all_statuses.append(status)
        except Exception as e:
            console.print(f"[red]Error checking {env_enum}: {e}[/red]")
            continue

    # Group statuses by category
    schema_only = [s for s in all_statuses if s.status == SyncStatus.SCHEMA_ONLY]
    schema_model = [s for s in all_statuses if s.status == SyncStatus.SCHEMA_MODEL]
    schema_model_emplacement = [s for s in all_statuses if s.status == SyncStatus.SCHEMA_MODEL_EMPLACEMENT]
    complete = [s for s in all_statuses if s.status == SyncStatus.COMPLETE]
    missing = [s for s in all_statuses if s.status == SyncStatus.MISSING]

    # Print summary
    console.print("\n[bold]Sync Status Summary[/bold]")
    console.print(f"Total environment/table pairs: {len(all_statuses)}")
    console.print(f"  ✅ Complete: {len(complete)}")
    console.print(f"  ⚠️  Schema + Model + Emplacement (no data): {len(schema_model_emplacement)}")
    console.print(f"  🔶 Schema + Model (no emplacement/data): {len(schema_model)}")
    console.print(f"  📄 Schema Only: {len(schema_only)}")
    console.print(f"  ❌ Missing: {len(missing)}")

    # Create detailed table
    if all_statuses:
        console.print("\n[bold]Detailed Status[/bold]")
        table = Table(title="Environment/Table Sync Status")
        table.add_column("Environment", style="cyan")
        table.add_column("Table", style="magenta")
        table.add_column("Schema", style="green")
        table.add_column("Model", style="blue")
        table.add_column("Emplacement", style="yellow")
        table.add_column("Data", style="green")
        table.add_column("Status", style="bold")

        # Sort by status for better readability
        all_statuses.sort(key=lambda x: (x.status, x.environment, x.table))

        for status in all_statuses:
            table.add_row(
                status.environment,
                status.table,
                "✓" if status.has_schema else "✗",
                "✓" if status.has_model else "✗",
                "✓" if status.has_emplacement else "✗",
                "✓" if status.has_data else "✗",
                status.status_emoji,
            )

        console.print(table)

    # Print recommendations
    if schema_only:
        console.print("\n[yellow]📄 Schema Only (needs model generation):[/yellow]")
        for status in schema_only[:5]:  # Show first 5
            console.print(f"  - {status.environment}/{status.table}")
        if len(schema_only) > 5:
            console.print(f"  ... and {len(schema_only) - 5} more")

    if schema_model:
        console.print("\n[yellow]🔶 Schema + Model (needs emplacement):[/yellow]")
        for status in schema_model[:5]:
            console.print(f"  - {status.environment}/{status.table}")
        if len(schema_model) > 5:
            console.print(f"  ... and {len(schema_model) - 5} more")

    if schema_model_emplacement:
        console.print("\n[yellow]⚠️  Ready for data sync:[/yellow]")
        for status in schema_model_emplacement[:5]:
            console.print(f"  - {status.environment}/{status.table}")
        if len(schema_model_emplacement) > 5:
            console.print(f"  ... and {len(schema_model_emplacement) - 5} more")
        console.print("\n[green]Run 'rhizome sync data' to fetch data for these tables[/green]")

    if missing:
        console.print("\n[red]❌ Missing everything:[/red]")
        for status in missing[:5]:
            console.print(f"  - {status.environment}/{status.table}")
        if len(missing) > 5:
            console.print(f"  ... and {len(missing) - 5} more")