"""Utility functions for test failure messages and debugging."""

from rhizome.environments.environment_list import RhizomeEnvironment


def generate_sync_fix_commands(emplacement_module_path: str, table_name: str = "") -> str:
    """
    Generate suggested fix commands for test failures.

    Args:
        emplacement_module_path: Module path of the emplacement class
                                (e.g., "rhizome.environments.dev.expected_data.billing_bookkeeper_fee_summary")
        table_name: Optional specific table name if known

    Returns:
        Formatted string with suggested fix commands
    """
    # Parse the module path to extract environment and database info
    parts = emplacement_module_path.split(".")

    if len(parts) < 5 or parts[0] != "rhizome" or parts[1] != "environments":
        # Fallback for unknown module structure
        return (
            "\n\n🔧 SUGGESTED FIX COMMANDS:\n"
            "Run schema sync followed by data sync:\n"
            "   rhizome sync schema\n"
            "   rhizome sync data\n"
        )

    env_folder = parts[2]  # e.g., "dev", "demo", "na_prod"
    db_and_table = parts[4]  # e.g., "billing_bookkeeper_fee_summary"

    # Extract table name from the module if not provided
    if not table_name and "_" in db_and_table:
        # Find the table part by looking at known database prefixes
        db_prefixes = ["billing_bookkeeper", "billing_event", "billing"]
        for prefix in sorted(db_prefixes, key=len, reverse=True):  # Longest first
            if db_and_table.startswith(prefix + "_"):
                table_name = db_and_table[len(prefix) + 1:]
                break

    # Map environment folder to CLI environment names using the actual enum
    cli_env = _infer_cli_environment(env_folder, db_and_table)

    # Generate the fix commands
    fix_message = (
        f"\n\n🔧 SUGGESTED FIX COMMANDS:\n"
        f"To resolve this test failure, run these commands in order:\n\n"
        f"1. First sync schema (run ALL schema syncs before data syncs):\n"
        f"   rhizome sync schema --env {cli_env}"
    )

    if table_name:
        fix_message += f" --table {table_name}"

    fix_message += (
        f"\n\n2. Then sync data:\n"
        f"   rhizome sync data --env {cli_env}"
    )

    if table_name:
        fix_message += f" --table {table_name}"

    fix_message += (
        f"\n\n💡 TIP: If this is a schema evolution issue, the schema sync will update "
        f"the model definitions. If this is a data volatility issue, the data sync "
        f"will update the expected values.\n"
        f"💡 IMPORTANT: Always run schema syncs before data syncs to ensure proper ordering."
    )

    return fix_message


def _infer_cli_environment(env_folder: str, db_and_table: str) -> str:
    """
    Infer the CLI environment name from folder and database info.

    Uses the actual RhizomeEnvironment enum to ensure we stay in sync.
    """
    # Extract database type from db_and_table
    db_type = "billing"  # default
    if db_and_table.startswith("billing_bookkeeper"):
        db_type = "billing_bookkeeper"
    elif db_and_table.startswith("billing_event"):
        db_type = "billing_event"
    elif db_and_table.startswith("billing"):
        db_type = "billing"

    # Construct the expected environment name and validate it exists
    if env_folder == "na_prod":
        cli_env_name = f"na_prod_{db_type}"
    else:
        cli_env_name = f"{env_folder}_{db_type}"

    # Verify this environment exists in our enum
    try:
        RhizomeEnvironment(cli_env_name)
        return cli_env_name
    except ValueError:
        # Fallback - try to find a matching environment
        for env in RhizomeEnvironment:
            if env.value.startswith(env_folder) and db_type in env.value:
                return env.value

        # Final fallback
        return f"{env_folder}_{db_type}"


def enhance_assertion_error_with_fix_commands(
    original_error: AssertionError,
    emplacement_module_path: str,
    table_name: str = ""
) -> AssertionError:
    """
    Enhance an AssertionError with suggested fix commands.

    Args:
        original_error: The original AssertionError that was raised
        emplacement_module_path: Module path of the emplacement class
        table_name: Optional specific table name if known

    Returns:
        New AssertionError with enhanced message including fix commands
    """
    original_message = str(original_error)
    fix_commands = generate_sync_fix_commands(emplacement_module_path, table_name)
    enhanced_message = f"{original_message}{fix_commands}"

    return AssertionError(enhanced_message)