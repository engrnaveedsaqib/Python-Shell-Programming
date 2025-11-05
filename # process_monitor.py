# process_monitor.py

import os
import sys
import subprocess

try:
    import psutil
except ImportError:
    print("Installing required module: psutil...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil  # retry import after installation

print("Running Processes:")
for proc in psutil.process_iter(['pid', 'name']):
    print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")
