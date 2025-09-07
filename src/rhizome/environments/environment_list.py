"""
Environment list for rhizome.

This module defines all environments tracked in rhizome across different
clusters and connection types.
"""

from __future__ import annotations

from enum import StrEnum, auto


class RhizomeEnvironment(StrEnum):
    """Environment identifiers for rhizome database environments."""
    
    # Development environments
    dev_billing_bookkeeper = auto()
    dev_billing_event = auto()
    
    # Demo environments  
    demo_billing_bookkeeper = auto()
    demo_billing_event = auto()
    
    # Production environments
    na_prod_billing = auto()
    na_prod_billing_bookkeeper = auto()
    na_prod_billing_event = auto()