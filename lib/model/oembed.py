from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class OEmbedFile:
    """Contenu d'un fichier .oembed chargé depuis le miroir."""

    path: Path
    data: dict[str, Any]