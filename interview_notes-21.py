# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: InterviewNotes
class Reminder:
    def __init__(self, title, date_str):
        self.title = title
        self.date_str = date_str
        self.is_done = False

    def is_due(self):
        from datetime import date
        today = date.today()
        if not self.is_done and today >= date.fromisoformat(self.date_str):
            return True
        return False

    def __repr__(self):
        status = "Done" if self.is_done else ("Due!" if self.is_due() else "Pending")
        return f"<Reminder: {self.title} [{status}]>"

# Пример использования напоминаний для интервью
reminders = [
    Reminder("Подготовить вопросы про алгоритмы", "2024-12-15"),
    Reminder("Отправить письмо кандидату", "2024-12-20"),
]

for r in reminders:
    print(r)
