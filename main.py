import sys
from collections import Counter

from config import (
    REPORTS_JSON_DIR,
    SITE_MIRROR_DIR,
    create_output_directories,
)
from lib.extractor import Inventory, scan_directory
from lib.oembed_parser import (
    load_oembed_files,
    display_oembed_files,
)
from lib.parser import FilenameFinding, find_suspicious_filenames
from lib.report import export_inventory_json
from lib.utils import format_size


APP_NAME = "Shopify OSINT Toolkit"
APP_VERSION = "0.1.0"
TOP_FILES_LIMIT = 20


def display_header() -> None:
    """Affiche l'en-tête du programme."""
    print("=" * 76)
    print(f"{APP_NAME} - Version {APP_VERSION}")
    print("=" * 76)
    print(f"Python : {sys.version.split()[0]}")
    print()


def validate_mirror_directory() -> bool:
    """Vérifie que le dossier du miroir existe et est exploitable."""
    if not SITE_MIRROR_DIR.exists():
        print("[ERREUR] Le dossier du miroir est introuvable :")
        print(SITE_MIRROR_DIR)
        return False

    if not SITE_MIRROR_DIR.is_dir():
        print("[ERREUR] Le chemin configuré n'est pas un dossier :")
        print(SITE_MIRROR_DIR)
        return False

    print("[OK] Dossier du miroir trouvé")
    print(f"     {SITE_MIRROR_DIR}")
    return True


def display_inventory(inventory: Inventory) -> None:
    """Affiche les statistiques principales de l'inventaire."""
    print()
    print("=" * 76)
    print("INVENTAIRE DU MIROIR")
    print("=" * 76)

    print(f"Nombre de fichiers : {len(inventory.files)}")
    print(f"Taille totale       : {format_size(inventory.total_size)}")

    print()
    print("FICHIERS PAR EXTENSION")
    print("-" * 76)

    for extension, count in inventory.extension_counts.most_common():
        print(f"{extension:<24} {count:>6}")

    largest_files = sorted(
        inventory.files,
        key=lambda file_info: file_info.size,
        reverse=True,
    )[:TOP_FILES_LIMIT]

    print()
    print(f"{TOP_FILES_LIMIT} PLUS GROS FICHIERS")
    print("-" * 76)

    for index, file_info in enumerate(largest_files, start=1):
        size = format_size(file_info.size)
        print(f"{index:>2}. {size:>12}  {file_info.relative_path}")


def display_filename_findings(
    findings: list[FilenameFinding],
) -> None:
    """Affiche les mots-clés détectés dans les noms de fichiers."""
    print()
    print("=" * 76)
    print("INDICES DANS LES NOMS DE FICHIERS")
    print("=" * 76)

    if not findings:
        print("Aucun mot-clé particulier détecté.")
        return

    keyword_counts = Counter(finding.keyword for finding in findings)

    print("RÉSUMÉ")
    print("-" * 76)

    for keyword, count in keyword_counts.most_common():
        print(f"{keyword:<30} {count:>5}")

    print()
    print("DÉTAILS")
    print("-" * 76)

    findings_by_keyword: dict[str, list[FilenameFinding]] = {}

    for finding in findings:
        findings_by_keyword.setdefault(finding.keyword, []).append(finding)

    for keyword in sorted(findings_by_keyword):
        print()
        print(f"[{keyword}]")

        unique_paths = sorted(
            {
                finding.relative_path
                for finding in findings_by_keyword[keyword]
            }
        )

        for relative_path in unique_paths:
            print(f"  - {relative_path}")


def main() -> None:
    """Point d'entrée principal du programme."""
    display_header()
    create_output_directories()

    if not validate_mirror_directory():
        raise SystemExit(1)

    print()
    print("Analyse du miroir en cours...")

    inventory = scan_directory(SITE_MIRROR_DIR)
    display_inventory(inventory)

    filename_findings = find_suspicious_filenames(inventory)
    display_filename_findings(filename_findings)
    
    oembed_files = load_oembed_files(inventory)
    display_oembed_files(oembed_files)

    output_file = REPORTS_JSON_DIR / "inventory.json"
    export_inventory_json(inventory, output_file)

    print()
    print("[OK] Inventaire JSON généré :")
    print(f"     {output_file}")


if __name__ == "__main__":
    main()