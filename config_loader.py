import json
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).resolve().parent


def load_countries(path: Path | str | None = None) -> List[Dict]:
    target = Path(path) if path else BASE_DIR / "countries.json"
    with target.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_impacted_areas(path: Path | str | None = None) -> List[str]:
    target = Path(path) if path else BASE_DIR / "impacted_areas.json"
    with target.open(encoding="utf-8") as fh:
        return json.load(fh)