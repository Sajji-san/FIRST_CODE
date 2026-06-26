# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: InterviewNotes
class InterviewNotes:
    def __init__(self):
        self.candidates = {}
        self.interviews = []

    def add_candidate(self, name: str) -> dict:
        if name not in self.candidates:
            self.candidates[name] = {"name": name, "skills": [], "history": []}
        return self.candidates[name]

    def create_interview(self, candidate_name: str, date: str, questions: list[str], answers: dict) -> dict:
        if candidate_name not in self.candidates:
            raise ValueError(f"Candidate {candidate_name} not found")
        interview_id = len(self.interviews) + 1
        record = {
            "id": interview_id,
            "candidate": candidate_name,
            "date": date,
            "questions": questions,
            "answers": answers,
            "score": sum(1 for q in questions if answers.get(q)) / len(questions) * 100 if questions else 0
        }
        self.interviews.append(record)
        self.candidates[candidate_name]["history"].append(interview_id)
        return record

    def get_interview(self, interview_id: int) -> dict | None:
        for i in range(len(self.interviews)):
            if self.interviews[i]["id"] == interview_id:
                return self.interviews[i]
        return None
