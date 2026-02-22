# Port Scanner

A command-line TCP port scanner built in Python. Supports single hosts, multiple hosts via file, single ports, port ranges, and comma-separated port lists with optional result logging.

---

## Requirements

- Python 3.14.2
- uses only Python standard library (`socket`, `ipaddress`, `argparse`)

---

## Usage

```bash
usage: Port Scanner [-h] (-H TARGETHOST | -t TARGETFILE) -p TARGETPORT [-L LOGFILE] [--timeout TIMEOUT] [-v]
```

### Arguments

| Argument | Description |
|----------|-------------|
| `-H` | Single target IP address |
| `-t` | Path to a file containing a list of target IPs (one per line) |
| `-p` | Target port(s) — see formats below |
| `-L` | *(Optional)* File path to log scan results |
| `-v` | (Optional) Verbose, show closed ports |
| `--timeout` | *(Optional)* Connection timeout in seconds (default: 4) |

> `-H` and `-t` are mutually exclusive, use one or the other.

### Port Formats

| Format | Example | Description |
|--------|---------|-------------|
| Single | `80` | Scan one port |
| Range | `80-100` | Scan all ports in range |
| List | `22,80,443` | Scan specific ports |

---

## Examples

**Scan a single host on common ports:**
```bash
python3 main.py -H 192.168.1.1 -p 22,80,443
```

**Scan a port range:**
```bash
python3 main.py -H 192.168.1.1 -p 1-1024
```

**Scan multiple hosts from a file:**
```bash
python3 main.py -t hosts.txt -p 80,443
```

**Scan and log results:**
```bash
python3 main.py -H 192.168.1.1 -p 22,80,443 -L results.txt
```
**Scan with verbose:**
```bash
python3 main.py -H 192.168.1.1 -p 22-25 -v
```
**Set a custom timeout:**
```bash
python3 main.py -H 192.168.1.1 -p 1-500 --timeout 2
```

---

## Logging

When a log file is specified with `-L`, the scanner appends results to that file with a timestamped banner for each run. If the file does not exist it will be created automatically.

Example log output:
```
=========================================
           PORT SCANNER
=========================================
    Started: 21/02/2026 at 23:29
=========================================

Scanned host: 192.168.1.1
Port     Status   Service
22       Open     ssh
80       Open     http
443      Open     https
```

---

## Legal Disclaimer

This tool is intended for **authorised testing only**. Scanning hosts without explicit permission is illegal under the **Computer Misuse Act 1990** in the UK and equivalent legislation in other countries. Only use this tool against systems you own or have written permission to test.
