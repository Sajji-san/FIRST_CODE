# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: InterviewNotes
def load_from_json(filepath):
    """Загрузка данных из локального JSON-файла с обработкой ошибок."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект (dict), а не список или скаляр.")
        return {k: v for k, v in data.items() if isinstance(v, (str, int, float, bool))}
    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден. Создайте его с данными перед загрузкой.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в '{filepath}': {e}")
        return {}
    except PermissionError:
        print(f"Нет доступа к файлу '{filepath}'. Проверьте права на запись.")
        return {}
    except Exception as e:
        print(f"Непредвиденная ошибка при загрузке: {e}")
        return {}

if __name__ == "__main__":
    loaded = load_from_json("interviews.json")
    if loaded:
        print(f"\n✅ Загружено {len(loaded)} элементов из интервью:")
        for key, value in loaded.items():
            print(f"  • {key}: {value}")
