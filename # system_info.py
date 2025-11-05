# system_info.py
import subprocess
try:
    result = subprocess.run(["ipconfig"], capture_output=True, text=True)
    print("Network Info:\n" + result.stdout)
except Exception as e:
    print(f"Error: {e}")