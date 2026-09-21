# === Stage 45: Добавь восстановление из резервной копии ===
# Project: InterviewNotes
def load_from_backup():
    """Загрузить данные из резервной копии JSON-файла."""
    if not _has_backups():
        print("Резервных копий не найдено")
        return
    backup_path = _find_latest_backup()
    try:
        with open(backup_path, 'r') as f:
            data = json.load(f)
        _merge_data(data)
        print(f"Восстановлено из {backup_path}")
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
