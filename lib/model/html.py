from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class HTMLPage:
    """Information extracted from a mirrored HTML page."""

    path: Path
    relative_path: Path

    title: str | None = None
