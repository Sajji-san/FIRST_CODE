# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: InterviewNotes
def demo():
    """Запуск набора демо-команд для ручного тестирования."""
    from .notes import Note, Tag, Candidate, Interview, Rating, Decision, Solution, Question
    
    # Создаём теги
    tag1 = Tag("Python")
    tag2 = Tag("Algorithms")
    
    # Создаём кандидата
    candidate = Candidate(name="John Doe", email="john@example.com", phone="555-0100")
    
    # Создаём вопросы и оценки
    question1 = Question(text="Reverse a string", tags=[tag1])
    question2 = Question(text="Two Sum", tags=[tag1, tag2])
    question3 = Question(text="Binary Tree Traversal", tags=[tag2])
    
    rating1 = Rating(question=question1, score=8, feedback="Good logic")
    rating2 = Rating(question=question2, score=6, feedback="Needs practice")
    rating3 = Rating(question=question3, score=9, feedback="Excellent")
    
    # Создаём решение для одного вопроса
    solution = Solution(question=question1, answer="return s[::-1]", explanation="Slice with step -1")
    
    # Создаём интервью
    interview = Interview(
        candidate=candidate,
        questions=[question1, question2, question3],
        ratings=[rating1, rating2, rating3],
        solution=solution,
        decision=Decision.ACCEPTED,
        feedback="Strong Python skills"
    )
    
    # Создаём заметки
    note1 = Note(title="Python Basics", body="String manipulation is powerful")
    note2 = Note(title="Algorithms Intro", body="Start with sorting algorithms")
    
    # Демонстрация работы с объектами
    print(f"Кандидат: {candidate.name}, Email: {candidate.email}")
    print(f"Теги: {[t.name for t in [tag1, tag2]]}")
    print(f"Вопросы: {[q.text for q in interview.questions]}")
    print(f"Оценки: {[(r.question.text, r.score) for r in interview.ratings]}")
    print(f"Решение: {solution.answer if solution else 'Нет'}")
    print(f"Решение объяснение: {solution.explanation if solution else 'Нет'}")
    print(f"Интервью: {interview.decision.name}")
    print(f"Обратная связь: {interview.feedback}")
    print(f"Заметки: {[n.title for n in [note1, note2]]}")
    
    return interview

if __name__ == "__main__":
    demo()
