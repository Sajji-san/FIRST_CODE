# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: InterviewNotes
def archive_completed_interviews(interviews, cutoff_days=365):
    """Archive interviews older than cutoff_days or with final status."""
    import datetime as dt

    now = dt.datetime.now()
    cutoff = (now - dt.timedelta(days=cutoff_days)).date()
    archived = []

    for interview in interviews:
        if isinstance(interview, dict):
            created = _parse_date_internet_notes(interview.get("created", ""))
            status = interview.get("status", "").lower()
            if not created or not _is_date(created):
                continue
            record_date = min(created, now.date())
        elif hasattr(interview, "created"):
            record_date = min(_parse_date_internet_notes(str(getattr(interview, "created"))), now.date())
        else:
            continue

        if status in ("done", "closed", "archived") or _is_past(record_date, cutoff):
            interview["status"] = "archived"
            archived.append(interview)

    return [interview for interview in interviews if interview not in archived]
