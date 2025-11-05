# task4_packet_stats.py

import subprocess, sys, os
try:
    import pandas as pd
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "numpy", "openpyxl"])
    import pandas as pd
    import numpy as np

file_name = "packets.xlsx"
if not os.path.exists(file_name):
    print(f"'{file_name}' not found — creating sample data...")
    sample_data = {
        "packet_size": [512, 768, 1024, 256, 1280, 640, 900, 1100, 500, 750]
    }
    df_sample = pd.DataFrame(sample_data)
    df_sample.to_excel(file_name, index=False)
    print(f"Sample '{file_name}' created successfully.\n")

df = pd.read_excel(file_name)

if "packet_size" not in df.columns:
    print("Error: Excel file must contain a 'packet_size' column.")
    sys.exit(1)

sizes = df["packet_size"]

mean = sizes.mean()
median = sizes.median()
std = sizes.std()
value_range = sizes.max() - sizes.min()

print("\n=== Packet Size Statistics ===")
print(f"Mean:        {mean:.2f}")
print(f"Median:      {median:.2f}")
print(f"Std Dev:     {std:.2f}")
print(f"Range:       {value_range:.2f}")
