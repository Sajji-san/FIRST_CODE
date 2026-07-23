# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: InterviewNotes
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


class CandidateTagsMixin:
    def add_tag(self, tag_name):
        tag = Tag(tag_name)
        if tag not in self.tags:
            self.tags.append(tag)
        return tag

    def remove_tag(self, tag_name):
        tag = Tag(tag_name)
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False


class Candidate(CandidateTagsMixin):
    def __init__(self, name, email=None, phone=None):
        super().__init__()
        self.name = name
        self.email = email
        self.phone = phone
        self.tags = []

    @property
    def tags(self):
        return getattr(self, '_tags', [])

    @tags.setter
    def tags(self, value):
        self._tags = value if isinstance(value, list) else [value]


class Interview(CandidateTagsMixin):
    def __init__(self, candidate, question=None, answers=None):
        super().__init__()
        self.candidate = candidate
        self.question = question
        self.answers = answers or []

    @property
    def tags(self):
        return getattr(self, '_tags', [])

    @tags.setter
    def tags(self, value):
        self._tags = value if isinstance(value, list) else [value]


class Decision(CandidateTagsMixin):
    def __init__(self, outcome=None, notes=None):
        super().__init__()
        self.outcome = outcome  # 'hired', 'rejected', 'pending'
        self.notes = notes or ''

    @property
    def tags(self):
        return getattr(self, '_tags', [])

    @tags.setter
    def tags(self, value):
        self._tags = value if isinstance(value, list) else [value]


class InterviewSummary(CandidateTagsMixin):
    def __init__(self, outcome=None, notes=None):
        super().__init__()
        self.outcome = outcome  # 'hired', 'rejected'
        self.notes = notes or ''

    @property
    def tags(self):
        return getattr(self, '_tags', [])

    @tags.setter
    def tags(self, value):
        self._tags = value if isinstance(value, list) else [value]


class InterviewNotesApp:
    def __init__(self):
        self.candidates = []
        self.interviews = []
        self.decisions = []
        self.summaries = []

    @property
    def candidates(self):
        return getattr(self, '_candidates', [])

    @candidates.setter
    def candidates(self, value):
        self._candidates = value if isinstance(value, list) else [value]


if __name__ == '__main__':
    app = InterviewNotesApp()
    c = Candidate(name='Alice')
    print(c.add_tag('frontend'))  # Tag('frontend')
    print(c.remove_tag('backend'))  # True (не существовало, но не ошибка)
