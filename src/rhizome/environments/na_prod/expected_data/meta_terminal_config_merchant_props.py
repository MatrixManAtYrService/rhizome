"""
Expected data for terminal_config_merchant_props table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.terminal_config_merchant_props_v1 import TerminalConfigMerchantPropsV1


class TerminalConfigMerchantPropsNaProd(Emplacement[TerminalConfigMerchantPropsV1]):
    """Expected data for TerminalConfigMerchantProps in na_prod environment."""

    @classmethod
    def get_expected(cls) -> TerminalConfigMerchantPropsV1:
        """Get expected terminal_config_merchant_props data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_terminal_config_merchant_props.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return TerminalConfigMerchantPropsV1.model_validate(data)
