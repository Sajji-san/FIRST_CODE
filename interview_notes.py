# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: InterviewNotes
class Candidate:
    def __init__(self, name): self.name = name
class Question:
    def __init__(self, text): self.text = text
def main():
    candidates = [Candidate("Alice"), Candidate("Bob")]
    questions = [Question("Tell me about yourself?"), Question("How do you handle stress?")]
    interviews = []
    for c in candidates:
        interview = {"candidate": c, "questions": [], "score": 0}
        for q in questions:
            answer = f"Answer to {q.text}"
            score = len(answer) % 10
            interview["questions"].append({"question": q, "answer": answer, "score": score})
        interviews.append(interview)
    print(f"Candidates processed: {len(candidates)}")
    for i in interviews:
        print(f"{i['candidate'].name}: Total Score = {sum(q['score'] for q in i['questions'])}")

if __name__ == "__main__": main()
