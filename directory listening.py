# list_files.py

import os

print("Files in current directory:")
for file in os.listdir("."):
    print(file)
