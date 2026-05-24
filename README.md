# CHICKfidele

Conversion fidele de PDF scientifique vers une structure exploitable par IA, avec focus equations.

## Sorties

Les fichiers sont generes dans `Publication_convertie/`:

- `paper.md`: texte extrait
- `equations/eq_XXX.tex` et `equations/eq_XXX.json`: equations individuelles
- `equations_catalog.json`: catalogue canonique pour IA/RAG
- `equations_presented.md`: document Markdown des equations mises en forme
- `equations_presented.html`: document HTML stylise des equations mises en forme
- `validation_report.md`: rapport de validation automatique
- `manual_checklist.md`: checklist de verification humaine
- `metadata.json`: metadonnees globales

## Execution (Windows PowerShell)

```powershell
Set-Location "C:\Users\pmanonni\PycharmProjects\CHICKfidele"
.\.venv\Scripts\python.exe main.py
```

Si Nougat echoue, le pipeline utilise le fallback PyPDF2 + heuristiques mathematiques.

## Regenerer uniquement le document de presentation des equations

```powershell
Set-Location "C:\Users\pmanonni\PycharmProjects\CHICKfidele"
.\.venv\Scripts\python.exe build_equation_docs.py
```

Puis ouvrir `Publication_convertie/equations_presented.html` dans un navigateur pour un rendu plus lisible.

## Supprimer les numeros de ligne a gauche du PDF

```powershell
Set-Location "C:\Users\pmanonni\PycharmProjects\CHICKfidele"
.\.venv\Scripts\python.exe remove_left_line_numbers.py src/Publi2.pdf --margin 40
```

Le script recadre le PDF en place et cree automatiquement une sauvegarde : `src/Publi2_backup_before_crop.pdf`.

## Verification manuelle

```powershell
Set-Location "C:\Users\pmanonni\PycharmProjects\CHICKfidele"
.\.venv\Scripts\python.exe verify_manual.py
```

Puis ouvrir `Publication_convertie/manual_checklist.md` et verifier equation par equation dans `src/Publi2.pdf`.



