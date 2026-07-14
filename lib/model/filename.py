from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FilenameFinding:
    """Correspondance trouvée dans le nom d'un fichier."""

    keyword: str
    relative_path: str