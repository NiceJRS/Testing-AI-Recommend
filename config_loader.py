import json
from pathlib import Path
from typing import List, Dict

from utils.path_helper import resource_path


def load_countries(path: Path | str | None = None) -> List[Dict]:
    target = Path(path) if path else resource_path("rules/countries.json")
    with target.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_impacted_areas(path: Path | str | None = None) -> List[str]:
    target = Path(path) if path else resource_path("rules/impacted_areas.json")
    with target.open(encoding="utf-8") as fh:
        return json.load(fh)