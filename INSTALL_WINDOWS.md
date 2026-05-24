# Installation Windows (PowerShell)

Ce projet utilise un pipeline PDF scientifique avec `nougat-ocr`.

## 1) Pre-requis systeme

- Python 3.12 (venv deja cree: `.venv`)
- Tesseract OCR (optionnel mais recommande pour OCR fallback)
- Poppler (necessaire si vous utilisez `pdf2image`)

## 2) Installation automatique

Dans PowerShell, depuis la racine du projet:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install_windows.ps1
```

## 3) Verification rapide

```powershell
.\.venv\Scripts\python.exe -m pip show nougat-ocr
.\.venv\Scripts\nougat.exe --help
```

Si `nougat.exe` n'existe pas:

```powershell
.\.venv\Scripts\python.exe -m nougat --help
```

## 4) Pourquoi cette methode

Sur Python 3.12, `pip` peut retrograder `datasets` vers des versions anciennes qui tirent `pyarrow<4` (incompatible, build error). On pre-installe donc:

- `datasets==2.21.0`
- `pyarrow==24.0.0`

avant `nougat-ocr` pour eviter ce conflit.

## 5) En cas d'echec torch

CPU-only (stable):

```powershell
.\.venv\Scripts\python.exe -m pip install --index-url https://download.pytorch.org/whl/cpu torch torchvision
```

Si vous voulez CUDA, installez les wheels PyTorch adaptes a votre version CUDA puis relancez `install_windows.ps1`.

