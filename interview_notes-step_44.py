# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: InterviewNotes
def backup_data_file(data_path: str, backup_dir: str = "backups") -> str:
    import shutil, os
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"interview_data_{timestamp}.csv")
    shutil.copy2(data_path, backup_path)
    return backup_path
