# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: InterviewNotes
class UndoManager:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def push(self, action):
        self._history.append(action)
        self._redo_stack.clear()

    def undo(self):
        if not self._history:
            return None
        action = self._history.pop()
        self._redo_stack.append(action)
        return action

    def redo(self):
        if not self._redo_stack:
            return None
        action = self._redo_stack.pop()
        self._history.append(action)
        return action

    def clear(self):
        self._history.clear()
        self._redo_stack.clear()
