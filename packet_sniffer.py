#!/usr/bin/env python3
import sys
from scapy.all import *

# Function to handle each packet
def handle_packet(packet, log):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        log.write(f"TCP Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}\n")
        print(f"Captured: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

# Main function to start sniffing
def main(interface):
    logfile_name = f"sniffer_{interface}_log.txt"
    try:
        with open(logfile_name, 'w') as logfile:
            print(f"Starting packet sniffing on {interface}... Press Ctrl+C to stop.")
            sniff(iface=interface, prn=lambda pkt: handle_packet(pkt, logfile), store=0)
    except KeyboardInterrupt:
        print("\nStopped sniffing.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sudo python3 packet_sniffer.py <interface>")
        print("Example: sudo python3 packet_sniffer.py eth0")
        sys.exit(1)
    main(sys.argv[1])
