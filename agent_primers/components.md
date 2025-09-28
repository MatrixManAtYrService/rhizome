# Trifolium Component Architecture

This document provides an overview of the Trifolium project structure and guides agents on which component-specific primers to consult.

## Project Overview

**Trifolium** is a unified data access system for Clover's infrastructure, using a botanical metaphor where two complementary systems work together:

- **Rhizome** (Underground/Database Layer) - Database access via port-forwarding, kubectl, CloudSQL
- **Stolon** (Aboveground/API Layer) - HTTP API access via authentication tokens

Both systems share common configuration and utilities through the **trifolium** package.

## Component Selection Guide

### For Database-Related Tasks

If working with databases, table models, SQL queries, port-forwarding, or kubectl operations:
- **Consult**: `agent_primers/rhizome/` directory
- **Key areas**: Database connections, table versioning, environment management, testing

### For API-Related Tasks

If working with HTTP APIs, authentication tokens, REST endpoints, or browser integration:
- **Consult**: `agent_primers/stolon/` directory
- **Key areas**: Session token capture, API authentication, browser extensions

### For Cross-Component Tasks

If working with shared functionality like configuration, general architecture, or project-wide concerns:
- **Start here** with this components.md
- **Then check both** component directories for relevant details

## Shared Configuration (XDG Standards)

Both Rhizome and Stolon use the **trifolium** package for unified configuration management following XDG Base Directory standards:

### Configuration Locations
- **Config Directory**: `~/.config/trifolium/` - User preferences and settings
  - `trifolium.json` - Main configuration file with user preferences
- **State Directory**: `~/.local/state/trifolium/` - Runtime data and temporary files
  - `rhizome_port` - Current Rhizome server port
  - Other runtime state files

### Configuration Model
```python
from trifolium.config import Home, TrifoliumConfig, InternalTokenPreference

# Load configuration
home = Home()
config = home.load_config()

# Access user preferences
if config.internal_token_preference == InternalTokenPreference.AUTO:
    # Proceed with automatic token capture
```

### Key Configuration Features
- **User Preferences**: Stored persistently across sessions
- **Sandboxed Testing**: Support for isolated test configurations
- **XDG Compliance**: Follows Linux/Unix standards for config file locations
- **Type Safety**: Pydantic models ensure configuration validation

## Architecture Benefits

1. **Separation of Concerns**: Database complexity (Rhizome) vs API complexity (Stolon)
2. **Tribal Knowledge Capture**: Infrastructure complexity hidden behind simple interfaces
3. **Environment Abstraction**: Same code works across dev, demo, production
4. **Unified Configuration**: Consistent settings management across both components
5. **Type Safety**: Strong typing throughout with automatic sanitization

## Development Workflow

### For Rhizome Development
1. Check `agent_primers/rhizome/` for database-specific guidance
2. Use `rhizome serve` for local development server
3. Configure environments and table models as needed

### For Stolon Development
1. Check `agent_primers/stolon/` for API-specific guidance
2. Use `stolon serve` for local development server
3. Set up browser extensions for token capture as needed

### For Integration Work
1. Review this components.md for overall architecture
2. Consult both component directories for specific requirements
3. Use shared trifolium configuration for cross-component settings

## Version Management

All three packages (rhizome, stolon, trifolium) use synchronized versioning:
- **Single Source**: `nix/version.nix` contains master version
- **Code Generation**: `nix run .#codegen` updates all package versions
- **Consistent Releases**: All components release together with same version number