# Exploration Scripts

This directory contains temporary exploration scripts used to understand the Clover infrastructure, API patterns, and database structures.

## Purpose

These scripts follow the exploration workflow described in `agent_primers/exploration.md`:

1. **Explore**: Query and analyze the target system
2. **Analysis**: Summarize findings and identify patterns
3. **Implementation**: Apply discoveries to actual code

## Usage

Exploration scripts are **temporary** and serve as examples for:
- Understanding how to query databases via Rhizome
- Learning how to interact with HTTP APIs via Stolon
- Discovering data patterns and field values
- Testing API endpoints and understanding responses

## Important Notes

- These scripts **require external infrastructure** (VPN access, authentication, etc.)
- They are **not run as part of the test suite** (pytest ignores this directory)
- They serve as **reference examples** for writing new exploration scripts
- Once insights are extracted, they may be kept as examples or removed

## Categories

- **`explore_*.py`**: Database queries to understand data patterns (Rhizome)
- **`test_*.py`**: API endpoint testing scripts (Stolon)
- **`find_*.py`**: Scripts to locate specific data or patterns
- **`check_*.py`**: Validation scripts for specific behaviors
- **`cleanup_*.py`**: Scripts to clean up test data

## See Also

- `agent_primers/exploration.md` - Full exploration workflow documentation
- `agent_primers/rhizome/` - Rhizome-specific documentation
- `agent_primers/stolon/` - Stolon-specific documentation
