# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: InterviewNotes
import json, base64

def export_state_to_json():
    """Экспортирует текущее состояние всех данных в JSON-строку."""
    state = {
        'candidates': list(candidates.values()),
        'interviews': list(interviews.values()),
        'questions': list(questions.values()),
        'evaluations': dict(evaluations),
        'decisions': list(decisions.values()) if decisions else None,
    }
    return json.dumps(state, indent=2)

if __name__ == '__main__':
    print(export_state_to_json())
