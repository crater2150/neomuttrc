#!/usr/bin/env python3
import sys
import re
# import subprocess
from email.utils import format_datetime, parsedate_to_datetime
from charset_normalizer import CharsetNormalizerMatches as CnM

in_headers = True
data = sys.stdin.buffer.read()
detected = CnM.from_bytes(data, preemptive_behaviour=False).best().first()
for line in str(detected).splitlines():
    if line == "\n": in_headers = False
    match = re.match(r'^Date: (.+)', line)

    if not in_headers or not match:
        print(line)
        continue

    date_string = match.group(1)
    # use this if you do not have python 3.3+
    # converted_date = subprocess.Popen(['date','-d',date_string], stdout=subprocess.PIPE).communicate()[0].strip()
    converted_date = format_datetime(parsedate_to_datetime(date_string).astimezone(tz=None))
    print('Date:', converted_date)

