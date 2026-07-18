from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ImageInfo:
    path: Path
    relative_path: Path

    filename: str
    extension: str

    filesize: int

    width: int | None = None
    height: int | None = None

    sha256: str | None = None
    phash: str | None = None
