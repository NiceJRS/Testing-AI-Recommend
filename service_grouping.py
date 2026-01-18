from typing import List, Dict


def derive_platform(mobile: bool, web_console: bool) -> str:
    if mobile and web_console:
        return "Both"
    if mobile:
        return "Mobile"
    if web_console:
        return "Web"
    return "Unknown"


def aggregate_service_groups(rows: List[Dict]) -> List[Dict]:
    groups: Dict[str, Dict] = {}
    for row in rows:
        service = row.get("service", "").strip()
        if not service:
            continue

        group = groups.setdefault(
            service,
            {
                "service": service,
                "scenarios": 0,
                "priority": None,
                "priority_rank": float("inf"),
                "security": row.get("security", "Medium"),
                "country": row.get("country", ""),
                "mobile": False,
                "web_console": False,
                "actions": [],
            },
        )

        group["scenarios"] += 1
        action = row.get("action")
        if action:
            group["actions"].append(action)

        priority = row.get("priority", "").lower()
        ranking = {"high": 1, "medium": 2, "low": 3}
        if priority in ranking:
            rank = ranking[priority]
            if rank < group["priority_rank"]:
                group["priority_rank"] = rank
                group["priority"] = priority.capitalize()

        security = row.get("security")
        if security and not group["security"]:
            group["security"] = security

        country = row.get("country")
        if country and not group["country"]:
            group["country"] = country

        group["mobile"] = group["mobile"] or row.get("mobile", False)
        group["web_console"] = group["web_console"] or row.get("web_console", False)

    for group in groups.values():
        group["platform"] = derive_platform(group["mobile"], group["web_console"])

    sorted_groups = sorted(groups.values(), key=lambda g: g["service"])
    for idx, group in enumerate(sorted_groups, start=1):
        if not group.get("priority"):
            group["priority"] = "Medium"
        if not group.get("security"):
            group["security"] = "Medium"
    return sorted_groups
