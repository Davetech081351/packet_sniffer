import socket
import argparse

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_ports(target, start_port, end_port):
    print(f"\n[+] Scanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")

    args = parser.parse_args()
    scan_ports(args.target, args.start_port, args.end_port)
