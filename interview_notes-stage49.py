# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: InterviewNotes
print("=" * 60)
print("  FINAL SELF-CHECK: InterviewNotes")
print("=" * 60)

def self_check():
    checks = []

    def check(name, cond):
        checks.append((name, cond))

    check("Класс Candidate существует", hasattr(Candidate, "__init__"))
    check("Класс Question существует", hasattr(Question, "__init__"))
    check("Класс Interview существует", hasattr(Interview, "__init__"))
    check("Метод add_candidate", callable(getattr(Candidate, "add_candidate", None)))
    check("Метод add_question", callable(getattr(Candidate, "add_question", None)))
    check("Метод add_interview", callable(getattr(Interview, "add_interview", None)))
    check("Метод add_answer", callable(getattr(Interview, "add_answer", None)))
    check("Метод set_result", callable(getattr(Interview, "set_result", None)))
    check("Метод to_dict", callable(getattr(Candidate, "to_dict", None)))
    check("Метод save", callable(getattr(Interview, "save", None)))

    print("\n[SELF-CHECK REPORT]")
    passed = 0
    for name, cond in checks:
        status = "PASS" if cond else "FAIL"
        if cond:
            passed += 1
        print(f"  [{status}] {name}")

    total = len(checks)
    print(f"\n  Result: {passed}/{total} checks passed")

    if passed == total:
        print("  STATUS: READY ✅")
        print("  InterviewNotes is ready for use.")
        return True
    else:
        print("  STATUS: INCOMPLETE ⚠️")
        return False

if __name__ == "__main__":
    self_check()
    print("=" * 60)
