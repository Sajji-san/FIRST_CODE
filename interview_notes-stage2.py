# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: InterviewNotes
class InterviewData:
    def __init__(self):
        self.candidates = {}
        self.interviews = []
    
    def validate_name(self, name: str) -> bool:
        if not isinstance(name, str) or len(name.strip()) < 2:
            return False
        return True
    
    def validate_score(self, score: float) -> bool:
        try:
            s = float(score)
            return 0.0 <= s <= 10.0
        except (ValueError, TypeError):
            return False

def add_candidate(data: InterviewData, name: str, email: str) -> None:
    if not data.validate_name(name):
        raise ValueError("Имя кандидата должно быть строкой длиной не менее 2 символов.")
    existing = [c for c in data.candidates.values() if c['email'] == email]
    if existing:
        raise ValueError(f"Кандидат с почтой {email} уже существует.")
    data.candidates[name] = {'email': email, 'interviews': []}

def add_interview(data: InterviewData, candidate_name: str) -> None:
    if candidate_name not in data.candidates:
        raise ValueError(f"Кандидат {candidate_name} не найден.")
    interview_id = len(data.interviews) + 1
    data.interviews.append({
        'id': interview_id,
        'candidate': candidate_name,
        'questions': [],
        'score': None,
        'notes': ''
    })

def add_question(data: InterviewData, interview_idx: int, question_text: str) -> None:
    if not data.validate_interview_index(interview_idx):
        raise ValueError("Неверный индекс интервью.")
    interview = data.interviews[interview_idx]
    if len(interview['questions']) >= 5:
        raise ValueError("Максимум 5 вопросов на одно интервью.")
    interview['questions'].append(question_text)

def add_result(data: InterviewData, interview_idx: int, score: float, notes: str = "") -> None:
    if not data.validate_interview_index(interview_idx):
        raise ValueError("Неверный индекс интервью.")
    if not data.validate_score(score):
        raise ValueError("Оценка должна быть числом от 0.0 до 10.0.")
    interview = data.interviews[interview_idx]
    interview['score'] = score
    interview['notes'] = notes

def validate_interview_index(self, idx: int) -> bool:
    return isinstance(idx, int) and 0 <= idx < len(self.interviews)
