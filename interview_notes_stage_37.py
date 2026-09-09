# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: InterviewNotes
import unittest

def test_basic_operations():
    assert 2 + 2 == 4
    assert "hello"[0] == "h"
    assert [1, 2, 3] == [1, 2, 3]
    assert {"a": 1} == {"a": 1}
    assert True is not False
    assert "" == ""
    assert 0 == 0
    assert 1.5 + 1.5 == 3.0

def test_string_operations():
    assert "Hello World".upper() == "HELLO WORLD"
    assert "hello world".startswith("hello")
    assert "hello world".endswith("world")
    assert "  hello  ".strip() == "hello"
    assert "a|b|c".split("|") == ["a", "b", "c"]

def test_list_operations():
    lst = [1, 2, 3, 4, 5]
    assert lst[0] == 1
    assert lst[-1] == 5
    assert len(lst) == 5
    assert lst + [6] == [1, 2, 3, 4, 5, 6]
    assert lst * 2 == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def test_dict_operations():
    d = {"key": "value", "num": 42}
    assert d["key"] == "value"
    assert "num" in d
    assert len(d) == 2
    assert d.get("missing", "default") == "default"

if __name__ == "__main__":
    test_basic_operations()
    test_string_operations()
    test_list_operations()
    test_dict_operations()
    print("All tests passed!")
