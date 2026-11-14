# NIDS Architecture

## System Overview

The NIDS monitors network traffic using Scapy and identifies potential TCP SYN port scanning activity.

## Detection Workflow

1. Capture TCP packets on the configured network interface.
2. Check whether packets contain IPv4 and TCP layers.
3. Identify SYN packets without the ACK flag.
4. Track destination ports for each source IP within a 10-second window.
5. Trigger an alert when 10 unique destination ports are detected.
6. Apply a 10-second alert cooldown.
7. Display the alert and save it to a CSV file.

## Architecture Diagram

```mermaid
flowchart TD
    A[Network Traffic] --> B[Scapy Packet Capture]
    B --> C{TCP SYN without ACK?}
    C -- No --> D[Ignore Packet]
    C -- Yes --> E[Track Source IP and Port]
    E --> F{10 Unique Ports in 10 Seconds?}
    F -- No --> B
    F -- Yes --> G{Cooldown Expired?}
    G -- No --> B
    G -- Yes --> H[Generate Alert]
    H --> I[Display in Terminal]
    H --> J[Save to CSV]


Main Components
- Scapy: Captures and processes network packets.
- Packet Processor: Examines TCP flags and destination ports.
- Detection Logic: Identifies possible port scanning based on a threshold.
- Alert Handler: Displays and records detected activity.
- CSV Logger: Stores alert details in evidence/alerts.csv.
