# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: InterviewNotes
def validate_interview_data(interviews):
    errors = []
    for idx, interview in enumerate(interviews):
        if 'candidate' not in interview or 'questions' not in interview:
            errors.append(f"Interview {idx+1}: missing 'candidate' or 'questions'")
            continue
        for i, q in enumerate(interview['questions']):
            if 'answer' not in q:
                errors.append(f"Interview {idx+1}, Q{i+1}: missing 'answer'")
                q['answer'] = ''
            if 'rating' in q and not isinstance(q['rating'], (int, float)):
                errors.append(f"Interview {idx+1}, Q{i+1}: invalid 'rating' -> {q['rating']}")
                q['rating'] = 0.0
            if 'resolved' not in q:
                q['resolved'] = False
    return errors

def repair_interviews(interviews):
    interviews = validate_interview_data(interviews)
    for i, interview in enumerate(interviews):
        if 'candidate' not in interview:
            print(f"Warning: Interview {i+1} has no candidate; skipping")
            continue
        for j, q in enumerate(interview['questions']):
            if 'answer' not in q:
                q['answer'] = 'TBD'
            if 'rating' not in q:
                q['rating'] = 0.0
            if 'resolved' not in q:
                q['resolved'] = False
    return interviews
