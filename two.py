import socket
import threading
def scan_port(ip,port):
 try:
    # create socket
sock = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip,
port))
    if result == 0:
       print(f"port {port} is open")
    sock.close()
  except socket.error:
    pass
def scan_ports(ip, start_port,
end_port):
   threads = []
   for port in range(start_port,
end_port + 1):
     thread =
threading.Thread(target=scan_port,
args=(ip, port))
      threads.append(thread)
      thread.start()
  for thread in threads:
      thread.join()
def main():
  target_ip = "192.168.71.128" # Your
IP address is hardcoded here
  start_port = int(input("Enter the
start port: "))
  end_port = int(input("Enter the
end port: "))
  print(f"scanning ports
{start_port} to {end_port} on
{target_ip}...")
  scan_port(target_ip, start_port,
end_port)
if __name__ == '__main__":
    main()
