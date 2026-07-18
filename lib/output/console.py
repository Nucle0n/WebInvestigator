from collections import Counter

from lib.model.duplicate import DuplicateImageGroup
from lib.model.filename import FilenameFinding
from lib.model.image import ImageInfo
from lib.model.inventory import Inventory
from lib.model.oembed import OEmbedFile
from lib.model.similar import SimilarImageGroup
from lib.utils import format_size


TOP_FILES_LIMIT = 20


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


def display_oembed_files(files: list[OEmbedFile]) -> None:
    """Affiche le contenu des fichiers .oembed."""
    print()
    print("=" * 76)
    print("FICHIERS OEMBED")
    print("=" * 76)

    print(f"{len(files)} fichier(s)\n")

    for oembed_file in files:
        print("-" * 76)
        print(oembed_file.path)
        print("-" * 76)

        for key, value in oembed_file.data.items():
            print(f"{key:20} : {value}")

        print()
   

def display_images(images: list[ImageInfo]) -> None:
    """Affiche les informations techniques des images analysées."""
    print()
    print("=" * 76)
    print("IMAGES")
    print("=" * 76)

    if not images:
        print("Aucune image détectée.")
        return

    print(f"{len(images)} image(s)\n")

    for image in images:
        print("-" * 76)
        print(image.relative_path)
        print("-" * 76)

        if image.width is None or image.height is None:
            dimensions = "Inconnues"
        else:
            dimensions = f"{image.width} x {image.height}"

        print(f"{'Dimensions':20} : {dimensions}")
        print(f"{'Taille':20} : {format_size(image.filesize)}")
        print(f"{'Extension':20} : {image.extension}")
        if image.sha256 is None:
            sha256 = "Inconnu"
        else:
            sha256 = image.sha256

        if image.phash is None:
            phash = "Inconnu"
        else:
            phash = image.phash

        print(f"{'SHA-256':20} : {sha256}")
        print(f"{'pHash':20} : {phash}")

        print()


def display_duplicate_images(
    duplicates: list[DuplicateImageGroup],
) -> None:
    """Affiche les groupes d'images identiques."""

    print()
    print("=" * 76)
    print("IMAGES IDENTIQUES (SHA-256)")
    print("=" * 76)

    if not duplicates:
        print("Aucun doublon détecté.")
        return

    total_images = sum(
        len(group.images)
        for group in duplicates
    )

    print(
        f"{len(duplicates)} groupe(s), "
        f"{total_images} image(s)"
    )
    print()

    for group in duplicates:
        print("-" * 76)
        print(f"SHA-256 : {group.sha256}")
        print()

        for image in group.images:
            print(f"  - {image.relative_path}")

        print()


def display_similar_images(
    similar_images: list[SimilarImageGroup],
) -> None:
    """Affiche les groupes d'images similaires."""

    print()
    print("=" * 76)
    print("IMAGES SIMILAIRES (pHash)")
    print("=" * 76)

    if not similar_images:
        print("Aucune image similaire détectée.")
        return

    total_images = sum(
        len(group.images)
        for group in similar_images
    )

    print(
        f"{len(similar_images)} groupe(s), "
        f"{total_images} image(s)"
    )
    print()

    for group in similar_images:
        print("-" * 76)
        print(f"Distance maximale : {group.max_distance}")
        print()

        for image in group.images:
            print(
                f"  - {image.relative_path} "
                f"(pHash: {image.phash})"
            )

        print()