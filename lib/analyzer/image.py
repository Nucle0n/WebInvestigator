from lib.model.image import ImageInfo
from lib.model.inventory import Inventory


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


def analyze_images(
    inventory: Inventory,
) -> list[ImageInfo]:
    """Analyze image files contained in the inventory."""

    images: list[ImageInfo] = []

    for file in inventory.files:

        if not is_supported_image(file.extension):
            continue

        images.append(
            ImageInfo(
                path=file.path,
                relative_path=file.relative_path,
                filename=file.path.name,
                extension=file.extension,
                filesize=file.size,
            )
        )

    return images