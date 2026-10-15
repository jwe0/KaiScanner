# Python Port Scanner

A simple port scanner written in Python that scans open ports on a target IP address. It uses `socket` to connect to each port and check if it's up.

## Features

- Scan a range of ports on a target IP
- Grab the banner or title of the target
- Display in a clean unicode table

## Requirements

- Python 3.x

## Example output

```
╭───────────────┬─────────────────────────────────────────────────────────────┬─────────────────────────┬────────────────────────────────────────────────────────────╮
│ Port          │ Service                                                     │ Protocols               │ Banner                                                     │
├───────────────┼─────────────────────────────────────────────────────────────┼─────────────────────────┼────────────────────────────────────────────────────────────┤
│ 80            │ HTTP                                                        │ TCP, UDP, SCTP          │ 301 Moved Permanently                                      │
│ 53            │ DNS                                                         │ TCP, UDP                │ No banner or title                                         │
│ 443           │ HTTPS (HTTP over SSL)                                       │ TCP, UDP, SCTP          │ 400 The plain HTTP request was sent to HTTPS port          │
│ 853           │ Unknown                                                     │ Unknown                 │ No banner or title                                         │
│ 2053          │ Unknown                                                     │ Unknown                 │ 400 The plain HTTP request was sent to HTTPS port          │
│ 2052          │ Unknown                                                     │ Unknown                 │ 301 Moved Permanently                                      │
│ 2083          │ Secure RADIUS Service (radsec), cPanel default SSL          │ TCP, UDP                │ 400 The plain HTTP request was sent to HTTPS port          │
│ 2087          │ Unknown                                                     │ Unknown                 │ 400 The plain HTTP request was sent to HTTPS port          │
│ 2082          │ cPanel default                                              │ TCP, UDP                │ 301 Moved Permanently                                      │
│ 2086          │ Unknown                                                     │ Unknown                 │ 301 Moved Permanently                                      │
│ 2095          │ Unknown                                                     │ Unknown                 │ 301 Moved Permanently                                      │
│ 2096          │ Unknown                                                     │ Unknown                 │ 400 The plain HTTP request was sent to HTTPS port          │
│ 8080          │ HTTP Proxy                                                  │ TCP                     │ 301 Moved Permanently                                      │
│ 8443          │ Unknown                                                     │ Unknown                 │ 400 The plain HTTP request was sent to HTTPS port          │
╰───────────────┴─────────────────────────────────────────────────────────────┴─────────────────────────┴────────────────────────────────────────────────────────────╯```