# === Stage 32: Добавь журнал действий пользователя ===
# Project: InterviewNotes
import json
from datetime import datetime, timezone

LOG_FILE = "interview_notes_log.json"
LOG_LOCK = None

def load_log():
    global LOG_LOCK
    if LOG_LOCK is None:
        LOG_LOCK = _file_lock(LOG_FILE)
    with LOG_LOCK:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                return json.load(f)
        return []

def save_log(log):
    with _file_lock(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump(log, f, indent=2)

def log_action(action_type, details):
    log = load_log()
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action_type,
        "details": details
    }
    log.append(entry)
    save_log(log)
    return entry

def _file_lock(path):
    import threading
    import fcntl
    return threading.Lock() if sys.platform == "win32" else _posix_flock_lock(path)

def _posix_flock_lock(path):
    import os
    _fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o644)
    return _fd
