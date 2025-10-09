"""
SQLModel definition for the processing_note_mutation table, version 1.

This module provides the V1 implementation of the ProcessingNoteMutation model.
"""

from __future__ import annotations

from .processing_note_mutation import ProcessingNoteMutation


class ProcessingNoteMutationV1(ProcessingNoteMutation, table=True):
    """
    Version 1 of the ProcessingNoteMutation model.

    Currently a name-only inheritance from the base ProcessingNoteMutation class.
    """

    __tablename__ = "processing_note_mutation"  # type: ignore
