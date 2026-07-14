from collections import Counter
from pathlib import Path

from lib.model.inventory import FileInfo, Inventory


def normalize_extension(file_path: Path) -> str:
    """Retourne l'extension normalisée d'un fichier."""
    extension = file_path.suffix.lower()

    if extension:
        return extension

    return "[sans extension]"


def scan_directory(root_directory: Path) -> Inventory:
    """Parcourt récursivement un dossier et construit son inventaire."""
    files: list[FileInfo] = []
    extension_counts: Counter[str] = Counter()
    total_size = 0

    for path in root_directory.rglob("*"):
        if not path.is_file():
            continue

        try:
            size = path.stat().st_size
        except OSError as error:
            print(f"[AVERTISSEMENT] Fichier illisible : {path}")
            print(f"                {error}")
            continue

        extension = normalize_extension(path)

        files.append(
            FileInfo(
                path=path,
                relative_path=path.relative_to(root_directory),
                extension=extension,
                size=size,
            )
        )

        extension_counts[extension] += 1
        total_size += size

    return Inventory(
        files=files,
        extension_counts=extension_counts,
        total_size=total_size,
    )