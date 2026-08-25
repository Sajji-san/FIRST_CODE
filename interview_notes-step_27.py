# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: InterviewNotes
def reset_demo_data():
    """Сбросить все демо-данные и вернуть пустые коллекции."""
    global candidates, questions, interviews, results
    candidates = []
    questions = []
    interviews = []
    results = []

def clear_state():
    """Полная очистка состояния приложения: сброс данных + сброс UI."""
    reset_demo_data()
    selected_candidate = None
    selected_question = None
    current_interview = None
