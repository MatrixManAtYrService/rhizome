"""Expected data for processing_note_mutation table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.processing_note_mutation_v1 import ProcessingNoteMutationV1


class ProcessingNoteMutationDemo(Emplacement[ProcessingNoteMutationV1]):
    """Expected data for ProcessingNoteMutation in demo environment."""

    @classmethod
    def get_expected(cls) -> ProcessingNoteMutationV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_processing_note_mutation.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return ProcessingNoteMutationV1.model_validate(data)
