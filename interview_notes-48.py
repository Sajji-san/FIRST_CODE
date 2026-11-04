# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: InterviewNotes
class InterviewNote:
    def __init__(self, interview_id, interviewee, interview_date):
        self.interview_id = interview_id
        self.interviewee = interviewee
        self.interview_date = interview_date
        self.questions = []
        self.answers = []
        self.assessments = []
        self.result = None

    def add_question(self, question_text):
        self.questions.append(question_text)

    def add_answer(self, question_index, answer_text):
        self.answers.append((question_index, answer_text))

    def add_assessment(self, question_index, score, comment):
        self.assessments.append((question_index, score, comment))

    def set_result(self, decision, reason):
        self.result = (decision, reason)

    def to_dict(self):
        return {
            'interview_id': self.interview_id,
            'interviewee': self.interviewee,
            'interview_date': self.interview_date,
            'questions': self.questions,
            'answers': self.answers,
            'assessments': self.assessments,
            'result': self.result,
        }

    def save(self, filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(self.to_dict(), ensure_ascii=False) + '\n')

    @classmethod
    def load(cls, filename):
        notes = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    notes.append(cls.from_dict(json.loads(line)))
        return notes

    @classmethod
    def from_dict(cls, data):
        note = cls(
            data['interview_id'],
            data['interviewee'],
            data['interview_date'],
        )
        note.questions = data.get('questions', [])
        note.answers = data.get('answers', [])
        note.assessments = data.get('assessments', [])
        note.result = data.get('result', None)
        return note
