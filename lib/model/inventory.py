from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class FileInfo:
    """Informations élémentaires sur un fichier du miroir."""

    path: Path
    relative_path: Path
    extension: str
    size: int


@dataclass(slots=True)
class Inventory:
    """Inventaire complet d'un dossier analysé."""

    files: list[FileInfo]
    extension_counts: Counter[str]
    total_size: int