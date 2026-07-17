from dataclasses import dataclass

from lib.model.image import ImageInfo


@dataclass(slots=True)
class SimilarImageGroup:
    max_distance: int
    images: list[ImageInfo]