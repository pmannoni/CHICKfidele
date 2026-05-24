from pathlib import Path
import json
import sys
import os

# Force UTF-8 sur Windows
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    sys.stdout.reconfigure(encoding='utf-8')

from converter import PublicationConverter
from loguru import logger

def verify_equations(output_dir: str = "Publication_convertie"):
    """Affiche équations extraites pour review"""
    eq_dir = Path(output_dir) / "equations"

    if not eq_dir.exists():
        print("[X] Repertoire equations non trouve")
        return

    print(f"\n{'='*70}")
    print("VERIFICATION DES EQUATIONS EXTRAITES")
    print(f"{'='*70}\n")

    json_files = sorted(eq_dir.glob("*.json"))

    for json_file in json_files:
        with open(json_file, encoding='utf-8') as f:
            eq = json.load(f)

        status = "[OK]" if eq['validation']['valid'] else "[!]"

        print(f"\n{eq['id']} - {status}")
        print(f"Confidence: {eq['validation']['confidence']:.1%}")
        print(f"Type: {eq.get('type', 'unknown')}")

        if not eq['validation']['valid']:
            print(f"[!] Issue: {eq['validation']['brace_check']['message']}")

        print(f"\nLaTeX:\n{eq['latex']}")
        print(f"{'-'*70}")

if __name__ == "__main__":
    # Chemin du PDF
    pdf_file = "src/Publi2.pdf"

    logger.info("[*] Demarrage de la conversion")

    converter = PublicationConverter()
    result = converter.convert(pdf_file, title="Publication scientifique")

    if result:
        print(f"\n[+] CONVERSION REUSSIE")
        print(f"[*] Resultat: {result['output_dir']}")
        print(f"[*] Equations extraites: {len(result['equations'])}")
        print(f"[*] Equations valides: {result['valid_count']}")

        # Vérification
        print("\n[*] Lancement de la verification...")
        verify_equations()
    else:
        print(f"\n[-] CONVERSION ECHOUEE")

