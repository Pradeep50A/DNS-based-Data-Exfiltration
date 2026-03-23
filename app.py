import math
import re
import base64
import os
import time
from datetime import datetime

DOMAIN = "ns1.internal-node.net"

def calculate_entropy(data):
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += -p_x * math.log2(p_x)
    return entropy

def is_harmful(data):
    score = 0
    data_lower = data.lower()
    harmful_keywords = ["password", "secret", "apikey", "auth", "login", "token", "admin", "db_user"]

    if any(word in data_lower for word in harmful_keywords):
        score += 2

    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", data):
        score += 2

    if calculate_entropy(data) > 3.5:
        score += 1

    return score >= 2

def simulate_exfiltration(data):
    encoded = base64.b32encode(data.encode()).decode().replace("=", "").lower()
    fake_dns_query = f"{encoded[:63]}.{DOMAIN}"
    log_filename = "dns_log.txt"

    for _ in range(5):
        try:
            with open(log_filename, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] DNS_QUERY: {fake_dns_query} | DATA: {data}\n")
                f.flush()
                os.fsync(f.fileno())
            return
        except (OSError, IOError):
            time.sleep(0.5)

if __name__ == "__main__":
    user_input = input("Enter system data: ")

    if is_harmful(user_input):
        simulate_exfiltration(user_input)

    print("Request processed.")
