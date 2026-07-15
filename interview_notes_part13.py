# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: InterviewNotes
def search_interviews(query, fields=None):
    if fields is None:
        fields = ['candidate', 'position']
    results = []
    for interview in all_interviews:
        match = True
        for field in fields:
            val = getattr(interview, field, '').lower()
            q = query.lower()
            if q not in val:
                match = False
                break
        if match:
            results.append(interview)
    return results
