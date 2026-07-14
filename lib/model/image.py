from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ImageInfo:
    """Informations techniques extraites d'une image."""

    path: Path
    relative_path: Path
    width: int
    height: int
    filesize: int
    sha256: str
    phash: str
    extension: str
    