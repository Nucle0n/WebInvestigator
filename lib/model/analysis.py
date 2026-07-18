from dataclasses import dataclass, field

from lib.model.duplicate import DuplicateImageGroup
from lib.model.filename import FilenameFinding
from lib.model.image import ImageInfo
from lib.model.inventory import Inventory
from lib.model.html import HTMLPage
from lib.model.oembed import OEmbedFile
from lib.model.similar import SimilarImageGroup


@dataclass(slots=True)
class AnalysisResult:
    """Résultat complet d'une analyse du miroir."""

    inventory: Inventory
    filename_findings: list[FilenameFinding] = field(default_factory=list)
    oembed_files: list[OEmbedFile] = field(default_factory=list)
    html_pages: list[HTMLPage] = field(default_factory=list)
    images: list[ImageInfo] = field(default_factory=list)
    duplicate_images: list[DuplicateImageGroup] = field(default_factory=list)
    similar_images: list[SimilarImageGroup] = field(default_factory=list)
