from collections import defaultdict
from pathlib import Path

LOG_FILE = Path(__file__).with_name("sample.log")
FAILURE_THRESHOLD = 3

failed_by_ip = defaultdict(int)
successful_after_threshold = set()
events_analyzed = 0

with LOG_FILE.open(encoding="utf-8") as log_file:
    for line_number, line in enumerate(log_file, start=1):
        line = line.strip()
        if not line or line.startswith("//"):
            continue

        parts = line.split()
        if len(parts) != 4:
            print(f"Skipping malformed line {line_number}: {line}")
            continue

        timestamp, ip, status, username = parts
        if status == "FAIL":
            failed_by_ip[ip] += 1
            events_analyzed += 1
        elif status == "SUCCESS":
            events_analyzed += 1
            if failed_by_ip[ip] >= FAILURE_THRESHOLD:
                successful_after_threshold.add(ip)
        else:
            print(f"Skipping unknown status on line {line_number}: {line}")

print("Login Log Summary:")
print(f"Events analyzed: {events_analyzed}")

for ip, failures in sorted(failed_by_ip.items()):
    print(f"{ip}: {failures} failed attempted login(s)")

for ip in sorted(successful_after_threshold):
    print(f"REVIEW: {ip} had a successful login after at least {FAILURE_THRESHOLD} failed attempts")
