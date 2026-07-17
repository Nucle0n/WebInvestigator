from lib.model.duplicate import DuplicateImageGroup
from lib.model.image import ImageInfo


def find_duplicate_images(
    images: list[ImageInfo],
) -> list[DuplicateImageGroup]:
    """Return groups of images sharing the same SHA-256 hash."""

    hashes: dict[str, list[ImageInfo]] = {}

    for image in images:
        if image.sha256 is None:
            continue

        hashes.setdefault(
            image.sha256,
            [],
        ).append(image)

    duplicates: list[DuplicateImageGroup] = []

    for sha256, group in hashes.items():
        if len(group) < 2:
            continue

        duplicates.append(
            DuplicateImageGroup(
                sha256=sha256,
                images=group,
            )
        )

    return duplicates