# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: InterviewNotes
def print_summary(data):
    """Генерирует краткую сводку по текущим данным проекта."""
    interviews = data.get("interviews", [])
    candidates = {name: info for name, info in data.get("candidates", {}).items()}
    
    if not interviews and not candidates:
        print("\n📊 Сводка проекта InterviewNotes\n" + "=" * 40)
        return
    
    total = len(interviews)
    completed = sum(1 for i in interviews if "result" in i.get("interview", {}))
    
    print(f"\n📊 Сводка проекта InterviewNotes")
    print("=" * 40)
    print(f"💼 Всего интервью: {total}")
    print(f"✅ Завершено: {completed} из {total}")
    if candidates:
        print(f"👤 Кандидаты в базе: {len(candidates)}")
    
    for i in interviews:
        name = i.get("name", "Без имени")
        result = i["interview"].get("result", {}).get("status", "?")
        score = i["interview"].get("score", 0)
        print(f"  • {name}: [{result}] (Оценка: {score})")

if __name__ == "__main__":
    sample_data = {"interviews": [{"name": "Алексей", "interview": {"result": {"status": "passed"}, "score": 85}}, {"name": "Мария", "interview": {"result": {"status": "rejected"}, "score": 42}}], "candidates": {}}
    print_summary(sample_data)
