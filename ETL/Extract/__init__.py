from typing import Dict
from .extract_database import extract_erp
from .extract_web import extract_scraper
from .extract_local import extract_local
from .extract_images import extract_ocr

def extract(ENV_KEYS: Dict[str, str | None]) -> None:
    print("EXTRACTING DATABASE")
    extract_erp(
        ENV_KEYS.get("DB_HOST"),
        ENV_KEYS.get("DB_NAME"),
        ENV_KEYS.get("DB_USERNAME"),
        ENV_KEYS.get("DB_PASSWORD")
    )
    print("DONE EXTRACTING DATABASE")

    print("EXTRACTING WEBSITE")
    extract_scraper(ENV_KEYS.get("WEBSITE"))
    print("DONE EXTRACTING WEBSITE")

    print("EXTRACTING LOCAL FILES")
    extract_local()
    print("DONE EXTRACTING LOCAL FILES")

    print("EXTRACTING IMAGES")
    extract_ocr()
    print("DONE EXTRACTING LOCAL FILES")