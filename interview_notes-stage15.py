# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: InterviewNotes
def weekly_stats(interviews):
    from collections import defaultdict, Counter
    weeks = defaultdict(Counter)
    for i in interviews:
        dt = i.get("date") or datetime.fromisoformat(i["created_at"]) if isinstance(i.get("created_at"), str) else None
        if not dt:
            continue
        week_key = (dt.year, (dt.weekday() + dt.day) // 7)
        weeks[week_key][i["id"]] += 1
    return {"year": list(weeks.keys())[0][0] if weeks else None, "weekly": dict(weeks)}
