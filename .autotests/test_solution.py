import os
import re

def test_solution_file_exists():
    assert os.path.isfile("webpage.html"), "solution.html is missing"

def test_solution_contains_heading():
    with open("webpage.html", encoding="utf-8") as f:
        text = f.read()
    assert re.search(r"<h1>.*Hello World.*</h1>", text, re.I), \
        "Expected an <h1>Hello World</h1> heading"