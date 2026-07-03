# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: InterviewNotes
def sort_interviews(key='date', reverse=False):
    if key == 'date':
        return sorted(interview_list, key=lambda x: x.get('scheduled_date') or '', reverse=reverse)
    elif key == 'priority':
        priority_map = {'high': 0, 'medium': 1, 'low': 2}
        return sorted(interview_list, key=lambda x: priority_map.get(x.get('priority', 'medium'), 1), reverse=not reverse)
    elif key == 'name':
        return sorted(interview_list, key=lambda x: (x.get('candidate_name') or '').lower(), reverse=False)
    else:
        raise ValueError(f"Неподдерживаемый ключ сортировки: {key}")

def get_sorted_interviews():
    """Получить отсортированный список собеседований по умолчанию (по дате)."""
    return sort_interviews('date')
