import json
from pathlib import Path

from lib.model.inventory import Inventory


def export_inventory_json(
    inventory: Inventory,
    output_file: Path,
) -> None:
    """Exporte l'inventaire complet au format JSON."""
    data = {
        "summary": {
            "file_count": len(inventory.files),
            "total_size_bytes": inventory.total_size,
            "extensions": dict(inventory.extension_counts),
        },
        "files": [
            {
                "relative_path": str(file_info.relative_path),
                "extension": file_info.extension,
                "size_bytes": file_info.size,
            }
            for file_info in inventory.files
        ],
    }

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
