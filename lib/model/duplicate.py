from dataclasses import dataclass

from lib.model.image import ImageInfo


@dataclass
class DuplicateImageGroup:
    sha256: str
    images: list[ImageInfo]