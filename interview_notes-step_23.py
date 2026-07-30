# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: InterviewNotes
def print_interview_table(interviews):
    if not interviews:
        print("Нет записей.")
        return
    headers = ["ID", "Кандидат", "Дата", "Результат"]
    col_widths = {h: max(len(h), *([len(str(i[h]) or len(h)) for i in interviews])) for h in headers}
    separator = "+".join("-" * (col_widths[h] + 2) for h in headers)
    row_format = " | ".join("{:<{w}}" for w in col_widths.values())
    print(separator)
    print(row_format.format(*headers, *[len(h) - 1]))
    print(separator)
    for i in interviews:
        result_str = str(i.get("result", "")) or "-"
        date_str = str(i.get("date", "")) or "-"
        print(row_format.format(
            i["id"],
            i["candidate"][:col_widths["Кандидат"]] if len(i["candidate"]) > col_widths["Кандидат"] else i["candidate"],
            date_str,
            result_str
        ))
    print(separator)

print_interview_table(interview_notes.interviews)
