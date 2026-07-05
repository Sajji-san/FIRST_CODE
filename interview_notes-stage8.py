# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: InterviewNotes
def show_menu():
    print("\n=== Меню InterviewNotes ===")
    print("1. Добавить кандидата")
    print("2. Показать список кандидатов")
    print("3. Создать новый вопрос к интервью")
    print("4. Просмотреть вопросы по кандидату")
    print("5. Оценить ответ на вопрос (баллы)")
    print("6. Сохранить и выйти")
    try:
        choice = input("\nВыберите действие [1-6]: ").strip()
        return int(choice) if choice.isdigit() else 0
    except ValueError:
        return 0

def handle_add_candidate():
    name = input("Имя кандидата: ")
    role = input("Должность: ")
    candidates.append({"name": name, "role": role, "questions": [], "scores": []})
    print(f"Кандидат '{name}' добавлен.")

def handle_list_candidates():
    if not candidates:
        print("Список кандидатов пуст.")
        return
    for i, c in enumerate(candidates):
        print(f"{i+1}. {c['name']} ({c['role']}) - Вопросы: {len(c['questions'])}")

def handle_add_question():
    if not candidates:
        print("Нет добавленных кандидатов.")
        return
    idx = int(input("Номер кандидата (по списку): ")) - 1
    if idx < 0 or idx >= len(candidates):
        print("Неверный номер кандидата.")
        return
    q_text = input("Текст вопроса: ")
    candidates[idx]["questions"].append(q_text)
    print(f"Вопрос добавлен к {candidates[idx]['name']}.")

def handle_view_questions():
    if not candidates:
        print("Нет кандидатов.")
        return
    idx = int(input("Номер кандидата (по списку): ")) - 1
    if idx < 0 or idx >= len(candidates):
        print("Неверный номер кандидата.")
        return
    cand = candidates[idx]
    for i, q in enumerate(cand["questions"], 1):
        print(f"{i}. {q}")

def handle_score_question():
    if not candidates:
        print("Нет кандидатов.")
        return
    idx = int(input("Номер кандидата (по списку): ")) - 1
    if idx < 0 or idx >= len(candidates):
        print("Неверный номер кандидата.")
        return
    cand = candidates[idx]
    q_idx = int(input(f"Номер вопроса ({len(cand['questions'])}): ")) - 1
    score = int(input("Оценка (от 0 до 10): "))
    if not (0 <= score <= 10):
        print("Некорректная оценка.")
        return
    cand["scores"].append({"question_idx": q_idx, "score": score})
    print(f"Ответ оценен: {score}/10")

def main():
    candidates = []
    while True:
        choice = show_menu()
        if choice == 1: handle_add
