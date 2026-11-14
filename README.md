# Network Intrusion Detection System (NIDS)

## Overview

This project is a lightweight, Python-based Network Intrusion Detection System designed to identify potential TCP SYN port scanning activity.

It monitors network traffic using Scapy, analyzes incoming TCP packets, and generates alerts when a source IP address targets multiple unique ports within a short time window.

## Features

- Real-time network packet monitoring
- TCP SYN port scan detection
- Detection based on unique destination ports
- Configurable detection threshold and time window
- Console-based security alerts
- Automatic CSV alert logging
- Alert cooldown to reduce repeated notifications

## Technologies Used

- Python 3.13.12
- Scapy 2.8.0
- Kali Linux
- Ubuntu Server
- Nmap
- VirtualBox

## Project Structure

```text
NIDS/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── detector.py
├── tests/
├── docs/
│   ├── architecture.md
│   └── testing.md
└── evidence/
    └── alerts.csv

## How It Works

1. Scapy captures TCP packets on the configured network interface.
2. The detector identifies TCP SYN packets without the ACK flag.
3. It tracks unique destination ports contacted by each source IP.
4. An alert is generated when a source IP targets at least 10 unique ports within 10 seconds.
5. Alerts are displayed in the terminal and saved to a CSV file.
6. A 10-second cooldown helps prevent repeated alerts for the same source IP.

## Requirements

- Python 3.13 or compatible version
- Scapy 2.8.0
- Linux environment
- Root privileges for packet capture

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd NIDS

Create a virtual environment:
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt


Configuration
Open src/detector.py and check these settings:
THRESHOLD = 10TIME_WINDOW = 10ALERT_COOLDOWN = 10INTERFACE = "eth1"



Change the interface to match your network.
Usage
sudo ./venv/bin/python src/detector.py


Press Ctrl + C to stop monitoring.
Testing
The system was tested in an isolated VirtualBox environment using Kali Linux as the monitoring machine, Ubuntu Server as the target, and Nmap to generate TCP SYN scan traffic.

Example authorized test:
sudo nmap -sS -p 1-100 <target-ip>


Alert Logging
Alerts are saved in evidence/alerts.csv. Each record includes:
- Timestamp
- Source IP address
- Targeted destination ports
Limitations
- Detects TCP SYN port scanning only.
- Uses threshold-based detection.
- May produce false positives.
- Does not inspect packet payloads.
- Currently configured for a specific network interface.
- Designed and tested in a controlled virtual lab.
Future Improvements
- Support configurable network interfaces.
- Detect additional suspicious network activities.
- Improve alert reporting.
- Expand automated testing.
Ethical Use
This project is intended for educational purposes and authorized network monitoring only. Test it only on systems and networks you own or have permission to assess.

**Then save the file:**

1. Press `Ctrl + O`.
2. Press `Enter`.
3. Press `Ctrl + X`.

After that, run:

```bash
ls -l README.md
