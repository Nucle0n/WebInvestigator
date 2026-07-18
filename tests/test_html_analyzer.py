import unittest

from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory

from lib.analyzer.html import (
    HTMLTitleParser,
    analyze_html_files,
    extract_html_title,
)
from lib.model.inventory import (
    FileInfo,
    Inventory,
)


class HTMLTitleParserTests(unittest.TestCase):
    def test_extracts_title(self) -> None:
        parser = HTMLTitleParser()

        parser.feed(
            "<html><head><title>Hello World</title></head></html>"
        )
        parser.close()

        self.assertEqual(
            parser.title,
            "Hello World",
        )
    
    def test_normalizes_title_whitespace(self) -> None:
        parser = HTMLTitleParser()

        parser.feed(
            """
            <html>
                <head>
                    <title>
                        Contact
                        – AtelierdeLea
                    </title>
                </head>
            </html>
            """
        )
        parser.close()

        self.assertEqual(
            parser.title,
            "Contact – AtelierdeLea",
        )
    
    def test_keeps_first_title(self) -> None:
        parser = HTMLTitleParser()

        parser.feed(
            """
            <html>
                <head>
                    <title>Real title</title>
                </head>
                <body>
                    <svg>
                        <title>Visa</title>
                    </svg>
                </body>
            </html>
            """
        )
        parser.close()

        self.assertEqual(
            parser.title,
            "Real title",
        )

    def test_extract_html_title(self) -> None:
        with TemporaryDirectory() as directory:
            html_path = Path(directory) / "index.html"

            html_path.write_text(
                """
                <html>
                    <head>
                        <title>Example page</title>
                    </head>
                </html>
                """,
                encoding="utf-8",
            )

            self.assertEqual(
                extract_html_title(html_path),
                "Example page",
            )
            
    def test_analyze_html_files(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)

            html_path = root / "index.html"
            text_path = root / "notes.txt"

            html_path.write_text(
                """
                <html>
                    <head>
                        <title>Home</title>
                    </head>
                </html>
                """,
                encoding="utf-8",
            )

            text_path.write_text(
                "Not an HTML page",
                encoding="utf-8",
            )

            inventory = Inventory(
                files=[
                    FileInfo(
                        path=html_path,
                        relative_path=Path("index.html"),
                        extension=".html",
                        size=html_path.stat().st_size,
                    ),
                    FileInfo(
                        path=text_path,
                        relative_path=Path("notes.txt"),
                        extension=".txt",
                        size=text_path.stat().st_size,
                    ),
                ],
                extension_counts=Counter(
                    {
                        ".html": 1,
                        ".txt": 1,
                    }
                ),
                total_size=(
                    html_path.stat().st_size
                    + text_path.stat().st_size
                ),
            )

            html_pages = analyze_html_files(
                inventory,
            )

            self.assertEqual(
                len(html_pages),
                1,
            )

            self.assertEqual(
                html_pages[0].title,
                "Home",
            )

            self.assertEqual(
                html_pages[0].relative_path,
                Path("index.html"),
            )


if __name__ == "__main__":
    unittest.main()
