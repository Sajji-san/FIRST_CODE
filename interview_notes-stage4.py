# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: InterviewNotes
def edit_interview_note(note_id: int, updates: dict) -> InterviewNote | None:
    if note_id not in notes_db:
        return None
    existing = notes_db[note_id]
    for key, value in updates.items():
        if hasattr(existing, key):
            setattr(existing, key, value)
        elif key == 'questions':
            existing.questions.extend(value)
        elif key == 'solutions':
            existing.solutions.update(value)
    return notes_db[note_id]
