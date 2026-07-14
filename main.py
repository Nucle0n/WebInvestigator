import sys

from config import (
    REPORTS_JSON_DIR,
    SITE_MIRROR_DIR,
    create_output_directories,
)
from lib.analyzer.filename import find_suspicious_filenames
from lib.analyzer.oembed import load_oembed_files
from lib.output.console import (
    display_filename_findings,
    display_inventory,
    display_oembed_files,
)
from lib.output.json import export_inventory_json
from lib.scanner import scan_directory


APP_NAME = "Web Investigator"
APP_VERSION = "0.1.0"


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