from html.parser import HTMLParser
from pathlib import Path

from lib.model.html import HTMLPage
from lib.model.inventory import Inventory


class HTMLTitleParser(HTMLParser):
    """Extract the document title from an HTML document."""

    def __init__(self) -> None:
        super().__init__()

        self.title: str | None = None
        self._inside_title = False
        self._title_processed = False
        self._title_parts: list[str] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        if tag == "title" and not self._title_processed:
            self._inside_title = True
            self._title_parts = []

    def handle_endtag(
        self,
        tag: str,
    ) -> None:
        if tag == "title" and self._inside_title:
            raw_title = "".join(self._title_parts)
            normalized_title = " ".join(raw_title.split())

            if normalized_title:
                self.title = normalized_title

            self._inside_title = False
            self._title_processed = True

    def handle_data(
        self,
        data: str,
    ) -> None:
        if self._inside_title:
            self._title_parts.append(data)


def extract_html_title(
    html_path: Path,
) -> str | None:
    """Extract the title from an HTML file."""

    parser = HTMLTitleParser()

    parser.feed(
        html_path.read_text(
            encoding="utf-8",
            errors="ignore",
        )
    )

    parser.close()

    return parser.title


def analyze_html_files(
    inventory: Inventory,
) -> list[HTMLPage]:
    """Analyze mirrored HTML pages."""

    html_pages: list[HTMLPage] = []

    for file in inventory.files:
        if file.path.suffix.lower() != ".html":
            continue

        title = extract_html_title(file.path)

        html_pages.append(
            HTMLPage(
                path=file.path,
                relative_path=file.relative_path,
                title=title,
            )
        )

    return html_pages
