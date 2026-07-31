# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: InterviewNotes
def show_interview_note(interview):
    """Компактный вывод одной записи собеседования."""
    if not interview:
        return
    print(f"=== Интервью: {interview.get('candidate', 'Неизвестный')} ===")
    print(f"Дата: {interview.get('date', '—')}\n")

    questions = interview.get("questions", [])
    for q in questions[:5]:  # показываем до 5 вопросов
        tags = ", ".join(q.get("tags", [])) if isinstance(q, dict) and q.get("tags") else "—"
        print(f"Вопрос: {q.get('text', '—')} (теги: {tags})")
        if isinstance(q, dict):
            score = q.get("score", 0)
            decision = q.get("decision", None)
            print(f"Оценка: {score}/10 — Решение: {decision or 'Нет'}")
        print()

    summary = interview.get("summary", "")
    if summary:
        print(f"\nРезюме интервью: {summary}")

    verdict = interview.get("verdict", "Без вердикта")
    print(f"Итог: {verdict}")
