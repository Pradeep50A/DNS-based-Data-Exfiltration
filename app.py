import math
import re
import base64
import os
import time
from datetime import datetime

def calculate_entropy(data):
    if not data: return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log2(p_x)
    return entropy

def is_harmful(data):
    data_lower = data.lower()
    harmful_keywords = ["password", "secret", "apikey", "auth", "login", "token", "admin", "db_user"]
    
    if any(word in data_lower for word in harmful_keywords):
        return True
            
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", data):
        return True
        
    return False

def simulate_exfiltration(data):
    encoded = base64.b32encode(data.encode()).decode().replace("=", "").lower()
    fake_dns_query = f"{encoded[:63]}.ns1.internal-node.net"
    log_filename = "dns_log.txt"
    
    for attempt in range(5):
        try:
            with open(log_filename, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] DNS_QUERY: {fake_dns_query} | DATA: {data}\n")
                f.flush()
                os.fsync(f.fileno())
            return
        except (OSError, IOError):
            time.sleep(0.5)
        except Exception:
            break

if __name__ == "__main__":
    user_input = input("Enter system data: ")

    if is_harmful(user_input):
        simulate_exfiltration(user_input)

    print("Request processed.")
