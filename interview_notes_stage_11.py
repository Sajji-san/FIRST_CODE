# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: InterviewNotes
import json, os

DATA_FILE = "interview_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"candidates": [], "questions": [], "interviews": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
