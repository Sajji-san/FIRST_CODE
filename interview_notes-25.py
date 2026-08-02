# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: InterviewNotes
def parse_date_safe(raw):
    """Парсинг даты с понятным сообщением об ошибке."""
    if not raw or not isinstance(raw, str):
        return None, "Некорректный формат даты: пустое значение или не строка"
    
    try:
        parts = raw.strip().split('-')
        if len(parts) != 3:
            return None, f"Дата должна быть в формате 'ГГГГ-ММ-ДД', получено: {raw}"
        
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        
        if not (1 <= year <= 9999):
            return None, f"Недопустимый год: {year} (должен быть от 1 до 9999)"
        if not (1 <= month <= 12):
            return None, f"Недопустимый месяц: {month} (должен быть от 1 до 12)"
        if not (1 <= day <= 31):
            return None, f"Недопустимый день: {day} (должен быть от 1 до 31)"
        
        return year, month, day
    except ValueError as e:
        return None, f"Ошибка при парсинге даты '{raw}': {str(e)}"

def parse_date(raw):
    """Обёртка для совместимости с остальным кодом."""
    result = parse_date_safe(raw)
    if result[0] is not None:
        return datetime.date(int(result[0]), int(result[1]), int(result[2]))
    return result[1]  # сообщение об ошибке
