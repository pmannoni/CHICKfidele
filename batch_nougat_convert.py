import json
import re
import subprocess
import sys
from pathlib import Path

from PyPDF2 import PdfReader


def extract_equations(markdown_text: str):
    equations = []
    display_matches = list(re.finditer(r"\$\$(.*?)\$\$", markdown_text, re.DOTALL))
    for idx, m in enumerate(display_matches, start=1):
        latex = m.group(1).strip()
        if latex:
            equations.append({
                "id": f"eq_{idx:03d}",
                "latex": latex,
                "source": "nougat",
                "type": "display",
            })
    return equations


def main():
    project_root = Path(__file__).resolve().parent
    pdf_path = project_root / "src" / "Publi2.pdf"
    out_root = project_root / "Publication_convertie"
    chunks_dir = out_root / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)

    progress_file = out_root / "batch_progress.json"

    total_pages = len(PdfReader(str(pdf_path)).pages)
    chunk_size = 5

    nougat_exe = Path(sys.executable).with_name("nougat.exe")
    if not nougat_exe.exists():
        raise FileNotFoundError(f"nougat.exe introuvable: {nougat_exe}")

    merged_parts = []
    progress = {
        "pdf": str(pdf_path),
        "total_pages": total_pages,
        "chunk_size": chunk_size,
        "chunks": [],
        "status": "running",
    }
    # État initial pour monitoring en temps réel
    progress_file.write_text(json.dumps(progress, indent=2, ensure_ascii=False), encoding="utf-8")

    for start in range(1, total_pages + 1, chunk_size):
        end = min(start + chunk_size - 1, total_pages)
        page_spec = f"{start}-{end}"
        chunk_out = chunks_dir / f"pages_{start:02d}_{end:02d}"
        chunk_out.mkdir(parents=True, exist_ok=True)

        # Marque le chunk en cours avant l'appel nougat
        progress["current_chunk"] = page_spec
        progress_file.write_text(json.dumps(progress, indent=2, ensure_ascii=False), encoding="utf-8")

        cmd = [
            str(nougat_exe),
            str(pdf_path),
            "-o",
            str(chunk_out),
            "--markdown",
            "--recompute",
            "-p",
            page_spec,
        ]

        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")

        chunk_entry = {
            "pages": page_spec,
            "returncode": proc.returncode,
            "stdout_tail": proc.stdout[-1200:],
            "stderr_tail": proc.stderr[-1200:],
        }

        mmd_file = chunk_out / "Publi2.mmd"
        if proc.returncode == 0 and mmd_file.exists():
            content = mmd_file.read_text(encoding="utf-8", errors="ignore").strip()
            merged_parts.append(f"<!-- chunk {page_spec} -->\n{content}\n")
            chunk_entry["status"] = "ok"
            chunk_entry["mmd"] = str(mmd_file)
        else:
            chunk_entry["status"] = "failed"

        progress["chunks"].append(chunk_entry)
        progress_file.write_text(json.dumps(progress, indent=2, ensure_ascii=False), encoding="utf-8")

    merged = "\n\n".join(merged_parts).strip() + "\n"
    full_mmd = out_root / "Publi2_full.mmd"
    full_mmd.write_text(merged, encoding="utf-8")

    equations = extract_equations(merged)
    eq_dir = out_root / "equations"
    eq_dir.mkdir(parents=True, exist_ok=True)
    for eq in equations:
        (eq_dir / f"{eq['id']}.tex").write_text(eq["latex"], encoding="utf-8")
        (eq_dir / f"{eq['id']}.json").write_text(json.dumps(eq, indent=2, ensure_ascii=False), encoding="utf-8")

    metadata = {
        "title": "Publication scientifique",
        "total_pages": total_pages,
        "total_equations": len(equations),
        "chunks_ok": sum(1 for c in progress["chunks"] if c["status"] == "ok"),
        "chunks_failed": sum(1 for c in progress["chunks"] if c["status"] == "failed"),
        "source": "nougat batched",
    }
    (out_root / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_root / "paper.md").write_text(merged, encoding="utf-8")

    progress["status"] = "done"
    progress_file.write_text(json.dumps(progress, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()

