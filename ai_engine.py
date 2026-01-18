import json
from pathlib import Path
from typing import Dict, Iterable, List, Optional

RULES_PATH = Path(__file__).with_name("ai_rules.json")


def load_rules(path: Optional[str] = None) -> Dict:
    target = Path(path) if path else RULES_PATH
    with target.open() as fh:
        return json.load(fh)


def _has_forced_action(actions: Iterable[str], rules: Dict) -> bool:
    forced_keywords = rules.get("forced_manual_actions", [])
    for action in actions:
        normalized = action.lower()
        for keyword in forced_keywords:
            if keyword.lower() in normalized:
                return True
    return False


def calculate_risk_score(
    rows: List[Dict],
    change_type: str,
    impacted_areas: List[str],
) -> List[Dict]:
    """Calculate per-service risk score and risk level (no ratio logic)."""
    change_type_value = (change_type or "Minor").strip().lower()
    impacted_values = [value.lower() for value in (impacted_areas or [])]

    change_type_score = 25 if change_type_value == "major" else 10
    max_possible = 25 + 25 + 25 + 10 + 10 + 15 + 10 + 5 + 8

    scored_rows = []
    for row in rows:
        total = change_type_score

        priority_value = str(row.get("priority", "")).strip().lower()
        if priority_value in ("1", "high"):
            total += 25
        elif priority_value in ("2", "medium"):
            total += 15
        else:
            total += 5

        security_value = str(
            row.get("security priority", row.get("security", ""))
        ).strip().lower()
        if security_value == "high":
            total += 25
        elif security_value == "medium":
            total += 15
        else:
            total += 5

        if str(row.get("evidence mobile", "")).strip().upper() == "Y" or row.get("mobile"):
            total += 10
        if str(row.get("evidence web console", "")).strip().upper() == "Y" or row.get("web_console"):
            total += 10

        if str(row.get("need actual car", "")).strip().upper() == "Y" or row.get("need_actual_car"):
            total += 15

        if any(keyword in impacted_values for keyword in ("ios", "android", "huawei")):
            total += 10
        if any(keyword in impacted_values for keyword in ("rts", "batch", "api")):
            total += 5
        if "common tenant" in impacted_values:
            total += 8

        risk_score = int(round((total / max_possible) * 100))
        if risk_score >= 70:
            risk_level = "High"
        elif risk_score >= 40:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        scored_row = dict(row)
        scored_row["risk_score"] = risk_score
        scored_row["risk_level"] = risk_level
        scored_rows.append(scored_row)

    return scored_rows


def calculate_test_ratio(rows: List[Dict]) -> Dict:
    """Calculate manual/auto ratio from Action field only."""
    manual_actions = {"test drive", "vehicle support", "application"}
    manual_count = 0
    total = 0

    for row in rows:
        total += 1
        actions = row.get("actions") or row.get("action") or []
        if isinstance(actions, str):
            action_list = [actions]
        else:
            action_list = list(actions)
        if any(action.strip().lower() in manual_actions for action in action_list):
            manual_count += 1

    if total:
        manual_percent = int(round((manual_count / total) * 100))
    else:
        manual_percent = 0
    auto_percent = 100 - manual_percent if total else 0

    return {
        "manual_percent": manual_percent,
        "auto_percent": auto_percent,
        "manual_count": manual_count,
        "auto_count": total - manual_count,
    }


def _normalize_level(value: Optional[str]) -> str:
    if not value:
        return "medium"
    return str(value).strip().lower()


def _score_level(level: str) -> int:
    if level == "high":
        return 25
    if level == "medium":
        return 15
    return 5


def _value_is_yes(value: Optional[object]) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return str(value).strip().lower() == "y"


def _has_backend_flag(row: Dict, impacted_areas: List[str]) -> bool:
    if _value_is_yes(row.get("backend")) or _value_is_yes(row.get("api")) or _value_is_yes(row.get("batch")):
        return True
    for area in impacted_areas:
        lowered = area.lower()
        if "backend" in lowered or "api" in lowered or "batch" in lowered:
            return True
    return False


def _has_common_tenant_flag(row: Dict, impacted_areas: List[str]) -> bool:
    tenant = str(row.get("tenant_requirement") or "").lower()
    if "common tenant" in tenant:
        return True
    for area in impacted_areas:
        if "common tenant" in area.lower():
            return True
    return False

def evaluate_service(service: Dict, context: Dict, rules: Optional[Dict] = None) -> Dict:
    rules = rules or load_rules()
    actions = service.get("actions", [])

    if _has_forced_action(actions, rules):
        return {
            "risk_score": 100,
            "recommended_type": "Manual",
            "manual_percent": 100,
            "auto_percent": 0,
            "forced_manual": True,
        }

    priority = service.get("priority", "Medium").lower()
    security = service.get("security", "Medium").lower()
    priority_score = rules.get("priority_weights", {}).get(priority, 1)
    security_score = rules.get("security_weights", {}).get(security, 1)

    risk = (priority_score + security_score) * 10

    scenario_rules = rules.get("scenario", {})
    scenario_weight = scenario_rules.get("weight", 1)
    scenario_cap = scenario_rules.get("cap", 30)
    risk += min(service.get("scenarios", 0) * scenario_weight, scenario_cap)

    change_type = context.get("change_type", "Minor")
    risk += rules.get("change_type", {}).get(change_type, 0)

    requirement_type = context.get("requirement_type", "Common")
    risk += rules.get("requirement_type", {}).get(requirement_type, 0)

    platform = context.get("platform", "Unknown")
    risk += rules.get("platform", {}).get(platform, 0)


    max_risk = rules.get("max_risk", 100)
    risk_score = int(round(max(0, min(risk, max_risk))))

    ratio_map: List[Dict] = sorted(
        rules.get("ratio_map", []), key=lambda item: item.get("min_risk", 0), reverse=True
    )

    recommended_type = "Automation"
    manual_percent = 0
    auto_percent = 100

    for template in ratio_map:
        if risk_score >= template.get("min_risk", 0):
            recommended_type = template.get("type", "Automation")
            manual_percent = template.get("manual", 0)
            auto_percent = template.get("auto", 100)
            break
    else:
        if ratio_map:
            fallback = ratio_map[-1]
            recommended_type = fallback.get("type", "Automation")
            manual_percent = fallback.get("manual", 0)
            auto_percent = fallback.get("auto", 100)

    return {
        "risk_score": risk_score,
        "recommended_type": recommended_type,
        "manual_percent": manual_percent,
        "auto_percent": auto_percent,
        "forced_manual": False,
    }
