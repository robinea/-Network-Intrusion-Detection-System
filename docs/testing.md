# NIDS Testing and Validation

## Test Environment

The NIDS was tested in an isolated VirtualBox network.

| Machine | Role | IP Address |
|---|---|---|
| Kali Linux | NIDS monitoring machine | 192.168.50.10 |
| Ubuntu Server | Target machine | 192.168.50.20 |

## Testing Tool

Nmap was used to generate TCP SYN scan traffic.

## Test Procedure

1. Start the NIDS on Kali Linux.
2. Run an Nmap SYN scan from Kali against the Ubuntu target.
3. Observe the NIDS terminal for alerts.
4. Check `evidence/alerts.csv` for recorded alerts.

## Example Test Command

```bash
sudo nmap -sS -p 1-100 192.168.50.20


Observed Results
- The NIDS successfully captured TCP traffic on eth1.
- SYN scans targeting multiple ports triggered detection alerts.
- Alerts displayed the source IP and targeted ports.
- Alert records were successfully saved to the CSV log.
- The alert cooldown reduced repeated notifications.
Test Outcome
The tests demonstrated that the NIDS can identify and log TCP SYN port scanning activity in the controlled virtual lab environment.
Limitations
Testing was performed in a controlled environment and does not establish detection accuracy across all network conditions.
