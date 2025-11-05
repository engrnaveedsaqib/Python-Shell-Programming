# task1_log_analysis.py

import sys, subprocess

# Auto-install required packages if missing
for pkg in ["pandas", "matplotlib"]:
    try:
        __import__(pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import subprocess, sys

try:
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "matplotlib"])
    import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("data_analysis_logs.csv")

ip_counts = df['IP'].value_counts()

top5 = ip_counts.head(5)
print("\nTop 5 IPs by request count:")
print(top5)

top5.plot(kind='bar', color='steelblue', title="Top 5 IPs by Request Count")
plt.xlabel("IP Address")
plt.ylabel("Request Count")
plt.tight_layout()
plt.show()
