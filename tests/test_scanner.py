import tempfile
import unittest
from pathlib import Path

from lib.scanner import normalize_extension, scan_directory


class NormalizeExtensionTests(unittest.TestCase):
    def test_normalizes_extension_to_lowercase(self) -> None:
        path = Path("example.PNG")

        self.assertEqual(normalize_extension(path), ".png")

    def test_returns_placeholder_when_extension_is_missing(self) -> None:
        path = Path("LICENSE")

        self.assertEqual(
            normalize_extension(path),
            "[sans extension]",
        )


class ScanDirectoryTests(unittest.TestCase):
    def test_builds_inventory_from_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            text_content = b"hello"
            image_content = b"fake image"
            no_extension_content = b"license"

            (root / "document.txt").write_bytes(text_content)
            (root / "picture.PNG").write_bytes(image_content)
            (root / "LICENSE").write_bytes(no_extension_content)

            inventory = scan_directory(root)

            self.assertEqual(len(inventory.files), 3)

            self.assertEqual(
                inventory.total_size,
                (
                    len(text_content)
                    + len(image_content)
                    + len(no_extension_content)
                ),
            )

            self.assertEqual(inventory.extension_counts[".txt"], 1)
            self.assertEqual(inventory.extension_counts[".png"], 1)
            self.assertEqual(
                inventory.extension_counts["[sans extension]"],
                1,
            )

    def test_scans_subdirectories_recursively(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            nested_directory = root / "assets" / "images"
            nested_directory.mkdir(parents=True)

            nested_file = nested_directory / "example.jpg"
            nested_file.write_bytes(b"image")

            inventory = scan_directory(root)

            self.assertEqual(len(inventory.files), 1)
            self.assertEqual(
                inventory.files[0].relative_path,
                Path("assets/images/example.jpg"),
            )


if __name__ == "__main__":
    unittest.main()
