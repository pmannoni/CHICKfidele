import html
import json
from pathlib import Path
from typing import List, Dict
from loguru import logger
from config import Config
from latex_validator import LaTeXValidator
from pdf_processor import PDFProcessor

class PublicationConverter:
    """Convertisseur complet PDF → Structure canonique"""

    def __init__(self):
        self.config = Config
        self.config.setup()
        self.processor = PDFProcessor(self.config)
        self.validator = LaTeXValidator()
        logger.info("🚀 PublicationConverter initialized")

    def convert(self, pdf_path: str, title: str = "Publication") -> Dict:
        """Pipeline complet de conversion"""

        if not Path(pdf_path).exists():
            logger.error(f"❌ PDF not found: {pdf_path}")
            return None

        # 1. Extraction Nougat
        logger.info("📄 Étape 1: Extraction du PDF...")
        markdown = self.processor.extract_with_nougat(pdf_path)
        if not markdown:
            logger.error("❌ Conversion échouée: extraction impossible")
            return None

        # 2. Extraction équations
        logger.info("📐 Étape 2: Extraction des équations...")
        equations = self.processor.extract_equations(markdown)

        if not equations:
            logger.warning("⚠️ Aucune équation trouvée")

        # 3. Validation + refinement
        logger.info("✅ Étape 3: Validation...")
        validated_eqs = self.processor.refine_equations(equations)

        # 4. Sauvegarde
        logger.info("💾 Étape 4: Sauvegarde...")
        self._save_equations(validated_eqs)
        self._save_markdown(markdown, validated_eqs)
        self._save_equation_documents(title, validated_eqs)
        self._save_metadata(title, validated_eqs)

        logger.success(f"✅ Conversion complète: {len(validated_eqs)} équations extraites")
        return {
            'equations': validated_eqs,
            'markdown': markdown,
            'output_dir': str(self.config.OUTPUT_BASE),
            'valid_count': sum(1 for eq in validated_eqs if eq['validation']['valid'])
        }

    def build_equation_documents_from_catalog(self, title: str = "Publication") -> Dict:
        """Régénère les documents de présentation à partir du catalogue existant."""
        catalog_file = self.config.OUTPUT_BASE / "equations_catalog.json"
        if not catalog_file.exists():
            logger.error(f"❌ Catalogue introuvable: {catalog_file}")
            return None

        equations = json.loads(catalog_file.read_text(encoding="utf-8"))
        self._save_equation_documents(title, equations)
        self._save_metadata(title, equations)

        return {
            "equations": len(equations),
            "output_dir": str(self.config.OUTPUT_BASE),
            "markdown_doc": str(self.config.OUTPUT_BASE / "equations_presented.md"),
            "html_doc": str(self.config.OUTPUT_BASE / "equations_presented.html")
        }

    def _save_equations(self, equations: List[Dict]):
        """Sauvegarde équations en .tex + .json"""
        # Nettoie les sorties précédentes pour éviter les équations fantômes d'un run antérieur.
        for old_file in self.config.EQUATIONS_DIR.glob("eq_*.*"):
            old_file.unlink(missing_ok=True)

        for eq in equations:
            eq_id = eq['id']

            # .tex
            tex_file = self.config.EQUATIONS_DIR / f"{eq_id}.tex"
            tex_file.write_text(eq['latex'], encoding='utf-8')

            # .json
            json_file = self.config.EQUATIONS_DIR / f"{eq_id}.json"
            json_file.write_text(
                json.dumps(eq, indent=2, ensure_ascii=False),
                encoding='utf-8'
            )

        # Catalogue canonique unique pour usage IA/RAG
        catalog = []
        for eq in equations:
            catalog.append({
                "equation_id": eq["id"],
                "latex": eq["latex"],
                "source": eq.get("source"),
                "equation_type": eq.get("type"),
                "source_page": eq.get("source_page"),
                "context": eq.get("context"),
                "validation": eq.get("validation", {})
            })

        catalog_file = self.config.OUTPUT_BASE / "equations_catalog.json"
        catalog_file.write_text(
            json.dumps(catalog, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )

    def _save_markdown(self, markdown: str, equations: List[Dict]):
        """Sauvegarde Markdown structuré avec rapport validation"""
        md_file = self.config.OUTPUT_BASE / "paper.md"
        md_file.write_text(markdown, encoding='utf-8')

        # Rapport validation
        report = "# Rapport de Validation de Conversion\n\n"
        report += f"**Total équations extraites:** {len(equations)}\n"
        report += f"**Équations valides:** {sum(1 for eq in equations if eq['validation']['valid'])}\n\n"

        report += "## Détails par équation\n\n"

        for eq in equations:
            status = "✅" if eq['validation']['valid'] else "⚠️"
            report += f"### {eq['id']} {status}\n"
            report += f"- **Valid:** {eq['validation']['valid']}\n"
            report += f"- **Confidence:** {eq['validation']['confidence']:.1%}\n"
            report += f"- **Type:** {eq.get('type', 'unknown')}\n"
            report += f"- **Page:** {eq.get('source_page', 'unknown')}\n"
            if eq.get('context'):
                report += f"- **Context:** {eq['context']}\n"

            if not eq['validation']['valid']:
                report += f"- **Issue:** {eq['validation']['brace_check']['message']}\n"

            report += f"\n**LaTeX:**\n```latex\n{eq['latex']}\n```\n\n"

        report_file = self.config.OUTPUT_BASE / "validation_report.md"
        report_file.write_text(report, encoding='utf-8')
        logger.info(f"📋 Rapport sauvegardé: {report_file}")

    def _save_equation_documents(self, title: str, equations: List[Dict]):
        """Crée des documents lisibles présentant les équations extraites."""
        valid_count = sum(1 for eq in equations if eq.get('validation', {}).get('valid'))

        markdown_lines = [
            f"# Équations extraites — {title}",
            "",
            f"- **Total équations:** {len(equations)}",
            f"- **Équations validées automatiquement:** {valid_count}",
            "- **Conseil:** ouvrir aussi `equations_presented.html` dans un navigateur pour une lecture plus confortable.",
            "",
            "---",
            ""
        ]

        html_sections = []
        for eq in equations:
            eq_id = eq.get('equation_id', eq.get('id', 'unknown'))
            latex = eq.get('latex', '').strip()
            eq_type = eq.get('equation_type', eq.get('type', 'unknown'))
            page = eq.get('source_page', 'unknown')
            context = eq.get('context', '')
            validation = eq.get('validation', {})
            is_valid = validation.get('valid', False)
            confidence = validation.get('confidence', 0.0)
            status = "✅" if is_valid else "⚠️"
            issue = validation.get('brace_check', {}).get('message', '') if not is_valid else ''

            markdown_lines.extend([
                f"## {eq_id} {status}",
                "",
                f"- **Page:** {page}",
                f"- **Type:** {eq_type}",
                f"- **Validation auto:** {is_valid}",
                f"- **Confiance:** {confidence:.1%}",
            ])

            if context:
                markdown_lines.append(f"- **Contexte:** {context}")
            if issue:
                markdown_lines.append(f"- **Alerte:** {issue}")

            markdown_lines.extend([
                "",
                "### Version mise en forme",
                "",
                "$$",
                latex,
                "$$",
                "",
                "### Texte brut extrait",
                "",
                "```latex",
                latex,
                "```",
                "",
                "---",
                ""
            ])

            html_sections.append(f"""
            <section class=\"equation-card\" id=\"{html.escape(eq_id)}\">
              <div class=\"card-header\">
                <h2>{html.escape(eq_id)} <span class=\"status\">{status}</span></h2>
                <div class=\"meta\">Page {html.escape(str(page))} · {html.escape(str(eq_type))} · confiance {confidence:.1%}</div>
              </div>
              <div class=\"rendered\">\\[{html.escape(latex)}\\]</div>
              <details>
                <summary>Voir le texte brut extrait</summary>
                <pre>{html.escape(latex)}</pre>
              </details>
              {f'<p class=\"context\"><strong>Contexte :</strong> {html.escape(context)}</p>' if context else ''}
              {f'<p class=\"warning\"><strong>Alerte :</strong> {html.escape(issue)}</p>' if issue else ''}
            </section>
            """)

        md_file = self.config.OUTPUT_BASE / "equations_presented.md"
        md_file.write_text("\n".join(markdown_lines), encoding="utf-8")

        html_doc = f"""<!DOCTYPE html>
<html lang=\"fr\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Équations extraites — {html.escape(title)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; background: #f6f8fb; color: #1f2937; }}
    main {{ max-width: 1100px; margin: 0 auto; padding: 32px 20px 64px; }}
    h1 {{ margin-bottom: 8px; }}
    .summary {{ background: white; border-radius: 14px; padding: 18px 20px; box-shadow: 0 6px 18px rgba(0,0,0,.08); margin-bottom: 24px; }}
    .equation-card {{ background: white; border-radius: 14px; padding: 20px; box-shadow: 0 6px 18px rgba(0,0,0,.08); margin-bottom: 18px; }}
    .card-header {{ margin-bottom: 14px; }}
    .card-header h2 {{ margin: 0 0 6px; font-size: 1.2rem; }}
    .meta {{ color: #4b5563; font-size: .95rem; }}
    .rendered {{ overflow-x: auto; padding: 14px; background: #f8fafc; border-radius: 10px; border: 1px solid #e5e7eb; margin: 12px 0; }}
    pre {{ white-space: pre-wrap; word-break: break-word; background: #111827; color: #f9fafb; padding: 14px; border-radius: 10px; overflow-x: auto; }}
    details summary {{ cursor: pointer; font-weight: 600; }}
    .warning {{ color: #b45309; }}
    .context {{ color: #374151; }}
    .status {{ font-size: .95rem; }}
  </style>
  <script>
    window.MathJax = {{ tex: {{ inlineMath: [['$', '$'], ['\\(', '\\)']] }}, svg: {{ fontCache: 'global' }} }};
  </script>
  <script defer src=\"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js\"></script>
</head>
<body>
  <main>
    <section class=\"summary\">
      <h1>Équations extraites — {html.escape(title)}</h1>
      <p><strong>Total :</strong> {len(equations)} · <strong>Validées automatiquement :</strong> {valid_count}</p>
      <p>Ce document tente un rendu mathématique via MathJax et conserve le texte brut extrait pour contrôle visuel.</p>
    </section>
    {''.join(html_sections)}
  </main>
</body>
</html>
"""

        html_file = self.config.OUTPUT_BASE / "equations_presented.html"
        html_file.write_text(html_doc, encoding="utf-8")
        logger.info(f"🧾 Documents de présentation sauvegardés: {md_file} / {html_file}")

    def _save_metadata(self, title: str, equations: List[Dict]):
        """Métadonnées globales"""
        metadata = {
            'title': title,
            'total_equations': len(equations),
            'valid_equations': sum(1 for eq in equations if eq['validation']['valid']),
            'equations_ids': [eq.get('id', eq.get('equation_id')) for eq in equations],
            'format_version': '1.0',
            'structure': {
                'paper_md': 'paper.md',
                'equations_dir': 'equations/',
                'equations_catalog': 'equations_catalog.json',
                'equations_presented_md': 'equations_presented.md',
                'equations_presented_html': 'equations_presented.html',
                'validation_report': 'validation_report.md',
                'metadata': 'metadata.json'
            }
        }

        meta_file = self.config.OUTPUT_BASE / "metadata.json"
        meta_file.write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
        logger.info(f"📊 Métadonnées sauvegardées: {meta_file}")

