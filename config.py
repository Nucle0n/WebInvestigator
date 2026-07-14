from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent

SITE_MIRROR_DIR = (
    PROJECT_ROOT
    / "01_site"
    / "atelierdelea.shop"
    / "atelierdelea.shop"
)

REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_JSON_DIR = REPORTS_DIR / "json"
REPORTS_CSV_DIR = REPORTS_DIR / "csv"
REPORTS_HTML_DIR = REPORTS_DIR / "html"
LOGS_DIR = PROJECT_ROOT / "logs"


def create_output_directories() -> None:
    """Crée les dossiers de sortie manquants."""
    directories = (
        REPORTS_JSON_DIR,
        REPORTS_CSV_DIR,
        REPORTS_HTML_DIR,
        LOGS_DIR,
    )

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)