# === Stage 17: Добавь группировку записей по категориям ===
# Project: InterviewNotes
def group_by_category(records):
    """Group interview records by their category field."""
    result = {}
    for record in records:
        cat = record.get("category", "Uncategorized")
        result.setdefault(cat, []).append(record)
    return dict(sorted(result.items()))


if __name__ == "__main__":
    data = [
        {"id": 1, "question": "Tell me about yourself.", "answer": "...", "rating": 5, "category": "Intro"},
        {"id": 2, "question": "What is Python?", "answer": "...", "rating": 4, "category": "Tech"},
        {"id": 3, "question": "Describe a project.", "answer": "...", "rating": 5, "category": "Intro"},
        {"id": 4, "question": "Explain closures.", "answer": "...", "rating": 3, "category": "Tech"},
    ]
    grouped = group_by_category(data)
    for cat, recs in grouped.items():
        print(f"{cat}:")
        for r in recs:
            print(f"  - {r['question']} (rating={r['rating']})")
