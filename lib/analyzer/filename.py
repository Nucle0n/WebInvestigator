from lib.model.filename import FilenameFinding
from lib.model.inventory import Inventory


DEFAULT_FILENAME_KEYWORDS = (
    "chatgpt",
    "midjourney",
    "openai",
    "dall-e",
    "dalle",
    "flux",
    "stable_diffusion",
    "stable-diffusion",
    "reference_image",
    "using_the_reference",
    "prompt",
    "generated",
    "upscaled",
    "capture_d_ecran",
    "screenshot",
)


def find_suspicious_filenames(
    inventory: Inventory,
    keywords: tuple[str, ...] = DEFAULT_FILENAME_KEYWORDS,
) -> list[FilenameFinding]:
    """Repère les noms de fichiers contenant certains mots-clés."""
    findings: list[FilenameFinding] = []
    normalized_keywords = tuple(keyword.lower() for keyword in keywords)

    for file_info in inventory.files:
        filename = file_info.path.name.lower()

        for keyword in normalized_keywords:
            if keyword in filename:
                findings.append(
                    FilenameFinding(
                        keyword=keyword,
                        relative_path=str(file_info.relative_path),
                    )
                )

    return findings