# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: InterviewNotes
TEMPLATES = {
    "python": {
        "questions": [
            "1. Describe yourself.",
            "2. What is your experience with Python?",
            "3. How do you handle errors?",
            "4. Explain your last project.",
            "5. What are your strengths?",
        ],
        "scoring": {
            "communication": (1, 10, "Communication"),
            "technical": (1, 10, "Technical Skills"),
            "problem_solving": (1, 10, "Problem Solving"),
        },
        "final": ["Hired", "Rejected", "Maybe"],
    },
    "java": {
        "questions": [
            "1. Describe yourself.",
            "2. What is your experience with Java?",
            "3. How do you handle concurrency?",
            "4. Explain your last project.",
            "5. What are your strengths?",
        ],
        "scoring": {
            "communication": (1, 10, "Communication"),
            "technical": (1, 10, "Technical Skills"),
            "problem_solving": (1, 10, "Problem Solving"),
        },
        "final": ["Hired", "Rejected", "Maybe"],
    },
}

def get_template(language="python"):
    if language not in TEMPLATES:
        raise ValueError(f"Unknown language template: {language}. Available: {list(TEMPLATES.keys())}")
    return TEMPLATES[language]
