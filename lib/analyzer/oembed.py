import json

from lib.model.inventory import Inventory
from lib.model.oembed import OEmbedFile


def load_oembed_files(inventory: Inventory) -> list[OEmbedFile]:
    """Charge tous les fichiers .oembed valides du miroir."""
    oembed_files: list[OEmbedFile] = []

    for file_info in inventory.files:
        if file_info.extension != ".oembed":
            continue

        try:
            with file_info.path.open("r", encoding="utf-8") as file:
                data = json.load(file)

        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            print(f"[AVERTISSEMENT] Fichier .oembed illisible :")
            print(f"                {file_info.relative_path}")
            print(f"                {error}")
            continue

        oembed_files.append(
            OEmbedFile(
                path=file_info.relative_path,
                data=data,
            )
        )

    return oembed_files