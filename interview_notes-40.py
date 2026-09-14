# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: InterviewNotes
import argparse


def main():
    parser = argparse.ArgumentParser(description="InterviewNotes CLI")
    sub = parser.add_subparsers(dest="command")

    # add-candidate
    p = sub.add_parser("add-candidate", help="Add a candidate")
    p.add_argument("--name", required=True)
    p.add_argument("--email", required=True)

    # add-interview
    p = sub.add_parser("add-interview", help="Add an interview for a candidate")
    p.add_argument("--candidate", required=True)
    p.add_argument("--date", default="")
    p.add_argument("--interviewer", default="")

    # add-question
    p = sub.add_parser("add-question", help="Add a question to an interview")
    p.add_argument("--interview", required=True)
    p.add_argument("--text", required=True)
    p.add_argument("--category", default="")

    # add-answer
    p = sub.add_parser("add-answer", help="Add an answer to a question")
    p.add_argument("--interview", required=True)
    p.add_argument("--question", required=True)
    p.add_argument("--text", required=True)

    # add-rating
    p = sub.add_parser("add-rating", help="Add a rating for a question")
    p.add_argument("--interview", required=True)
    p.add_argument("--question", required=True)
    p.add_argument("--score", required=True, type=float)

    # add-decision
    p = sub.add_parser("add-decision", help="Add a final decision for a candidate")
    p.add_argument("--candidate", required=True)
    p.add_argument("--decision", required=True)

    # list
    p = sub.add_parser("list", help="List interviews")
    p.add_argument("--format", default="text", choices=["text", "json"])

    args = parser.parse_args()
    if args.command == "add-candidate":
        add_candidate(args.name, args.email)
    elif args.command == "add-interview":
        add_interview(args.candidate, args.date, args.interviewer)
    elif args.command == "add-question":
        add_question(args.interview, args.text, args.category)
    elif args.command == "add-answer":
        add_answer(args.interview, args.question, args.text)
    elif args.command == "add-rating":
        add_rating(args.interview, args.question, args.score)
    elif args.command == "add-decision":
        add_decision(args.candidate, args.decision)
    elif args.command == "list":
        list_interviews(args.format)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
