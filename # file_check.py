# file_check.py
import os
filename = "cyber_log.txt"
if os.path.exists(filename):
    print(f"File {filename} exists.")
else:
    print(f"File {filename} does not exist.")