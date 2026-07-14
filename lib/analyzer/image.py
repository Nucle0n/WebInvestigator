from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ImageInfo:
    path: Path
    relative_path: str

    width: int
    height: int

    filesize: int

    sha256: str
    phash: str

    extension: str