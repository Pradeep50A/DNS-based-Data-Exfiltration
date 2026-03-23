# DNS Data Exfiltration Detection 
## Overview

This project detects sensitive input and simulates DNS-based data exfiltration using a blind (out-of-band) approach.
---

## Features

Keyword detection
Email pattern detection
Entropy-based detection
DNS exfiltration simulation
---

## How It Works

1. User enters input
2. Input is analyzed using multiple detection techniques
3. If sensitive → data is encoded and logged (`dns_log.txt`)
4. User always sees:

   ```
   Request processed
   ```

---

## Usage

```bash
python app.py
```

---

## Example

**Input:**

```
my password is 1234
```

**Output:**

```
Request processed
```
## Sample Output
When a threat is detected, the script generates a stealthy DNS query logged in `dns_log.txt`:
`[2026-03-22] DNS_QUERY: mfsg22loibrw63...ns1.internal-node.net | DATA: admin@company.com SECRET_API_KEY_2026`

## Tech Used

* Python
