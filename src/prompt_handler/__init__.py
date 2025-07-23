from .loader import load_prompt  # noqa: F401  # импорт для публичного API
from .renderer import render_prompt as prepare_prompt  # noqa: F401

__all__ = [
    "load_prompt",
    "prepare_prompt",
]

__version__ = "0.0.1dev0" 