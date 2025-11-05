# task3_password_strength.py
import re
import os

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 2:
        label = "weak"
    elif score in (3, 4):
        label = "medium"
    else:
        label = "strong"
    return score, label


# 🔹 Create sample file if missing
if not os.path.exists("passwords.txt"):
    with open("passwords.txt", "w") as f:
        f.write("password123\n")
        f.write("Pass@2025\n")
        f.write("HELLO\n")
        f.write("abc123\n")
        f.write("Strong#Pass99\n")

# 🔹 Read passwords safely
with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

print(f"{'Password':20} | {'Score':5} | Strength")
print("-" * 45)

# 🔹 Evaluate each password
for pw in passwords:
    score, label = check_strength(pw)
    print(f"{pw:20} | {score:^5} | {label}")
