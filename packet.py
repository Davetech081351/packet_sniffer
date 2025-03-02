from scapy.all import sniff,IP,TCP,UDP

# Function to process captured packets
def packet_callback(packet):
    if IP in packet: # Check if packet has an IP layer
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"

        print(f"packet:{src_ip}->{dst_ip} | Protocol:{protocol}")

# Sniff packets (adjust iface for your system,e.g.,'Wi-Fi' on Windows)
sniff(filter="ip",prn=packet_callback,store=False, count=10)

