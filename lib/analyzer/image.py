import hashlib
import imagehash

from pathlib import Path

from PIL import Image, UnidentifiedImageError

from lib.model.image import ImageInfo

from lib.model.inventory import Inventory

from lib.model.similar import SimilarImageGroup


IMAGE_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".webp",
    ".svg",
    ".ico",
)


def is_supported_image(extension: str) -> bool:
    """Return True if the extension belongs to an image."""

    return extension.lower() in IMAGE_EXTENSIONS


def calculate_sha256(file_path: Path) -> str | None:
    """Return the SHA-256 hash of a file."""

    try:
        with file_path.open("rb") as file:
            return hashlib.file_digest(file, "sha256").hexdigest()
    except OSError:
        return None


def calculate_phash(file_path: Path) -> str | None:
    """Return the perceptual hash of an image."""

    try:
        with Image.open(file_path) as image:
            return str(imagehash.phash(image))
    except (OSError, UnidentifiedImageError):
        return None


def phash_distance(
    first_phash: str,
    second_phash: str,
) -> int:
    """Return the Hamming distance between two perceptual hashes."""

    first_hash = imagehash.hex_to_hash(first_phash)
    second_hash = imagehash.hex_to_hash(second_phash)

    return first_hash - second_hash
    
    
def find_matching_phashes(
    images: list[ImageInfo],
    max_distance: int,
) -> list[SimilarImageGroup]:
    """Group images into connected perceptual similarity clusters."""

    if max_distance < 0:
        raise ValueError("max_distance must be greater than or equal to 0")

    images_by_phash: dict[str, list[ImageInfo]] = {}

    for image in images:
        if image.phash is None:
            continue

        images_by_phash.setdefault(
            image.phash,
            [],
        ).append(image)

    unique_phashes = list(images_by_phash)

    similarity_graph: dict[str, list[str]] = {
        phash: []
        for phash in unique_phashes
    }

    for first_index, first_phash in enumerate(unique_phashes):
        for second_phash in unique_phashes[first_index + 1:]:
            distance = phash_distance(
                first_phash,
                second_phash,
            )

            if distance > max_distance:
                continue

            similarity_graph[first_phash].append(second_phash)
            similarity_graph[second_phash].append(first_phash)

    groups: list[SimilarImageGroup] = []
    visited_phashes: set[str] = set()

    for starting_phash in unique_phashes:
        if starting_phash in visited_phashes:
            continue

        component_phashes: list[str] = []
        phashes_to_visit = [starting_phash]

        while phashes_to_visit:
            current_phash = phashes_to_visit.pop()

            if current_phash in visited_phashes:
                continue

            visited_phashes.add(current_phash)
            component_phashes.append(current_phash)

            phashes_to_visit.extend(
                similarity_graph[current_phash]
            )

        component_images = sorted(
            (
                image
                for image in images
                if image.phash in component_phashes
            ),
            key=lambda image: image.relative_path,
        )

        if len(component_images) < 2:
            continue

        greatest_distance = 0

        for first_index, first_phash in enumerate(component_phashes):
            for second_phash in component_phashes[first_index + 1:]:
                distance = phash_distance(
                    first_phash,
                    second_phash,
                )

                greatest_distance = max(
                    greatest_distance,
                    distance,
                )

        groups.append(
            SimilarImageGroup(
                max_distance=greatest_distance,
                images=component_images,
            )
        )

    return groups


def read_image_dimensions(
    image_path: Path,
) -> tuple[int | None, int | None]:
    """Return image dimensions using Pillow."""

    try:
        with Image.open(image_path) as image:
            return image.width, image.height
    except (OSError, UnidentifiedImageError):
        return None, None


def analyze_images(
    inventory: Inventory,
) -> list[ImageInfo]:
    """Analyze image files contained in the inventory."""

    images: list[ImageInfo] = []

    for file in inventory.files:
        if not is_supported_image(file.extension):
            continue

        width, height = read_image_dimensions(file.path)
        sha256 = calculate_sha256(file.path)
        phash = calculate_phash(file.path)

        images.append(
            ImageInfo(
                path=file.path,
                relative_path=file.relative_path,
                filename=file.path.name,
                extension=file.extension,
                filesize=file.size,
                width=width,
                height=height,
                sha256=sha256,
                phash=phash,
            )
        )

    return images