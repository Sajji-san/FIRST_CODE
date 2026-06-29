# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: InterviewNotes
def delete_record(record_id: int, collection_name: str) -> bool:
    if record_id not in _data[collection_name]:
        print(f"Ошибка: запись с ID {record_id} в коллекции '{collection_name}' не найдена.")
        return False
    
    del _data[collection_name][record_id]
    print(f"Успешно удалена запись с ID {record_id} из коллекции '{collection_name}'.")
    return True

def handle_missing_ids(collection_name: str, missing_ids: list) -> None:
    if not missing_ids:
        return
    
    print(f"\nПредупреждение: следующие ID отсутствуют в коллекции '{collection_name}':", ", ".join(map(str, missing_ids)))
    
    for mid in missing_ids:
        if mid in _data.get(collection_name, {}):
            del _data[collection_name][mid]
