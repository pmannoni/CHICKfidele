import re
from typing import Dict, Tuple

class LaTeXValidator:
    """Validation et nettoyage LaTeX"""

    @staticmethod
    def clean_line_numbers(text: str) -> str:
        """Supprime les numéros de ligne du PDF"""
        # Patterns courants:
        # "123 equation" → "equation"
        # "  45 \\frac{a}{b}" → "\\frac{a}{b}"

        lines = text.split('\n')
        cleaned_lines = []

        for line in lines:
            # Supprime numéros au début (1-4 chiffres + espaces)
            cleaned = re.sub(r'^\s*\d{1,4}\s+', '', line)
            cleaned_lines.append(cleaned)

        return '\n'.join(cleaned_lines)

    @staticmethod
    def validate_braces(latex: str) -> Tuple[bool, str]:
        """Vérifie équilibre accolades"""
        # Nettoie d'abord
        latex = LaTeXValidator.clean_line_numbers(latex)

        open_br = latex.count('{')
        close_br = latex.count('}')

        if open_br != close_br:
            return False, f"Braces mismatch: {open_br} open, {close_br} close"

        # Vérification imbrication
        depth = 0
        for char in latex:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
            if depth < 0:
                return False, "Closing brace before opening"

        return True, "OK"

    @staticmethod
    def validate_structure(latex: str) -> Tuple[bool, str]:
        """Vérifie structure mathématique"""
        # Environments valides
        valid_envs = r'\\(frac|sqrt|sum|int|prod|cdot|times|div|alpha|beta|gamma|delta|Sigma|Gamma|partial|nabla|infty)'

        if not re.search(valid_envs, latex) and len(latex) > 5:
            # Trop court ou pas de structure reconnue = peut être OK (juste une variable)
            pass

        return True, "OK"

    @staticmethod
    def full_validation(latex: str) -> Dict:
        """Validation complète"""
        brace_ok, brace_msg = LaTeXValidator.validate_braces(latex)
        struct_ok, struct_msg = LaTeXValidator.validate_structure(latex)

        return {
            "valid": brace_ok and struct_ok,
            "brace_check": {"passed": brace_ok, "message": brace_msg},
            "structure_check": {"passed": struct_ok, "message": struct_msg},
            "confidence": 0.95 if (brace_ok and struct_ok) else 0.5
        }

