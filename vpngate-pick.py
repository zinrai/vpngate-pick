#!/usr/bin/env python3

import csv
import random
import base64
import sys
import urllib.request
from io import StringIO

def get_vpngate_config():
    # Fetch and decode a random OpenVPN config from VPNGate
    url = 'https://www.vpngate.net/api/iphone/'

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read().decode('utf-8')

        # Parse CSV data (skip the first line starting with *)
        csv_data = data.split('\n', 1)[1]

        # Count valid rows and find config index
        reader = csv.reader(StringIO(csv_data))
        headers = next(reader)
        config_index = headers.index('OpenVPN_ConfigData_Base64')

        # Convert to list for random access
        rows = list(reader)
        if not rows:
            return None

        # Try to decode a random row
        max_attempts = 3  # Limit retry attempts
        while max_attempts > 0:
            row = random.choice(rows)
            if not row:  # Skip empty rows
                max_attempts -= 1
                continue

            try:
                config = base64.b64decode(row[config_index]).decode('utf-8')
                return config
            except (IndexError, base64.binascii.Error, UnicodeDecodeError):
                max_attempts -= 1
                continue

        return None

    except Exception:
        return None

if __name__ == '__main__':
    config = get_vpngate_config()
    if config:
        sys.stdout.write(config)
    else:
        sys.exit(1)
