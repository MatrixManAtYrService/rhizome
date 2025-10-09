"""Expected data for processing_note table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.processing_note_v1 import ProcessingNoteV1


class ProcessingNoteDemo(Emplacement[ProcessingNoteV1]):
    """Expected data for ProcessingNote in demo environment."""

    @classmethod
    def get_expected(cls) -> ProcessingNoteV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_processing_note.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ProcessingNoteV1.model_validate(data)
