from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
}

COLLAPSED_DIRECTORIES = {
    "docs",
    "investigations",
}

TEXT_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".html",
    ".htm",
    ".css",
    ".js",
    ".ts",
    ".toml",
    ".ini",
    ".cfg",
    ".csv",
    ".xml",
}

@dataclass(slots=True)
class SnapshotOptions:
    show_all: bool = False
    show_size: bool = False
    show_lines: bool = False
    entry_width: int = 0


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"

    size_kb = size_bytes / 1024

    if size_kb < 1024:
        return f"{size_kb:.1f} KB"

    size_mb = size_kb / 1024
    return f"{size_mb:.1f} MB"


def count_lines(file_path: Path) -> int | None:
    if file_path.suffix.lower() not in TEXT_EXTENSIONS:
        return None

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return sum(1 for _ in file)
    except (UnicodeDecodeError, OSError):
        return None

def iter_directory_entries(directory: Path) -> list[Path]:
    entries = []

    for entry in directory.iterdir():
        if entry.is_dir() and entry.name in IGNORED_DIRECTORIES:
            continue

        entries.append(entry)

    return sorted(
        entries,
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    
def find_longest_entry_width(
    directory: Path,
    prefix: str = "",
) -> int:
    longest = 0
    entries = iter_directory_entries(directory)

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "

        name = entry.name

        if entry.is_dir():
            name += "/"

        entry_width = len(
            f"{prefix}{connector}{name}"
        )

        longest = max(longest, entry_width)

        if (
            entry.is_dir()
            and entry.name not in COLLAPSED_DIRECTORIES
        ):
            child_prefix = (
                prefix + "    "
                if is_last
                else prefix + "│   "
            )

            longest = max(
                longest,
                find_longest_entry_width(
                    directory=entry,
                    prefix=child_prefix,
                ),
            )

    return longest

def format_entry(
    entry: Path,
    prefix: str,
    is_last: bool,
    options: SnapshotOptions,
) -> str:

    connector = "└── " if is_last else "├── "

    name = entry.name

    if entry.is_dir():
        name += "/"

    result = (
        f"{prefix}"
        f"{connector}"
        f"{name}"
    )

    result = result.ljust(options.entry_width)

    if entry.is_file():

        if options.show_size:

            size_bytes = entry.stat().st_size

            if size_bytes == 0:
                size = "-"
            else:
                size = format_size(size_bytes)

            result += f"    {size:^8}"

        if options.show_lines:

            line_count = count_lines(entry)

            if line_count is None:
                line_info = " "

            elif line_count == 0:
                line_info = " "

            else:
                label = (
                    "line"
                    if line_count == 1
                    else "lines"
                )

                line_info = f"{line_count} {label}"

            result += f"    {line_info:^10}"

    return result

def walk_directory(
    directory: Path,
    lines: list[str],
    options: SnapshotOptions,
    prefix: str = "",
) -> None:

    entries = iter_directory_entries(directory)

    for index, entry in enumerate(entries):

        is_last = index == len(entries) - 1

        lines.append(
            format_entry(
                entry=entry,
                prefix=prefix,
                is_last=is_last,
                options=options,
            )
        )

        if entry.is_dir():

            if (
                not options.show_all
                and entry.name in COLLAPSED_DIRECTORIES
            ):
                child_prefix = (
                    prefix + "    "
                    if is_last
                    else prefix + "│   "
                )

                connector = "└── "

                lines.append(
                    f"{child_prefix}{connector}... (collapsed)"
                )

                continue

            child_prefix = (
                prefix + "    "
                if is_last
                else prefix + "│   "
            )

            walk_directory(
                directory=entry,
                lines=lines,
                options=options,
                prefix=child_prefix,
            )

def build_snapshot(
    options: SnapshotOptions,
) -> list[str]:

    header = []

    if options.show_size:
        header.append("Size")

    if options.show_lines:
        header.append("Lines")

    title = "## Repository Snapshot"

    if header:
        title += f" ({' + '.join(header)})"

    lines = [
        title,
        "",
        "```text",
        f"{ROOT_DIR.name}/",
    ]

    walk_directory(
        directory=ROOT_DIR,
        lines=lines,
        options=options,
    )

    lines.append("```")

    return lines

def parse_flags() -> set[str]:
    valid_flags = {"e", "h", "s", "l"}
    flags: set[str] = set()

    for argument in sys.argv[1:]:

        if not argument.startswith("-"):
            raise ValueError(
                f"Unexpected argument: {argument}"
            )

        for flag in argument[1:]:

            if flag not in valid_flags:
                raise ValueError(
                    f"Unknown option: -{flag}"
                )

            flags.add(flag)
        
        if "h" in flags:
            print(
                """
        Repository Snapshot

        Usage:
            repository_snapshot.py [-s] [-l]

        Options:
            -e    Expand all directories
            -s    Show file sizes
            -l    Show line counts
            -h    Show this help
        """.strip()
            )
            sys.exit(0)
        
    return flags
    
def parse_options() -> SnapshotOptions:
    flags = parse_flags()
    entry_width = find_longest_entry_width(ROOT_DIR)

    return SnapshotOptions(
        show_all="e" in flags,
        show_size="s" in flags,
        show_lines="l" in flags,
        entry_width=entry_width,
    )

def main() -> None:
    try:
        options = parse_options()
        snapshot = build_snapshot(options)

        print("\n".join(snapshot))

    except ValueError as error:
        print(error)
        sys.exit(1)

if __name__ == "__main__":
    main()