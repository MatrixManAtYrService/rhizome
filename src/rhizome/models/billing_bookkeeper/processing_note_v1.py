"""
SQLModel definition for the processing_note table, version 1.

This module provides the V1 implementation of the ProcessingNote model.
"""

from __future__ import annotations

from .processing_note import ProcessingNote


class ProcessingNoteV1(ProcessingNote, table=True):
    """
    Version 1 of the ProcessingNote model.

    Currently a name-only inheritance from the base ProcessingNote class.
    """

    __tablename__ = "processing_note"  # type: ignore
