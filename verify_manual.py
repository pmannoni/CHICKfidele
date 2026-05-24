import json
from pathlib import Path


def build_manual_checklist(output_dir: str = "Publication_convertie") -> Path:
    """Genere une checklist markdown pour verification manuelle des equations extraites."""
    base = Path(output_dir)
    catalog_file = base / "equations_catalog.json"

    if not catalog_file.exists():
        raise FileNotFoundError(f"Catalogue introuvable: {catalog_file}")

    equations = json.loads(catalog_file.read_text(encoding="utf-8"))

    lines = [
        "# Checklist de verification manuelle",
        "",
        "Verifier chaque equation dans le PDF source et cocher l'etat.",
        "",
        "| Equation | Page | Statut auto | Verification humaine | Notes |",
        "|---|---:|---|---|---|",
    ]

    for eq in equations:
        eq_id = eq.get("equation_id", "unknown")
        page = eq.get("source_page", "?")
        valid = eq.get("validation", {}).get("valid", False)
        auto_status = "OK" if valid else "A revoir"
        lines.append(f"| `{eq_id}` | {page} | {auto_status} | [ ] OK / [ ] KO |  |")

    out_file = base / "manual_checklist.md"
    out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_file


if __name__ == "__main__":
    checklist = build_manual_checklist()
    print(f"Checklist generee: {checklist}")

