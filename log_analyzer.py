# log_analyzer.py

import re

def analyze_log(filename, keyword="error"):
    try:
        with open(filename, "r") as file:
            content = file.read()
            matches = re.findall(keyword, content, re.IGNORECASE)
            print(f"Found {len(matches)} '{keyword}' in {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
