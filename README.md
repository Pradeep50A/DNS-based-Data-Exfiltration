# DNS Data Exfiltration Detection 
## Overview

This project demonstrates detection and simulation of **DNS-based data exfiltration**. It identifies sensitive user input and logs it in a DNS-like format while showing a normal response to the user (blind/OOB behavior).
---

## Features

* Keyword detection (password, token, etc.)
* Regex detection (emails)
* Entropy-based detection (API keys, random strings)
* Context-based analysis
* DNS exfiltration simulation (encoded logging)

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

**Logged:**

```
bXkgcGFzc3dvcmQgaXMgMTIzNA==.attacker.com
```

---

## Tech Used

* Python
* ---
