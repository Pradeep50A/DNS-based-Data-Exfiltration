import re
import math
import base64
import os
from datetime import datetime

def calculate_entropy(data):
    if not data: return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log2(p_x)
    return entropy

def analyze_threat(data):
    score = 0
    data_lower = data.lower()

    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", data):
        score += 4
    if re.search(r"[A-Za-z0-9]{20,}", data):
        score += 3

    if len(data) > 12 and calculate_entropy(data) > 3.8:
        score += 5

    keywords = ["password", "secret", "apikey", "auth", "login", "token"]
    if any(k in data_lower for k in keywords):
        score += 3

    return score

def simulate_exfiltration(data):
    encoded = base64.b32encode(data.encode()).decode().replace("=", "").lower()
    fake_dns_query = f"{encoded[:63]}.ns1.internal-node.net"
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_dir, "dns_log.txt")
    
    with open(log_path, "a") as f:
        f.write(f"[{datetime.now()}] DNS_QUERY_REQUEST: {fake_dns_query} | ORIGIN: {data}\n")

if __name__ == "__main__":
    user_input = input("Enter system data: ")

    if analyze_threat(user_input) >= 4:
        simulate_exfiltration(user_input)

    print("Request processed.")