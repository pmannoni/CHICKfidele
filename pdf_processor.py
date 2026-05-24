import re
import tempfile
from pathlib import Path
from typing import List, Dict
from loguru import logger
import subprocess
from latex_validator import LaTeXValidator

# Essaie d'importer PyPDF2 comme fallback
try:
    from PyPDF2 import PdfReader
    HAS_PYPDF2 = True
except:
    HAS_PYPDF2 = False

class PDFProcessor:
    """Pipeline d'extraction PDF"""

    def __init__(self, config):
        self.config = config
        logger.add(str(config.LOG_FILE), rotation="500 MB")
        self.validator = LaTeXValidator()

    def extract_with_nougat(self, pdf_path: str) -> str:
        """Extrait PDF avec Nougat"""
        logger.info(f"🔍 Extraction Nougat: {pdf_path}")

        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                cmd = [
                    'nougat',
                    str(pdf_path),
                    '-o', tmpdir,
                    '--batchsize', str(self.config.NOUGAT_BATCH_SIZE),
                    '--markdown'
                ]

                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

                if result.returncode != 0:
                    logger.error(f"Nougat error: {result.stderr}")
                    return self._fallback_extraction(pdf_path)

                # Récupère output.mmd
                output_files = list(Path(tmpdir).glob("*.mmd"))
                if output_files:
                    markdown = output_files[0].read_text(encoding='utf-8')
                    logger.success("✓ Nougat extraction réussie")
                    return markdown

        except subprocess.TimeoutExpired:
            logger.warning("Nougat timeout, fallback")
            return self._fallback_extraction(pdf_path)
        except Exception as e:
            logger.error(f"Nougat exception: {e}")
            return self._fallback_extraction(pdf_path)

        return None

    def _fallback_extraction(self, pdf_path: str) -> str:
        """Fallback simple: extraction texte basique"""
        logger.warning("⚠️ Utilisation fallback (extraction basique)")
        if HAS_PYPDF2:
            try:
                text = []
                with open(pdf_path, 'rb') as f:
                    reader = PdfReader(f)
                    for page_idx, page in enumerate(reader.pages, start=1):
                        text.append(f"[[PAGE:{page_idx}]]")
                        text.append(page.extract_text() or "")

                return '\n\n'.join(text)
            except Exception as e:
                logger.error(f"PyPDF2 fallback error: {e}")

        return None

    @staticmethod
    def _clean_extracted_line(line: str) -> str:
        """Nettoie les artefacts fréquents d'extraction PDF (numéros de ligne/pages)."""
        cleaned = line.strip()
        # Supprime les marqueurs de page du type "5 / 35"
        cleaned = re.sub(r'^\s*\d+\s*/\s*\d+\s*$', '', cleaned)
        # Supprime un numéro de ligne en fin de ligne (très fréquent dans ce PDF)
        cleaned = re.sub(r'\s+\d{1,4}\s*$', '', cleaned)
        # Supprime un numéro de ligne en début de ligne
        cleaned = re.sub(r'^\s*\d{1,4}\s+', '', cleaned)
        return cleaned.strip()

    @staticmethod
    def _is_equation_like_line(line: str) -> bool:
        """Heuristique robuste pour reconnaître une ligne mathématique sans balises LaTeX."""
        if not line:
            return False

        # Ignore les lignes clairement textuelles
        lower = line.lower()
        if lower.startswith(("fig.", "table", "introduction", "discussion", "methods", "references")):
            return False
        if "http://" in lower or "https://" in lower:
            return False

        # Commandes LaTeX explicites
        if re.search(r'\\(frac|sqrt|sum|int|prod|begin|end|left|right|alpha|beta|gamma|delta|lambda|mu|sigma|omega|mathcal|mathbf)', line):
            return True

        alpha_words = re.findall(r'[A-Za-z]{2,}', line)
        word_count = len(alpha_words)

        # Marqueurs math forts (Unicode math/grec stylisé, opérateurs spécialisés)
        special_math = bool(re.search(r'[≤≥≈≠×÷∑∏∫√∞ℛ𝓡≜]|[\U0001D400-\U0001D7FF]', line))
        has_equal = '=' in line or '≜' in line
        has_latex_ops = bool(re.search(r'\\(frac|sqrt|sum|int|prod|alpha|beta|gamma|delta|lambda|mu|sigma|omega|mathcal|mathbf)', line))

        # '/' est accepté uniquement si ça ressemble à une fraction/dérivée
        has_fraction_like = bool(re.search(r'\b[dD][A-Za-z0-9_]*\s*/\s*d[tT]\b', line)) or bool(re.search(r'[\U0001D400-\U0001D7FF0-9)]\s*/\s*[\U0001D400-\U0001D7FF0-9(]', line))

        if has_latex_ops:
            return True

        if special_math:
            # Écarte les phrases longues contenant juste un symbole isolé
            return word_count <= 5 or has_equal or has_fraction_like

        # Sans symboles math forts: exige une structure très explicite
        if has_equal and word_count <= 3:
            return True
        if has_fraction_like and word_count <= 4:
            return True

        return False

    @staticmethod
    def _is_prose_like_line(line: str) -> bool:
        """Détecte les lignes majoritairement textuelles pour éviter les faux positifs."""
        if not line:
            return False

        # Une ligne avec point/virgule + beaucoup de mots est rarement une équation
        words = re.findall(r'[A-Za-z]{2,}', line)
        if len(words) >= 7 and re.search(r'[\.;:]', line):
            return True

        # Forte proportion de mots et absence d'opérateurs typiques
        has_operator = bool(re.search(r'[=^_]|[≤≥≈≠×÷∑∏∫√]|\\(frac|sqrt|sum|int|prod)', line))
        if len(words) >= 10 and not has_operator:
            return True

        return False

    @staticmethod
    def _extract_context_window(lines: List[str], idx: int) -> str:
        """Construit un petit contexte local utile pour vérification manuelle."""
        start = max(0, idx - 1)
        end = min(len(lines), idx + 2)
        window = [lines[i].strip() for i in range(start, end)]
        window = [x for x in window if x and not re.match(r'^\[\[PAGE:\d+\]\]$', x)]
        return " ".join(window)[:220]

    def _extract_equation_blocks_from_plain_text(self, markdown: str, start_idx: int) -> List[Dict]:
        """Extrait des blocs mathématiques depuis du texte OCR/fallback sans délimiteurs $$."""
        equations = []
        lines = markdown.splitlines()
        current_block = []
        current_page = None
        block_page = None
        block_context = ""

        def flush_block() -> None:
            nonlocal current_block, block_page, block_context
            if not current_block:
                return

            latex = "\n".join(current_block).strip()
            latex = self.validator.clean_line_numbers(latex)
            if len(latex) >= 6:
                equations.append({
                    'id': f'eq_{start_idx + len(equations):03d}',
                    'latex': latex,
                    'source': 'fallback_heuristic',
                    'type': 'block',
                    'source_page': block_page,
                    'context': block_context
                })
            current_block = []
            block_page = None
            block_context = ""

        for idx, raw_line in enumerate(lines):
            marker = re.match(r'^\[\[PAGE:(\d+)\]\]$', raw_line.strip())
            if marker:
                current_page = int(marker.group(1))
                flush_block()
                continue

            line = self._clean_extracted_line(raw_line)

            if self._is_prose_like_line(line):
                flush_block()
                continue

            if self._is_equation_like_line(line):
                if not current_block:
                    block_page = current_page
                    block_context = self._extract_context_window(lines, idx)
                current_block.append(line)
            else:
                flush_block()

        flush_block()

        # Déduplication simple (certains blocs peuvent être répétés dans le texte extrait)
        seen = set()
        deduped = []
        for eq in equations:
            key = re.sub(r'\s+', ' ', eq['latex']).strip()
            if key and key not in seen:
                seen.add(key)
                deduped.append(eq)

        # Réindexe après déduplication
        for i, eq in enumerate(deduped, start_idx):
            eq['id'] = f'eq_{i:03d}'

        return deduped

    def _page_for_offset(self, text: str, offset: int) -> int:
        """Retourne la page la plus proche selon les marqueurs [[PAGE:n]]."""
        page = None
        for marker in re.finditer(r'\[\[PAGE:(\d+)\]\]', text):
            if marker.start() <= offset:
                page = int(marker.group(1))
            else:
                break
        return page

    def _context_for_offset(self, text: str, offset: int, width: int = 180) -> str:
        """Retourne un extrait de contexte autour d'une équation détectée par regex."""
        start = max(0, offset - width)
        end = min(len(text), offset + width)
        snippet = text[start:end]
        snippet = re.sub(r'\[\[PAGE:\d+\]\]', ' ', snippet)
        snippet = re.sub(r'\s+', ' ', snippet).strip()
        return snippet[:220]

    def extract_equations(self, markdown: str) -> List[Dict]:
        """Extrait équations du Markdown"""
        if not markdown:
            return []

        equations = []

        # Pattern 1: $$ ... $$ (display math)
        pattern_display = r'\$\$(.*?)\$\$'
        matches = list(re.finditer(pattern_display, markdown, re.DOTALL))

        # Pattern 2: $ ... $ (inline math)
        pattern_inline = r'\$([^\$]+)\$'
        inline_matches = list(re.finditer(pattern_inline, markdown))

        # Pattern 3: environnements LaTeX
        env_pattern = r'\\begin\{(equation\*?|align\*?|gather\*?)\}(.*?)\\end\{\1\}'
        env_matches = list(re.finditer(env_pattern, markdown, re.DOTALL))

        # Traite display math
        for i, match in enumerate(matches, 1):
            latex = match.group(1).strip()
            # Nettoie les numéros de ligne
            latex = self.validator.clean_line_numbers(latex)

            if latex and len(latex) > 1:
                equations.append({
                    'id': f'eq_{i:03d}',
                    'latex': latex,
                    'source': 'nougat',
                    'type': 'display',
                    'source_page': self._page_for_offset(markdown, match.start()),
                    'context': self._context_for_offset(markdown, match.start())
                })

        # Traite inline math (utile si Nougat renvoie du inline)
        next_idx = len(equations) + 1
        for match in inline_matches:
            latex = self.validator.clean_line_numbers(match.group(1).strip())
            if latex and len(latex) > 2:
                equations.append({
                    'id': f'eq_{next_idx:03d}',
                    'latex': latex,
                    'source': 'nougat',
                    'type': 'inline',
                    'source_page': self._page_for_offset(markdown, match.start()),
                    'context': self._context_for_offset(markdown, match.start())
                })
                next_idx += 1

        # Traite les environnements LaTeX
        for match in env_matches:
            latex = self.validator.clean_line_numbers(match.group(2).strip())
            if latex and len(latex) > 2:
                equations.append({
                    'id': f'eq_{next_idx:03d}',
                    'latex': latex,
                    'source': 'nougat',
                    'type': 'environment',
                    'source_page': self._page_for_offset(markdown, match.start()),
                    'context': self._context_for_offset(markdown, match.start())
                })
                next_idx += 1

        # Si rien trouvé via balises LaTeX, bascule en mode heuristique pour fallback OCR
        if not equations:
            equations = self._extract_equation_blocks_from_plain_text(markdown, start_idx=1)

        logger.info(f"📊 {len(equations)} équations extraites")
        return equations

    def refine_equations(self, equations: List[Dict]) -> List[Dict]:
        """Valide et améliore équations"""
        refined = []

        for eq in equations:
            validation = self.validator.full_validation(eq['latex'])
            eq['validation'] = validation
            refined.append(eq)

            if not validation['valid']:
                logger.warning(f"⚠️ {eq['id']} suspect: {validation['brace_check']['message']}")

        return refined

