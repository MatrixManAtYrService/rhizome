# Rhizome Sync Commands

This document describes the usage of the `rhizome sync` commands.

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

The `rhizome sync schema` command is used to fetch the `CREATE TABLE` statement for each table in a given environment and save it as a `.sql` file. This is useful for keeping a local snapshot of the table schemas in each environment.

### Usage

```bash
rhizome sync schema [OPTIONS]
```

### Options

-   `--env TEXT`: The environment to sync. If not provided, all environments are synced. The available environments are the same as for `rhizome sync data`.
-   `--verbose`: Show the full stack trace on error.

### Example

To sync the schema for the `dev_billing_bookkeeper` environment:

```bash
rhizome sync schema --env dev_billing_bookkeeper
```

This will create a file named `{table_name}.sql` for each table in the `dev_billing_bookkeeper` environment inside the `src/rhizome/environments/dev/expected_data/` directory.
