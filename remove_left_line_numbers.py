from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject


def crop_left_margin(input_pdf: Path, output_pdf: Path, margin_points: float, backup: bool = True) -> dict:
    """Supprime une marge fixe à gauche sur toutes les pages d'un PDF."""
    if not input_pdf.exists():
        raise FileNotFoundError(f"PDF introuvable: {input_pdf}")

    if margin_points <= 0:
        raise ValueError("La marge à retirer doit être > 0")

    if backup and input_pdf.resolve() == output_pdf.resolve():
        backup_path = input_pdf.with_name(f"{input_pdf.stem}_backup_before_crop{input_pdf.suffix}")
        if not backup_path.exists():
            shutil.copy2(input_pdf, backup_path)
    else:
        backup_path = None

    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)
        new_page = writer.pages[-1]

        left = float(new_page.mediabox.left)
        bottom = float(new_page.mediabox.bottom)
        right = float(new_page.mediabox.right)
        top = float(new_page.mediabox.top)

        new_left = left + margin_points
        if new_left >= right:
            raise ValueError("Marge trop grande: la page serait vide")

        new_box = RectangleObject((new_left, bottom, right, top))
        new_page.mediabox = new_box
        new_page.cropbox = RectangleObject((new_left, bottom, right, top))
        new_page.trimbox = RectangleObject((new_left, bottom, right, top))
        new_page.bleedbox = RectangleObject((new_left, bottom, right, top))
        new_page.artbox = RectangleObject((new_left, bottom, right, top))

    with output_pdf.open("wb") as fh:
        writer.write(fh)

    return {
        "pages": len(reader.pages),
        "margin_points": margin_points,
        "output": str(output_pdf),
        "backup": str(backup_path) if backup_path else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Supprime les numéros de ligne à gauche en recadrant le PDF.")
    parser.add_argument("input_pdf", nargs="?", default="src/Publi2.pdf")
    parser.add_argument("--output", dest="output_pdf", default=None)
    parser.add_argument("--margin", type=float, default=40.0, help="Marge gauche à retirer en points PDF")
    parser.add_argument("--no-backup", action="store_true", help="Ne pas créer de sauvegarde si on écrase le fichier source")
    args = parser.parse_args()

    input_pdf = Path(args.input_pdf)
    output_pdf = Path(args.output_pdf) if args.output_pdf else input_pdf

    result = crop_left_margin(
        input_pdf=input_pdf,
        output_pdf=output_pdf,
        margin_points=args.margin,
        backup=not args.no_backup,
    )

    print("PDF recadré avec succès")
    print(f"Pages: {result['pages']}")
    print(f"Marge retirée: {result['margin_points']} pt")
    print(f"Sortie: {result['output']}")
    if result["backup"]:
        print(f"Sauvegarde: {result['backup']}")


if __name__ == "__main__":
    main()



