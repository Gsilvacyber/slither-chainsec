import os
import json

print(f"\nRunning from: {os.getcwd()}")

file_path = "slither_output.json"

if not os.path.exists(file_path):
    print(f"[!] File not found: {file_path}")
else:
    with open(file_path, "r") as file:
        data = json.load(file)
        print("[+] slither_output.json loaded!")
        print(json.dumps(data, indent=2))  # Show full content (or truncate if it's huge)
