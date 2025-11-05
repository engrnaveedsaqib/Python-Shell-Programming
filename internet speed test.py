import subprocess
import sys
import importlib

required = ['speedtest-cli', 'schedule']
for package in required:
    try:
        importlib.import_module(package.split('-')[0])
    except ImportError:
        print(f"[INFO] Installing missing package: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import speedtest
import schedule
import datetime
import csv
import time
import os


def run_speed_test(log_file='speed_log.csv'):
    """Runs a speed test and logs results to a CSV file."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        download = st.download() / 1_000_000  # Convert to Mbps
        upload = st.upload() / 1_000_000      # Convert to Mbps
        ping = st.results.ping
        server = st.results.server['name']

        jitter = getattr(st.results, 'jitter', 'N/A')
        packet_loss = getattr(st.results, 'packet_loss', 'N/A')

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, round(download, 2), round(upload, 2),
                             ping, jitter, packet_loss, server])

        print(f"[{timestamp}] ✅ Logged: Download={download:.2f} Mbps | Upload={upload:.2f} Mbps | Ping={ping} ms")

    except Exception as e:
        print(f"[ERROR] Speed test failed: {e}")


def initialize_csv(file_path='speed_log.csv'):
    """Creates CSV header if file does not exist."""
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Download (Mbps)', 'Upload (Mbps)', 'Ping (ms)',
                             'Jitter (ms)', 'Packet Loss (%)', 'Server'])
        print(f"[INFO] Created log file: {file_path}")


def main():
    log_file = 'speed_log.csv'
    initialize_csv(log_file)

    # Run once immediately
    run_speed_test(log_file)

    # Schedule hourly tests
    schedule.every(1).hours.do(run_speed_test, log_file=log_file)
    print("[INFO] Internet Speed Monitor started — running tests every 1 hour.\n")

    # Continuous loop
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()

