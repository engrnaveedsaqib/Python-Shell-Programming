# task5_firewall_rules.py

import json
import os

file_name = "firewall_rules.json"

if not os.path.exists(file_name):
    print(f"'{file_name}' not found — creating sample data...")
    sample_rules = [
        {"id": 1, "source_ip": "192.168.1.10", "destination_ip": "10.0.0.5", "action": "allow"},
        {"id": 2, "source_ip": "192.168.1.11", "destination_ip": "10.0.0.8", "action": "deny"},
        {"id": 3, "source_ip": "192.168.1.12", "destination_ip": "10.0.0.9", "action": "deny"},
        {"id": 4, "source_ip": "192.168.1.10", "destination_ip": "10.0.0.5", "action": "deny"},
        {"id": 5, "source_ip": "192.168.1.15", "destination_ip": "10.0.0.6", "action": "allow"}
    ]
    with open(file_name, "w") as f:
        json.dump(sample_rules, f, indent=4)
    print(f"Sample '{file_name}' created successfully.\n")

try:
    with open(file_name, "r") as f:
        rules = json.load(f)
except json.JSONDecodeError:
    print(f"Error: '{file_name}' contains invalid JSON data.")
    exit(1)

denied = [r for r in rules if r.get("action") == "deny"]

with open("denied_rules.json", "w") as f:
    json.dump(denied, f, indent=4)

unique_ips = {r.get("source_ip") for r in denied if r.get("source_ip")}

print("\n=== Firewall Rule Analysis ===")
print(f"Total rules: {len(rules)}")
print(f"Total denied rules: {len(denied)}")
print(f"Unique source IPs in deny list: {len(unique_ips)}")

if unique_ips:
    print("Denied Source IPs:")
    for ip in unique_ips:
        print("  -", ip)
