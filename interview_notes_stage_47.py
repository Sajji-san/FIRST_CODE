# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: InterviewNotes
def demo():
    print("=" * 60)
    print("Интервью: Алина, Senior Python Developer")
    print("=" * 60)

    # Создаём кандидатов и вопросы
    alina = Candidate(name="Алина", exp_years=5, role="Senior Python Developer")
    ivan = Candidate(name="Иван", exp_years=2, role="Junior Python Developer")
    questions = [
        Question("Опишите паттерн Singleton.", "Python", 10),
        Question("Как работает GIL?", "Python", 8),
        Question("Что такое дескриптор?", "Python", 12),
        Question("Объясните работу asyncio.", "Python", 9),
    ]

    # Интервью Алины — успешно
    print("\n--- Интервью Алины ---")
    for q in questions:
        score = random.randint(8, 10)
        alina.add_question(q, score)
        print(f"[{q.subject}] Оценка: {score}/10")
    alina.set_decision("Passed", "Отличная кандидатура")
    alina.print_report()

    # Интервью Ивана — не прошёл
    print("\n--- Интервью Ивана ---")
    for q in questions:
        score = random.randint(3, 6)
        ivan.add_question(q, score)
        print(f"[{q.subject}] Оценка: {score}/10")
    ivan.set_decision("Rejected", "Не достаточно опыта")
    ivan.print_report()

    # Выводим статистику
    print("\n--- Итоговая статистика ---")
    print(f"Прошло интервью: {sum(1 for c in candidates if c.decision == 'Passed')}")
    print(f"Не прошло: {sum(1 for c in candidates if c.decision == 'Rejected')}")
    print(f"Всего вопросов: {sum(len(c.questions) for c in candidates)}")
    print("\nДемо завершён.")
