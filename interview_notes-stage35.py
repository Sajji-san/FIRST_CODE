# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: InterviewNotes
def get_next_action(state):
    """Returns a single-line recommendation string based on current interview state."""
    if state.get("candidate") is None:
        return "Начните с создания нового кандидата."
    if state.get("questions", []).get("count") == 0:
        return "Добавьте первый вопрос интервью."
    if state.get("questions", []).get("count") == state.get("questions", {}).get("total", 0):
        return "Все вопросы добавлены — оцените ответы и запишите итоговое решение."
    if state.get("questions", []).get("count", 0) < state.get("questions", {}).get("total", 0):
        return "Продолжайте добавлять вопросы интервью."
    if state.get("questions", {}).get("total", 0) == 0:
        return "Определите количество вопросов для этого интервью."
    return "Продолжайте заполнять данные интервью."
