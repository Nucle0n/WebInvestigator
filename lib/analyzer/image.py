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
) -> list[SimilarImageGroup]:
    """Group images sharing the same perceptual hash."""

    images_by_phash: dict[str, list[ImageInfo]] = {}

    for image in images:
        if image.phash is None:
            continue

        images_by_phash.setdefault(
            image.phash,
            [],
        ).append(image)

    groups: list[SimilarImageGroup] = []

    for matching_images in images_by_phash.values():
        if len(matching_images) < 2:
            continue

        groups.append(
            SimilarImageGroup(
                max_distance=0,
                images=matching_images,
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