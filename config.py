from pathlib import Path
from typing import Literal

class Config:
    """Configuration centralisée pour la conversion"""

    # Répertoires
    OUTPUT_BASE = Path("Publication_convertie")
    EQUATIONS_DIR = OUTPUT_BASE / "equations"
    MATHML_DIR = OUTPUT_BASE / "mathml"
    FIGURES_DIR = OUTPUT_BASE / "figures"
    FIGURE_SEMANTICS_DIR = OUTPUT_BASE / "figure_semantics"

    # Nougat config
    NOUGAT_MODEL = "0.1.0-small"
    NOUGAT_BATCH_SIZE = 16

    # Validation
    MIN_LATEX_CONFIDENCE = 0.75
    VALIDATE_BRACES = True
    VALIDATE_COMMANDS = True

    # Logging
    LOG_FILE = OUTPUT_BASE / "conversion.log"

    @classmethod
    def setup(cls):
        """Crée structure répertoires"""
        cls.EQUATIONS_DIR.mkdir(parents=True, exist_ok=True)
        cls.MATHML_DIR.mkdir(parents=True, exist_ok=True)
        cls.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        cls.FIGURE_SEMANTICS_DIR.mkdir(parents=True, exist_ok=True)
        cls.OUTPUT_BASE.mkdir(parents=True, exist_ok=True)

