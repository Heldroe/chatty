#!/usr/bin/env python3

import argparse
import json
import time

LOG_LINE_TEXT = "Hello, World!"
LOG_LINE_JSON = json.dumps({"Hello": "World!"})

parser = argparse.ArgumentParser()
parser.add_argument("--json", help="log in JSON format", action="store_true")
parser.add_argument(
    "-f",
    "--frequency",
    type=int,
    help="log line frequency per second",
    default=5,
)
args = parser.parse_args()

if args.json:
    log_line = LOG_LINE_JSON
else:
    log_line = LOG_LINE_TEXT

while True:
    print(log_line)
    time.sleep(1 / args.frequency)
