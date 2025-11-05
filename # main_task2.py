# main_task2.py
import os
import sys
import json
from collections import Counter

# ==========================
# 🔹 Step 1: Ensure folder and file exist
# ==========================
folder_name = "mymodules"
os.makedirs(folder_name, exist_ok=True)
functions_path = os.path.join(folder_name, "functions.py")

# If functions.py doesn’t exist, create it automatically
if not os.path.exists(functions_path):
    with open(functions_path, "w") as f:
        f.write('''\
import json
from collections import Counter

def summary_report(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        user_failures = Counter()
        ip_failures = Counter()

        for entry in data:
            if entry.get("status") == "failure":
                user_failures[entry["user"]] += 1
                ip_failures[entry["ip"]] += 1

        flagged_users = [u for u, c in user_failures.items() if c > 3]
        flagged_ips = [ip for ip, c in ip_failures.items() if c > 3]

        print("\\n=== Login Failure Summary ===")
        print("User Failures:", dict(user_failures))
        print("IP Failures:", dict(ip_failures))
        print("\\nFlagged Users (more than 3):", flagged_users)
        print("Flagged IPs (more than 3):", flagged_ips)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
''')

# ==========================
# 🔹 Step 2: Add folder to Python path
# ==========================
sys.path.append(os.path.abspath(folder_name))

# ==========================
# 🔹 Step 3: Import the function dynamically
# ==========================
from functions import summary_report

# ==========================
# 🔹 Step 4: Create a sample JSON file if missing
# ==========================
sample_data = [
    {"user": "alice", "ip": "192.168.1.10", "status": "failure"},
    {"user": "alice", "ip": "192.168.1.10", "status": "failure"},
    {"user": "bob", "ip": "192.168.1.11", "status": "failure"},
    {"user": "charlie", "ip": "192.168.1.12", "status": "success"},
    {"user": "bob", "ip": "192.168.1.11", "status": "failure"},
    {"user": "bob", "ip": "192.168.1.11", "status": "failure"},
    {"user": "alice", "ip": "192.168.1.10", "status": "failure"}
]

json_file = "login_attempts.json"
if not os.path.exists(json_file):
    with open(json_file, "w") as f:
        json.dump(sample_data, f, indent=4)

# ==========================
# 🔹 Step 5: Run the summary report
# ==========================
if __name__ == "__main__":
    summary_report(json_file)