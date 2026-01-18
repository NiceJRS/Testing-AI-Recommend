from typing import Iterable, Dict, List

from config_loader import load_countries

COUNTRY_CONFIG = load_countries()
COUNTRY_CODES = [
    entry.get("code", "").upper()
    for entry in COUNTRY_CONFIG
    if entry.get("code")
]


def filter_rows(
    rows: Iterable[Dict],
    requirement_type: str,
    country_code: str,
    country_codes: List[str],
) -> List[Dict]:
    requirement_type = (requirement_type or "").lower()
    country_code = (country_code or "").upper()
    except_phrase = f"except {country_code.lower()}" if country_code else ""
    other_codes = {
        code.upper() for code in country_codes if code and code.upper() != country_code
    }

    filtered = []
    for row in rows:
        tenant = str(row.get("tenant_requirement", "")).strip()
        if not tenant:
            continue

        lowered = tenant.lower()

        if requirement_type == "common":
            if "common" in lowered:
                if country_code and except_phrase in lowered:
                    continue
                filtered.append(row)
                continue

            if country_code and country_code.lower() in lowered:
                if except_phrase in lowered:
                    continue
                filtered.append(row)
                continue

            continue

        if requirement_type == "local":
            if not country_code:
                continue
            if country_code.lower() not in lowered:
                continue
            if "common" in lowered:
                continue
            if except_phrase and except_phrase in lowered:
                continue
            if any(other.lower() in lowered for other in other_codes):
                continue
            filtered.append(row)
            continue

        filtered.append(row)

    return filtered
