# Login Log Analyzer

A lightweight Python app that parses authentication logs to track failed login attempts by IP address and flag potential brute-force or suspicious login activity.

## Overview

This script reads a local `sample.log` file containing timestamped login attempts and performs the following checks:
* Counts total valid login events (`FAIL` and `SUCCESS`).
* Tracks the number of failed login attempts per IP address.
* Flags any IP address that achieves a `SUCCESS` status after reaching or exceeding the defined failure threshold (default: `3` failed attempts).
* Skips blank lines, `//` comments, and malformed log entries with console warnings.

## Project Structure

```text
.
├── log_analyzer.py   # Main Python analysis script
├── sample.log        # Sample authentication log data
└── README.md         # Project documentation
```

## Log Format

Each valid entry in `sample.log` follows a space-separated 4-column format:
```text
<TIMESTAMP> <IP_ADDRESS> <STATUS> <USERNAME>
```

Example:
```text
2026-10-10T09:00:00 10.0.0.8 FAIL Eli
2026-10-10T09:03:00 10.0.0.8 SUCCESS Eli
```

## How to Run

1. Ensure you have **Python 3** installed on your system.
2. Place your Python script and `sample.log` in the same directory.
3. Run the script from your terminal:

```bash
python log_analyzer.py
```
*(Note: Update `log_analyzer.py` in the command above if you named your script differently.)*

## Sample Output

Using the included `sample.log` file, the script produces:

```text
Login Log Summary:
Events analyzed: 6
10.0.0.8: 3 failed attempted login(s)
10.0.0.9: 1 failed attempted login(s)
REVIEW: 10.0.0.8 had a successful login after at least 3 failed attempts
```
