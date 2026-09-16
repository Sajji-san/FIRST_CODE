# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: InterviewNotes
def dry_run(operation, data, *, dry=True):
    if not dry:
        return operation(data)
    log = []
    try:
        result = operation(data)
        log.append(('OK', result))
    except Exception as e:
        log.append(('FAIL', str(e)))
    return log
