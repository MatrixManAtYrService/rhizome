"""
Sanitization helpers for rhizome database models.

This module provides utilities for sanitizing database records by replacing
sensitive information with deterministic hashes.
"""

import hashlib
from typing import Any

import base58


def hash_uuid_to_base58(uuid_str: str, target_length: int) -> str:
    """
    Convert a UUID string to a deterministic base58 hash of the specified length.
    
    The output will be prefixed with "Hash" to clearly indicate it's not a real UUID.
    
    Args:
        uuid_str: The UUID string to hash
        target_length: The target length for the output string
        
    Returns:
        str: A base58-encoded hash prefixed with "Hash" and truncated/padded to target_length
    """
    # Create SHA256 hash of the UUID
    hash_bytes = hashlib.sha256(uuid_str.encode('utf-8')).digest()
    
    # Encode to base58
    base58_hash = base58.b58encode(hash_bytes).decode('ascii')
    
    # Prefix with "Hash" to make it clear this is not a real UUID
    prefix = "Hash"
    available_length = target_length - len(prefix)
    
    if available_length <= 0:
        # If target length is too small for prefix, just return truncated hash
        return base58_hash[:target_length]
    
    # Truncate or pad the hash portion to fit remaining space
    if len(base58_hash) >= available_length:
        hash_portion = base58_hash[:available_length]
    else:
        # If shorter, pad with repeated pattern
        padding_needed = available_length - len(base58_hash)
        padding = (base58_hash * ((padding_needed // len(base58_hash)) + 1))[:padding_needed]
        hash_portion = base58_hash + padding
    
    return prefix + hash_portion


def sanitize_uuid_field(value: Any, field_length: int) -> Any:
    """
    Sanitize a UUID field, handling None values.
    
    Args:
        value: The value to sanitize (str or None)
        field_length: The expected length of the field
        
    Returns:
        The sanitized value or None if input was None
    """
    if value is None:
        return None
    return hash_uuid_to_base58(str(value), field_length)