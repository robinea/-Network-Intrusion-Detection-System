

from scapy.all import sniff, IP, TCP
from collections import defaultdict
from datetime import datetime
import time
import csv
import os

THRESHOLD = 10
TIME_WINDOW = 10
ALERT_COOLDOWN = 10
INTERFACE = "eth1"

connections = defaultdict(list)
last_alert = {}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "evidence", "alerts.csv")


def log_alert(src_ip, ports):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n[ALERT] Possible TCP port scan!")
    print(f"Time: {timestamp}")
    print(f"Source IP: {src_ip}")
    print(f"Ports targeted: {sorted(ports)}")

    new_file = not os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if new_file:
            writer.writerow(["Timestamp", "Source IP", "Ports Targeted"])

        writer.writerow([timestamp, src_ip, sorted(ports)])


def process_packet(packet):
    if IP not in packet or TCP not in packet:
        return

    tcp = packet[TCP]

    # Detect TCP SYN packets without ACK
    if tcp.flags & 0x02 and not tcp.flags & 0x10:
        src_ip = packet[IP].src
        current_time = time.time()

        # Keep only packets within the time window
        connections[src_ip] = [
            (t, port) for t, port in connections[src_ip]
            if current_time - t <= TIME_WINDOW
        ]

        connections[src_ip].append((current_time, tcp.dport))

        unique_ports = {
            port for _, port in connections[src_ip]
        }

        # Alert when the threshold is reached
        if len(unique_ports) >= THRESHOLD:
            if current_time - last_alert.get(src_ip, 0) >= ALERT_COOLDOWN:
                log_alert(src_ip, unique_ports)
                last_alert[src_ip] = current_time


def main():
    print("================================")
    print("       PYTHON-BASED NIDS")
    print("================================")
    print(f"Interface: {INTERFACE}")
    print("Detection: TCP SYN port scanning")
    print(f"Threshold: {THRESHOLD} unique ports / {TIME_WINDOW} seconds")
    print("Monitoring started. Press CTRL+C to stop.")

    try:
        sniff(
            iface=INTERFACE,
            filter="tcp",
            prn=process_packet,
            store=False
        )
    except KeyboardInterrupt:
        print("\nNIDS stopped.")


if __name__ == "__main__":
    main()

