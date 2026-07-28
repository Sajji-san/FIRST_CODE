# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: InterviewNotes
def check_overdue_reminders():
    overdue = []
    today = datetime.now().date()
    for interview in all_interviews:
        if interview['reminder_date'] and interview['status'] != 'done':
            reminder_dt = datetime.combine(today, time(8, 0))
            scheduled = datetime.fromisoformat(interview['reminder_date'])
            if today > scheduled.date():
                overdue.append({
                    "interview_id": interview["id"],
                    "candidate": interview.get("candidate", ""),
                    "scheduled": str(scheduled),
                    "days_overdue": (today - scheduled.date()).days,
                })
    return overdue
