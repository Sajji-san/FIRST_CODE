# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: InterviewNotes
def test_edge_cases():
    assert InterviewNotes() is not None
    assert InterviewNotes("name") is not None
    assert InterviewNotes("name", "desc") is not None
    assert len(InterviewNotes("name", "desc").get_notes()) == 0
    assert len(InterviewNotes("name", "desc").get_notes("interview")) == 0
    assert len(InterviewNotes("name", "desc").get_notes("interview", "section")) == 0

    note = InterviewNotes("name", "desc").add_note("interview", "section", "text")
    assert note is not None
    assert note.get_text() == "text"
    assert note.get_id() is not None
    assert note.get_date() is not None
    assert note.get_interview() == "interview"
    assert note.get_section() == "section"
    assert len(InterviewNotes("name", "desc").get_notes("interview", "section")) == 1

    note2 = InterviewNotes("name", "desc").add_note("interview", "section", "text")
    assert note2.get_text() == "text"
    assert note2.get_id() != note.get_id()

    note3 = InterviewNotes("name", "desc").add_note("interview", "section", "text")
    assert len(InterviewNotes("name", "desc").get_notes("interview", "section")) == 3

    note4 = InterviewNotes("name", "desc").add_note("interview", "section", "text")
    assert note4.get_id() != note3.get_id()
    assert note3.get_id() != note2.get_id()
    assert note2.get_id() != note.get_id()

    note5 = InterviewNotes("name", "desc").add_note("interview", "section", "text")
    assert len(InterviewNotes("name", "desc").get_notes("interview", "section")) == 5

    note6 = InterviewNotes("name", "desc").add_note("interview", "section", "text")
    assert note6.get_id() != note5.get_id()
    assert note5.get_id() != note4.get_id()
    assert note4.get_id() != note3.get_id()
    assert note3.get_id() != note2.get_id()
    assert note2.get_id() != note.get_id()
