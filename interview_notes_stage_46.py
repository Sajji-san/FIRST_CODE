# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: InterviewNotes
import json

# Миграция формата хранения интервью: добавляем поле 'rounds' для хранения истории раундов
# и обновляем структуру данных интервью с поддержкой истории оценок.

def migrate_interview_format(interviews_file):
    """
    Миграция интервью: добавляет структуру для хранения раундов.
    """
    try:
        with open(interviews_file, 'r', encoding='utf-8') as f:
            interviews = json.load(f)
    except FileNotFoundError:
        return []
    
    # Обновляем структуру интервью
    updated_interviews = []
    for interview in interviews:
        if 'rounds' not in interview:
            # Создаём структуру для хранения раундов
            rounds = []
            if 'answers' in interview:
                for answer in interview['answers']:
                    if 'round' in answer:
                        rounds.append({
                            'round_number': answer['round'],
                            'question': answer.get('question', ''),
                            'answer': answer.get('answer', ''),
                            'score': answer.get('score', None),
                            'notes': answer.get('notes', '')
                        })
            interview['rounds'] = rounds
            # Сохраняем ответы в новом формате
            if 'answers' in interview:
                del interview['answers']
        updated_interviews.append(interview)
    
    # Сохраняем обновлённые данные
    with open(interviews_file, 'w', encoding='utf-8') as f:
        json.dump(updated_interviews, f, ensure_ascii=False, indent=2)
    
    return updated_interviews
