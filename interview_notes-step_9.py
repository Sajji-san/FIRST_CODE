# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: InterviewNotes
import json

INITIAL_DATA = """[{"id":1,"name":"Алексей","position":"Backend Dev","interviews":[{"id":101,"date":"2024-03-05","questions":[{"text":"Как работает REST API?", "answer":"...", "score":8}, {"text":"Что такое Redis?", "answer":"...", "score":7}], "verdict":"Passed"}]},{"id":2,"name":"Мария","position":"Frontend Dev","interviews":[{"id":102,"date":"2024-03-06","questions":[{"text":"Как работает React?", "answer":"...", "score":9}, {"text":"CSS Grid vs Flexbox", "answer":"...", "score":8}], "verdict":"Passed"}]}]"""

def load_initial_data():
    return json.loads(INITIAL_DATA)

candidates = load_initial_data()
print(f"Загружено {len(candidates)} кандидатов:")
for c in candidates:
    print(f"  - {c['name']} ({c['position']})")
