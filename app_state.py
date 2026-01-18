"""Shared in-memory application state."""

app_context = {
    "raw_rows": [],
    "raw_headers": [],
    "filtered_rows": [],
    "aggregated_rows": [],
    "service_groups": [],
    "filtered_groups": [],
    "ai_results": [],
    "risk_score": 0,
    "ratio_result": {},
}
