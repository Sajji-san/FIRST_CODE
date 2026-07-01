# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: InterviewNotes
def filter_interviews(status=None, category=None, tags=None):
    filtered = []
    for interview in interviews:
        if status and interview.get('status') != status:
            continue
        if category and interview.get('category') != category:
            continue
        if tags:
            interview_tags = set(interview.get('tags', []))
            if not any(tag in interview_tags for tag in tags):
                continue
        filtered.append(interview)
    return filtered
