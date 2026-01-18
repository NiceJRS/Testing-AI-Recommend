from typing import Iterable, Tuple, Dict, List


def derive_platform(mobile: bool, web_console: bool) -> str:
    if mobile and web_console:
        return "Both"
    if mobile:
        return "Mobile"
    if web_console:
        return "Web"
    return "Unknown"


def aggregate_service_rows(rows: Iterable[Dict]) -> Tuple[List[List[str]], List[Dict]]:
    priority_rank = {"high": 1, "medium": 2, "low": 3}
    groups: Dict[str, Dict] = {}

    for row in rows:
        service = row.get("service", "").strip()
        if not service:
            continue

        priority = row.get("priority", "Medium").strip()
        security = row.get("security", "Medium").strip()

        mobile = row.get("mobile", False)
        web_console = row.get("web_console", False)
        country = row.get("country", "").strip()
        actions = list(row.get("actions", []))
        need_actual_car = row.get("need_actual_car", False)
        tenant_requirement = row.get("tenant_requirement", "")

        group = groups.get(service)
        if not group:
            group = {
                "service": service,
                "scenarios": 0,
                "priority": priority.capitalize() or "Medium",
                "priority_rank": float("inf"),
                "security": security or "Medium",
                "country": country,
                "mobile": mobile,
                "web_console": web_console,
                "actions": actions,
                "need_actual_car": need_actual_car,
                "tenant_requirement": tenant_requirement,
            }
            groups[service] = group

        group["scenarios"] += 1
        group["actions"].extend(actions)

        normalized_priority = priority.lower()
        if normalized_priority in priority_rank:
            rank = priority_rank[normalized_priority]
            if rank < group["priority_rank"]:
                group["priority_rank"] = rank
                group["priority"] = normalized_priority.capitalize()

        if security and not group["security"]:
            group["security"] = security

        if country and not group["country"]:
            group["country"] = country

        if mobile:
            group["mobile"] = True
        if web_console:
            group["web_console"] = True
        if need_actual_car:
            group["need_actual_car"] = True
        if tenant_requirement and not group.get("tenant_requirement"):
            group["tenant_requirement"] = tenant_requirement

    for group in groups.values():
        group["platform"] = derive_platform(group["mobile"], group["web_console"])

    sorted_groups = sorted(groups.values(), key=lambda g: g["service"])
    rows_table: List[List[str]] = []
    for idx, group in enumerate(sorted_groups, start=1):
        rows_table.append(
            [
                str(idx),
                group["service"],
                str(group["scenarios"]),
                group["priority"],
                group["security"],
                "Y" if group["mobile"] else "N",
                "Y" if group["web_console"] else "N",
                   group["country"],
            ]
        )

    return rows_table, sorted_groups
